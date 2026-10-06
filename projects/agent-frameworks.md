# 智能体框架与编排

多智能体框架、编排层和工作流运行时。

## 2026-10

### [Agent Foundation](https://github.com/converge-ai-labs/agent-foundation)
- 发现：2026-10-01
- 一句话：开源可自托管的智能体基础库与平台，整合托管智能体、记忆、沙箱、电脑使用与持久执行。
- 摘要：又称 a13n，通过 Service 用 API 配置智能体并管理权限与执行恢复；Harness 可嵌入运行时并用插件、自定义工具与提供方扩展；Harness UI 提供终端与 Web playground 试模型与工具。Docker Compose 可拉起 Service、Console、PostgreSQL、Redis 等，无需克隆仓库即可运行。当前为 0.x 活跃开发，API 可能变动。
- 标签：`自托管` `多智能体` `沙箱` `Pydantic AI`
- 来源：GitHub Star

### [OpenShell](https://github.com/NVIDIA/OpenShell)
- 发现：2026-10-01
- 一句话：为自主 AI 智能体舰队提供安全、私有的沙箱运行时，用策略约束文件、系统调用与网络访问。
- 摘要：每个智能体在隔离沙箱中运行，内核级控制限制可访问文件与系统调用，外连须经策略检查；凭证由 OpenShell 注入到获准端点而非暴露给智能体。策略变更前可用形式化验证预判新增风险访问并等待人工审核。提供 CLI 与本地 gateway，支持 Linux、Apple Silicon macOS 与 WSL2 实验环境，通过安装脚本可创建默认沙箱。
- 标签：`沙箱` `策略` `自主智能体` `NVIDIA`
- 来源：GitHub Star


## 2026-09

### [Raven](https://github.com/EverMind-AI/Raven)
- 发现：2026-09-29
- 一句话：面向递归自改进的多智能体 Host，用 DAG 编排内置与第三方智能体完成复杂任务。
- 摘要：Raven 作为 Host Agent 聚合 Raven-Research、Raven-Code、Raven-Design、Raven-Oncall 等内置角色，并支持迭代改进自身 harness 的规划与执行方式。基于 EverOS 在会话间承载记忆与上下文，可自主驱动从需求到交付的多轮规划开发与验证。项目处于 pre-alpha，接口与配置可能快速变化。
- 标签：`多智能体编排` `RSI` `EverOS` `Host Agent`
- 来源：GitHub Star

### [apowerb](https://github.com/apowerb/apowerb)
- 发现：2026-09-26
- 一句话：用于构建、编排与运维生产级 AI 智能体的开源框架。
- 摘要：apowerb 是面向生产环境构建、运行与治理 AI 智能体的开源平台。它覆盖多智能体编排、检索增强与 Text-to-SQL、MCP 服务与内置业务工具，以及邮件与定时触发等运行方式。可用 Docker Compose 或 Helm 自托管部署。
- 标签：`编排` `RAG` `MCP` `自托管`
- 来源：GitHub Star

### [Holon](https://github.com/holon-run/holon)
- 发现：2026-09-25
- 一句话：面向持续性任务的本地智能体工作台，可保存目标并在条件满足时恢复执行。
- 摘要：Holon 是处理持续性工作的本地工作台，用显式 WorkItem 保存目标、计划、进度与等待条件，使任务可跨会话、命令、人工输入与外部事件继续推进。Holon 本身不是智能体，而是为多个智能体提供本地运行环境。支持终端 TUI 与 Web 图形界面两种交互方式。
- 标签：`工作台` `本地优先` `事件驱动` `运行时`
- 来源：GitHub Star

### [Strands Agents](https://github.com/strands-agents/harness-sdk)
- 发现：2026-09-24
- 一句话：用少量代码在 Python 与 TypeScript 中构建生产级 AI 智能体的开源 SDK。
- 摘要：Strands Agents 是在自有进程内运行的开源 SDK，无需托管控制平面，覆盖智能体循环、工具与结构化输出、MCP、多智能体模式、记忆与会话、模型可移植性与流式等能力。还提供护栏、追踪与评测等配套。适合原本要手写 agent loop 的场景。
- 标签：`SDK` `多智能体` `MCP` `Python`
- 来源：GitHub Star

### [Univer](https://github.com/dream-num/univer)
- 发现：2026-09-24
- 一句话：面向 AI 智能体的 Office 能力运行时，集成表格、文档、幻灯片等。
- 摘要：Univer 是可在自有产品中嵌入办公能力的开源 SDK，提供表格、文档、演示等构建块，并强调插件架构、Canvas 渲染、公式引擎与统一 Facade API，可在浏览器与 Node.js 运行。产品族内各办公工具共享存储与计算运行时，人与 AI 智能体可在同一文件中协作。
- 标签：`Office SDK` `表格` `插件` `智能体`
- 来源：GitHub Star

### [Nasiko](https://github.com/Nasiko-Labs/nasiko)
- 发现：2026-09-24
- 一句话：面向编码智能体与 harness 的开源运行时，用于发现、计费统计与模型路由。
- 摘要：Nasiko 作为 OpenRuntime，可发现本机已在运行的编码智能体，将花费统一到同一 schema，并按策略把流量路由到你选择的模型。发现过程默认只读、可不改 harness 配置；上报与路由为显式可选能力。开发者可继续使用原有 harness 命令与界面。
- 标签：`运行时` `路由` `可观测` `Rust`
- 来源：GitHub Star

### [Agent-Native](https://github.com/BuilderIO/agent-native)
- 发现：2026-09-24
- 一句话：为带专用 UI 的智能体应用提供的 TypeScript 框架。
- 摘要：Agent-Native 让同一能力以 action 形式同时供智能体当工具调用、供 UI 从代码调用，共享校验、权限与实现。智能体与界面还共享数据与应用状态，例如当前页面或选中记录。智能体不通过点击 UI 操作，而是与界面走同一 action 层。
- 标签：`TypeScript` `React` `action` `智能体应用`
- 来源：GitHub Star

### [Hindsight](https://github.com/vectorize-io/hindsight)
- 发现：2026-09-23
- 一句话：强调学习与反思的智能体记忆系统，而非仅保存对话历史。
- 摘要：Hindsight 旨在让智能体随时间学习，提供 retain、recall、reflect 等记忆操作，并支持记忆库、心理模型与知识页等概念。可与多种智能体、编码助手及 MCP 集成，也可嵌入式运行或独立起服务。项目提供文档、集成示例与 cookbook。
- 标签：`智能体记忆` `学习` `MCP` `Python`
- 来源：GitHub Star

### [SkillOpt](https://github.com/microsoft/SkillOpt)
- 发现：2026-09-22
- 一句话：在文本空间优化冻结 LLM 智能体可复用自然语言技能的训练器。
- 摘要：SkillOpt 把技能文档当作可训练状态，通过轨迹驱动编辑、验证门控更新与 epoch 式训练流程改进技能，而不改动模型权重。部署产物为紧凑的 best_skill.md，在目标模型与 harness 上直接运行。提供 CLI、WebUI 与 SkillOpt-Sleep 等离线自进化能力。
- 标签：`技能优化` `自进化` `验证门控` `Microsoft`
- 来源：GitHub Star

### [deco Studio](https://github.com/decocms/studio)
- 发现：2026-09-22
- 一句话：面向组织的开源 AI 智能体控制平面与工作空间。
- 摘要：deco Studio 打包模型路由、MCP 鉴权、智能体配置、单点登录、权限、审计与用量核算等企业 rollout 所需能力。通过统一 MCP 端点连接 GitHub、Slack、数据库等工具，令牌存入加密 vault。可本地安装保持私有，也可同步到云端供团队协作。
- 标签：`控制平面` `MCP` `企业` `TypeScript`
- 来源：GitHub Star

