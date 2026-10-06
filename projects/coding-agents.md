# 编码智能体与开发工具

写代码、改仓库、跑命令的编码智能体和开发工具。

## 2026-01

### [ECC](https://github.com/affaan-m/ECC)
- 发现：2026-01-24
- 一句话：面向 Claude Code、Codex、Cursor 等编码智能体 harness 的性能与工程化增强套件。
- 摘要：ECC 是智能体 harness 操作系统，整合技能、本能、记忆、安全与研究优先开发等能力，用于优化编码智能体的表现。可通过官方插件、npm 包与 GitHub App 等方式安装，并强调仅从官方渠道获取。面向需要在多种编码客户端上统一工作流、上下文与安全策略的团队与个人开发者。
- 标签：`编码智能体` `harness` `技能` `MCP` `安全`
- 来源：GitHub Star

### [CCG](https://github.com/fengshao1227/ccg-workflow)
- 发现：2026-01-17
- 一句话：多模型协作工作流引擎，用一个命令让 Claude、Codex 与 Gemini 按策略协同完成编码任务。
- 摘要：CCG 是 Claude、Codex 与 Gemini 多模型协作工作流，通过统一命令分析意图、选择策略并编排各模型分工执行。以 Node.js 实现，提供安装向导、文档站点与 CI 测试，可与 DeepSeek Harness 等环境集成。适合希望在 Claude Code 生态内组合多家模型能力的开发者。
- 标签：`多模型` `工作流` `Claude Code` `Codex` `Gemini`
- 来源：GitHub Star

### [OpenCode](https://github.com/anomalyco/opencode)
- 发现：2026-01-13
- 一句话：开源 AI 编码智能体，可在终端与桌面端协助开发与改代码。
- 摘要：OpenCode 是开源 AI 编码智能体，定位为在开发流程中写代码与执行任务。支持通过安装脚本与多种包管理器安装 CLI，并提供 Beta 版桌面应用下载。文档站为 opencode.ai。
- 标签：`编码智能体` `CLI` `开源`
- 来源：GitHub Star

### [Ralph](https://github.com/snarktank/ralph)
- 发现：2026-01-13
- 一句话：自主 AI 编码循环，反复调用 Amp 或 Claude Code 直至 PRD 条目全部完成。
- 摘要：Ralph 是一种自主智能体循环，默认驱动 Amp 或 Claude Code，在每次全新上下文中重复执行，直到 prd.json 中的需求项完成。记忆依赖 git 历史、progress.txt 与 prd.json，并提供 PRD 与 Ralph 相关技能与 Claude Code 插件市场安装方式。
- 标签：`编码智能体` `自动化` `PRD`
- 来源：GitHub Star

### [OpenSkills](https://github.com/numman-ali/openskills)
- 发现：2026-01-11
- 一句话：面向各类 AI 编码智能体的通用技能加载 CLI，兼容 Claude Code 技能格式。
- 摘要：OpenSkills 将 Anthropic 风格的 SKILL.md 技能系统带到 Claude Code、Cursor、Windsurf、Aider、Codex 等能读取 AGENTS.md 的智能体。通过 install 与 sync 把技能装入项目或全局目录，并生成与 Claude Code 相同的 available_skills 提示结构，按需渐进加载技能。
- 标签：`技能加载` `CLI` `编码智能体`
- 来源：GitHub Star

### [Spec Kit](https://github.com/github/spec-kit)
- 发现：2026-01-04
- 一句话：为 AI 编码智能体提供规格驱动开发、修 bug 与想法评估等结构化流程与技能的开源工具包。
- 摘要：Spec Kit 向编码智能体提供可复用模板、文档化产出与独立入口流程，涵盖规格驱动开发、缺陷修复与想法评估三类场景。通过 specify CLI 初始化项目并集成 Copilot 等宿主，在智能体对话中按序调用 speckit 系列技能完成各阶段。
- 标签：`规格驱动` `编码智能体` `GitHub`
- 来源：GitHub Star

### [iFlow CLI](https://github.com/iflow-ai/iflow-cli)
- 发现：2026-01-01
- 一句话：终端内的 AI 编码助手 CLI，可分析仓库并执行从文件操作到工作流自动化的任务。
- 摘要：iFlow CLI 在终端中提供自然语言驱动的代码库分析与编码任务执行，可通过 iFlow 开放平台使用多种模型，并支持 SubAgent、MCP 与市场一键安装扩展。README 注明将于 2026 年 4 月 17 日关停，并附迁移说明链接。
- 标签：`CLI` `编码智能体` `终端`
- 来源：GitHub Star

### [OpenSpec](https://github.com/Fission-AI/OpenSpec)
- 发现：2026-01-01
- 一句话：面向 AI 编码助手的规格驱动开发框架，用 Markdown 工件组织需求与实现。
- 摘要：OpenSpec 强调灵活迭代、适配存量项目，通过 opsx 工作流在仓库中生成 proposal、specs、design 与 tasks 等 Markdown 工件，再驱动实现与归档。哲学定位为轻量可扩展的 SDD，适合个人到团队用对话命令推进功能开发。
- 标签：`规格驱动` `SDD` `编码智能体`
- 来源：GitHub Star

### [Vibe Kanban](https://github.com/BloopAI/vibe-kanban)
- 发现：2026-01-01
- 一句话：用看板规划与审查编码智能体工作的开发工作台，支持多 agent 与内嵌预览。
- 摘要：Vibe Kanban 通过看板 issue 规划任务，在工作区为编码智能体提供分支、终端与开发服务器环境，并支持 diff 审查、内嵌浏览器预览与切换多种编码 agent。可用 npx vibe-kanban 启动；README 宣布产品即将停运并附公告链接。
- 标签：`看板` `编码智能体` `工作台`
- 来源：GitHub Star
