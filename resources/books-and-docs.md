# 书籍与官方文档

[返回首页](../README.md) · [Agent 路线](../roadmaps/agent-development.md) · [算法路线](../roadmaps/ai-research.md)

共 10 项：6 本书籍、4 项官方文档。书籍记录 2017–2026 年范围内的具体版本；持续更新的文档记录页面核查日期。语言以英文原版为准，推荐理由使用中文。书籍、配套项目与开发文档分别承担不同学习用途，各自只在对应清单维护一次。

**核查日期：2026-10-08。** 免费全文、免费代码和付费正文分别标注；提供下载入口不代表本轮下载并读完所有文件。

## 快速导航

| 条目 | 资源 | 类型 | 版本 / 年份 | 难度 |
| --- | --- | --- | --- | --- |
| BOK-01 | [Mathematics for Machine Learning](#bok-01) | 书籍 | 2020 年 Cambridge University Press 版 | 入门 → 中级 |
| BOK-02 | [An Introduction to Statistical Learning with Applications in Python](#bok-02) | 书籍 | Python 版，2023 年 | 入门 → 中级 |
| BOK-03 | [Dive into Deep Learning](#bok-03) | 书籍 | 2023 年 Cambridge University Press 版 | 入门 → 中级 |
| BOK-04 | [Understanding Deep Learning](#bok-04) | 书籍 | 2023 年 MIT Press 版（2023-12-05 出版） | 入门 → 中级 |
| BOK-05 | [Build a Large Language Model (From Scratch)](#bok-05) | 书籍 | 2024 年 Manning 版（2024 年 9 月出版） | 中级 |
| BOK-06 | [Reinforcement Learning: An Introduction](#bok-06) | 书籍 | 第二版，2018 年 MIT Press 版 | 中级 → 进阶 |
| BOK-07 | [PyTorch Tutorials](#bok-07) | 官方文档 | 持续更新，2026-10-08 快照 | 入门 → 中级 |
| BOK-08 | [Hugging Face Transformers Documentation](#bok-08) | 官方文档 | 持续更新，2026-10-08 快照 | 中级 |
| BOK-09 | [Model Context Protocol Documentation](#bok-09) | 官方文档 | 持续更新，2026-10-08 快照 | 入门 → 中级 |
| BOK-10 | [LangGraph Documentation](#bok-10) | 官方文档 | 持续更新，2026-10-08 快照 | 中级 |

<a id="bok-01"></a>

<!-- resource: BOK-01 -->
### Mathematics for Machine Learning

- **官方入口**：[作者 / 出版社页面](https://mml-book.github.io/)。
- **类型 / 版本**：书籍 / 2020 年 Cambridge University Press 版；在线勘误持续更新。
- **难度 / 路线**：入门 → 中级 / 算法。
- **前置知识**：基础代数；微积分基础有帮助。
- **推荐理由**：以线性代数、解析几何、概率与优化连接机器学习，适合按薄弱环节补数学。
- **获取方式**：作者提供免费全文 PDF；纸质版付费。PDF 入口见作者官网，未逐页审阅。
- **建议先阅读**：线性代数 → 向量微积分 → 概率 → 优化；再读线性回归和 PCA。
- **实践任务**：推导线性回归梯度，解释 PCA 的投影与方差，并用 NumPy 验证。
- **配套材料 / 版本依据**：[作者官网与下载入口](https://mml-book.github.io/)。
- **核查日期 / 状态**：2026-10-08；已读取作者页面的出版年份、下载与内容说明。

<a id="bok-02"></a>

<!-- resource: BOK-02 -->
### An Introduction to Statistical Learning with Applications in Python

- **官方入口**：[作者 / 出版社页面](https://www.statlearning.com/)。
- **类型 / 版本**：书籍 / Python 版，2023 年；区别于 R 版的出版年份。
- **难度 / 路线**：入门 → 中级 / 算法。
- **前置知识**：Python、基本概率统计。
- **推荐理由**：从回归、分类、交叉验证到树模型，适合建立可解释的机器学习基线与评估习惯。
- **获取方式**：官网提供免费全文入口；纸质版付费，Python 配套实验公开。
- **建议先阅读**：统计学习 → 回归 / 分类 → 重采样；结合对应 Python Labs。
- **实践任务**：完成一个分类任务，用交叉验证选模型，再报告留出测试集结果。
- **配套材料 / 版本依据**：[官方 Python Labs](https://intro-stat-learning.github.io/ISLP/)。
- **核查日期 / 状态**：2026-10-08；已读取官方 Python 版介绍与配套实验入口；未运行所有实验。

<a id="bok-03"></a>

<!-- resource: BOK-03 -->
### Dive into Deep Learning

- **官方入口**：[作者 / 出版社页面](https://d2l.ai/)。
- **类型 / 版本**：书籍 / 2023 年 Cambridge University Press 版；在线版持续更新，核查时页面标示 1.0.3。
- **难度 / 路线**：入门 → 中级 / 算法；Agent 路线的模型基础选读。
- **前置知识**：Python、基础线性代数与微积分。
- **推荐理由**：把数学解释和可运行训练代码放在一起，从基础网络走到注意力、Transformer 与计算实践。
- **获取方式**：在线全文与配套代码免费；纸质版付费。官网提供多种框架版本，建议先选 PyTorch。
- **建议先阅读**：预备知识 → 线性神经网络 → 多层感知机 → 注意力机制与 Transformer。
- **实践任务**：训练一个小型分类模型，保存训练与验证曲线，分析过拟合并做一次改进。
- **配套材料 / 版本依据**：[作者在线教材与出版 BibTeX](https://d2l.ai/)。
- **核查日期 / 状态**：2026-10-08；已读取官网内容目录与 2023 年出版记录；未执行全部代码。

<a id="bok-04"></a>

<!-- resource: BOK-04 -->
### Understanding Deep Learning

- **官方入口**：[作者 / 出版社页面](https://udlbook.github.io/udlbook/)。
- **类型 / 版本**：书籍 / 2023 年 MIT Press 版（2023-12-05 出版）。
- **难度 / 路线**：入门 → 中级 / 算法。
- **前置知识**：基础线性代数、微积分与概率；练习需要 Python。
- **推荐理由**：适合用图示建立神经网络、优化、Transformer 和生成模型的直觉，再补数学推导。
- **获取方式**：出版社明确提供 Open Access 全文入口；作者的 Notebooks、Slides 等配套材料公开。作者站正文依赖前端渲染，本轮网页文本未解析到完整正文，PDF 下载未回读。
- **建议先阅读**：监督学习与网络 → 损失和训练 → Transformer / 扩散模型；选对应 Notebook。
- **实践任务**：解释损失函数和反向传播，完成一个优化或网络训练 Notebook 并写学习笔记。
- **配套材料 / 版本依据**：[出版社：年份与 Open Access](https://mitpress.mit.edu/9780262377102/understanding-deep-learning/) · [作者配套仓库](https://github.com/udlbook/udlbook)。
- **核查日期 / 状态**：2026-10-08；已核对出版社年份、开放访问说明与作者仓库目录；全文文件可下载性待核查。

<a id="bok-05"></a>

<!-- resource: BOK-05 -->
### Build a Large Language Model (From Scratch)

- **官方入口**：[作者 / 出版社页面](https://www.manning.com/books/build-a-large-language-model-from-scratch)。
- **类型 / 版本**：书籍 / 2024 年 Manning 版（2024 年 9 月出版）。
- **难度 / 路线**：中级 / 双路线。
- **前置知识**：Python、基础 ML 与 PyTorch。
- **推荐理由**：通过分词、注意力、GPT 训练和微调形成完整链条，帮助应用开发者理解模型内部。
- **获取方式**：完整书籍付费；官方配套代码免费，代码公开不等于正文免费。
- **建议先阅读**：文本处理 → 注意力 → GPT 结构 → 预训练 → 微调；与章节代码同步。
- **实践任务**：实现并训练一个小型 GPT，记录参数量、数据划分、损失和生成样例。
- **配套材料 / 版本依据**：[作者官方代码](https://github.com/rasbt/LLMs-from-scratch) · [本合集项目条目](../projects/README.md#prj-18)。
- **核查日期 / 状态**：2026-10-08；已核对出版社出版时间和官方代码入口；未复现书中完整训练。

<a id="bok-06"></a>

<!-- resource: BOK-06 -->
### Reinforcement Learning: An Introduction

- **官方入口**：[作者 / 出版社页面](http://incompleteideas.net/book/the-book-2nd.html)。
- **类型 / 版本**：书籍 / 第二版，2018 年 MIT Press 版；不采用 1998 年第一版。
- **难度 / 路线**：中级 → 进阶 / 算法 · RL。
- **前置知识**：概率、期望、基础线性代数；实验需要 Python。
- **推荐理由**：建立 MDP、Bellman 方程、动态规划、TD 与策略梯度基础，避免直接读深度 RL 时混淆核心概念。
- **获取方式**：出版社列出作者提供的免费 Open Access 版；纸质版付费。本轮作者站 HTTP / HTTPS 访问超时，使用出版社确认版本与免费入口，PDF 下载待核查。
- **建议先阅读**：多臂老虎机 → MDP → 动态规划 → MC / TD → 函数近似 → 策略梯度。
- **实践任务**：实现表格型 TD 或 Q-learning，分析探索率与学习率对结果的影响。
- **配套材料 / 版本依据**：[出版社：第二版与 Open Access](https://mitpress.mit.edu/9780262039246/reinforcement-learning/)。
- **核查日期 / 状态**：2026-10-08；已读取出版社说明；作者站访问与全文文件可下载性待核查。

<a id="bok-07"></a>

<!-- resource: BOK-07 -->
### PyTorch Tutorials

- **官方入口**：[官方文档](https://docs.pytorch.org/tutorials/)。
- **类型 / 版本**：官方文档 / 持续更新；页面快照 2026-10-08，使用时按实际安装的 PyTorch 版本选择文档。
- **难度 / 路线**：入门 → 中级 / 双路线。
- **前置知识**：Python、数组与基本 ML 概念。
- **推荐理由**：从 Tensor、Dataset / DataLoader、Autograd 到训练循环，建立读论文代码所需的框架基础。
- **获取方式**：官方教程免费；执行示例需要匹配 Python、PyTorch 和设备环境。
- **建议先阅读**：Learn the Basics → Tensors → Datasets / DataLoaders → Autograd → Optimization。
- **实践任务**：写一个能训练、保存和重新加载的分类模型，并确认训练与推理模式的区别。
- **配套材料 / 版本依据**：[官方教程](https://docs.pytorch.org/tutorials/)。
- **核查日期 / 状态**：2026-10-08；已读取官方教程入口；示例执行与版本兼容性未验证。

<a id="bok-08"></a>

<!-- resource: BOK-08 -->
### Hugging Face Transformers Documentation

- **官方入口**：[官方文档](https://huggingface.co/docs/transformers/index)。
- **类型 / 版本**：官方文档 / 持续更新；页面快照 2026-10-08，不固定库版本。
- **难度 / 路线**：中级 / 双路线。
- **前置知识**：Python、PyTorch、Tokenizer 与语言模型基础。
- **推荐理由**：连接公开模型、分词器、推理与训练接口，适合在理解基础模型后学习工程化使用。
- **获取方式**：文档免费；不同模型的权重、许可、访问审批和运行资源要求分别查看模型卡。
- **建议先阅读**：安装 / Quickstart → Tokenizer 与模型加载 → 推理 → 训练或微调；按实际版本读 API。
- **实践任务**：固定模型与依赖版本，完成一项推理任务并记录输入处理、输出和限制。
- **配套材料 / 版本依据**：[官方文档](https://huggingface.co/docs/transformers/index)。
- **核查日期 / 状态**：2026-10-08；已读取官方入口；具体模型下载、库安装与示例执行未验证。

<a id="bok-09"></a>

<!-- resource: BOK-09 -->
### Model Context Protocol Documentation

- **官方入口**：[官方文档](https://modelcontextprotocol.io/docs/getting-started/intro)。
- **类型 / 版本**：官方文档 / 持续更新；页面快照 2026-10-08；实现时另记录使用的协议版本。
- **难度 / 路线**：入门 → 中级 / Agent。
- **前置知识**：Python 或 TypeScript、JSON、API 与客户端 / 服务端概念。
- **推荐理由**：理解 Agent 应用如何通过标准接口连接工具与数据，并区分 Host、Client、Server 的职责。
- **获取方式**：官方文档免费；协议介绍与具体 SDK 文档需要结合阅读。
- **建议先阅读**：Introduction → 架构概念 → Tools / Resources / Prompts → 选择 SDK 与传输方式。
- **实践任务**：接入一个本地只读工具，定义输入 Schema、超时和错误返回，并记录调用过程。
- **配套材料 / 版本依据**：[官方入门文档](https://modelcontextprotocol.io/docs/getting-started/intro)。
- **核查日期 / 状态**：2026-10-08；已读取官方介绍；协议 / SDK 兼容性与服务运行未验证。

<a id="bok-10"></a>

<!-- resource: BOK-10 -->
### LangGraph Documentation

- **官方入口**：[官方文档](https://docs.langchain.com/oss/python/langgraph/overview)。
- **类型 / 版本**：官方文档 / Python OSS 文档；持续更新，页面快照 2026-10-08。
- **难度 / 路线**：中级 / Agent。
- **前置知识**：Python、类型标注、状态机、模型与工具调用。
- **推荐理由**：系统学习状态、节点、边、持久化和人工介入，将多步骤任务变成可检查的执行过程。
- **获取方式**：OSS 开发文档免费；相关托管服务的访问与计费另行查看服务说明。
- **建议先阅读**：Overview → Quickstart → Graph API → Persistence → Interrupts；结合项目示例。
- **实践任务**：实现带检查点和人工确认节点的工作流，验证失败后能够恢复并避免重复执行。
- **配套材料 / 版本依据**：[官方 Python OSS 文档](https://docs.langchain.com/oss/python/langgraph/overview) · [本合集项目条目](../projects/README.md#prj-04)。
- **核查日期 / 状态**：2026-10-08；已读取官方入口与职责说明；未运行工作流。
