#!/usr/bin/env python3
"""Validate common App Store naming metadata constraints.

This is a deterministic helper, not a live availability or trademark checker.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).casefold()
    return re.sub(r"[\s\-_:：·•—–,.，。/\\()（）\[\]{}]+", "", text)


def split_keywords(raw: str) -> list[str]:
    return [item.strip() for item in re.split(r"[,，]", raw) if item.strip()]


def keyword_overlap(keyword: str, name: str, subtitle: str) -> bool:
    k = normalize(keyword)
    if not k:
        return False
    return k in normalize(name) or k in normalize(subtitle)


def validate(name: str, subtitle: str, keywords: str) -> dict:
    keyword_items = split_keywords(keywords)
    keyword_bytes = len(keywords.encode("utf-8"))

    warnings: list[str] = []
    errors: list[str] = []

    if not (2 <= len(name) <= 30):
        errors.append(f"App name length is {len(name)} characters; expected 2–30.")

    if len(subtitle) > 30:
        errors.append(f"Subtitle length is {len(subtitle)} characters; maximum is 30.")

    if keyword_bytes > 100:
        errors.append(f"Keyword field is {keyword_bytes} UTF-8 bytes; maximum is 100 bytes.")

    normalized_items = [normalize(x) for x in keyword_items]
    duplicates = sorted({
        keyword_items[i]
        for i, token in enumerate(normalized_items)
        if token and normalized_items.count(token) > 1
    })
    if duplicates:
        warnings.append("Duplicate keyword entries: " + ", ".join(duplicates))

    overlaps = [k for k in keyword_items if keyword_overlap(k, name, subtitle)]
    if overlaps:
        warnings.append(
            "Keywords that appear to duplicate name/subtitle terms (heuristic): "
            + ", ".join(overlaps)
        )

    return {
        "name": {
            "value": name,
            "characters": len(name),
            "valid": 2 <= len(name) <= 30,
        },
        "subtitle": {
            "value": subtitle,
            "characters": len(subtitle),
            "valid": len(subtitle) <= 30,
        },
        "keywords": {
            "value": keywords,
            "utf8_bytes": keyword_bytes,
            "items": keyword_items,
            "valid": keyword_bytes <= 100,
        },
        "errors": errors,
        "warnings": warnings,
        "valid": not errors,
        "note": "This does not check App Store Connect availability, search volume, or trademark status.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate App Store naming metadata.")
    parser.add_argument("--name", required=True, help="App Store app name")
    parser.add_argument("--subtitle", default="", help="App Store subtitle")
    parser.add_argument("--keywords", default="", help="Comma-separated keyword field")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    args = parser.parse_args()

    result = validate(args.name, args.subtitle, args.keywords)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Name: {result['name']['characters']}/30 chars — {'OK' if result['name']['valid'] else 'INVALID'}")
        print(f"Subtitle: {result['subtitle']['characters']}/30 chars — {'OK' if result['subtitle']['valid'] else 'INVALID'}")
        print(f"Keywords: {result['keywords']['utf8_bytes']}/100 UTF-8 bytes — {'OK' if result['keywords']['valid'] else 'INVALID'}")
        for error in result["errors"]:
            print(f"ERROR: {error}")
        for warning in result["warnings"]:
            print(f"WARN: {warning}")
        print(result["note"])

    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
