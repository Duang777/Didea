# 浏览器与电脑操作

让智能体操作浏览器、桌面或整台电脑的项目。

## 2026-09

### [Obscura](https://github.com/h4ckf0r0day/obscura)
- 发现：2026-09-29
- 一句话：Rust 编写的开源无头浏览器，面向 AI 智能体自动化与网页抓取，可替代 headless Chrome。
- 摘要：Obscura 通过 V8 执行真实 JavaScript，支持 Chrome DevTools Protocol，并宣称可作为 Puppeteer 与 Playwright 的 drop-in 替代。内置反检测能力，支持原生渲染截图、录屏与 PDF 导出而无需捆绑 Chromium。开源引擎采用 Apache-2.0，全功能不人为阉割；另规划托管版 Obscura Cloud 提供代理与运维支持。
- 标签：`无头浏览器` `Rust` `CDP` `网页抓取`
- 来源：GitHub Star

### [PawBrowse](https://github.com/ItaiZeilig/pawbrowse)
- 发现：2026-09-28
- 一句话：Chrome 扩展加零依赖 MCP 服务，让编码智能体操作你已登录的真实 Chrome 标签页。
- 摘要：PawBrowse 通过 CDP 以元素表形式感知页面，无需远程调试端口、第二套模型或 API Key，由现有智能体做决策。支持 Claude Code、Cursor、VS Code、Claude Desktop 等 MCP 客户端；Claude Code 可用 npx 一行注册 MCP。扩展可从 Chrome Web Store 安装，连接成功后徽章变绿并返回 extension_connected 状态。
- 标签：`MCP` `Chrome` `浏览器自动化` `Claude Code`
- 来源：GitHub Star

### [screenpipe](https://github.com/screenpipe/screenpipe)
- 发现：2026-09-26
- 一句话：本地持续采集屏幕与音频，为智能体提供电脑工作上下文。
- 摘要：screenpipe 在本地持续记录公司的电脑工作画面与音频，用于梳理工作流、发现值得自动化的环节，并为智能体补充上下文。默认采用本地优先策略，采集历史可留在本机。还支持用自然语言检索已记录内容。
- 标签：`屏幕录制` `本地优先` `工作流` `智能体上下文`
- 来源：GitHub Star

### [Jevry](https://github.com/michaelswissa/jevry)
- 发现：2026-09-25
- 一句话：开源桌面浏览器智能体，用自然语言完成网站任务与调研。
- 摘要：Jevry 是 MIT 许可的开源桌面浏览器，可用自然语言浏览、调研并在支持的网站上执行任务，动作可见且可中止或改向。运行时由 Chromium 执行浏览器动作，文本模型负责规划与语言处理。网站支持范围因站点而异，需自行配置 API 与模型连接。
- 标签：`浏览器自动化` `桌面应用` `Electron` `调研`
- 来源：GitHub Star

### [agent-browser](https://github.com/vercel-labs/agent-browser)
- 发现：2026-09-06
- 一句话：供 AI 智能体使用的 Rust 原生浏览器自动化 CLI。
- 摘要：agent-browser 提供打开页面、无障碍树快照、按引用点击与填表、截图与关闭等命令。可通过 npm、Homebrew 或 Cargo 安装，并引导下载 Chrome for Testing 作为自动化浏览器。设计为快速、可脚本化的智能体侧浏览器控制，无需 Playwright 守护进程即可运行核心能力。
- 标签：`浏览器自动化` `CLI` `Rust` `智能体`
- 来源：GitHub Star

### [BrowserOS](https://github.com/browseros-ai/BrowserOS)
- 发现：2026-09-02
- 一句话：面向 AI 智能体的开源智能浏览器，可并行执行任务并连接 MCP 客户端。
- 摘要：BrowserOS neo 是专供 AI 智能体使用的第二浏览器，可从 Chrome 一键导入登录态，连接 Claude Code、Codex 或任意 MCP 智能体并交接网页任务。智能体在独立标签页并行运行，用户可实时观看或回放会话。开源且默认在本地运行。
- 标签：`浏览器` `MCP` `自动化` `Chromium` `智能体`
- 来源：GitHub Star


## 2026-08

### [mobile-use](https://github.com/minitap-ai/mobile-use)
- 发现：2026-08-14
- 一句话：开源 AI 智能体，用自然语言操控真实 Android 或 iOS 设备界面完成任务与数据采集。
- 摘要：mobile-use 理解自然语言指令并基于无障碍树等方式与 App UI 交互，可用于发消息、导航复杂应用或按描述抽取结构化数据。支持配置 OpenAI、Google、xAI、OpenRouter、MiniMax 等多种 LLM 驱动内部智能体。可在本机 Android 或 iOS 设备上运行，并提供 MCP 文档入口。
- 标签：`移动自动化` `Android` `iOS` `自然语言` `Python`
- 来源：GitHub Star

