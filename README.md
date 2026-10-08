# AI Learning Hub · AI 学习资源与 Roadmap

面向中文读者的 AI 学习合集：从 Python 与模型基础，到 Agent 应用开发、机器学习、深度学习和强化学习研究。保留资源原文标题，用中文说明为什么学、先读什么、可以做什么。

首版收录 **80 项资源**，采用纯 Markdown，无需构建网站即可在 GitHub 阅读。核查日期：**2026-10-08**。

## 从这里开始

| 你想做什么 | 建议入口 | 最终产出 |
| --- | --- | --- |
| 开发知识库助手、工具助手和多步骤 Agent | [Agent 应用开发路线](roadmaps/agent-development.md) | 一个有评估集、调用记录和恢复能力的 Agent |
| 理解并复现 ML / DL / RL 算法 | [算法研究路线](roadmaps/ai-research.md) | 小型模型训练、RL 实验与论文复现报告 |
| 找参考代码和完整系统 | [项目清单](projects/README.md) | 选择一个项目读源码、改功能 |
| 按主题或年份读论文 | [论文清单](papers/README.md) | 从基础论文衔接到近期研究 |

两条路线可以交叉学习。已有 Python 基础可跳过编程入门；应用开发先掌握模型调用与评估，算法研究则需要更多数学、训练和实验基础。

## 资源导航

| 分类 | 数量 | 收录范围 |
| --- | ---: | --- |
| [Projects](projects/README.md) | 20 | OpenClaw、DeerFlow、nanobot、Agent 框架、RAG、评估与训练实践 |
| [Papers](papers/README.md) | 35 | 2017–2026 年首次公开的 Transformer、训练、多模态、Agent 与深度 RL 论文 |
| [Courses](resources/courses.md) | 15 | Harvard、MIT、Stanford、Berkeley 的公开课程及具体版本 |
| [Books / Docs](resources/books-and-docs.md) | 10 | 6 本教材与 4 项官方开发文档，注明获取方式 |
| **合计** | **80** | 首页与 Roadmap 的重复引用不增加数量 |

论文的「首次公开年份」在首版按 arXiv v1 记录，另列会议或期刊信息；2025–2026 年条目标为「近期研究」。课程不受论文年份窗口限制。项目关注度为核查时的 GitHub Stars 快照，适合发现参考项目，不代表年度增长排名。

## 10 个推荐起点

按目标选读，无需全部完成后再开始实践。

| 资源 | 适合谁 | 先完成什么 |
| --- | --- | --- |
| [CS50P](resources/courses.md#crs-01) | Python 新手 | 一个有异常处理和测试的命令行程序 |
| [CS229](resources/courses.md#crs-06) | 想系统学 ML | 线性模型、分类与评估基础 |
| [PyTorch Tutorials](resources/books-and-docs.md#bok-07) | 准备读训练代码 | Tensor、Autograd 和训练循环 |
| [Attention Is All You Need](papers/README.md#pap-01) | 想理解 Transformer | 画出注意力模块，说明张量形状 |
| [LLMs from Scratch](projects/README.md#prj-18) | 想从代码理解 LLM | 分词、注意力和小型 GPT |
| [nanobot](projects/README.md#prj-03) | 想读轻量 Agent 源码 | 追踪一次消息、模型和工具调用 |
| [LangGraph](projects/README.md#prj-04) | 想做多步骤工作流 | 状态、条件分支与检查点 |
| [MCP Documentation](resources/books-and-docs.md#bok-09) | 想连接外部工具 | 一个本地只读工具的输入和错误 Schema |
| [CS336](resources/courses.md#crs-10) | 已有 DL 基础，想学大模型训练 | 分词与语言模型基础作业 |
| [Reinforcement Learning: An Introduction](resources/books-and-docs.md#bok-06) | 想进入 RL | MDP、Bellman 方程与 TD 学习 |

## 两条路线概览

**Agent 应用开发**：Python / API → LLM 基础 → RAG → 工具调用与 MCP → 工作流与多 Agent → 评估与部署。阶段任务依次形成问答应用、知识库助手、工具助手和可评估的 Agent。[查看阶段任务与验收标准](roadmaps/agent-development.md)。

**算法研究**：数学 / ML → PyTorch / DL → Transformer 与训练 → 多模态或 RL → 论文复现。阶段任务包括基础模型训练、小型 Transformer、PPO / SAC 实验与复现报告。[查看阶段任务与实验要求](roadmaps/ai-research.md)。

## 如何阅读条目

- **入门**：可从对应基础课程开始；**中级**：已有 Python 和该主题基础；**进阶**：需要论文阅读、训练实验或系统工程经验。难度是本合集的学习建议。
- **官方来源优先**：论文作者、项目组织、大学或出版社页面。每项提供中文推荐理由、前置知识、适用路线和核查日期。
- **文档核查与运行验证分开**：已读取官网或 README，不代表项目已部署、课程作业已执行或论文结果已复现。首版本地未运行这 20 个外部项目。
- **待核查明确保留**：部分发表信息、整套录播覆盖及下载入口仍待核查。课程访问限制与书籍获取方式在详情页注明。

维护状态、来源快照与待核查事项见 [核查记录](VERIFICATION.md)。欢迎按 [贡献指南](CONTRIBUTING.md) 补充来源、勘误与学习实践。

## 目录与维护

```text
README.md
projects/README.md
papers/README.md
resources/courses.md
resources/books-and-docs.md
roadmaps/agent-development.md
roadmaps/ai-research.md
CONTRIBUTING.md
VERIFICATION.md
scripts/check_catalog.py
```

内容使用 Markdown；校验脚本只依赖 Python 标准库。修改后运行：

```sh
python3 scripts/check_catalog.py
```
