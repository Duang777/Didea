# 编码智能体与开发工具

写代码、改仓库、跑命令的编码智能体和开发工具。

## 2026-07

### [Cockpit Tools](https://github.com/jlcodes99/cockpit-tools)
- 发现：2026-07-31
- 一句话：通用 AI IDE 账号管理工具，支持多账号切换、配额监控与多开实例。
- 摘要：Cockpit Tools 帮助管理 Antigravity、Codex、GitHub Copilot、Windsurf、Kiro、Cursor 等多家 AI IDE 与 CLI 的账号。提供一键切号、配额监控、自动唤醒与应用多开并行运行，并支持插件联动与 GitHub Copilot 等专项管理。官方支持 macOS、Windows 与 Linux，界面提供多语言。
- 标签：`IDE` `账号管理` `Codex` `Cursor` `配额`
- 来源：GitHub Star

### [agentic-engineering-framework](https://github.com/DimitriGeelen/agentic-engineering-framework)
- 发现：2026-07-29
- 一句话：围绕 AI 编码智能体的治理与连续性 harness，强调任务可追溯与审计。
- 摘要：该框架为 Claude Code、Cursor、Copilot 等 CLI 智能体提供任务追踪、结构门禁、会话连续性与审计轨迹，协调而非替代 agent 执行。核心原则是无任务不做事，并通过 Context Fabric 记录决策与对话，Component Fabric 在变更前展示影响范围。人类在品味或高风险节点被强制拉回确认。
- 标签：`治理` `审计` `Claude Code` `Cursor` `任务追踪`
- 来源：GitHub Star

### [img2threejs](https://github.com/img2threejs/img2threejs)
- 发现：2026-07-27
- 一句话：把参考图里的物体重建为纯代码、可动画的 Three.js 程序化模型。
- 摘要：img2threejs 通过写代码而非摄影测量或网格抽取，从参考图像重建 Three.js 模型，并强调质量门禁、动画就绪与 token 效率。在线画廊展示浏览器内运行的生成代码模型，无外部 mesh 文件下载。适合需要可编辑、可动画 Web 3D 的编码 agent 工作流。
- 标签：`Three.js` `图生3D` `程序化` `WebGL` `Claude Code`
- 来源：GitHub Star

### [oh-my-pi](https://github.com/can1357/oh-my-pi)
- 发现：2026-07-25
- 一句话：内置 IDE 能力的编码智能体，由 Stencil Labs 维护。
- 摘要：oh-my-pi 自称开箱即用、可完全打开的 coding agent 表面，Fork 自 Pi 并持续按真实使用调优。支持 60 余家模型提供商、大量内置工具以及 LSP 与 DAP 操作，核心含约八万行 Rust。提供 curl、Homebrew、Bun 与 Nix 等安装方式，面向 macOS、Linux 与 Windows 终端工作流。
- 标签：`CLI` `编码智能体` `LSP` `Rust` `多模型`
- 来源：GitHub Star

### [TurnCoder](https://github.com/nightwindnohen/TurnCoder)
- 发现：2026-07-24
- 一句话：透明可控的本地 AI 编码工作台，回合制多模型编排工具调用。
- 摘要：TurnCoder 以聊天气泡构成可编辑上下文，用户可见并修改模型收到的全部内容。AI 一次输出带依赖关系的工具调用计划，系统按图执行而非每步再问模型。支持二十余家模型提供商混用，工具在本地执行，并面向按次计费场景减少重复送上下文。
- 标签：`本地优先` `回合制` `编码工作台` `多模型` `DAG`
- 来源：GitHub Star

### [HappyClaw](https://github.com/riba2534/happyclaw)
- 发现：2026-07-22
- 一句话：自托管多用户的 Claude Code 智能体工作台，经 Web 与多种 IM 长期在线。
- 摘要：HappyClaw 基于 Claude Agent SDK，把完整 Claude Code 运行时封装为可持续服务。智能体可读写项目、跑终端、用浏览器与 MCP，并在多工作区、多会话间隔离权限与上下文。支持飞书、Telegram、钉钉等八种渠道，以及宿主机目录或 Docker 沙箱执行、定时任务与用量统计。
- 标签：`Claude Code` `自托管` `多用户` `IM 渠道` `沙箱`
- 来源：GitHub Star

### [Letta Code](https://github.com/letta-ai/letta-code)
- 发现：2026-07-20
- 一句话：带记忆与身份的状态化编码智能体 harness，可交互或常驻主动工作。
- 摘要：Letta Code 智能体通过改写记忆块、技能与提示在长时间尺度上学习与适应，并可用 MemFS 用 git 跟踪全部上下文。提供 CLI、桌面端、浏览器与 Telegram 等渠道，支持子智能体、技能加载与 /search 跨会话检索。强调可自我配置，亦支持周期性 dreaming 与行为诊断命令。
- 标签：`记忆` `Harness` `技能` `CLI` `状态化`
- 来源：GitHub Star