### [tRPC-Agent-Go](https://github.com/trpc-group/trpc-agent-go)
- 发现：2026-09-22
- 一句话：用于构建生产级智能体系统的 Go 框架。
- 摘要：tRPC-Agent-Go 在单一 Go 技术栈中提供 LLM 智能体、图工作流、工具调用、会话与记忆、知识检索、自进化、评测与 OpenTelemetry 可观测性。支持 A2A、AG-UI 与 MCP 等协议集成，并包含可复用的 SKILL.md 工作流与安全执行能力。适合需要并发友好、易部署的智能体服务。
- 标签：`Go` `图工作流` `MCP` `可观测性`
- 来源：GitHub Star

### [AX](https://github.com/google/ax)
- 发现：2026-09-21
- 一句话：在集群上声明式编排大规模自主智能体工作负载的运行时。
- 摘要：AX 是基于 Agent Substrate 沙箱的高吞吐声明式编排器，用 Workspace、Task、Model 等 Kubernetes 风格清单描述智能体任务与环境。可为任务预置 Git 仓库、MCP 服务与技能包，并支持挂起恢复与 ssh 进入运行中的沙箱观察。项目仍在快速演进，可能有破坏性变更。
- 标签：`编排` `Kubernetes` `沙箱` `Go`
- 来源：GitHub Star

### [OpenFang](https://github.com/RightNow-AI/openfang)
- 发现：2026-09-18
- 一句话：用 Rust 构建的开源智能体操作系统。
- 摘要：OpenFang 面向自主智能体而非单纯聊天框架，支持按计划持续运行、构建知识图谱与向仪表板汇报等能力。系统编译为单一二进制，通过 init 与 start 启动本地仪表板。核心创新 Hands 是预置的自主能力包，可独立定时执行多阶段任务流程。
- 标签：`Agent OS` `Rust` `自主智能体` `Hands`
- 来源：GitHub Star

### [SwarmForge](https://github.com/unclebob/swarm-forge)
- 发现：2026-09-08
- 一句话：在独立 git worktree 与 tmux 会话中协调多台 AI 智能体并用手递交接的编排工具。
- 摘要：SwarmForge 通过隔离 worktree 与 tmux 运行多台智能体，并以提交物交换耐久交接。操作者用本地仪表盘启动任务、审批关卡、回答澄清并停止蜂群。提供多种 pack 与 forge 安装形态，需 zsh、git、tmux、Babashka 及 grok、codex、claude 或 copilot 等后端之一。
- 标签：`多智能体` `worktree` `tmux` `编排`
- 来源：GitHub Star

### [TeamAI](https://github.com/Tencent/teamai-cli)
- 发现：2026-09-07
- 一句话：把个人 AI 能力沉淀为团队共享的技能、规则与 MCP 等资产的 CLI 与技能体系。
- 摘要：TeamAI 帮助团队在共享 Git 仓库中统一智能体、机器与成员的工作方式。通过 teamai 技能或 CLI 可初始化团队空间、邀请成员加入并共享技能与 MCP 等资源。成员配置完成后打开常用智能体即可加载团队全部 AI 资产，并可用仪表盘查看与管理。
- 标签：`团队` `技能共享` `CLI` `MCP`
- 来源：GitHub Star

### [Evolver](https://github.com/EvoMap/evolver)
- 发现：2026-09-05
- 一句话：基于 GEP 的可审计智能体自进化引擎，管理基因、胶囊与事件。
- 摘要：Evolver 为 AI 智能体提供带 Genes、Capsules 与 Events 的自进化运行时，并与 evomap.ai 生态衔接。它强调可审计的演化过程与记忆、技能资产治理，可通过 npm 安装使用。仓库说明未来版本将转向 source-available，已发布的 MIT 与 GPL 版本仍按原许可使用。
- 标签：`自进化` `GEP` `技能库` `智能体`
- 来源：GitHub Star

### [Docker Agent](https://github.com/docker/docker-agent)
- 发现：2026-09-05
- 一句话：用 YAML 声明式配置构建、运行与分发多智能体团队的 Docker CLI 插件。
- 摘要：docker-agent 作为 docker agent 子命令，让你无需写代码即可定义模型、指令与工具集。支持多智能体分工、内置与 MCP 工具、多模型提供商以及 think、todo、记忆与 RAG 等能力。可将智能体打包推送到 OCI 仓库并在任意环境拉取运行，Docker Desktop 4.63 及以上预装该插件。
- 标签：`Docker` `YAML` `MCP` `多智能体`
- 来源：GitHub Star

### [TrueForge](https://github.com/truefoundry/trueforge)
- 发现：2026-09-05
- 一句话：把大模型变成可运行智能体的开源 harness，含聊天 UI、HTTP API 与沙箱工具。
- 摘要：TrueForge 负责智能体执行循环，涵盖流式调用、会话持久化、MCP、技能、沙箱、审批与上下文管理。可从目录一次配置模型、MCP、技能与沙箱，并通过内置聊天界面、HTTP API 与 TypeScript SDK 接入。支持子智能体、延迟加载工具、大结果卸载与对话压缩等上下文工程能力。
- 标签：`harness` `MCP` `沙箱` `运行时`
- 来源：GitHub Star

### [AURA](https://github.com/mezmo/aura)
- 发现：2026-09-05
- 一句话：可在数分钟内部署、面向生产运维的 SRE 智能体平台。
- 摘要：AURA 是已在生产环境验证的 SRE 智能体平台，通过引导式接入连接现有技术栈，预置智能体团队可结合你已有的模型调查事故。平台负责护栏、API、状态管理、流式输出、失败处理与可观测性，在运维者划定的边界内把大模型接到生产工具上。
- 标签：`SRE` `Rust` `运维` `多智能体` `MCP`
- 来源：GitHub Star

### [AgentTeams](https://github.com/agentscope-ai/AgentTeams)
- 发现：2026-09-05
- 一句话：基于 Matrix 房间、支持人机协同与全程介入的开源多智能体协作运行时。
- 摘要：AgentTeams 是开源的多智能体协作运行时，多个智能体在可审计的房间内协作，人类可全程可见并干预。采用 Manager-Workers 架构，由 Manager 编排多个 Worker 容器，自身不实现智能体逻辑。支持 OpenClaw、QwenPaw、Hermes 等运行时同处一室，并提供 MinIO 共享文件系统与 Matrix 即时通讯集成。
- 标签：`多智能体` `Matrix` `OpenClaw` `编排` `人机协同`
- 来源：GitHub Star

### [Wemux](https://github.com/wemux-ai/wemux)
- 发现：2026-09-03
- 一句话：可自托管的开源智能体协作平台，在隔离工作区于自有 Worker 上执行真实编码任务。
- 摘要：Wemux 是 Apache 2.0 许可、可完全自托管的智能体协作平台。控制面负责规划、路由与审查，实际编码在用户自有 Worker 机器的隔离 Git worktree 中执行，而非云端黑盒。提供主对话编排、看板任务、工作区会话与群组协作等能力。
- 标签：`自托管` `协作` `Worker` `编排` `开源`
- 来源：GitHub Star


## 2026-08

### [OpenHuman](https://github.com/tinyhumansai/openhuman)
- 发现：2026-08-27
- 一句话：以 Rust 为核心的开源智能体 harness，轻量模块化并可插接多种大模型。
- 摘要：OpenHuman 是开源智能体 harness，强调本地优先、隐私与可扩展。提供桌面体验，可接入 MCP，适合作为个人 AI 助手与第二大脑的运行底座。项目自称在效率与成本上针对通用 harness 场景做了优化。
- 标签：`Rust` `harness` `本地优先` `MCP` `个人 AI`
- 来源：GitHub Star

