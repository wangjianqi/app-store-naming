# app-store-naming

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language](https://img.shields.io/badge/docs-English%20%7C%20%E4%B8%AD%E6%96%87-blueviolet)](README.md)
[![Python](https://img.shields.io/badge/python-3.10%2B-informational)](scripts/validate_metadata.py)
[![Platform](https://img.shields.io/badge/agent-Codex%20%7C%20Claude%20Code-black)](#安装)

一个可复用的 Agent Skill，用于 App Store 应用命名与改名：包含实时冲突调研、ASO 推理、品牌与延展性检查、本地化、元数据校验，以及明确的 App Store Connect 可用性边界说明。

> English documentation: [README.md](README.md)。

## 为什么需要它

大多数命名流程止步于"给你几个好听的名字"。这个 Skill 把命名当作一个上线问题来处理：

- **可用性是硬门槛，不是加分项。** 公开的 App Store 搜索永远无法证明名字可注册——在没有 App Store Connect 验证之前，本 Skill 绝不说"可用"。
- **ASO 是一个元数据系统。** 应用名称、副标题、关键词字段、开发者名称按协同预算分配，而不是各自孤立优化。
- **不编造数据。** 不虚构搜索量、关键词难度、下载量估算或商标状态。所有证据标注为 Confirmed（已确认）/ Inferred（推断）/ Unverified（未验证）。
- **名称经得起产品扩展。** 候选名会对照产品路线图测试，避免产品扩张后名字变得尴尬。

## 它做什么

- 从真实产品和路线图构建命名简报（支持 CREATE / EVALUATE / RENAME / VERIFY / LOCALIZE 五种模式）
- 有联网工具时，调研现有 App Store 名称与品牌冲突
- 从多种命名策略生成候选，然后按合规与冲突风险硬过滤
- 用透明评分表对比候选（ASO、品牌、清晰度、记忆度、延展性、本地化）
- 输出一个推荐名加备选名，并给出配套副标题/关键词策略
- 附带确定性的 Python 元数据校验脚本（长度/字节上限、重复关键词、名称/副标题重复）

## 安装

### Codex

把文件夹复制到 Codex skills 目录：

```bash
git clone https://github.com/wangjianqi/app-store-naming.git
mkdir -p ~/.codex/skills
cp -R app-store-naming ~/.codex/skills/
```

也可以使用你惯用的 Skills CLI 或本地技能安装流程。

### Claude Code

`SKILL.md` 的 frontmatter 格式与 Claude Code 技能兼容：

```bash
git clone https://github.com/wangjianqi/app-store-naming.git
mkdir -p ~/.claude/skills
cp -R app-store-naming ~/.claude/skills/
```

### 其他 Agent

任何能读取带 `name` / `description` frontmatter 的 `SKILL.md` 的 Agent 都可以加载本技能，指向仓库目录即可。

## 示例提示词

```text
用 app-store-naming 给这个 App 起名。主要做英语听力，但以后会扩展其他语言学习材料，主打中国市场，兼顾 ASO 和品牌。
```

```text
用 app-store-naming 评估 ScanLoom 这个名字，检查公开冲突、ASO、品牌延展性，并给我 5 个更好的候选。
```

```text
用 app-store-naming 检查这三个名字哪个更适合上 App Store：A、B、C。不要只看好不好听，要查当前冲突和元数据风险。
```

## 本地元数据校验

```bash
python3 scripts/validate_metadata.py \
  --name "Example: Voice Notes" \
  --subtitle "Record, transcribe, organize" \
  --keywords "memo,meeting,audio,speech"
```

JSON 输出：

```bash
python3 scripts/validate_metadata.py \
  --name "Example" \
  --subtitle "Voice Notes" \
  --keywords "memo,meeting,audio" \
  --json
```

## 项目结构

```
app-store-naming/
├── SKILL.md                     # 技能入口：工作流、模式、输出格式
├── agents/
│   └── openai.yaml              # Codex agent 界面配置
├── references/
│   ├── apple-rules.md           # 当前 Apple 元数据规则 + 官方链接
│   ├── scoring-rubric.md        # 100 分制评分表
│   ├── availability-check.md    # Level A/B/C 验证阶梯
│   └── aso-framework.md         # 元数据分配框架
├── templates/
│   └── naming-report.md         # 报告模板
├── scripts/
│   └── validate_metadata.py     # 确定性元数据校验脚本
└── assets/
    └── icon.svg
```

## 重要说明

公开的 App Store/网络搜索无法证明名称可注册。最终的操作性可用性，是 App Store Connect 在对应本地化/应用记录流程中接受该名称。本技能中的商标筛查只是风险初筛，不构成法律意见。

本技能是独立的开源项目，与 Apple Inc. 无隶属、背书或赞助关系。

## 参与贡献

欢迎提交 Issue 和 Pull Request，参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE) © Jianqi Wang
