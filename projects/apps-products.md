# 应用与产品

给人直接用的完整应用和产品。

## 2025-12

### [Paper Burner X](https://github.com/Feather-2/Burner-X)
- 发现：2025-12-14
- 一句话：浏览器内即用的 AI 文献识别、翻译、阅读与分析工具。
- 摘要：Paper Burner X 面向研究生与研究人员，支持 PDF、DOCX、PPTX、EPUB 等格式的 OCR、翻译与智能分析，并保留公式与排版。前端实现 Agentic RAG、术语库匹配与 BYOK 自定义模型端点，数据默认保存在浏览器本地。适合长文献对照阅读、批量翻译与长文本问答分析。
- 标签：`文献` `PDF` `翻译` `浏览器` `BYOK`
- 来源：GitHub Star

### [AIA Academic Illustrator](https://github.com/qwwzdyj/AIA-Academic-Illustrator-)
- 发现：2025-12-14
- 一句话：将论文摘要或 PDF 转为 CVPR 与 NeurIPS 风格学术示意图的 AI 工具。
- 摘要：工具采用逻辑架构师生成 Schema、再由视觉模型渲染图像的两步流程，支持文本输入、PDF 或图片上传及参考图风格引导。提供中英文界面、浏览器端历史记录与 BYOK 自带 API Key，可在线体验或本地部署前端。适合快速生成论文方法图与示意图草稿。
- 标签：`学术绘图` `论文` `Gemini` `BYOK` `Web`
- 来源：GitHub Star


## 2025-11

### [Deep RAG](https://github.com/boluo2077/deep-rag)
- 发现：2025-11-19
- 一句话：超越向量检索、支持多跳推理与否定查询的高级 RAG 应用系统。
- 摘要：Deep RAG 用文件摘要作为知识地图，让模型主动导航并多轮检索完整文件或目录，而非碎片化切块。支持否定、数值比较、极值与跨文档聚合等查询，后端为 Python FastAPI，前端为 React UI，可配置 OpenAI、Anthropic、Gemini 等模型。适合需要复杂问答的企业知识库场景。
- 标签：`RAG` `多跳推理` `FastAPI` `React` `知识库`
- 来源：GitHub Star

### [Data Formulator](https://github.com/microsoft/data-formulator)
- 发现：2025-11-17
- 一句话：交互式 AI 数据分析工作台，用于连接数据源、探索数据并生成可视化。
- 摘要：Data Formulator 提供统一可视化工作区，用数据连接器让智能体以一致方式接入文件、数据库与 Databricks 等来源，并维护数据关系记忆。Data Threads 支持在分支问题间对比路径并用图表探索。图表基于开源 Flint 可视化语言生成。
- 标签：`数据分析` `可视化` `AI` `数据连接器`
- 来源：GitHub Star

### [Streamline Analyst](https://github.com/Wilson-ZheLin/Streamline-Analyst)
- 发现：2025-11-15
- 一句话：基于大语言模型的开源数据分析智能体应用，自动化清洗、建模与可视化。
- 摘要：Streamline Analyst 用大模型驱动端到端数据分析，包括目标变量识别、缺失值处理、编码与模型选择等步骤。用户选择数据文件与分析模式即可启动流程，并提供 Streamlit 在线演示。上传数据与 API Key 按说明为一次性使用且不保存。
- 标签：`数据分析` `LLM` `Streamlit` `智能体`
- 来源：GitHub Star


## 2025-10

### [AgentChat](https://github.com/Shy2593666979/AgentChat)
- 发现：2025-10-13
- 一句话：基于大模型的智能对话产品，支持自定义 Agent、RAG、MCP 与三层记忆。
- 摘要：AgentChat 是前后端分离的智能体交流平台，内置默认 Agent 并支持多轮协作完成复杂任务。集成 LangChain、Function Call、MCP、RAG、Milvus、ElasticSearch 与 HITL 等人机协同能力。提供 FastAPI 后端、在线文档与可体验的云端站点。
- 标签：`对话系统` `RAG` `MCP` `FastAPI`
- 来源：GitHub Star


## 2025-09

### [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)
- 发现：2025-09-28
- 一句话：可离线部署的本地知识库问答与 Agent 开源应用。
- 摘要：原 Langchain-ChatGLM 项目，基于 Langchain 思想实现中文友好的本地知识库问答方案。支持通过 Xinference、Ollama 等接入多种开源大模型与向量库，提供 FastAPI 服务与 Streamlit WebUI，流程涵盖文档加载、切分、检索与生成。项目侧重应用部署，不涉及模型训练与微调流程。
- 标签：`RAG` `知识库` `本地部署` `Agent`
- 来源：GitHub Star

### [weChatRobot](https://github.com/MartinDai/weChatRobot)
- 发现：2025-09-07
- 一句话：对接微信公众号、可调用大模型回复的智能聊天机器人。
- 摘要：基于 Vert.x 的微信公众号服务端项目，用户向公众号发消息后按关键字或大模型接口自动回复。支持自定义关键字，并可配置 OpenAI、通义千问或图灵机器人等后端，优先级为关键字优先于各模型服务。需提供公众号账号并在后台配置回调 URL 与 token。
- 标签：`微信公众号` `聊天机器人` `OpenAI` `Java`
- 来源：GitHub Star