### [FrontierAgent](https://github.com/ApodexAI/FrontierAgent)
- 发现：2026-08-27
- 一句话：面向长程研究与文件型工作的开源智能体运行时、终端产品与评测套件。
- 摘要：FrontierAgent 提供 frontier-agent 终端界面，内置 ReAct 单智能体与 Agent Team 协调多子任务两种工作流。同一引擎也用于官方基准评测，框架、工具与工作流层彼此解耦可复用。支持 macOS 与 Linux 一条命令安装。
- 标签：`智能体框架` `TUI` `ReAct` `多智能体` `评测`
- 来源：GitHub Star

### [OMA](https://github.com/open-multi-agent/open-multi-agent)
- 发现：2026-08-25
- 一句话：可自托管的 TypeScript 智能体运行时，强调持久审批与可离线校验的运行记录。
- 摘要：OMA 面向组织自托管部署，关键操作需经持久、可防篡改的审批，每次运行留下可字节级离线验证的记录。无遥测与托管控制面，模型可用云端或本地推理。可通过 npm create oma-app 脚手架创建 PR 审查或教学等入门智能体。
- 标签：`自托管` `审批` `审计` `TypeScript` `企业`
- 来源：GitHub Star

### [E.D.D.I](https://github.com/labsai/EDDI)
- 发现：2026-08-25
- 一句话：用 JSON 配置驱动、面向对话式 AI 的多智能体编排中间件。
- 摘要：E.D.D.I 是生产级可配置多智能体编排中间件，通过智能路由、持久记忆与 API 编排连接用户、智能体与业务系统而无需手写编排代码。基于 Java 与 Quarkus，内置管理台与聊天界面，支持 MCP、A2A、RAG 与多种 LLM 提供方。
- 标签：`Java` `多智能体` `对话` `MCP` `Quarkus`
- 来源：GitHub Star

### [OpenSRE](https://github.com/Tracer-Cloud/opensre)
- 发现：2026-08-24
- 一句话：用于自建 AI SRE 智能体的开源工具包与训练评测环境。
- 摘要：OpenSRE 帮助团队连接现有运维与可观测工具，自定义工作流并在自有基础设施上回答生产问题。提供 CLI 安装与本地启动方式，整合告警、根因分析与事件处理等 SRE 场景能力。项目处于公开 Alpha，API 可能继续演进。
- 标签：`SRE` `运维` `智能体` `可观测性` `开源`
- 来源：GitHub Star

### [OpenBot](https://github.com/CopilotKit/OpenBot)
- 发现：2026-08-23
- 一句话：可自托管的 AI 同事模板：每位同事拥有独立浏览器、文件与工具，动作事前决策、事后留痕，兼容 AG-UI 智能体。
- 摘要：OpenBot 形态接近常见聊天助手，但设计为在你自己的基础设施上运行并可深度定制。每位同事拥有真实浏览器、独立登录与受控工具，支持通过 AG-UI 接入任意智能体栈。仓库定位为可克隆改造的起步模板而非托管产品，需在本地自行部署与配置。
- 标签：`AG-UI` `自托管` `浏览器自动化` `智能体治理` `TypeScript`
- 来源：GitHub Star

### [QM](https://github.com/yc-software/qm)
- 发现：2026-08-22
- 一句话：面向团队协作的多人智能体 harness，支持 Slack 与 Web，可在自有云环境部署并切换多种底层编码智能体。
- 摘要：QM 为初创团队设计：员工拥有隔离工作区，也可在频道、群聊与项目中与同一智能体协作。每人与每个房间具备独立的作用域记忆、文件、权限、定时任务与持久沙箱。可接入 Pi、OpenCode、Codex、Claude Code 等 harness，组织级可配置可用模型与安全策略。
- 标签：`Slack` `多人协作` `harness` `自托管` `技能`
- 来源：GitHub Star

### [AstrBot](https://github.com/AstrBotDevs/AstrBot)
- 发现：2026-08-18
- 一句话：开源一体化智能体聊天机器人平台，对接多种即时通讯应用与 LLM，支持插件、MCP 与知识库。
- 摘要：AstrBot 为个人、开发者与团队提供可扩展的对话式 AI 基础设施，可快速在 IM 工作流中搭建生产级应用。支持多模态对话、Agent、MCP、Skills、知识库、人设与自动上下文压缩。可对接 QQ、企业微信、飞书、钉钉、Telegram、Slack 等多平台，并集成 Dify、阿里云百炼、Coze 等外部智能体平台。
- 标签：`聊天机器人` `IM` `插件` `MCP` `Python`
- 来源：GitHub Star

### [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit)
- 发现：2026-08-14
- 一句话：面向自主 AI 智能体的治理工具包：策略执行、零信任身份、沙箱与可靠性工程，覆盖 OWASP Agentic Top 10。
- 摘要：Agent Governance Toolkit 通过 pip 安装，可与任意智能体框架配合，回答动作是否允许、哪一智能体执行、以及如何防篡改审计。提供策略引擎、身份与执行沙箱等控制面，而非仅依赖提示词层面的安全请求。当前为公开预览阶段，GA 前可能有破坏性变更。
- 标签：`治理` `安全` `策略` `Python` `微软`
- 来源：GitHub Star

### [Mastra](https://github.com/mastra-ai/mastra)
- 发现：2026-08-13
- 一句话：现代 TypeScript 框架，用于构建 AI 应用与智能体，含模型路由、工作流、记忆与评测能力。
- 摘要：Mastra 帮助团队从原型到生产构建可靠的 AI 产品与智能体，可嵌入 React、Next.js、Node 或独立部署。提供统一模型路由、自主智能体、图式工作流、人机协同挂起恢复，以及对话历史、RAG 与 Observational Memory 等上下文管理。集成 MCP、评测与多种前端智能体 UI 库。
- 标签：`TypeScript` `工作流` `智能体` `评测` `MCP`
- 来源：GitHub Star

### [Semantica](https://github.com/semantica-agi/semantica)
- 发现：2026-08-12
- 一句话：面向上下文与可问责 AI 的图原生基础设施：摄入数据、构建知识图并做确定性推理与溯源。
- 摘要：Semantica 帮助开发者将企业数据转为上下文图与知识图，并在其上运行图分析与因果推理，强调决策溯源与可解释性。支持多语言图存储、RDF 与 LPG 及 W3C 相关标准，可通过 pip install semantica 使用。定位为开源、可治理的知识基础设施，面向高监管场景。
- 标签：`知识图谱` `上下文工程` `RAG` `Python` `可解释 AI`
- 来源：GitHub Star

### [Shepherd](https://github.com/shepherd-agents/shepherd)
- 发现：2026-08-10
- 一句话：将智能体执行记录为可逆、可分叉 Git 式追踪的运行时基底，供元智能体观察、回放与回滚。
- 摘要：Shepherd 为需要检查、可逆与监督的智能体工作提供 durable 执行追踪，并保留工作区产出供审阅后再应用或丢弃。任务体可以是沙箱化智能体，其改动以可审提案形式返回，接受前不写入你的文件。在 macOS 与 Linux 上执行 OS 级权限约束，要求 Python 3.11 以上。
- 标签：`元智能体` `可逆执行` `沙箱` `追踪` `Python`
- 来源：GitHub Star

### [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)
- 发现：2026-08-03
- 一句话：可用单个 Rust 二进制配置运行的个人 AI 助手智能体运行时。
- 摘要：ZeroClaw 是智能体运行时，以单个 Rust 二进制形式配置并运行。它连接多家大模型提供商，经 Discord、Telegram、Matrix、邮件、语音、Webhook 与 CLI 等渠道对外交互，并通过 Shell、浏览器、HTTP、硬件与自定义 MCP 等工具执行动作。一切可在本机、使用自有密钥与工作区运行。
- 标签：`智能体运行时` `Rust` `自托管` `MCP` `多渠道`
- 来源：GitHub Star