### [Moli](https://github.com/lexmount/moli)
- 发现：2026-08-13
- 一句话：面向 AI 智能体的生产级 Rust 无头浏览器，轻量高速，支持 CLI、CDP 与 WebDriver。
- 摘要：Moli 采用按需布局与渲染，在较小资源占用下提供完整浏览器运行时，帮助智能体抓取网页、搜索与自动化浏览任务。支持 Linux、macOS、Windows，可通过 CLI、CDP、WebDriver Classic 或 WebDriver BiDi 使用。仓库内 skills 可指导智能体安装预编译二进制并用 moli-webfetch 拉取页面。
- 标签：`无头浏览器` `Rust` `网页抓取` `CDP` `智能体`
- 来源：GitHub Star


## 2026-07

### [AppAgent](https://github.com/TencentQQGYLab/AppAgent)
- 发现：2026-07-21
- 一句话：基于多模态大模型的智能手机应用操作智能体框架。
- 摘要：AppAgent 通过点击、滑动等类人交互操作手机应用，无需系统后端权限即可跨应用工作。智能体可通过自主探索或观察人类演示学习新应用，并生成知识库支撑后续操作。仓库为 CHI 2025 相关工作实现，并提供评测基准与可选网格叠加点击方案。
- 标签：`手机自动化` `多模态` `GUI 智能体` `Android` `研究原型`
- 来源：GitHub Star

### [GenericAgent](https://github.com/lsdefine/GenericAgent)
- 发现：2026-07-21
- 一句话：极简自进化自主智能体框架，用少量原子工具控制浏览器、终端与桌面。
- 摘要：GenericAgent 核心约三千行种子代码，以九个原子工具与约百行 Agent Loop 赋予大模型本机级控制能力，覆盖浏览器、文件系统、键鼠与屏幕等。完成任务后会把执行路径结晶为可复用 Skill，逐步形成个人技能树。强调不预置技能、随使用进化，并兼容多种主流模型 API。
- 标签：`自进化` `Skill` `桌面控制` `浏览器` `轻量`
- 来源：GitHub Star

### [Understudy](https://github.com/understudy-ai/understudy)
- 发现：2026-07-21
- 一句话：开源本地智能体，用 GUI、浏览器与 Shell 等操作整台电脑。
- 摘要：Understudy 从单条指令完成调研、浏览器操控与技能调用等通用任务。支持通过手机消息远程派发到桌面执行 GUI 自动化，并可通过演示一次来学习任务意图后泛化重放。数据留在本机，用户自带 Claude、Gemini 等模型提供商。
- 标签：`电脑操作` `GUI 智能体` `本地优先` `远程派发` `教学重放`
- 来源：GitHub Star

### [肉包 Roubao](https://github.com/Turbo1123/roubao)
- 发现：2026-07-19
- 一句话：基于视觉语言模型的开源 Android 手机自动化助手，无需电脑即可本机运行。
- 摘要：肉包用 Kotlin 在手机上完成截图、分析与点击输入，通过 Shizuku 获得系统级自动化权限而无需 Root。采用 Tools 加 Skills 双层架构，可在快速委派与 GUI 循环路径间切换。用户安装 App、配置 API Key 后用自然语言描述任务即可执行，对标无需外接 ADB 的手机智能体方案。
- 标签：`Android` `VLM` `手机自动化` `Kotlin` `Shizuku`
- 来源：GitHub Star

### [Nanobrowser](https://github.com/nanobrowser/nanobrowser)
- 发现：2026-07-14
- 一句话：在浏览器内运行的开源 AI 网页自动化 Chrome 扩展。
- 摘要：Nanobrowser 是本地浏览器中的 AI 网页自动化工具，使用你自己的 LLM API Key，采用多智能体协作完成复杂流程。提供侧栏聊天界面与任务自动化，支持多家主流与兼容 OpenAI 的模型提供商。
- 标签：`Chrome扩展` `多智能体` `自动化` `本地`
- 来源：GitHub Star

### [Page Agent](https://github.com/alibaba/page-agent)
- 发现：2026-07-03
- 一句话：嵌入网页的 JavaScript GUI 智能体，用自然语言操控页面界面。
- 摘要：Page Agent 只需一段 in-page JavaScript 即可为任意网页提供 AI 智能体，无需浏览器扩展、Python 或 headless 浏览器。它基于文本的 DOM 操作，不依赖截图或多模态模型，可自带多种主流或本地大模型。可选 Chrome 扩展处理多页任务，并提供 Beta 版 MCP Server 从外部控制。
- 标签：`浏览器` `DOM` `JavaScript` `MCP`
- 来源：GitHub Star


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
