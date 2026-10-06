# MCP 与工具集成

MCP 服务，以及把外部系统接到智能体上的集成。

## 2025-12

### [Firecrawl](https://github.com/firecrawl/firecrawl)
- 发现：2025-12-19
- 一句话：为 AI 智能体提供网页抓取、搜索与结构化数据的开源数据服务。
- 摘要：Firecrawl 可将 URL 转为 Markdown、HTML、截图或结构化 JSON，并支持搜索、爬站、与页面交互后提取内容。README 说明代理轮换、速率限制与 JS 页面处理等由服务侧承担，并可通过单条命令接入 AI 代理或 MCP 客户端。适合为 RAG 或工具调用场景稳定获取网页与文档数据。
- 标签：`爬虫` `网页数据` `Markdown` `MCP` `智能体`
- 来源：GitHub Star

### [Spider_XHS](https://github.com/cv-cat/Spider_XHS)
- 发现：2025-12-03
- 一句话：面向 AI 运营场景的小红书数据采集、发布与签名接口封装。
- 摘要：项目逆向并实现小红书 PC 端与创作者平台核心 HTTP 接口，透明处理 a1、x-s 等签名参数，覆盖采集、内容发布与蒲公英 KOL 数据。README 说明可与上层 AI Agent 组成采集改写发布闭环，并支持通过 XhsSkills 以 skills 方式接入。仅供学习交流，禁止商业化使用。
- 标签：`小红书` `爬虫` `API` `智能体运营` `skills`
- 来源：GitHub Star


## 2025-11

### [Douyin_TikTok_Download_API](https://github.com/Evil0ctal/Douyin_TikTok_Download_API)
- 发现：2025-11-18
- 一句话：自托管的抖音与 TikTok 数据采集、无水印下载及 MCP 服务。
- 摘要：项目通过 docker compose 提供异步 REST API、MCP 服务器、CLI 与 Web 控制台，抓取帖子、作者、评论与搜索并支持无水印媒体流下载，数据可存入自建 PostgreSQL。强调开源、本地运行与身份池自维护。适合为智能体或自建应用提供社媒数据接口。
- 标签：`抖音` `TikTok` `MCP` `API` `自托管`
- 来源：GitHub Star

### [Playwright MCP](https://github.com/microsoft/playwright-mcp)
- 发现：2025-11-17
- 一句话：基于 Playwright 的 MCP 服务，为 LLM 提供结构化浏览器自动化能力。
- 摘要：Playwright MCP 是 Model Context Protocol 服务器，通过 Playwright 的可访问性树与结构化快照让大模型与网页交互，无需依赖截图或视觉模型。强调轻量、确定性工具调用，可用 npx 安装并在多种 MCP 客户端中配置。
- 标签：`MCP` `Playwright` `浏览器自动化` `LLM`
- 来源：GitHub Star

### [Browser MCP](https://github.com/BrowserMCP/mcp)
- 发现：2025-11-17
- 一句话：MCP 服务器与 Chrome 扩展，让 AI 应用自动化本机已登录的浏览器。
- 摘要：Browser MCP 由 MCP 服务与浏览器扩展组成，可在 VS Code、Claude、Cursor 等客户端中控制浏览器。自动化在本地执行，使用现有浏览器配置文件以保持登录态，并声称有助于降低基础风控与验证码拦截。实现思路改编自 Playwright MCP，改为操作用户真实浏览器实例。
- 标签：`MCP` `Chrome` `浏览器自动化` `本地`
- 来源：GitHub Star