### [GoRaven](https://github.com/8treenet/goraven)
- 发现：2026-08-02
- 一句话：面向团队的开源自托管 AI Harness，为成员提供独立智能体工作区。
- 摘要：GoRaven 为团队每人提供隔离的智能体工作区，智能体可读文件、写代码、跑命令、调 API、检索知识库并交付结果而非仅聊天。支持团队共享项目与技能库，管理员可管控模型配额、工具权限与数据访问。可 Docker 一键自托管，并接入 MCP 工具链与 RAG 知识。
- 标签：`自托管` `团队` `Harness` `RAG` `技能市场`
- 来源：GitHub Star

### [NanZi](https://github.com/RandyChen1985/nanzi-ai-agent-platform)
- 发现：2026-08-02
- 一句话：面向企业场景的开源多智能体编排与 ChatBI 平台。
- 摘要：NanZi 智能体平台聚焦企业级对话协作、多 Agent 编排与工具调用，并提供 RAG 知识库、长期记忆与 Redis 会话引擎。平台支持 Local、Docker、K8s、E2B、SSH 等多策略代码沙箱，以及持久化浏览器会话与企业级 ChatBI 数据洞察。同时提供 MCP 双向集成、Embed 挂件与 RBAC 权限管控。
- 标签：`企业级` `多智能体` `ChatBI` `RAG` `沙箱`
- 来源：GitHub Star

### [Open Mercato](https://github.com/open-mercato/open-mercato)
- 发现：2026-08-02
- 一句话：面向 CRM 与 ERP 的 TypeScript AI 工程基础框架，内置领域模块与智能体技能。
- 摘要：Open Mercato 解决 AI 代码助手只生成代码却不决定分层与一致性的问题，提供架构感知的 AI harness、随仓库交付的 spec-first 开发，以及面向代码审查与协作流程的技能。它附带可复用的 CRM、ERP 与电商等领域模块，开源可自托管，面向已使用 Cursor 或 Copilot 但仍需工程约束的团队。
- 标签：`TypeScript` `CRM` `ERP` `AI harness` `spec-first`
- 来源：GitHub Star

### [Output](https://github.com/growthxai/output)
- 发现：2026-08-02
- 一句话：用于构建 AI 工作流与智能体的开源 TypeScript 框架。
- 摘要：Output 将提示词、评测、追踪、成本统计、编排与凭据管理整合进同一代码库内的 TypeScript 框架，面向 Claude Code 等编码智能体可读写的工作流文件夹结构。它支持版本化的 .prompt 文件、自动追踪 LLM 与 HTTP 步骤，并提供 LLM-as-judge 评测与多提供商统一 API。
- 标签：`工作流` `TypeScript` `评测` `追踪` `Claude Code`
- 来源：GitHub Star


## 2026-07

### [HyperFrames](https://github.com/heygen-com/hyperframes)
- 发现：2026-07-29
- 一句话：将 HTML、CSS 与动画确定性渲染为 MP4 视频的开源框架，面向编码智能体。
- 摘要：HyperFrames 用 HTML、CSS、媒体与可 seek 动画生成确定性 MP4，可在本地 CLI、AI 编码 agent 技能或托管创作流程中使用。为 Claude Code 等提供插件与 skills 安装路径，并附带 Studio 与文档站点。口号为 Write HTML、Render video、Built for agents。
- 标签：`视频渲染` `HTML` `TypeScript` `skills` `FFmpeg`
- 来源：GitHub Star

### [CopilotKit](https://github.com/CopilotKit/CopilotKit)
- 发现：2026-07-25
- 一句话：构建智能体原生应用与 Generative UI 的前端 SDK，并推动 AG-UI 协议。
- 摘要：CopilotKit 提供 React、Angular、Vue、React Native 以及 Slack 与 Microsoft Teams 等表面的 agent 集成能力，涵盖生成式 UI、共享状态与人机协同工作流。团队维护 AG-UI 协议，用于连接各类 agent 框架与用户界面。生产场景可叠加 CopilotKit Intelligence 以持久线程、用户记忆与从使用中学习的 agent。
- 标签：`React` `Generative UI` `AG-UI` `SDK` `Slack`
- 来源：GitHub Star

### [IntentKit](https://github.com/crestalnetwork/intentkit)
- 发现：2026-07-25
- 一句话：开源自托管的云原生智能体集群，管理协作式 AI 团队。
- 摘要：IntentKit 定位为云端运行的 agent 集群，相较本地优先方案更省本机资源并便于免维护部署。特性包括多 agent 互调、默认安全配置使 agent 无法直接访问密钥、可选 Web3 集成、社交媒体连接与可扩展技能系统。也可作为 Python 库导入或通过内置 API 被外部应用调用。
- 标签：`云原生` `多智能体` `自托管` `Web3` `Python`
- 来源：GitHub Star

### [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)
- 发现：2026-07-24
- 一句话：基于 Qwen 的 LLM 应用开发框架，含工具调用、MCP 与示例应用。
- 摘要：Qwen-Agent 面向指令跟随、工具使用、规划与记忆等能力构建 LLM 应用。仓库附带浏览器助手、代码解释器、自定义助手等示例，并作为 Qwen Chat 的后端。文档与评测基准 DeepPlanning 等随仓库维护。
- 标签：`Qwen` `Function Calling` `MCP` `RAG` `示例应用`
- 来源：GitHub Star

### [Open Agent SDK（OasAIStudio）](https://github.com/OasAIStudio/open-agent-sdk)
- 发现：2026-07-24
- 一句话：轻量通用的 TypeScript 智能体运行时，定位为 Claude Agent SDK 的开源替代。
- 摘要：Open Agent SDK 提供可阅读、可扩展的 MIT 核心运行时，统一会话、工具、钩子、子智能体与多模型接入。支持权限模式、按工具门控与生命周期钩子，并内置本地 SWE-bench 与 Terminal-bench 评测 harness。可通过 npx open-agent-sdk init 脚手架启动项目。
- 标签：`TypeScript` `智能体运行时` `多模型` `MCP` `开源`
- 来源：GitHub Star

### [Orloj](https://github.com/OrlojHQ/orloj)
- 发现：2026-07-24
- 一句话：用 YAML 声明智能体、工具与策略的多智能体编排与治理运行时。
- 摘要：Orloj 将模型路由、工具权限、凭证、记忆、审批、调度、Webhook、追踪与部署等视为可版本化的基础设施资源。团队以声明式清单描述期望状态，由平台调度执行、路由与治理。文档称其覆盖从开发到生产的完整智能体栈，API 在 1.0 前可能变动。
- 标签：`YAML` `多智能体` `编排` `治理` `可观测`
- 来源：GitHub Star

### [Agno](https://github.com/agno-agi/agno)
- 发现：2026-07-23
- 一句话：用于构建、运行与管理智能体平台的框架与 AgentOS 运行时。
- 摘要：Agno 提供 SDK 构建智能体，并以 AgentOS 作为服务运行时，配合 Web UI 管理平台。强调数据、记忆与安全姿态由团队自持，并可通过模拟与使用数据形成学习闭环。官方引导通过 agentos 系列模板在 Docker 等环境拉起 REST API、Postgres、MCP 与控制面。
- 标签：`AgentOS` `智能体平台` `Python` `自托管` `MCP`
- 来源：GitHub Star

### [Griptape](https://github.com/griptape-ai/griptape)
- 发现：2026-07-23
- 一句话：用于构建生成式 AI 应用与智能体工作流的模块化 Python 框架。
- 摘要：Griptape 用 Agent、Pipeline 与 Workflow 等结构组织任务，并配套对话记忆、任务记忆与元数据记忆抽象。通过 Driver 层对接 LLM、检索、规则集与外部服务，便于替换提供商而不重写业务逻辑。文档亦指向 Griptape Nodes 可视化桌面产品作为无代码补充。
- 标签：`Python` `工作流` `RAG` `记忆` `Driver`
- 来源：GitHub Star

