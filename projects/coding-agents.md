# 编码智能体与开发工具

写代码、改仓库、跑命令的编码智能体和开发工具。

## 2026-09

### [OpenRig](https://github.com/mvschwarz/openrig)
- 发现：2026-09-29
- 一句话：用 YAML 定义 Claude Code、Codex 等编码智能体团队，一键启动持久协作的 rig。
- 摘要：OpenRig 把多终端里的 AI 编码会话组织成带角色、共享上下文与分工的团队；向 lead 智能体描述目标，由其协调跨团队专家并汇总待你决策的事项。通过 npm 全局安装 @openrig/cli，依赖 Node.js 22 与 tmux，在 macOS 或 Linux 仓库中启动。提供 TUI 查看席位、运行时、模型与上下文状态。
- 标签：`多智能体` `Claude Code` `Codex` `编排`
- 来源：GitHub Star

### [Piggery](https://github.com/sting8k/piggery)
- 发现：2026-09-29
- 一句话：用单一 Go 二进制与 SQLite 协调 Pi、Claude Code、Codex 等编码智能体团队的本地农场。
- 摘要：任务进入 trough 等待执行，只有真正完成才算 consumed；每个智能体有角色定义的 pen，限制通信对象与是否可 spawn 子 worker，农场自动校验围栏。支持 pi、Claude Code、Codex、omp、dsh、opencode 等 harness 的插件或 MCP 接入，通过 piggery setup 安装到各工具。全部数据本地 SQLite，无云端依赖。
- 标签：`多智能体` `编码智能体` `本地` `Go`
- 来源：GitHub Star

### [agentmemory](https://github.com/rohitg00/agentmemory)
- 发现：2026-09-28
- 一句话：面向 Claude Code、Cursor、Codex 等编码智能体的持久记忆层，基于 iii 引擎。
- 摘要：agentmemory 让编码智能体跨会话记住项目与用户偏好，减少重复解释。支持 Claude Code、GitHub Copilot CLI、Cursor、Gemini CLI、Codex、Hermes、OpenClaw、pi、OpenCode 及任意 MCP 客户端。在 Karpathy LLM Wiki 模式上扩展置信度、生命周期、知识图谱与混合检索等能力。
- 标签：`记忆` `MCP` `编码智能体` `iii`
- 来源：GitHub Star

### [ConnectOnion](https://github.com/openonion/connectonion)
- 发现：2026-09-27
- 一句话：智能体 CLI harness：用 co 命令为 AI 智能体接入邮箱、浏览器、文件与聊天等工具。
- 摘要：ConnectOnion 以单一命令行 co 管理智能体工作所需的账号与集成，包括 Gmail、Outlook、已登录浏览器、文件与聊天应用等。co rem 强调去中心化上下文流，把工作内容中的上下文留在本机并带到下一任务。文档提供 init、email、env、gmail、gcalendar 等子命令说明。
- 标签：`CLI` `harness` `工具集成` `Python`
- 来源：GitHub Star

### [tty7](https://github.com/l0ng-ai/tty7)
- 发现：2026-09-25
- 一句话：纯 Rust 的终端工作台，会话持久并面向编码智能体编排。
- 摘要：tty7 由后台服务持有 shell 与窗格，关闭窗口后会话仍可继续，并支持远程开发场景下的原生 SSH 栈。它可识别多种编码智能体 CLI，提供状态、通知与按仓库划分的 git 上下文。还附带 CLI 与 agent skill，使一个智能体可开 pane、派发任务并读取结果。
- 标签：`终端` `持久会话` `编码智能体` `Rust`
- 来源：GitHub Star

### [mu](https://github.com/qybaihe/mu)
- 发现：2026-09-25
- 一句话：内置判断内核的编码智能体，基于 pi 构建。
- 摘要：mu 把上下文裁剪、命令安全、协作与完成判定等决策交给名为 Jev 的小型快速模型，在每一轮多个决策点作答，大模型专注编码本身。提供命令行 mu 与可下载的 mu desktop 原生应用。项目处于早期开发阶段，名称与配置仍可能变化。
- 标签：`编码智能体` `判断内核` `pi` `CLI`
- 来源：GitHub Star