### [Archon](https://github.com/coleam00/Archon)
- 发现：2026-07-19
- 一句话：面向 AI 编码智能体的开源 harness 构建器，用 YAML 工作流让开发流程可重复。
- 摘要：Archon 把规划、实现、校验、评审与建 PR 等阶段写成确定性 YAML 工作流，AI 只在需要智能的节点介入。每次运行在独立 git worktree 中并行，可从 CLI、Web、Slack 或 GitHub 触发。理念类似为 AI 编码定制的 CI 编排，使同一仓库内流程可提交、可移植。
- 标签：`Harness` `YAML 工作流` `编码智能体` `worktree` `确定性`
- 来源：GitHub Star

### [Flowix](https://github.com/text2future/flowix)
- 发现：2026-07-18
- 一句话：Markdown 笔记本，把笔记变成编码智能体的持久上下文。
- 摘要：Flowix 让你在 Markdown 中写作，为智能体指定所需上下文，并把结果写回同一笔记以便审阅与复用。可连接 Codex、Claude Code、OpenCode、Hermes 等 MCP 或 CLI 工具，共用同一套笔记与记忆，也内置 DeepSeek Harness 相关插件以读写本地 memo。
- 标签：`记忆` `Markdown` `MCP` `笔记`
- 来源：GitHub Star

### [Orca](https://github.com/stablyai/orca)
- 发现：2026-07-15
- 一句话：并行编排多台编码智能体的 ADE，支持桌面、手机与远程运行时。
- 摘要：Orca 让你在自有订阅下并排运行 Codex、Claude Code、OpenCode 或 Pi，每台智能体在独立 git worktree 中工作并集中追踪。支持把一个提示扇出到多个智能体比较结果，并提供手机端伴生应用远程跟进与续聊。
- 标签：`编排` `worktree` `IDE` `并行`
- 来源：GitHub Star

### [Entire CLI](https://github.com/entireio/cli)
- 发现：2026-07-13
- 一句话：接入 Git 工作流，把 AI 智能体会话与提交一并索引留存。
- 摘要：Entire 在开发过程中捕获 AI 智能体会话，并与提交一起建立可检索记录，便于理解代码为何改动而不只看 diff。支持从检查点恢复会话、把智能体上下文放在分支历史之外，并兼容 Claude Code、Codex、Cursor 等多种智能体。
- 标签：`Git` `会话` `可追溯` `CLI`
- 来源：GitHub Star

### [Codewhale](https://github.com/codewhale-hq/Codewhale)
- 发现：2026-07-13
- 一句话：开源终端编码智能体，可用任意托管或本地模型读写项目并执行命令。
- 摘要：Codewhale 用 Rust 构建，在终端中阅读项目、编辑文件、运行命令并自检。通过 provider 与 model 命令连接托管密钥或本地运行时，支持 MCP 与多智能体等能力。
- 标签：`Rust` `终端` `CLI` `多模型`
- 来源：GitHub Star

### [bash-agent](https://github.com/lloydzhou/bash-agent)
- 发现：2026-07-11
- 一句话：极简 AI 编码智能体运行时，纯 bash 与 awk 实现且无运行时依赖。
- 摘要：bash-agent 仅需 bash、awk、curl 与 rg 即可运行编码智能体循环，并提供 bash、c、go、rust 等多实现且语义对齐。支持子 Agent 并行、会话持久化、按需加载技能与 stream-json 结构化输出。
- 标签：`bash` `极简` `CLI` `harness`
- 来源：GitHub Star

### [MiMoCode](https://github.com/XiaomiMiMo/MiMo-Code)
- 发现：2026-07-11
- 一句话：终端原生 AI 编程助手，可读写代码、执行命令并维护项目记忆。
- 摘要：MiMoCode 是终端里的 AI 编程助手，能读写代码、运行命令、管理 Git，并用持久记忆跨会话理解项目。可连接主流 LLM 提供商 API，小米 MiMo 桌面版也以 MiMo Code 为核心引擎。
- 标签：`CLI` `终端` `记忆` `小米`
- 来源：GitHub Star

### [OpenHands](https://github.com/OpenHands/OpenHands)
- 发现：2026-07-06
- 一句话：可自托管的编码智能体控制台，统一运行多种兼容 ACP 的编程智能体与自动化。
- 摘要：OpenHands Agent Canvas 把编码智能体变成可自托管、常在线的工程协作面，用于发起对话并自动化日常任务，例如生成报告发到 Slack 或拆解 GitHub Issue。默认可在本机运行，也可连接 Docker、虚拟机或企业内网等多种智能体后端。开箱支持开源 OpenHands 智能体，也可接入 Claude Code、Codex 等第三方智能体。
- 标签：`自托管` `ACP` `编码智能体` `自动化`
- 来源：GitHub Star

### [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent)
- 发现：2026-07-03
- 一句话：约百行核心的极简 AI 软件工程智能体，可解 GitHub Issue 或在命令行协助开发。
- 摘要：mini-swe-agent 是 SWE-bench 与 SWE-agent 团队推出的极简编码智能体，核心 agent 类约百行 Python，依赖刻意保持轻量。它在 SWE-bench verified 等基准上表现突出，支持本地、Docker、Podman 等多种运行环境，并通过 LiteLLM 等接入多种模型。v2 版本提供迁移指南，强调可部署与可研究的最小实现。
- 标签：`SWE-bench` `极简` `CLI` `Python`
- 来源：GitHub Star


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