### [iii](https://github.com/iii-hq/iii)
- 发现：2026-07-23
- 一句话：用统一实时运行时组合、发现、扩展与观测各类后端 Worker 的引擎。
- 摘要：iii 让队列、cron、HTTP、状态、观测与智能体等能力通过同一 live catalog 互联，Worker 注册触发器与函数后即可被其他 Worker 调用。智能体可在缺能力时动态添加 Worker 并追踪调用链。提供 compose 命令拉起命名空间，并在 workers.iii.dev 浏览可用 Worker。
- 标签：`运行时` `Worker` `可组合` `Rust` `多语言 SDK`
- 来源：GitHub Star

### [clawhive](https://github.com/longzhi/clawhive)
- 发现：2026-07-22
- 一句话：Rust 编写的轻量 AI 智能体平台，单二进制部署多聊天渠道机器人。
- 摘要：clawhive 定位为 OpenClaw 的开源 Rust 替代，约十四兆单文件、无 Node 与 Docker 运行时依赖。可通过 Web 或终端向导配置提供商、智能体与 Telegram、Discord、飞书等渠道。CLI 提供 chat、start、schedule、task trigger 与配置热重载等命令。
- 标签：`Rust` `多渠道` `自托管` `OpenClaw` `单二进制`
- 来源：GitHub Star

### [LoopX](https://github.com/loopx-project/loopx)
- 发现：2026-07-21
- 一句话：面向长程智能体与团队的本地优先控制平面，用持久状态核保持任务跨会话推进。
- 摘要：LoopX 为 Codex、Claude Code 等运行时提供可恢复的目标、决策与证据，减少人工盯进度。支持个人 Agent Workspace 管理项目、日程与待决事项，并与 LHTB 等长程基准评测联动展示收益。通过 pip 安装 loopx 并安装 workflow skills 后可在 Codex App 用 $loopx 触发心跳式推进。
- 标签：`控制平面` `长程任务` `Codex` `本地优先` `多智能体`
- 来源：GitHub Star

### [Pipelex](https://github.com/Pipelex/pipelex)
- 发现：2026-07-18
- 一句话：用编码智能体搭建可复用的 AI 方法，并以 MCP、网页或 API 运行。
- 摘要：Pipelex 让你用自然语言描述流程，由编码智能体通过插件把 expertise 建成多步骤、确定性的 method，可串联 LLM、OCR、图像生成等。建成后可作为团队网页、面向客户的 SaaS、聊天机器人的 MCP，或软件 API 调用。
- 标签：`编排` `MCP` `自托管` `FastAPI`
- 来源：GitHub Star

### [Flyto2 Core](https://github.com/flytohub/flyto-core)
- 发现：2026-07-17
- 一句话：面向 AI 智能体的 Python 执行引擎，分步记录浏览器与 API 操作并可断点重放。
- 摘要：Flyto2 Core 把浏览器与 API 工作拆成显式步骤，记录每步输入输出与耗时，失败时可从指定步骤重放而无需整任务重跑。内置大量注册模块，覆盖触发器、队列、浏览器自动化、API 调用、数据变换、校验与文件等场景。
- 标签：`工作流` `浏览器自动化` `重放` `Python`
- 来源：GitHub Star

### [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- 发现：2026-07-11
- 一句话：面向团队的 AI 智能体记忆中枢，把对话与文档沉淀为可复用记忆资产。
- 摘要：TencentDB Agent Memory 将对话、文档与代码整理为聊天记忆、技能、LLM-Wiki 与代码图谱等四类可治理、可共享的资产。通过 Proxy 统一接入多种智能体框架，无需改协议即可共用同一记忆服务。
- 标签：`记忆` `团队` `向量` `自托管`
- 来源：GitHub Star

### [MetaHarness](https://github.com/ruvnet/metaharness)
- 发现：2026-07-11
- 一句话：元脚手架，从任意仓库生成带 CLI、MCP、记忆与技能的定制智能体 harness。
- 摘要：metaharness 用 npx 在浏览器或本地为 GitHub 仓库或空白项目生成专属智能体脚手架，包含项目级 CLI、MCP 服务、记忆命名空间、技能与治理策略。产出可发布的 npm 包形态 harness，可接入 Claude Code、Codex、Hermes 等多种宿主。
- 标签：`脚手架` `MCP` `多智能体` `CLI`
- 来源：GitHub Star

### [elizaOS](https://github.com/elizaOS/eliza)
- 发现：2026-07-11
- 一句话：开源自主 AI 智能体操作系统与 TypeScript 框架单体仓库。
- 摘要：elizaOS 提供自主 AI 智能体的核心运行时、Eliza 应用、CLI、云服务与首批插件等完整产品栈。可从源码用 Bun 安装运行，也支持构建智能体、插件以及面向整机的 elizaOS 分发。
- 标签：`框架` `插件` `TypeScript` `自主智能体`
- 来源：GitHub Star

### [kagent](https://github.com/kagent-dev/kagent)
- 发现：2026-07-06
- 一句话：在 Kubernetes 上构建、部署与管理 AI 智能体的云原生框架。
- 摘要：kagent 是 Kubernetes 原生的 AI 智能体框架，利用 Kubernetes 编排能力在集群中构建、部署与管理智能体。框架强调易理解、易使用，并提供灵活的智能体构建方式。文档提供首个智能体入门与安装指南，并围绕 Agents 等核心概念组织技术说明。
- 标签：`Kubernetes` `云原生` `智能体框架` `CNCF`
- 来源：GitHub Star

### [AgentFactory](https://github.com/zzatpku/AgentFactory)
- 发现：2026-07-06
- 一句话：把成功任务沉淀为可执行子智能体代码并持续自我演化的框架。
- 摘要：AgentFactory 将成功任务方案保存为可执行的子智能体 Python 代码，而非纯文本经验，并依据执行反馈持续 refine。保存的子智能体带标准化文档，可在任意支持 Python 的环境间移植。框架经历 Install、Self-Evolve、Deploy 三阶段，含 Meta-Agent 编排、分层 Skill 体系与隔离工作区管理。
- 标签：`子智能体` `自我演化` `Python` `ACL`
- 来源：GitHub Star

### [Deep Researcher Agent](https://github.com/Xiangyue-Zhang/auto-deep-researcher-24x7)
- 发现：2026-07-03
- 一句话：可 24 小时自主运行深度学习实验的 AI 智能体。
- 摘要：Deep Researcher Agent 面向深度学习实验的 24 小时自主运行，采用 Leader-Worker 架构与恒定规模记忆设计。README 说明可通过配置项选用 DeepSeek、通义、Kimi、智谱等国内大模型 API 预设，并支持 Slurm 集群作为实验执行后端。监控会读取作业真实终态，避免失败运行被误记为完成。
- 标签：`深度学习` `实验自动化` `自主智能体` `MLOps`
- 来源：GitHub Star

### [GNAP](https://github.com/farol-team/gnap)
- 发现：2026-07-03
- 一句话：仅用 Git 仓库协调多 AI 智能体协作的 Git-Native Agent Protocol。
- 摘要：GNAP 让 OpenClaw、Codex、Claude Code 或自定义智能体通过共享 Git 仓库组队协作，无需独立服务器或数据库。协议在 .gnap 目录用 agents、tasks、runs、messages 等 JSON 文件描述团队与任务，智能体按心跳拉取、执行、提交并推送。Git 历史即审计日志，人类与 AI 均为一等参与者。
- 标签：`多智能体` `Git` `编排` `协议`
- 来源：GitHub Star

### [Flowise](https://github.com/FlowiseAI/Flowise)
- 发现：2026-07-02
- 一句话：可视化低代码搭建 AI 智能体与工作流的 Node 应用。
- 摘要：Flowise 用可视化界面编排智能体与自动化流程。仓库包含 server、ui、components 等模块，README 给出本地启动方式。README 注明项目已归档，并指向后续方向的讨论。
- 标签：`低代码` `可视化` `LangChain` `已归档`
- 来源：GitHub Star


