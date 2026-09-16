# Contributing to app-store-naming

Thanks for your interest in improving this skill. Contributions are welcome in both English and Chinese (中文).

## Ways to contribute

- **Rule updates**: Apple changes App Store metadata rules. If you notice a change, open an issue or PR updating `references/apple-rules.md` with the official link and date.
- **Workflow improvements**: Better filtering heuristics, rubric criteria, or report clarity in `SKILL.md` / `references/`.
- **Validator fixes**: Bug fixes or improved checks in `scripts/validate_metadata.py`.
- **Localization**: Corrections for non-English naming guidance.
- **Bug reports**: Wrong character/byte counts, broken links, misleading guidance.

## Ground rules

1. **No fabricated evidence.** Anything presented as a fact about App Store rules, trademarks, or availability must cite an authoritative source. Qualitative judgments must be labeled as such.
2. **Preserve the availability ladder.** Public search (Level A) and trademark screening (Level B) must never be presented as final availability (Level C, App Store Connect).
3. **Keep it deterministic.** The validator must stay offline and reproducible — no network calls, no heuristic that yields different results across runs.
4. **Current Apple docs win.** If this skill conflicts with current Apple documentation, the skill should be updated to match.

## Testing your changes

Run the validator against valid and invalid metadata before submitting:

```bash
python3 scripts/validate_metadata.py --name "Example: Voice Notes" --subtitle "Record, transcribe, organize" --keywords "memo,meeting,audio"
python3 scripts/validate_metadata.py --name "A Name That Is Definitely Way Too Long For The Store" --json
```

If you changed the validator, confirm both the human-readable and `--json` output paths work.

## Submitting a pull request

1. Fork the repo and create a branch from `main`.
2. Make your change and test it (see above).
3. Describe **what** changed and **why**, including evidence for any rule change.
4. Keep diffs focused — one logical change per PR.

## Reporting issues

Include:

- What you asked the skill to do (the prompt)
- What it produced
- What you expected instead, with sources if it concerns Apple rules
