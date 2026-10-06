# Didea

jialing 每天把发现的项目丢进来，由 AI 归类并写成中文摘要。每个分类内部按发现日期倒序，最新的在最前；同一天里，后加入的排在前面。发现日期是看到它的那天，不是项目发布日。

规则只维护 [AGENTS.md](AGENTS.md)。下面两个标记块由 `python3 scripts/catalog.py index` 生成，不要手改。

## 分类目录

<!-- categories:start -->
- [智能体框架与编排](projects/agent-frameworks.md)（35）
- [编码智能体与开发工具](projects/coding-agents.md)（18）
- [Skills/提示词/规则](projects/skills-prompts.md)（23）
- [MCP 与工具集成](projects/mcp-tools.md)（9）
- [浏览器与电脑操作](projects/browser-computer.md)（12）
- [评测与基准](projects/benchmarks.md)（1）
- [论文与研究](projects/papers.md)（5）
- [模型与推理服务](projects/models-inference.md)（5）
- [应用与产品](projects/apps-products.md)（34）
- [前端与设计](projects/frontend-design.md)（4）
- [博客与学习资料](projects/blogs-learning.md)（85）
- [其他](projects/other.md)（13）
<!-- categories:end -->

## 最近新增

最多 20 条，跨分类，按发现日期倒序。

<!-- recent:start -->
- 2026-10-07 [hairline](https://github.com/lucasmarkes/hairline) · [前端与设计](projects/frontend-design.md)：27 个会跟着指针动的等距线条插画，React 和任何 DOM 页面都能用。
- 2026-06-30 [PMB](https://github.com/oleksiijko/pmb) · [编码智能体与开发工具](projects/coding-agents.md)：面向 Claude Code、Cursor、Codex 等编码智能体的本地优先持久记忆，经 MCP 读写。
- 2026-06-27 [OxyGent](https://github.com/jd-opensource/OxyGent) · [智能体框架与编排](projects/agent-frameworks.md)：用 Oxy 抽象把工具、模型与智能体模块化的多智能体 Python 框架。
- 2026-06-27 [Design Patterns Implemented in Java](https://github.com/iluwatar/java-design-patterns) · [博客与学习资料](projects/blogs-learning.md)：用 Java 示例实现并讲解常见设计模式的开放源码学习仓库。
- 2026-06-27 [Trae Agent](https://github.com/bytedance/trae-agent) · [编码智能体与开发工具](projects/coding-agents.md)：面向通用软件工程任务的 LLM 命令行智能体，架构透明便于研究与扩展。
- 2026-06-26 [Eino](https://github.com/cloudwego/eino) · [智能体框架与编排](projects/agent-frameworks.md)：Go 语言的 LLM 应用与智能体开发框架，含组件、ADK 与图编排。
- 2026-06-22 [ego lite](https://github.com/citrolabs/ego-lite) · [浏览器与电脑操作](projects/browser-computer.md)：供 AI 智能体高速跑浏览器自动化、并与用户并行共用登录态的浏览器。
- 2026-06-22 [Cowart](https://github.com/zhongerxin/Cowart) · [编码智能体与开发工具](projects/coding-agents.md)：面向 Codex 的 tldraw 无限画布原生插件，经 MCP 在项目中持久化画布与 AI 生图。
- 2026-06-16 [AriaType](https://github.com/joe223/AriaType) · [应用与产品](projects/apps-products.md)：桌面端语音输入与润色层，把口述内容写入当前应用光标处。
- 2026-06-08 [bb-browser](https://github.com/epiral/bb-browser) · [浏览器与电脑操作](projects/browser-computer.md)：让 AI 智能体通过 CLI 与 MCP 复用你已登录 Chrome 状态的浏览器 API。
- 2026-06-08 [Midscene.js](https://github.com/web-infra-dev/midscene) · [浏览器与电脑操作](projects/browser-computer.md)：基于视觉的 GUI 智能体，用自然语言做 Web、移动端与桌面端端到端测试。
- 2026-06-07 [Browser Harness](https://github.com/browser-use/browser-harness) · [浏览器与电脑操作](projects/browser-computer.md)：经 CDP 连接真实浏览器、让 LLM 完成任务并自写可复用 helper 的自愈 harness。
- 2026-06-05 [x-cli](https://github.com/better-world-ai/x-cli) · [博客与学习资料](projects/blogs-learning.md)：展示用 agent-cli-creator 技能与 webbridge 为各网站生成的 CLI 示例集合。
- 2026-05-31 [HarnessClaw Engine](https://github.com/harnessclaw/harnessclaw-engine) · [编码智能体与开发工具](projects/coding-agents.md)：Go 实现的 LLM 编程助手引擎，支持 WebSocket、工具调用、权限与技能扩展。
- 2026-05-29 [GoClub](https://github.com/LeoninCS/GoClub) · [博客与学习资料](projects/blogs-learning.md)：汇总 Go 面试真题、八股与资料的 Hugo 学习站点仓库。
- 2026-05-27 [go-awesome](https://github.com/shockerli/go-awesome) · [博客与学习资料](projects/blogs-learning.md)：整理 Go 语言优秀开源资源与 learning 链接的中文 awesome 清单。
- 2026-05-26 [Ragent](https://github.com/nageoffer/ragent) · [智能体框架与编排](projects/agent-frameworks.md)：面向 Agentic RAG 的 Java 生产级平台，覆盖入库、检索、记忆与 MCP 工具。
- 2026-05-22 [Multica](https://github.com/multica-ai/multica) · [应用与产品](projects/apps-products.md)：可自托管的团队看板，像分配同事一样把 Issue 交给 AI 编码智能体。
- 2026-05-21 [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub) · [博客与学习资料](projects/blogs-learning.md)：整理 AI Agent 学习路线、todo 与精选资料的社区 hub。
- 2026-05-18 [Nexus Agent](https://github.com/java-up-up/nexus-agent) · [智能体框架与编排](projects/agent-frameworks.md)：企业级 AI 智能体平台，覆盖对话、RAG、MCP、Skills 与文档治理全链路。
<!-- recent:end -->

## 用法

更新分类计数和最近新增：

```bash
python3 scripts/catalog.py index
```

校验日期倒序、字段、日期格式，以及全库 URL 是否重复：

```bash
python3 scripts/catalog.py check
```

推送和拉取请求会在 GitHub Actions 里自动运行 `check`。