## 2026-06

### [OxyGent](https://github.com/jd-opensource/OxyGent)
- 发现：2026-06-27
- 一句话：用 Oxy 抽象把工具、模型与智能体模块化的多智能体 Python 框架。
- 摘要：OxyGent 是开源 Python 框架，将工具、模型与智能体统一为可组合的 Oxy 组件，提供透明端到端流水线以构建、运行与演化多智能体系统。强调高效开发、智能协作、弹性拓扑、持续评估进化与分布式调度扩展。文档面向快速组装生产级智能系统，并提供 Java 版 JDOxyGent4J 姊妹仓库链接。
- 标签：`多智能体` `模块化` `Python` `京东`
- 来源：GitHub Star

### [Eino](https://github.com/cloudwego/eino)
- 发现：2026-06-26
- 一句话：Go 语言的 LLM 应用与智能体开发框架，含组件、ADK 与图编排。
- 摘要：Eino 借鉴 LangChain、Google ADK 等思路，按 Go 习惯提供 ChatModel、Tool、Retriever 等可复用组件及官方多种模型实现。Agent Development Kit 支持工具调用、多智能体协作、上下文管理与人机协同中断恢复。还可把组件连成 graph 或 workflow 独立运行，或作为智能体工具暴露。
- 标签：`Go` `LLM` `ADK` `CloudWeGo`
- 来源：GitHub Star


## 2026-05

### [Ragent](https://github.com/nageoffer/ragent)
- 发现：2026-05-26
- 一句话：面向 Agentic RAG 的 Java 生产级平台，覆盖入库、检索、记忆与 MCP 工具。
- 摘要：Ragent 提供从文档解析到智能问答的 Agentic RAG 全链路，包括向量、关键词、图谱与联网的混合检索及 RRF 融合。支持问题重写、意图识别、多知识库路由、会话摘要记忆与 Redis 流量保护。集成 AgentScope MCP 工具发现调用，并提供入库 Pipeline、溯源、反馈 Trace 与管理后台。
- 标签：`RAG` `Java` `MCP` `企业级`
- 来源：GitHub Star

### [Nexus Agent](https://github.com/java-up-up/nexus-agent)
- 发现：2026-05-18
- 一句话：企业级 AI 智能体平台，覆盖对话、RAG、MCP、Skills 与文档治理全链路。
- 摘要：Nexus Agent 提供智能对话、文档问答、联网搜索、RAG、MCP 工具与 Skills 扩展及 Harness 控制与会话记忆。采用三层执行器体系，在确定性编排之后按场景选择追问、知识问答或 ReAct Agent。包含 Neo4j 文档结构图谱、双通道混合检索、证据预算与无证据短路、Parent-Child 切块及 Tika 解析入库等工程化模块。
- 标签：`RAG` `Spring` `MCP` `Skills`
- 来源：GitHub Star


## 2026-04

### [Open Deep Research](https://github.com/langchain-ai/open_deep_research)
- 发现：2026-04-07
- 一句话：可配置的开源深度研究智能体，支持多模型、搜索与 MCP。
- 摘要：Open Deep Research 是深度研究类智能体应用，可在多种模型提供商、搜索工具与 MCP 服务上运行。用户可通过 LangGraph 本地启动并在 Studio UI 中交互。仓库 README 说明环境配置、依赖安装与近期更新，并指向相关课程与评测基准。
- 标签：`深度研究` `LangGraph` `开源` `已归档` `MCP`
- 来源：GitHub Star

### [DeerFlow](https://github.com/bytedance/deer-flow)
- 发现：2026-04-06
- 一句话：开源长时程 SuperAgent harness，可研究、写代码并创作内容。
- 摘要：DeerFlow 2.0 是全新编写的超级智能体 harness，编排子智能体、记忆、沙箱与可扩展技能，处理从数分钟到数小时的任务。借助工具、技能与子智能体完成深度探索与高效研究流。官方站点提供案例演示，1.x 深度研究框架在独立分支维护。
- 标签：`SuperAgent` `harness` `多智能体` `沙箱` `LangGraph`
- 来源：GitHub Star

### [GPT Researcher](https://github.com/assafelovic/gpt-researcher)
- 发现：2026-04-03
- 一句话：面向任意任务的自主深度研究智能体，可产出带引用的报告。
- 摘要：GPT Researcher 是开源深度研究智能体，面向网页与本地数据生成详细、有据可查的研究报告。架构采用 planner 与 execution 智能体分工，并由 publisher 汇总成文。支持高度定制以构建领域研究智能体，并可安装为 Claude Skill 在对话中调用。
- 标签：`深度研究` `自主智能体` `报告` `网页研究` `Python`
- 来源：GitHub Star

### [Full-Stack AI Agent Template](https://github.com/vstorm-co/full-stack-ai-agent-template)
- 发现：2026-04-03
- 一句话：带 AI 智能体、RAG 与企业集成的 FastAPI 加 Next.js 全栈项目生成器。
- 摘要：该项目通过生成器产出生产向的 FastAPI 与 Next.js 应用，内置多种智能体框架选项、RAG 流水线、WebSocket 流式聊天与二十余项集成。涵盖 JWT、OAuth、管理面板、Celery 与 Docker 等能力，并支持 Milvus、Qdrant、pgvector、ChromaDB 等向量存储。可通过 PyPI 包 fastapi-fullstack 快速脚手架。
- 标签：`项目模板` `全栈` `RAG` `FastAPI` `Next.js`
- 来源：GitHub Star

### [Open Agent SDK（codeany-ai）](https://github.com/codeany-ai/open-agent-sdk-typescript)
- 发现：2026-04-01
- 一句话：进程内运行完整智能体循环的开源 TypeScript Agent SDK。
- 摘要：Open Agent SDK 无需子进程或外部 CLI 即可在进程内执行智能体循环，支持 Anthropic 与 OpenAI 兼容 API，可部署到云、Serverless、Docker 或 CI。提供 query 流式接口与 createAgent 多轮对话，并自动识别多种 OpenAI 兼容模型类型。亦提供 Go 语言版本。
- 标签：`Agent SDK` `TypeScript` `进程内` `OpenAI` `Anthropic`
- 来源：GitHub Star


## 2026-03

### [TinyTroupe](https://github.com/microsoft/TinyTroupe)
- 发现：2026-03-29
- 一句话：基于大模型的多智能体人格模拟库，用于商业洞察与想象增强。
- 摘要：TinyTroupe 用 LLM 模拟具个性、兴趣与目标的 TinyPerson 智能体，在 TinyWorld 环境中互动，侧重仿真而非直接辅助用户。适用于广告离线评估、系统测试输入、合成数据生成与产品管理情景探索等。库提供论文预印本与公开实验材料。
- 标签：`多智能体` `人格模拟` `LLM` `仿真` `Python`
- 来源：GitHub Star

### [Deep Agents](https://github.com/langchain-ai/deepagents)
- 发现：2026-03-18
- 一句话：开箱即用的开源智能体 harness，基于 LangGraph 可扩展替换各组件。
- 摘要：Deep Agents 是偏工程化的智能体运行时，默认面向长程多步任务，可与支持工具调用的各类模型配合。内置子智能体、可插拔文件系统、上下文摘要与工具输出落盘、沙箱命令执行、持久记忆、人机审批与按需加载 Skills，并支持 MCP 与自定义工具。
- 标签：`LangGraph` `harness` `子智能体` `MCP`
- 来源：GitHub Star

