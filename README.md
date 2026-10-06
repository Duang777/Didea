# Didea

duang777 每天把发现的项目丢进来，由 AI 归类并写成中文摘要。每个分类内部按发现日期倒序，最新的在最前；同一天里，后加入的排在前面。发现日期是看到它的那天，不是项目发布日。

规则只维护 [AGENTS.md](AGENTS.md)。下面两个标记块由 `python3 scripts/catalog.py index` 生成，不要手改。

## 分类目录

<!-- categories:start -->
- [智能体框架与编排](projects/agent-frameworks.md)（0）
- [编码智能体与开发工具](projects/coding-agents.md)（0）
- [Skills/提示词/规则](projects/skills-prompts.md)（0）
- [MCP 与工具集成](projects/mcp-tools.md)（0）
- [浏览器与电脑操作](projects/browser-computer.md)（0）
- [评测与基准](projects/benchmarks.md)（0）
- [论文与研究](projects/papers.md)（0）
- [模型与推理服务](projects/models-inference.md)（0）
- [应用与产品](projects/apps-products.md)（0）
- [前端与设计](projects/frontend-design.md)（1）
- [博客与学习资料](projects/blogs-learning.md)（0）
- [其他](projects/other.md)（0）
<!-- categories:end -->

## 最近新增

最多 20 条，跨分类，按发现日期倒序。

<!-- recent:start -->
- 2026-10-07 [hairline](https://github.com/lucasmarkes/hairline) · [前端与设计](projects/frontend-design.md)：27 个会跟着指针动的等距线条插画，React 和任何 DOM 页面都能用。
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