### [Herdr Projects](https://github.com/eliasstravik/herdr-projects)
- 发现：2026-09-25
- 一句话：Herdr 插件：用协调智能体并行分派多个编码任务线程。
- 摘要：Herdr Projects 在 Herdr 中运行较大项目：你只与一名协调智能体对话，它按任务在独立分支或目录启动工作线程，并为各线程共享目标、指令与记忆。侧边栏汇总待你处理、待评审与进行中的线程。插件免费、MIT 许可，在自有机器上运行，需 Herdr 0.9.1 及以上。
- 标签：`Herdr` `并行任务` `协调器` `编码智能体`
- 来源：GitHub Star

### [Apache Maka (Incubating)](https://github.com/apache/maka)
- 发现：2026-09-24
- 一句话：高性能编码智能体工作台，以完整运行日志记录每一次操作。
- 摘要：Apache Maka 是衡量任务完成度与成本的智能体 harness，在固定模型与官方验证器下发布评测结果。运行时将模型消息、工具调用、权限决策等追加为 RuntimeEvent，界面与恢复均基于该日志。会话与设置在本地，桌面、TUI、CLI 与 Eval 共用同一 Runtime Host。
- 标签：`harness` `事件溯源` `本地优先` `Apache`
- 来源：GitHub Star

### [LazyCodex](https://github.com/code-yeongyu/lazycodex)
- 发现：2026-09-22
- 一句话：面向复杂代码库的 Codex 编码智能体 harness，含记忆、规划与验收。
- 摘要：LazyCodex 在 Codex 内提供项目记忆、规划、执行与可验证的完成流程，定位为复杂代码库上的 agent harness。可通过 npx lazycodex-ai install 一键安装，也支持从 Codex 插件市场实验性安装 OmO 能力。与 Sisyphus Labs 的 OmO 质量取向相关联。
- 标签：`Codex` `harness` `规划` `OmO`
- 来源：GitHub Star

### [brain.md](https://github.com/mindmuxai/brain.md)
- 发现：2026-09-20
- 一句话：面向编码智能体的持久化、基于文件的仓库记忆层与 CLI 标准。
- 摘要：brain.md 提供零依赖 CLI 与开放约定，把项目决策、需求与约束写成仓库内 Markdown，供 Claude Code、Codex 等智能体跨会话读取。在项目中运行 brain init 会脚手架 BRAIN.md 与 brain 目录，并默认接入常见智能体配置。所有写入经 brain CLI 以保证结构一致。
- 标签：`项目记忆` `Markdown` `CLI` `编码智能体`
- 来源：GitHub Star

### [Munder Difflin](https://github.com/HarnessMD/munder-difflin)
- 发现：2026-09-16
- 一句话：在本地用现有订阅协调多台 Claude Code、Codex 等终端编码智能体的多智能体 harness 桌面应用。
- 摘要：Munder Difflin 是开源的多智能体 harness，把你已使用的终端编码 CLI 变成可并行协作的「办公室」智能体。它封装 Claude Code、Codex、Gemini CLI、OpenCode 等多种编码后端，支持本地优先与自带密钥。智能体可互发消息、路由与记忆，并在共享办公室场景中可视化协作。
- 标签：`多智能体` `harness` `Electron` `编码智能体`
- 来源：GitHub Star

### [Solo Agent](https://github.com/solo-agent/solo)
- 发现：2026-09-14
- 一句话：本地优先的人机协作工作台，用频道、任务板与记忆协调多台编码智能体。
- 摘要：Solo Agent 是开源、本地优先的工作空间，让人类与 Claude Code、Codex、OpenCode 等编码智能体在同一处协作。它提供频道、线程、任务板与频道级团队，把散落终端里的工作收成可认领、可评审的任务流。智能体保留长期记忆与固定工作区，减少每次会话重复解释上下文。
- 标签：`工作空间` `多智能体` `本地优先` `编码智能体`
- 来源：GitHub Star

