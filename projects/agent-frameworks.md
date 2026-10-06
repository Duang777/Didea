# 智能体框架与编排

多智能体框架、编排层和工作流运行时。

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
