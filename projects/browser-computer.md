# 浏览器与电脑操作

让智能体操作浏览器、桌面或整台电脑的项目。

## 2026-06

### [ego lite](https://github.com/citrolabs/ego-lite)
- 发现：2026-06-22
- 一句话：供 AI 智能体高速跑浏览器自动化、并与用户并行共用登录态的浏览器。
- 摘要：ego lite 让用户与 AI 智能体在同一浏览器内并行工作，智能体在隔离 Space 中执行任务而不抢占用户标签。相比需外接浏览器驱动的方案，它原生共享真实登录与标签，并通过 ego-browser 技能供 Codex 等调用。支持 macOS 应用安装、npx 添加技能或让智能体按文档自动安装。
- 标签：`浏览器自动化` `并行` `skills` `零配置`
- 来源：GitHub Star

### [bb-browser](https://github.com/epiral/bb-browser)
- 发现：2026-06-08
- 一句话：让 AI 智能体通过 CLI 与 MCP 复用你已登录 Chrome 状态的浏览器 API。
- 摘要：bb-browser 在你已登录的 Chrome 中执行站点适配命令，覆盖知乎、B 站、GitHub 等众多平台的检索与读取场景。理念是让机器直接使用人类浏览器界面而非依赖缺失的站点 API，通过 eval、fetch 或页面模块以用户身份访问。提供 npm 全局安装、社区适配器更新，并为 Claude Code、Cursor 等配置 MCP 服务。
- 标签：`Chrome` `MCP` `CLI` `登录态`
- 来源：GitHub Star

### [Midscene.js](https://github.com/web-infra-dev/midscene)
- 发现：2026-06-08
- 一句话：基于视觉的 GUI 智能体，用自然语言做 Web、移动端与桌面端端到端测试。
- 摘要：Midscene 结合视觉驱动 GUI 智能体与测试套件，通过同一套 Agent API 编写、验证与调试 UI 测试。它像人一样看屏幕、操作并检查可见结果，可点击无文字按钮、canvas 与跨域 iframe 而无需手写选择器。同一 API 可面向 Playwright Web、Android、iOS、HarmonyOS 与桌面应用，也可接入自定义截图与动作接口。
- 标签：`E2E` `视觉` `Playwright` `GUI Agent`
- 来源：GitHub Star

### [Browser Harness](https://github.com/browser-use/browser-harness)
- 发现：2026-06-07
- 一句话：经 CDP 连接真实浏览器、让 LLM 完成任务并自写可复用 helper 的自愈 harness。
- 摘要：Browser Harness 通过可编辑的 CDP WebSocket 把 LLM 直接接到真实浏览器，智能体缺 helper 时在工作区编写并复用。安装流程含 skill 注册与 chrome 远程调试授权，核心包受保护而 helper 写在 agent 本地 workspace。另提供 browser-harness-mcp，把浏览器控制 helper 暴露为 MCP 工具供多种客户端调用。
- 标签：`CDP` `Playwright` `MCP` `自愈合`
- 来源：GitHub Star


## 2026-03

### [OpenCLI](https://github.com/jackwener/OpenCLI)
- 发现：2026-03-30
- 一句话：把网站与已登录浏览器变成 CLI，供人与 AI 智能体确定性调用。
- 摘要：OpenCLI 将网站、浏览器会话、Electron 应用与本地工具统一为命令行接口，内置多站点适配器，并可通过 opencli browser 在已登录 Chrome 上导航、填表、点击与抽取数据。需安装 Browser Bridge 扩展与本地守护进程，提供 OpenCLIApp 桌面安装方式或 npm 全局安装。配套技能可指导智能体编写新适配器。
- 标签：`浏览器自动化` `CLI` `Chrome` `适配器` `Playwright`
- 来源：GitHub Star

### [AutoCLI](https://github.com/nashsu/AutoCLI)
- 发现：2026-03-25
- 一句话：Rust 实现的极速 CLI，从五十五余站点与桌面应用抓取信息供智能体使用。
- 摘要：AutoCLI 前身 opencli-rs，用单二进制从 Twitter、Reddit、B站、知乎等站点与 Electron 应用获取数据，并支持注册本地 CLI 供 Agent 发现。基于 OpenCLI 思路用 Rust 重写，强调更低内存与无 Node 运行时依赖。可与 AutoCLI.ai 云市场及 AI 生成适配规则同步。
- 标签：`CLI` `Rust` `浏览器会话` `适配器` `OpenCLI`
- 来源：GitHub Star


