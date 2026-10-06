# 模型与推理服务

模型权重、推理引擎和模型 API。

## 2026-09

### [magpie](https://github.com/yetone/magpie)
- 发现：2026-09-27
- 一句话：菜单栏统一管理多款编码智能体的模型与本地 API 网关。
- 摘要：magpie 把多款编码智能体各自的模型配置、密钥与接口地址集中在一处管理，可从菜单栏为单个智能体切换模型。本地网关同时支持多种主流 API 形态，并在流式、工具调用与推理场景下做协议转换。还支持路由组在配额或限流时自动切换后端，并把订阅登录转成各智能体可共用的提供方。
- 标签：`网关` `编码智能体` `菜单栏` `路由`
- 来源：GitHub Star

### [CLI Proxy API](https://github.com/router-for-me/CLIProxyAPI)
- 发现：2026-09-03
- 一句话：把多款编码 CLI 账号封装成 OpenAI、Gemini、Claude 等兼容 API 的本地代理服务。
- 摘要：CLIProxyAPI 是面向命令行编码工具的代理服务器，为 CLI 提供 OpenAI、Gemini、Claude、Codex、Grok 等兼容接口。可在本机通过多个 CLI 账号访问 Kimi、OpenAI、Anthropic 等多家模型提供方。也提供 EasyCLIProxyAPI 图形桌面客户端。
- 标签：`API 网关` `Codex` `Claude Code` `代理` `多模型`
- 来源：GitHub Star


## 2026-07

### [OmniRoute](https://github.com/diegosouzapw/OmniRoute)
- 发现：2026-07-25
- 一句话：MIT 开源 AI 网关，用单一端点聚合多家模型与免费额度并支持配额感知回退。
- 摘要：OmniRoute 为 Claude Code、Codex、Cursor、Cline 与 Copilot 等工具提供统一 AI 接入，聚合多家提供商与免费额度，并宣传 RTK 与 Caveman 压缩以节省 token。支持 MCP 与 A2A，提供 Desktop 与 PWA 管理面。目标是减少手工轮换 SDK 与额度，在一处路由与回退。
- 标签：`LLM网关` `免费额度` `Claude Code` `MCP` `自托管`
- 来源：GitHub Star


## 2025-11

### [Ollama](https://github.com/ollama/ollama)
- 发现：2025-11-08
- 一句话：在本地运行与管理 Kimi、Qwen、DeepSeek 等开源大模型的推理运行时。
- 摘要：Ollama 帮助用户下载并在本机运行多种开源模型，提供命令行交互与 REST API。支持通过 ollama launch 对接 Claude Code、Codex、Copilot 等编码集成，也可配合 OpenClaw 等助手产品使用。提供 macOS、Windows、Linux 安装方式及官方 Docker 镜像。
- 标签：`本地推理` `LLM` `开源模型` `API`
- 来源：GitHub Star


## 2025-10

### [MiniMind](https://github.com/jingyaogong/minimind)
- 发现：2025-10-02
- 一句话：从零用 PyTorch 训练超小规模大语言模型的开源复现项目。
- 摘要：项目以极低算力成本训练约 64M 参数的 MiniMind 系列模型，并开源极简模型结构与完整训练链路代码。覆盖预训练、监督微调、LoRA、RLHF、工具调用与 Agentic RL 等阶段，核心算法均用 PyTorch 原生实现。同时提供视觉与多模态等扩展方向的关联项目入口。
- 标签：`小模型` `预训练` `微调` `PyTorch`
- 来源：GitHub Star


## 2025-09

### [Qwen3 Fine-Tuning Playground](https://github.com/lijiayi-ai/Qwen3-FineTuning-Playground)
- 发现：2025-09-07
- 一句话：基于 Qwen3 系列的多方案微调与训后优化实战代码库。
- 摘要：仓库模块化提供监督微调全量与 LoRA、PPO 与 ORPO 等强化学习微调，以及知识蒸馏等训后脚本，均可通过命令行参数配置。文档引导使用 modelscope 下载 Qwen3 模型并给出 SFT-LoRA 端到端示例，另含心理学多轮对话 PsyDT 实验与推理评测目录。
- 标签：`Qwen3` `微调` `LoRA` `强化学习`
- 来源：GitHub Star

### [mini_qwen](https://github.com/qiufengqijun/mini_qwen)
- 发现：2025-09-01
- 一句话：从头训练约 1B 参数中英双语大语言模型的完整流程项目。
- 摘要：mini_qwen 在 Qwen2.5-0.5B 结构基础上扩展至约 1B 参数并随机初始化，使用智源研究院预训练、微调与偏好数据完成 PT、SFT 与 DPO 三阶段训练。仓库提供 demo 脚本与缩小数据集 mini_data，便于在约 12G 显存环境体验完整训练流程，并公开各阶段 checkpoint 下载链接。
- 标签：`预训练` `SFT` `DPO` `小模型`
- 来源：GitHub Star


## 2025-04

### [ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B)
- 发现：2025-04-19
- 一句话：开源中英双语对话语言模型权重与本地部署方案。
- 摘要：ChatGLM-6B 基于 GLM 架构，约 62 亿参数，针对中文问答与对话优化，支持 INT4 量化后在消费级显卡本地推理。仓库提供模型权重、推理示例与 P-Tuning v2 高效微调指南，学术研究完全开放，登记问卷后亦允许免费商业使用。
- 标签：`ChatGLM` `双语对话` `模型权重` `量化`
- 来源：GitHub Star
