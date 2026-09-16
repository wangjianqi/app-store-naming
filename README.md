# app-store-naming

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language](https://img.shields.io/badge/docs-English%20%7C%20%E4%B8%AD%E6%96%87-blueviolet)](README.zh-CN.md)
[![Python](https://img.shields.io/badge/python-3.10%2B-informational)](scripts/validate_metadata.py)
[![Platform](https://img.shields.io/badge/agent-Codex%20%7C%20Claude%20Code-black)](#install)

A reusable agent Skill for naming and renaming App Store apps with live collision research, ASO reasoning, brand/scalability checks, localization, metadata validation, and explicit App Store Connect availability caveats.

> 简体中文文档见 [README.zh-CN.md](README.zh-CN.md)。

## Why

Most naming workflows stop at "here are some catchy names". This skill treats naming as a shipping problem:

- **Availability is a gate, not a score.** A public App Store search can never prove a name is reservable — the skill never claims "available" without an App Store Connect check.
- **ASO is a metadata system.** App name, subtitle, keyword field, and developer name are allocated as a coordinated budget, not optimized in isolation.
- **No invented data.** No fabricated search volumes, keyword difficulty, download estimates, or trademark status. Evidence is labeled Confirmed / Inferred / Unverified.
- **Scope-safe names.** Candidates are tested against the product roadmap, so a name doesn't become embarrassing after expansion.

## What it does

- Builds a naming brief from the actual product and roadmap (CREATE / EVALUATE / RENAME / VERIFY / LOCALIZE modes)
- Researches existing App Store names/brands when live web tools are available
- Generates candidates from multiple naming strategies, then hard-filters on compliance and collision risk
- Scores finalists with a transparent rubric (ASO, brand, clarity, memorability, extensibility, localization)
- Produces one recommended name plus backups, with matching subtitle/keyword strategy
- Includes a deterministic Python metadata validator (length/byte limits, duplicate keywords, name/subtitle overlap)

## Install

### Codex

Copy the folder into your Codex skills directory:

```bash
git clone https://github.com/wangjianqi/app-store-naming.git
mkdir -p ~/.codex/skills
cp -R app-store-naming ~/.codex/skills/
```

Or use your preferred Skills CLI / local-skill installation flow.

### Claude Code

The `SKILL.md` frontmatter format is compatible with Claude Code skills:

```bash
git clone https://github.com/wangjianqi/app-store-naming.git
mkdir -p ~/.claude/skills
cp -R app-store-naming ~/.claude/skills/
```

### Other agents

Any agent that reads a `SKILL.md` with `name` / `description` frontmatter can load this skill. Point it at the repo folder.

## Example prompts

```text
用 app-store-naming 给这个 App 起名。主要做英语听力，但以后会扩展其他语言学习材料，主打中国市场，兼顾 ASO 和品牌。
```

```text
用 app-store-naming 评估 ScanLoom 这个名字，检查公开冲突、ASO、品牌延展性，并给我 5 个更好的候选。
```

```text
用 app-store-naming 检查这三个名字哪个更适合上 App Store：A、B、C。不要只看好不好听，要查当前冲突和元数据风险。
```

## Local metadata validation

```bash
python3 scripts/validate_metadata.py \
  --name "Example: Voice Notes" \
  --subtitle "Record, transcribe, organize" \
  --keywords "memo,meeting,audio,speech"
```

JSON output:

```bash
python3 scripts/validate_metadata.py \
  --name "Example" \
  --subtitle "Voice Notes" \
  --keywords "memo,meeting,audio" \
  --json
```

## Project structure

```
app-store-naming/
├── SKILL.md                     # Skill entry: workflow, modes, output format
├── agents/
│   └── openai.yaml              # Codex agent interface config
├── references/
│   ├── apple-rules.md           # Current Apple metadata rules + official links
│   ├── scoring-rubric.md        # 100-point scoring rubric
│   ├── availability-check.md    # Level A/B/C verification ladder
│   └── aso-framework.md         # Metadata allocation framework
├── templates/
│   └── naming-report.md         # Report template
├── scripts/
│   └── validate_metadata.py     # Deterministic metadata validator
└── assets/
    └── icon.svg
```

## Important

A public App Store/web search cannot prove that a name is reservable. Final operational availability is the name being accepted by App Store Connect for the intended localization/app record. Trademark screening in this skill is a risk screen, not legal clearance.

This skill is an independent open-source project and is not affiliated with, endorsed by, or sponsored by Apple Inc.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) © Jianqi Wang