### [Agent Orchestrator](https://github.com/OrchestratorInc/agent-orchestrator)
- 发现：2026-09-13
- 一句话：从规划到合并，在一处规划、运行并监督多台编码智能体团队的桌面工作空间。
- 摘要：Agent Orchestrator 面向需要并行多台编码智能体的项目级开发。添加仓库即可为任务创建 worker 会话，并匹配编码智能体、模型与界面；Git 工作可分配独立分支与 worktree。任务、对话、终端、变更、预览、PR、CI 与评审状态绑定在同一会话中，本地守护进程提供项目级实时视图。
- 标签：`编排` `worktree` `Kanban` `编码智能体`
- 来源：GitHub Star

### [Worktrunk](https://github.com/max-sixty/worktrunk)
- 发现：2026-09-13
- 一句话：面向并行 AI 编码工作流的 Git worktree 管理 CLI。
- 摘要：Worktrunk 让 git worktree 的使用体验接近分支管理，方便同时跑多台 Claude Code、Codex 等智能体。核心命令简化创建、切换与清理 worktree，并支持钩子与构建缓存等配套能力。路径可按模板自动计算，减少重复输入分支名与目录。
- 标签：`Git` `worktree` `CLI` `并行开发`
- 来源：GitHub Star

### [Context Mode](https://github.com/mksglu/context-mode)
- 发现：2026-09-13
- 一句话：通过 MCP 与钩子为编码智能体压缩工具输出、持久化会话记忆并优化上下文路由。
- 摘要：Context Mode 是面向编码智能体上下文窗口问题的 MCP 服务。沙箱化工具调用可把大量原始输出留在窗外，并用 SQLite 与全文检索在压缩后恢复相关编辑、任务与决策。它倡导用脚本代行数据分析以节省上下文，并跨多种客户端通过 MCP 与钩子统一接入。
- 标签：`MCP` `上下文` `记忆` `编码智能体`
- 来源：GitHub Star

### [Empryo](https://github.com/proxysoul/Empryo)
- 发现：2026-09-12
- 一句话：基于代码图谱与 LSP、按符号而非字符串编辑的 AI 编码智能体。
- 摘要：Empryo 在改动前先理解仓库结构与影响范围，并以 AST 级方式按名称替换函数或类。它在同一轮中可运行类型检查、lint 与测试并自行修复，并记录项目级决策与历史问题。提供终端与桌面应用，可通过官网脚本安装。
- 标签：`编码智能体` `LSP` `图谱` `AST`
- 来源：GitHub Star

### [ai-memory](https://github.com/akitaonrails/ai-memory)
- 发现：2026-09-11
- 一句话：为多种编码 CLI 提供跨工具、跨机器的长期记忆与一次性交接协议。
- 摘要：ai-memory 让 Claude Code、Codex、Cursor 等二十余种 harness 共享同一套项目记忆。记忆以 git 支持的 Markdown 维基为源，可自建服务器供团队复用，并带多用户鉴权与审计。生命周期钩子静默记录会话与工具调用，默认路径无需 LLM 即可完成捕获、检索与交接。
- 标签：`记忆` `交接` `编码智能体` `Markdown`
- 来源：GitHub Star

### [Kaku](https://github.com/tw93/Kaku)
- 发现：2026-09-07
- 一句话：基于 WezTerm、为 macOS AI 编码场景预配置字体主题与快捷方式的终端。
- 摘要：Kaku 是面向 AI 友好写作的 macOS 终端，默认集成 JetBrains Mono、深浅色主题与常用 Mac 快捷键。支持分屏、标签、可点击链接、可选 AI 聊天与命令建议，并保留 WezTerm Lua 配置能力。可通过 DMG 或 Homebrew 安装，并用 kaku 命令管理 shell 集成与可选工具。
- 标签：`终端` `macOS` `WezTerm` `AI 编码`
- 来源：GitHub Star