## 2026-01

### [Agent S](https://github.com/simular-ai/Agent-S)
- 发现：2026-01-14
- 一句话：开源计算机使用智能体，像人一样操作真实图形界面的鼠标、键盘与屏幕。
- 摘要：Agent S 是 Simular 开源的计算机使用智能体框架，在真实 GUI 上通过鼠标、键盘和屏幕完成任务。项目提供 Agent S 系列实现，并关联 Sai 与多篇技术论文与博客资料。适合研究或搭建桌面级计算机自动化与 GUI 智能体。
- 标签：`计算机使用` `GUI` `开源`
- 来源：GitHub Star


## 2025-12

### [AIO Sandbox](https://github.com/agent-infra/sandbox)
- 发现：2025-12-16
- 一句话：单容器内集成浏览器、终端、文件、VS Code、Jupyter 与 MCP 的智能体沙箱。
- 摘要：AIO Sandbox 是面向 AI 代理的一体化沙箱环境，在 Docker 中提供浏览器 VNC、Shell、文件操作、VS Code Server、Jupyter 与 MCP 服务。支持 API Key 保护各入口，并文档化云部署与评测示例。适合需要隔离环境中让代理同时操作浏览器、命令行与文件的开发与评测场景。
- 标签：`沙箱` `Docker` `浏览器` `MCP` `智能体`
- 来源：GitHub Star

### [DrissionPage](https://github.com/g1879/DrissionPage)
- 发现：2025-12-14
- 一句话：基于 Python 的网页自动化工具，兼顾浏览器控制与数据包收发。
- 摘要：DrissionPage 既能驱动浏览器完成自动化，也能像 requests 一样收发数据包，并可混合两种模式。采用自研内核，强调无需 webdriver、跨 iframe 查找、多标签页操作等能力。适合爬虫、自动化测试与需要兼顾浏览器与接口场景的 Python 开发者。
- 标签：`Python` `网页自动化` `爬虫` `浏览器` `自研内核`
- 来源：GitHub Star


## 2025-11

### [Playwright](https://github.com/microsoft/playwright)
- 发现：2025-11-17
- 一句话：用统一 API 驱动 Chromium、Firefox 与 WebKit 的 Web 自动化与端到端测试框架。
- 摘要：Playwright 面向 Web 自动化与测试，在测试、脚本以及 AI 智能体场景中驱动多浏览器引擎。提供 Playwright Test 测试运行器、CLI、MCP 接入方式与 Node 库等多种使用路径。内置自动等待、定位器与测试隔离等能力。
- 标签：`自动化测试` `浏览器` `E2E` `TypeScript`
- 来源：GitHub Star

### [Crawl4AI](https://github.com/unclecode/crawl4ai)
- 发现：2025-11-17
- 一句话：面向 LLM 与 AI 智能体的开源网页爬虫，将站点转为干净的 Markdown。
- 摘要：Crawl4AI 把任意网站抓取并整理为适合 RAG、智能体与数据管道的 Markdown。可本地 pip 安装自建，也可通过 Crawl4AI Cloud 以 API 方式抓取、搜索与抽取。项目同时提供 Docker 服务、CLI 与面向智能体的 MCP 接入方式。
- 标签：`爬虫` `Markdown` `RAG` `Python`
- 来源：GitHub Star

### [browser-use](https://github.com/browser-use/browser-use)
- 发现：2025-11-13
- 一句话：让 AI 智能体像人一样浏览网页并完成操作的开源浏览器智能体。
- 摘要：Browser Use 提供 Python 库、命令行，以及托管的云端智能体和浏览器。本地库可以使用自己的模型，并连接本机或云端浏览器。README 把开源库、云端浏览器和托管 Agent API 分成几条使用路径。
- 标签：`浏览器自动化` `智能体` `Python` `云端`
- 来源：GitHub Star
