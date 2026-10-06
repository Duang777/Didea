# 编码智能体与开发工具

写代码、改仓库、跑命令的编码智能体和开发工具。

## 2026-06

### [PMB](https://github.com/oleksiijko/pmb)
- 发现：2026-06-30
- 一句话：面向 Claude Code、Cursor、Codex 等编码智能体的本地优先持久记忆，经 MCP 读写。
- 摘要：PMB 为 MCP 感知的编码智能体提供本地工作区记忆，决策、教训与事实写入 SQLite，读路径不依赖云端 API 或额外 LLM 调用。通过 pip 安装后可用 setup 自动检测智能体并写入 MCP 配置，支持 recall 搜索与可视化实体图谱。强调离线、多语言与跨会话、跨智能体切换仍保留记忆。
- 标签：`MCP` `记忆` `SQLite` `本地优先`
- 来源：GitHub Star

### [Trae Agent](https://github.com/bytedance/trae-agent)
- 发现：2026-06-27
- 一句话：面向通用软件工程任务的 LLM 命令行智能体，架构透明便于研究与扩展。
- 摘要：Trae Agent 提供自然语言驱动的 CLI，可执行文件编辑、bash、顺序思考等工具链，并支持多轮交互与轨迹记录。支持 OpenAI、Anthropic、Doubao、Gemini 等多家模型与 YAML 配置。项目定位为研究友好：模块化架构便于修改、扩展与分析智能体行为，并附带 Lakeview 等步骤摘要能力。
- 标签：`CLI` `软件工程` `工具调用` `字节跳动`
- 来源：GitHub Star

### [Cowart](https://github.com/zhongerxin/Cowart)
- 发现：2026-06-22
- 一句话：面向 Codex 的 tldraw 无限画布原生插件，经 MCP 在项目中持久化画布与 AI 生图。
- 摘要：Cowart 是 Codex 原生无限画布 widget 插件，基于 tldraw 做构思、标注、生图与迭代，数据默认保存在用户项目的 canvas 目录。仓库含 Agent Plugins 规范下的 plugin.json、skills 与 MCP 入口，可在 Codex 内打开画布而非依赖外部浏览器。支持 AI 图片框、HTML 框、幻灯片与标注驱动改图，并提供 Cowart MCP 工具读写选择与资源。
- 标签：`Codex` `MCP` `画布` `tldraw`
- 来源：GitHub Star


## 2026-05

### [HarnessClaw Engine](https://github.com/harnessclaw/harnessclaw-engine)
- 发现：2026-05-31
- 一句话：Go 实现的 LLM 编程助手引擎，支持 WebSocket、工具调用、权限与技能扩展。
- 摘要：HarnessClaw Engine 经 WebSocket、HTTP、飞书等通道提供多轮对话、流式卡片 UI、工具执行与权限流水线。内置 Bash、读写文件、Grep 等工具，并从 SKILL.md 加载可参数化技能。Query Engine 采用预处理、LLM 流式、错误退避、工具执行与续跑检查的五阶段循环，并支持多 Provider 与上下文压缩。
- 标签：`Go` `WebSocket` `编程助手` `技能`
- 来源：GitHub Star


## 2026-04

### [hero-coding](https://github.com/lawrencewzen/hero-coding)
- 发现：2026-04-30
- 一句话：极简自治编码智能体 harness，故事入 inbox 即产出 git 提交。
- 摘要：hero-coding 是自治编码智能体的最小 harness，理念是推理放在循环与约束中，智能体本身可替换。Dispatcher 监听 inbox 并为每个用户故事创建隔离 git worktree，Worker、Verifier 与 Reviewer 组成执行—验证回合，通过后进入 done。Plan 通常在上游对话中写成故事文件，本 harness 专注 Execute 与 Verify。
- 标签：`编码智能体` `harness` `Execute-Verify` `Git` `Go`
- 来源：GitHub Star

### [claude-code（claude-code-best）](https://github.com/claude-code-best/claude-code)
- 发现：2026-04-01
- 一句话：可运行、可构建的 Claude Code 工程化复刻与扩展发行版。
- 摘要：项目称完整复原 Anthropic Claude Code，并扩展 Goal 持续驱动、Artifacts 上传、Ultracode 多智能体编排、Pipe IPC 群控与 ACP IDE 接入等能力。兼容原有配置，文档站点说明各特性用法。面向需要在本地构建与调试 Claude Code 类编码智能体的开发者。
- 标签：`Claude Code` `编码智能体` `开源复刻` `ACP` `编排`
- 来源：GitHub Star

### [Codex CLI](https://github.com/openai/codex)
- 发现：2026-04-01
- 一句话：在本地终端运行的 OpenAI 轻量编码智能体。
- 摘要：Codex CLI 是 OpenAI 的编码智能体，在本机运行。README 把它和编辑器里的 Codex、桌面应用，以及云端的 Codex Web 区分开。官方脚本、npm 和 Homebrew 都可以安装，也可以从 GitHub Release 下载对应平台的二进制。
- 标签：`编码智能体` `CLI` `OpenAI` `终端` `Rust`
- 来源：GitHub Star


## 2026-02

### [Pi](https://github.com/earendil-works/pi)
- 发现：2026-02-11
- 一句话：可扩展的极简编码智能体 harness，提供统一模型接口、智能体循环与终端交互式 CLI。
- 摘要：Pi 是一个极简、可扩展的智能体 harness，可通过扩展、技能、提示模板与主题按你的工作流定制。默认侧重编码场景，支持交互式使用、打印或 JSON 模式自动化、RPC 控制，也可用 TypeScript SDK 构建应用。安装命令行工具后在项目目录启动，即可连接内置或自备的模型提供商并下达任务。
- 标签：`编码智能体` `CLI` `harness` `TypeScript` `可扩展`
- 来源：GitHub Star

### [memU](https://github.com/NevaMind-AI/memU)
- 发现：2026-02-01
- 一句话：跨会话、跨智能体与跨设备的个人记忆系统，以 Wiki 形式沉淀可复用技能。
- 摘要：memU 是轻量的智能体驱动记忆系统，为用户在多次会话、多种编码智能体与多台设备间提供共享的 LLM Wiki。它会从智能体历史中自动蒸馏可复用的个人技能，核心记忆逻辑体量很小便于审阅与改造。通过 memu.so 获取 API Key 并按技能说明安装后，可与 Codex、Claude Code、Cursor、OpenClaw 等宿主配合做记忆写入与检索。
- 标签：`记忆` `Wiki` `编码智能体` `技能` `MCP`
- 来源：GitHub Star


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