### [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex)
- 发现：2026-09-03
- 一句话：面向 OpenAI Codex CLI 的工作流增强层，提供钩子、智能体团队与 HUD 等能力。
- 摘要：OMX 是 OpenAI Codex CLI 之上的工作流层，保留 Codex 作为执行引擎。默认强化 Codex 会话，并支持从澄清到完成的一致流程，以及 plan、team、code-review 等斜杠命令。项目状态与计划保存在 .omx 目录中。
- 标签：`Codex` `工作流` `CLI` `TypeScript` `智能体团队`
- 来源：GitHub Star

### [portless](https://github.com/vercel-labs/portless)
- 发现：2026-09-02
- 一句话：用稳定命名的本地域名替代端口号，方便人与智能体访问开发中的应用。
- 摘要：portless 为本地开发提供固定名称的 localhost 域名与 HTTPS 反向代理，常见框架可通过 PORT 或自动注入端口参数接入。适合团队与智能体在本地以一致 URL 访问各服务，避免记忆随机端口。
- 标签：`本地开发` `Vercel Labs` `代理` `HTTPS` `开发者工具`
- 来源：GitHub Star


## 2026-08

### [botmux](https://github.com/deepcoldy/botmux)
- 发现：2026-08-26
- 一句话：把飞书消息桥接到 Claude Code、Codex 等编码 CLI，每会话独立进程并流式回传。
- 摘要：botmux 以守护进程监听飞书，为每个新会话拉起独立 CLI 进程，将输出实时流式写入飞书卡片，并提供可写 Web 终端。不重造 Agent 能力，而是桥接二十余种编码 CLI 与 Agent 适配器，支持多机器人在群内分工协作。
- 标签：`飞书` `Claude Code` `Codex` `桥接` `CLI`
- 来源：GitHub Star

### [Wake](https://github.com/iAmCorey/Wake)
- 发现：2026-08-23
- 一句话：用 Rust 与 GPUI 打造的本地桌面应用，集中浏览、全文检索并一键恢复各编码智能体会话。
- 摘要：Wake 把分散在 ~/.claude、~/.codex 等目录里的编码智能体会话只读汇总到同一窗口，支持按智能体与项目分组浏览。内置 SQLite FTS5 全文搜索、逐条消息转录视图，以及一键在终端按原项目目录恢复会话。数据留在本机，并可选用只读 MCP 服务 wake-mcp 供其他客户端检索历史。
- 标签：`会话管理` `桌面应用` `Rust` `全文搜索` `MCP`
- 来源：GitHub Star

### [MoAI-ADK](https://github.com/modu-ai/moai-adk)
- 发现：2026-08-17
- 一句话：面向 Claude Code 的验证驱动智能体编排 harness，提供 SPEC 计划运行同步、质量门与多模型路由。
- 摘要：MoAI-ADK 用 Go 单二进制从外部约束 Claude Code 的规格驱动开发、TRUST 5 质量门与模型加 effort 路由。Factory Mode 将工作拆分为领导者会话与多条车道会话，单张卡片在车道内顺序完成 plan、run、sync。支持多语言界面与 Claude 与 GLM 等多 LLM 成本控制。
- 标签：`Claude Code` `harness` `SPEC` `Go` `多智能体`
- 来源：GitHub Star

### [dsh-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar)
- 发现：2026-08-14
- 一句话：DeepSeek Harness 的侧边栏插件：可编辑代码、终端、Git、子代理与侧边对话等开箱工作台，并开放扩展注册。
- 摘要：dsh-better-sidebar 在 DSH 原生右侧栏注册多种 tab，并提供底部工作台与 ctx.betterSidebar 服务供其他插件注册页面与文件预览器。相较官方侧栏增补可编辑 CodeMirror、增强文件树与 Git 面板、子代理拓扑与 Codex 风格侧边线程等能力。要求 DSH 0.2.0-rc.1 及以上版本。
- 标签：`DSH` `插件` `侧边栏` `Git` `DeepSeek Harness`
- 来源：GitHub Star