### [InsForge](https://github.com/InsForge/InsForge)
- 发现：2026-03-11
- 一句话：面向智能体编码的一体化开源后端，为编码智能体提供数据库、鉴权与托管等能力。
- 摘要：InsForge 让编码智能体像后端工程师一样操作基础设施：通过自托管或云端的 MCP 服务，以及云端的 CLI 与 Skills 读取文档与 schema、查看日志，并部署函数、迁移数据库、配置存储与鉴权等。平台集成认证、数据库、存储、边缘函数、模型网关、计算与部署等原语。
- 标签：`BaaS` `智能体编码` `MCP` `PostgreSQL`
- 来源：GitHub Star

### [CLI-Anything](https://github.com/HKUDS/CLI-Anything)
- 发现：2026-03-10
- 一句话：为各类软件生成可供智能体调用的 CLI harness 与社区 CLI-Hub。
- 摘要：CLI-Anything 旨在让现有软件以命令行形式被 AI 智能体操作，并提供 CLI-Hub 浏览、安装与管理社区构建的 CLI。README 展示智能体借助生成 CLI 与预览循环完成 CAD、3D、字幕等真实产出，并欢迎贡献新 CLI 或提交愿望单。
- 标签：`CLI` `Agent-Native` `harness` `CLI-Hub`
- 来源：GitHub Star

### [Paperclip](https://github.com/paperclipai/paperclip)
- 发现：2026-03-05
- 一句话：用任务看板编排多智能体团队、预算与目标的开源工作台。
- 摘要：Paperclip 是 Node 服务加 React 界面，用于为商业目标组建多角色智能体并跟踪工作与成本。支持为各智能体选择模型与 harness，同时统一管理任务、技能、权限与历史。README 将其类比为管理 AI 员工的公司层，而非单一代码仓库助手。
- 标签：`多智能体` `编排` `目标管理` `OpenClaw`
- 来源：GitHub Star


## 2026-02

### [OpenViking](https://github.com/volcengine/OpenViking)
- 发现：2026-02-14
- 一句话：面向 AI 智能体的开源上下文数据库，统一承载知识、记忆与技能。
- 摘要：OpenViking 是面向 AI 智能体的上下文数据库，把智能体所需的知识、记忆与技能放在同一套虚拟文件系统中组织。智能体可用类似浏览文件的方式列出、读取、写入与检索上下文，便于人工检查与编辑智能体所知内容。项目定位为可自进化的上下文基础设施，用于融合记忆、知识检索与技能管理。
- 标签：`智能体` `记忆` `RAG` `上下文` `知识库`
- 来源：GitHub Star

### [Refly](https://github.com/refly-ai/refly)
- 发现：2026-02-03
- 一句话：开源的智能体技能构建平台，用可视化工作流定义可版本化、可导出的原子技能。
- 摘要：Refly 定位为首个开源的智能体技能构建平台，把企业 SOP 编译成稳定、原子化且可版本管理的可执行技能，而非一次性提示词。技能可在 Refly 中一键运行，也可导出到 Claude Code、Cursor、Codex 等环境，或部署为 API 与 Slack、飞书等机器人。提供自托管部署指南、托管工作区与官方技能注册库。
- 标签：`技能构建` `工作流` `自动化` `Claude Code` `开源平台`
- 来源：GitHub Star


## 2026-01

### [Agent Kit](https://github.com/leemysw/agent-kit)
- 发现：2026-01-19
- 一句话：基于 Claude Agent SDK 的全栈智能体开发框架，含 FastAPI 后端与 Next.js 前端。
- 摘要：Agent Kit 帮助开发者快速构建、部署与扩展生产级 AI Agent 应用，深度集成 Claude Agent SDK 并支持流式响应。内置 WebSocket 实时通信，以及 Discord、Telegram 等多渠道接入与统一会话路由。采用工作区 JSON 或 JSONL 文件存储，并提供多 Agent 管理与正在扩展的工具、MCP 与技能支持。
- 标签：`智能体框架` `Claude SDK` `FastAPI` `Next.js` `多渠道`
- 来源：GitHub Star

### [graph-rag-agent](https://github.com/1517005260/graph-rag-agent)
- 发现：2026-01-16
- 一句话：融合 GraphRAG、LightRAG 与 DeepSearch 的私域问答与多智能体推理系统实现。
- 摘要：项目结合 GraphRAG 与私域 Deep Search，构建可解释、可推理的智能问答方案，并整合多 Agent 协作与知识图谱增强。核心包包含多种 Agent 实现、图谱构建与社区摘要、文档摄取管道，以及针对 GraphRAG 的评估框架。适合需要自建知识图谱检索、深度研究与多智能体编排的团队学习与二次开发。
- 标签：`GraphRAG` `RAG` `知识图谱` `智能体` `评估`
- 来源：GitHub Star

### [KAG](https://github.com/OpenSPG/KAG)
- 发现：2026-01-16
- 一句话：基于 OpenSPG 与大模型的逻辑形式引导推理与检索框架，用于垂直领域知识库问答。
- 摘要：KAG 在 OpenSPG 引擎与 LLM 之上构建逻辑推理与问答方案，缓解传统 RAG 向量相似度歧义与 OpenIE 类 GraphRAG 噪声问题。支持知识与文本块互索引、概念语义对齐、Schema 约束的知识构建，以及逻辑形式引导的混合推理与多跳问答。目标是在专业领域提供知识增强、可事实核验的 LLM 服务框架。
- 标签：`知识图谱` `推理` `RAG` `OpenSPG` `问答`
- 来源：GitHub Star

### [AWorld](https://github.com/inclusionAI/AWorld)
- 发现：2026-01-12
- 一句话：面向领域专家的智能体 Harness 平台，用于编排工具、记忆与执行并沉淀技能。
- 摘要：AWorld 提供完整的 Agent Harness，用于编排智能体的工具、记忆、上下文与执行，帮助将领域知识编码为可复用技能与自主智能体舰队。平台强调从专家经验到可重复生产能力的转化，并展示深度搜索、应用创建等示例配方。
- 标签：`智能体框架` `Harness` `技能`
- 来源：GitHub Star

### [MiroFlow](https://github.com/MiroMindAI/MiroFlow)
- 发现：2026-01-11
- 一句话：MiroMind 研究智能体项目的开源框架实现，面向多步联网深度研究任务。
- 摘要：本仓库是 MiroMind 研究智能体项目的官方实现之一，提供可复现的研究智能体框架 MiroFlow，用于处理未来事件预测等需要多步互联网检索的复杂问题。README 将其与 MiroThinker 模型及 MiroVerse 训练数据并列介绍，并提供快速上手与 Web 演示入口。
- 标签：`研究智能体` `深度研究` `开源框架`
- 来源：GitHub Star

### [MiroThinker](https://github.com/MiroMindAI/MiroThinker)
- 发现：2026-01-11
- 一句话：面向复杂研究与预测任务的深度研究智能体及模型系列。
- 摘要：MiroThinker 是优化研究与预测场景的深度研究智能体，提供 MiroThinker 系列开源模型权重与在线体验入口 dr.miromind.ai。支持扩展文档上传、研究报告生成与分享等功能，README 持续发布版本更新与基准相关说明。
- 标签：`深度研究` `研究智能体` `搜索`
- 来源：GitHub Star

### [data-to-paper](https://github.com/Technion-Kishony-lab/data-to-paper)
- 发现：2026-01-03
- 一句话：从原始数据驱动端到端科研、产出可反向追溯至代码的论文的自动化框架。
- 摘要：data-to-paper 通过多智能体协作完成从原始数据探索、文献与假设、分析到论文撰写的全流程，生成可点击追溯到生成代码的稿件。支持全自动或 Copilot 人工引导模式，并对统计代码加入护栏以减少常见 LLM 编码错误。
- 标签：`科研自动化` `多智能体` `可追溯`
- 来源：GitHub Star


## 2025-12

