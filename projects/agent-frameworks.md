# 智能体框架与编排

多智能体框架、编排层和工作流运行时。

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