### [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)
- 发现：2026-08-13
- 一句话：DeepSeek 开源的智能体 harness，基于一切皆插件架构并由 Cordis 驱动，默认提供 Web UI。
- 摘要：DeepSeek Harness 简称 dsh，采用一切皆插件架构，设计依托 Cordis 时空可组合编程范式。可通过 npx @deepseek-ai/dsh web 启动本地 Web 界面，或从源码构建运行。当前处于开发者预览，可能存在兼容性破坏变更，运行前需阅读安全说明。
- 标签：`DSH` `插件` `Cordis` `Web UI` `DeepSeek`
- 来源：GitHub Star

### [herdr](https://github.com/herdrdev/herdr)
- 发现：2026-08-12
- 一句话：编码智能体运行的终端运行时：后台保活、多机一窗、状态标记，并通过 CLI 供智能体编排窗格。
- 摘要：herdr 在关闭客户端或 SSH 断开后仍通过后台服务保持终端与布局，重启后可恢复布局并续跑受支持的智能体会话。支持本地与远程 SSH 机器统一视图，标记每个窗格的工作、阻塞或空闲状态。不包裹 Claude Code、Codex、Cursor 等工具，而是管理其终端，并提供智能体可调用的 socket API。
- 标签：`终端` `多路复用` `Claude Code` `Rust` `编码智能体`
- 来源：GitHub Star

### [pigo](https://github.com/smallnest/pigo)
- 发现：2026-08-11
- 一句话：用 Go 复刻 pi 的命令行编码智能体，支持无头脚本与交互 REPL、多 Provider 与会话续跑。
- 摘要：pigo 可读写文件、执行命令、检索代码与抓取网页，通过大模型完成需求到改码闭环。兼容 OpenRouter、Ollama、Anthropic 等多种协议网关，内置 read、write、edit、grep、bash 等工具，并支持技能、插件、项目信任与上下文自动压缩。可作为 SDK 嵌入或独立 CLI 使用。
- 标签：`Go` `pi` `编码智能体` `REPL` `技能`
- 来源：GitHub Star

### [Prime Agent](https://github.com/PrimeIntellect-ai/prime-agent)
- 发现：2026-08-08
- 一句话：面向编码与长时自主任务的自改进 RLM 智能体 harness，含递归语言模型与 Continual Harness 状态。
- 摘要：Prime Agent 围绕 Recursive Language Model 将上下文视为变量并在持久 REPL 中以子智能体作函数调用，Continual Harness 则把补充提示、记忆与技能描述存为可证据化更新的持久状态。提供一键安装脚本，适用于一般与长时间运行的编码与研究工作流。
- 标签：`RLM` `编码智能体` `Rust` `长任务` `自改进`
- 来源：GitHub Star

### [Reasonix](https://github.com/esengine/DeepSeek-Reasonix)
- 发现：2026-08-03
- 一句话：面向复杂软件工程任务的可靠开源编码智能体，单 Go 二进制，支持终端、桌面、浏览器与 ACP 编辑器接入。
- 摘要：Reasonix 提供计划模式、权限、工作区沙箱与按轮检查点，便于阅读与撤销长时自主运行。同一本地引擎可通过终端、桌面应用、浏览器或编辑器 ACP 使用。开源 MIT 许可，亦可作为 DeepSeek Harness 生态相关项目维护。
- 标签：`编码智能体` `Go` `沙箱` `ACP` `DeepSeek`
- 来源：GitHub Star

### [cc-haha](https://github.com/NanmiCoder/cc-haha)
- 发现：2026-08-03
- 一句话：本地优先的跨平台 Claude Code 桌面工作台，集成多会话、Worktree、Diff、MCP、Computer Use 与 IM 接入。
- 摘要：cc-haha 在 macOS、Windows、Linux 单一应用中集中多会话与全局搜索、分支或 Worktree 启动、Diff 审阅、浏览器预览与图形化权限审批。支持多模型选择、MCP 与 SubAgent 管理、Agent Teams、Workflow 编排、技能市场、桌面宠物，以及微信、飞书、钉钉、Telegram 等 IM 与 H5 远程访问。macOS 上 Computer Use 可操作其他应用且不占用真实键鼠。
- 标签：`Claude Code` `Electron` `桌面` `Computer Use` `MCP`
- 来源：GitHub Star


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