### [mcp-agent](https://github.com/lastmile-ai/mcp-agent)
- 发现：2025-12-29
- 一句话：基于 Model Context Protocol 的可组合智能体框架，实现多种有效智能体模式。
- 摘要：mcp-agent 完整支持 MCP 并管理服务器连接生命周期，以可组合方式实现 Anthropic《Building Effective Agents》中的工作流模式，并可扩展到基于 Temporal 的持久化执行。愿景是以 MCP 与简单模式构建可投产智能体，而非依赖复杂单体架构。
- 标签：`MCP` `智能体框架` `工作流`
- 来源：GitHub Star

### [Agentic Architectures](https://github.com/FareedKhan-dev/all-agentic-architectures)
- 发现：2025-12-22
- 一句话：封装三十五种智能体架构模式的 Python 库与可运行教材。
- 摘要：项目将文献中的主要智能体模式实现为统一接口的 Architecture 类，配套完整执行的 Jupyter 笔记本与多提供商 LLM 支持，基于 LangGraph 状态机构建。强调 deterministic-picker 等评分与决策模式，并提供十七项任务的对比基准排行榜。适合学习、对比不同智能体架构并直接调用 run 接口实验。
- 标签：`智能体架构` `LangGraph` `Python` `基准` `教材`
- 来源：GitHub Star

### [MCP Code Execution Demo](https://github.com/olaservo/code-execution-with-mcp)
- 发现：2025-12-02
- 一句话：基于 Claude Agent SDK 演示 MCP 代码执行模式的实验项目。
- 摘要：项目受 Anthropic 代码执行与 MCP 博文启发，为 MCP 工具生成可发现的类型安全 RPC 包装供代理以代码方式调用。使用 Claude Agent SDK 集成 Skills 与 MCP，README 明确当前默认无沙箱、需谨慎在可信环境使用。适合研究 MCP 工具发现与代码编排模式的原型验证。
- 标签：`MCP` `代码执行` `Claude Agent SDK` `实验` `TypeScript`
- 来源：GitHub Star

### [Open PTC Agent](https://github.com/Chen-zexi/open-ptc-agent)
- 发现：2025-12-02
- 一句话：开源实现通过代码执行调用 MCP 工具的程序化工具调用智能体。
- 摘要：项目实现 Anthropic 提出的 Programmatic Tool Calling，让代理在 Daytona 沙箱中写 Python 调用 MCP 工具，在本地处理大数据后仅将结果回传以节省上下文。基于 LangChain DeepAgents 构建，演示股票数据分析等场景。适合需要减少工具返回 token 占用的高数据量工作流。
- 标签：`PTC` `MCP` `沙箱` `LangGraph` `智能体`
- 来源：GitHub Star


## 2025-11

### [DeepAnalyze](https://github.com/ruc-datalab/DeepAnalyze)
- 发现：2025-11-15
- 一句话：面向自主数据科学的智能体大模型，可完成分析、建模、可视化与报告生成。
- 摘要：DeepAnalyze 被定位为自主完成数据相关任务的智能体大模型，覆盖数据准备、分析、建模、可视化与报告生成等流程。可对结构化、半结构化与非结构化数据源做开放式研究并产出分析报告。模型、代码、训练数据与演示均已开源发布。
- 标签：`数据科学` `智能体` `分析` `开源`
- 来源：GitHub Star

### [AI Data Science Team](https://github.com/business-science/ai-data-science-team)
- 发现：2025-11-15
- 一句话：面向常见数据科学流程的 Python 多智能体库，并附带 AI Pipeline Studio 应用。
- 摘要：AI Data Science Team 提供数据加载、清洗、可视化、建模与 SQL 等专用智能体组件，以及监督式多智能体工作流。旗舰应用 AI Pipeline Studio 用可视化流水线组织手动与 AI 步骤，支持谱系追踪、多数据集合并与 MLflow 等能力。通过 Streamlit 运行 Studio 应用。
- 标签：`数据科学` `多智能体` `Streamlit` `Python`
- 来源：GitHub Star

### [AutoML-Agent](https://github.com/DeepAuto-AI/automl-agent)
- 发现：2025-11-15
- 一句话：ICML 2025 提出的多智能体大模型框架，覆盖全流程 AutoML。
- 摘要：AutoML-Agent 是论文 AutoML-Agent 的官方实现，用多智能体大模型协作完成从数据到模型的自动化机器学习流水线。README 提供图像与文本等模态的基准数据集与评测指标说明。仓库包含环境与基准数据设置指引。
- 标签：`AutoML` `多智能体` `LLM` `ICML`
- 来源：GitHub Star

### [Haystack](https://github.com/deepset-ai/haystack)
- 发现：2025-11-11
- 一句话：用于构建生产级 RAG 与智能体工作流的 Python AI 编排开源框架。
- 摘要：Haystack 支持以模块化流水线与智能体工作流编排检索、路由、记忆与生成等环节。可构建可扩展的 RAG、语义搜索、问答与自治智能体，并强调可定制与可部署的透明架构。框架用 Python 实现，面向生产环境的大模型应用开发。
- 标签：`RAG` `编排` `智能体` `Python`
- 来源：GitHub Star

### [UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)
- 发现：2025-11-10
- 一句话：开源多模态智能体技术栈，包含 Agent TARS 与 UI-TARS 桌面 GUI 智能体。
- 摘要：仓库汇集 TARS 多模态智能体栈，其中 Agent TARS 提供 CLI 与 Web UI，可结合 MCP 工具完成更接近人类的任务流程。UI-TARS Desktop 是基于 UI-TARS 模型的桌面应用，提供本地与远程的电脑与浏览器操作能力。文档分别介绍两个子项目的快速上手与能力展示。
- 标签：`GUI智能体` `多模态` `MCP` `桌面`
- 来源：GitHub Star


## 2025-10

### [HelloAgents](https://github.com/jjyaoao/HelloAgents)
- 发现：2025-10-13
- 一句话：组件化多智能体框架，围绕原生 Function Calling 构建 Agent 循环与工具生态。
- 摘要：HelloAgents 提供 SimpleAgent 工具调用循环，并集成 MCP、RAG、GraphRAG、会话持久化、子代理、Skills 与流式追踪等组件。支持通过 ToolRegistry 注册工具并用 HelloAgentsLLM 对接多种 OpenAI 兼容等服务。仓库维护与 Datawhale Hello-Agents 教程对应的 learn_version 分支。
- 标签：`智能体框架` `Function Calling` `MCP` `Python`
- 来源：GitHub Star

### [CrewAIFlowsFullStack](https://github.com/NanGePlus/CrewAIFlowsFullStack)
- 发现：2025-10-13
- 一句话：FastAPI 与 CrewAI Flows 实现可持久化、可并发的 AI 智能体工作流全栈示例。
- 摘要：项目用 FastAPI 封装 CrewAI Flows，将营销战略类多 Agent 工作流对外提供 API，并用 MySQL 持久化 Flow 中间结果。借助 Celery 支持多 Flow 并行调度与状态查询。案例包含多个 Crew、Agent 与 Task 的分工协作流程。
- 标签：`CrewAI` `工作流` `FastAPI` `Celery`
- 来源：GitHub Star

### [my-langgraph-agent](https://github.com/mr-jay-wei/my-langgraph-agent)
- 发现：2025-10-13
- 一句话：基于 LangGraph 与 MCP 的智能聊天机器人示例，演示 ReAct 工具调用集成。
- 摘要：项目用 LangGraph 与 LangChain 构建具备工具调用与 ReAct 推理循环的对话智能体，并将 MCP 服务器工具通过适配层接入 Agent。同步与异步目录分别提供 MCP 服务、工具适配器与 FastAPI 用户 API 示例。强调工具需具备标准化名称、描述与参数结构以便模型调用。
- 标签：`LangGraph` `MCP` `ReAct` `Python`
- 来源：GitHub Star
