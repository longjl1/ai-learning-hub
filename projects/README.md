# 项目与参考实现

[返回首页](../README.md) · [Agent 路线](../roadmaps/agent-development.md) · [算法路线](../roadmaps/ai-research.md)

20 个项目：16 个 Agent 系统、框架或配套平台，以及 4 个模型 / RL 实践项目。收录顺序按学习用途，非热度排名。

**核查日期：2026-10-08（Asia/Hong_Kong）。** 官方仓库与 README 已读取；下列所有项目的运行状态均为「未在本地安装或运行」。Stars 是当日 API 快照，最近推送不等于稳定版本发布。详见[核查记录](../VERIFICATION.md)。

## 快速导航

| 条目 | 项目 | 分类 | 难度 | 路线 |
| --- | --- | --- | --- | --- |
| PRJ-01 | [OpenClaw](#prj-01) | 个人助手与完整 Agent 系统 | 进阶 | Agent |
| PRJ-02 | [DeerFlow](#prj-02) | 个人助手与完整 Agent 系统 | 进阶 | Agent |
| PRJ-03 | [nanobot](#prj-03) | 个人助手与完整 Agent 系统 | 入门 → 中级 | Agent |
| PRJ-04 | [LangGraph](#prj-04) | Agent 编排与开发框架 | 中级 | Agent |
| PRJ-05 | [smolagents](#prj-05) | Agent 编排与开发框架 | 入门 → 中级 | Agent |
| PRJ-06 | [CrewAI](#prj-06) | Agent 编排与开发框架 | 中级 | Agent |
| PRJ-07 | [Microsoft Agent Framework](#prj-07) | Agent 编排与开发框架 | 中级 → 进阶 | Agent |
| PRJ-08 | [PydanticAI](#prj-08) | Agent 编排与开发框架 | 中级 | Agent |
| PRJ-09 | [Agno](#prj-09) | Agent 编排与开发框架 | 中级 → 进阶 | Agent |
| PRJ-10 | [Dify](#prj-10) | RAG 与应用平台 | 入门 → 中级 | Agent |
| PRJ-11 | [RAGFlow](#prj-11) | RAG 与应用平台 | 中级 | Agent |
| PRJ-12 | [LlamaIndex](#prj-12) | RAG 与应用平台 | 中级 | Agent |
| PRJ-13 | [Haystack](#prj-13) | RAG 与应用平台 | 中级 | Agent |
| PRJ-14 | [Browser Use](#prj-14) | 浏览器、代码执行与评估 | 中级 → 进阶 | Agent |
| PRJ-15 | [OpenHands](#prj-15) | 浏览器、代码执行与评估 | 进阶 | Agent |
| PRJ-16 | [Langfuse](#prj-16) | 浏览器、代码执行与评估 | 中级 | Agent |
| PRJ-17 | [nanoGPT](#prj-17) | 模型训练与算法实践 | 中级 | 算法 |
| PRJ-18 | [LLMs from Scratch](#prj-18) | 模型训练与算法实践 | 中级 | 算法 |
| PRJ-19 | [CleanRL](#prj-19) | 模型训练与算法实践 | 中级 → 进阶 | 算法 |
| PRJ-20 | [Stable-Baselines3](#prj-20) | 模型训练与算法实践 | 中级 | 算法 |

<a id="prj-01"></a>

<!-- resource: PRJ-01 -->
### OpenClaw

- **官方仓库**：[openclaw/openclaw](https://github.com/openclaw/openclaw)；[README](https://github.com/openclaw/openclaw/blob/main/README.md)。
- **分类 / 难度 / 路线**：个人助手与完整 Agent 系统 / 进阶 / Agent。
- **前置知识**：TypeScript / Node.js、工具调用、服务部署。
- **推荐理由**：从消息通道、Gateway、工具与记忆的连接方式理解完整个人助手架构。
- **先读什么**：先读 README 的 How it fits together 与官方 Getting started，再读 Gateway / tools / skills 文档。
- **适合练习**：配置一个测试通道和一个只读工具，画出消息进入、模型调用、工具执行、回复的完整链路。
- **版本与状态**：保留 2026 关注入口；模型与通道配置影响运行成本。
- **关注度快照**：391,625 Stars；未归档；最近推送 2026-10-08T08:27:37Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-02"></a>

<!-- resource: PRJ-02 -->
### DeerFlow

- **官方仓库**：[bytedance/deer-flow](https://github.com/bytedance/deer-flow)；[README](https://github.com/bytedance/deer-flow/blob/main/README.md)。
- **分类 / 难度 / 路线**：个人助手与完整 Agent 系统 / 进阶 / Agent。
- **前置知识**：Python、前端基础、工作流、Docker。
- **推荐理由**：学习长任务中子 Agent、记忆、技能与沙箱如何协同。
- **先读什么**：先读 README 的 2.0 说明与核心功能，再看 backend 与配置示例。
- **适合练习**：做一个有来源引用的研究报告工作流，记录子任务、失败重试和最终引用。
- **版本与状态**：按 2.0 介绍；旧 Deep Research 1.x 位于 main-1.x 分支，不能混用旧教程。
- **关注度快照**：83,493 Stars；未归档；最近推送 2026-10-08T06:24:51Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-03"></a>

<!-- resource: PRJ-03 -->
### nanobot

- **官方仓库**：[HKUDS/nanobot](https://github.com/HKUDS/nanobot)；[README](https://github.com/HKUDS/nanobot/blob/main/README.md)。
- **分类 / 难度 / 路线**：个人助手与完整 Agent 系统 / 入门 → 中级 / Agent。
- **前置知识**：Python、API、基本异步编程。
- **推荐理由**：用相对易读的 Python 个人 Agent 核心理解工具、会话、长期记忆与消息渠道。
- **先读什么**：先读 README 的 Start Here，再读 docs/architecture.md 和 development 文档。
- **适合练习**：实现一个查询本地笔记的工具，观察会话历史、工具结果与长期记忆的区别。
- **版本与状态**：模型调用与外部通道仍需自行配置；轻量不等于没有部署条件。
- **关注度快照**：48,856 Stars；未归档；最近推送 2026-10-08T07:31:17Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-04"></a>

<!-- resource: PRJ-04 -->
### LangGraph

- **官方仓库**：[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)；[README](https://github.com/langchain-ai/langgraph/blob/main/README.md)。
- **分类 / 难度 / 路线**：Agent 编排与开发框架 / 中级 / Agent。
- **前置知识**：Python、状态管理、工具调用。
- **推荐理由**：把 Agent 写成有状态图，练习条件路由、持久化、恢复与人工介入。
- **先读什么**：先读官方 Overview，再看状态、节点、边和 checkpoint 示例。
- **适合练习**：构建检索 → 判断 → 回答流程，并测试中断后恢复和人工确认节点。
- **版本与状态**：低层编排框架；本条关注 graph 与持久状态，避免只复制聊天示例。
- **关注度快照**：42,877 Stars；未归档；最近推送 2026-10-08T07:26:46Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-05"></a>

<!-- resource: PRJ-05 -->
### smolagents

- **官方仓库**：[huggingface/smolagents](https://github.com/huggingface/smolagents)；[README](https://github.com/huggingface/smolagents/blob/main/README.md)。
- **分类 / 难度 / 路线**：Agent 编排与开发框架 / 入门 → 中级 / Agent。
- **前置知识**：Python、模型 API、工具函数。
- **推荐理由**：通过小型框架比较代码型 Agent 与结构化工具调用。
- **先读什么**：先读 README 与官方文档的 Agent / tools 示例。
- **适合练习**：让 Agent 调用两个明确的工具完成数据查询，对照两种行动表示。
- **版本与状态**：执行模型生成代码时应使用项目支持的隔离方式；这是学习任务的运行条件。
- **关注度快照**：29,729 Stars；未归档；最近推送 2026-10-06T18:35:07Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-06"></a>

<!-- resource: PRJ-06 -->
### CrewAI

- **官方仓库**：[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)；[README](https://github.com/crewAIInc/crewAI/blob/main/README.md)。
- **分类 / 难度 / 路线**：Agent 编排与开发框架 / 中级 / Agent。
- **前置知识**：Python、任务拆解、LLM API。
- **推荐理由**：学习角色、任务、协作流程，以及什么时候多 Agent 才有实际收益。
- **先读什么**：先看 README、官方 Crews 与 Flows 文档。
- **适合练习**：用同一组样例比较单 Agent 与研究员 / 审阅员流程的质量、成本和耗时。
- **版本与状态**：同时关注 Crew 与 Flow；用评估决定是否需要多个角色。
- **关注度快照**：59,445 Stars；未归档；最近推送 2026-10-08T06:03:59Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-07"></a>

<!-- resource: PRJ-07 -->
### Microsoft Agent Framework

- **官方仓库**：[microsoft/agent-framework](https://github.com/microsoft/agent-framework)；[README](https://github.com/microsoft/agent-framework/blob/main/README.md)。
- **分类 / 难度 / 路线**：Agent 编排与开发框架 / 中级 → 进阶 / Agent。
- **前置知识**：Python 或 .NET、异步编程、服务部署。
- **推荐理由**：学习跨运行时的 Agent 与工作流编排、checkpoint、观测和服务化。
- **先读什么**：先读 README 的适用场景，再看 python/samples 或 dotnet/samples 中的工作流。
- **适合练习**：实现顺序工作流与一次 handoff，记录状态恢复和 trace。
- **版本与状态**：AutoGen 已进入维护模式；微软官方建议新用户采用本框架。
- **关注度快照**：14,000 Stars；未归档；最近推送 2026-10-08T08:33:37Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-08"></a>

<!-- resource: PRJ-08 -->
### PydanticAI

- **官方仓库**：[pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)；[README](https://github.com/pydantic/pydantic-ai/blob/main/README.md)。
- **分类 / 难度 / 路线**：Agent 编排与开发框架 / 中级 / Agent。
- **前置知识**：Python 类型标注、Pydantic、API。
- **推荐理由**：用类型和验证约束模型输出，把 Agent 接入常规 Python 应用。
- **先读什么**：先读 README 和官方文档中的 typed outputs、tools 与 dependency 示例。
- **适合练习**：生成结构化研究摘要，并测试字段缺失、格式错误和工具失败。
- **版本与状态**：先建立输出验证，再扩展实时接口或更多模型提供商。
- **关注度快照**：20,481 Stars；未归档；最近推送 2026-10-08T04:00:32Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-09"></a>

<!-- resource: PRJ-09 -->
### Agno

- **官方仓库**：[agno-agi/agno](https://github.com/agno-agi/agno)；[README](https://github.com/agno-agi/agno/blob/main/README.md)。
- **分类 / 难度 / 路线**：Agent 编排与开发框架 / 中级 → 进阶 / Agent。
- **前置知识**：Python、Agent 基础、服务部署。
- **推荐理由**：学习 Agent SDK、运行时和管理界面如何组成可运维的平台。
- **先读什么**：先读 README 的 Introduction，再看官方 Agent / AgentOS 示例。
- **适合练习**：将一个已有工具助手服务化，检查会话保存、记忆读写与观测。
- **版本与状态**：README 当前围绕 SDK、AgentOS runtime 与 UI 展开。
- **关注度快照**：42,610 Stars；未归档；最近推送 2026-10-08T08:26:04Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-10"></a>

<!-- resource: PRJ-10 -->
### Dify

- **官方仓库**：[langgenius/dify](https://github.com/langgenius/dify)；[README](https://github.com/langgenius/dify/blob/main/README.md)。
- **分类 / 难度 / 路线**：RAG 与应用平台 / 入门 → 中级 / Agent。
- **前置知识**：LLM 基础、检索概念；自部署需 Docker。
- **推荐理由**：用可视化工作流快速理解 RAG、模型、工具和应用接口的组合。
- **先读什么**：先看 README、官方自部署说明和工作流文档。
- **适合练习**：建一个带引用的知识库问答应用，再比较检索设置与提示词修改的影响。
- **版本与状态**：仓库包含自定义许可条款；云服务费用与自部署条件见官方页面。
- **关注度快照**：158,079 Stars；未归档；最近推送 2026-10-08T08:17:32Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-11"></a>

<!-- resource: PRJ-11 -->
### RAGFlow

- **官方仓库**：[infiniflow/ragflow](https://github.com/infiniflow/ragflow)；[README](https://github.com/infiniflow/ragflow/blob/main/README.md)。
- **分类 / 难度 / 路线**：RAG 与应用平台 / 中级 / Agent。
- **前置知识**：RAG、文档解析、向量检索、Docker。
- **推荐理由**：理解文档解析、切分、检索和上下文质量对 Agent 的影响。
- **先读什么**：先读 README 与官方文档，优先看文档处理和检索流程。
- **适合练习**：对同一批文档比较解析和分块策略，记录引用定位及检索错误。
- **版本与状态**：本条关注文档上下文层；不要把产品功能列表视作已验证的效果。
- **关注度快照**：91,808 Stars；未归档；最近推送 2026-10-08T08:05:28Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-12"></a>

<!-- resource: PRJ-12 -->
### LlamaIndex

- **官方仓库**：[run-llama/llama_index](https://github.com/run-llama/llama_index)；[README](https://github.com/run-llama/llama_index/blob/main/README.md)。
- **分类 / 难度 / 路线**：RAG 与应用平台 / 中级 / Agent。
- **前置知识**：Python、RAG、索引与检索。
- **推荐理由**：学习把文档数据接到 LLM 应用，以及数据连接、索引和查询之间的边界。
- **先读什么**：先读 README 的当前定位说明，再查框架的 ingestion / query 示例。
- **适合练习**：实现有来源定位的文档问答，把数据摄取和在线查询拆成两个步骤。
- **版本与状态**：当前 README 强调文档解析与提取，框架仓库仍保留索引和查询能力；云产品与框架分开辨认。
- **关注度快照**：52,436 Stars；未归档；最近推送 2026-10-06T19:11:28Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-13"></a>

<!-- resource: PRJ-13 -->
### Haystack

- **官方仓库**：[deepset-ai/haystack](https://github.com/deepset-ai/haystack)；[README](https://github.com/deepset-ai/haystack/blob/main/README.md)。
- **分类 / 难度 / 路线**：RAG 与应用平台 / 中级 / Agent。
- **前置知识**：Python、检索、组件化流程。
- **推荐理由**：用显式组件与 Pipeline 组织检索、路由和生成，便于定位错误。
- **先读什么**：先读 README 和官方文档的 Pipeline / component 示例。
- **适合练习**：搭建检索 Pipeline，并为检索为空、路由失败、回答缺少依据设计检查。
- **版本与状态**：学习可组合的组件边界，避免仅关注最终聊天界面。
- **关注度快照**：26,694 Stars；未归档；最近推送 2026-10-07T16:35:09Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-14"></a>

<!-- resource: PRJ-14 -->
### Browser Use

- **官方仓库**：[browser-use/browser-use](https://github.com/browser-use/browser-use)；[README](https://github.com/browser-use/browser-use/blob/main/README.md)。
- **分类 / 难度 / 路线**：浏览器、代码执行与评估 / 中级 → 进阶 / Agent。
- **前置知识**：Python、浏览器自动化、工具调用。
- **推荐理由**：理解浏览器状态、观察与行动之间的反馈循环。
- **先读什么**：先看 README，再读官方 quickstart 与浏览器配置。
- **适合练习**：在自建测试页面完成搜索与信息提取，记录步骤、截图和失败原因。
- **版本与状态**：区分开源库、本地浏览器与托管服务；各自运行条件不同。
- **关注度快照**：117,441 Stars；未归档；最近推送 2026-10-07T18:42:14Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-15"></a>

<!-- resource: PRJ-15 -->
### OpenHands

- **官方仓库**：[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)；[README](https://github.com/OpenHands/OpenHands/blob/main/README.md)。
- **分类 / 难度 / 路线**：浏览器、代码执行与评估 / 进阶 / Agent。
- **前置知识**：Agent、开发环境、沙箱、服务部署。
- **推荐理由**：学习编码 Agent 的任务管理、后端连接与执行环境。
- **先读什么**：先读当前 README 的 Agent Canvas 与 backend 文档，再辨认 SDK / 旧版本材料。
- **适合练习**：用一个测试仓库完成小修改，检查工具日志、diff、测试与任务回放。
- **版本与状态**：当前主分支介绍 Agent Canvas（beta），与早期 OpenHands 平台教程存在版本差异；保留官方仓库入口并注明变化。
- **关注度快照**：90,247 Stars；未归档；最近推送 2026-10-08T06:02:25Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-16"></a>

<!-- resource: PRJ-16 -->
### Langfuse

- **官方仓库**：[langfuse/langfuse](https://github.com/langfuse/langfuse)；[README](https://github.com/langfuse/langfuse/blob/main/README.md)。
- **分类 / 难度 / 路线**：浏览器、代码执行与评估 / 中级 / Agent。
- **前置知识**：LLM 应用、日志、基础评估。
- **推荐理由**：学习 trace、数据集与评估如何帮助定位检索、模型和工具错误。
- **先读什么**：先读 README，按官方 tracing 和 evaluation 文档接入一个应用。
- **适合练习**：对固定 20 个样例记录版本、token、耗时和人工评分，比较两次改动。
- **版本与状态**：它是观测与评估平台，作为 Agent 工程配套资源收录。
- **关注度快照**：35,514 Stars；未归档；最近推送 2026-10-08T08:28:09Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-17"></a>

<!-- resource: PRJ-17 -->
### nanoGPT

- **官方仓库**：[karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)；[README](https://github.com/karpathy/nanoGPT/blob/master/README.md)。
- **分类 / 难度 / 路线**：模型训练与算法实践 / 中级 / 算法。
- **前置知识**：PyTorch、Transformer、训练循环。
- **推荐理由**：以紧凑的模型与训练脚本阅读 GPT 的核心实现。
- **先读什么**：先读 README 顶部弃用说明，再看 model.py 与 train.py。
- **适合练习**：在小文本集上训练字符模型，保存训练 / 验证损失与生成样例。
- **版本与状态**：作者于 2025-11 标注弃用并推荐 nanochat；本合集保留其经典代码阅读价值，不作为当前生产方案。
- **关注度快照**：63,630 Stars；未归档；最近推送 2025-11-12T19:52:34Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-18"></a>

<!-- resource: PRJ-18 -->
### LLMs from Scratch

- **官方仓库**：[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)；[README](https://github.com/rasbt/LLMs-from-scratch/blob/main/README.md)。
- **分类 / 难度 / 路线**：模型训练与算法实践 / 中级 / 算法。
- **前置知识**：Python、PyTorch、基础深度学习。
- **推荐理由**：从 tokenizer、注意力到预训练和微调逐步实现小型 LLM。
- **先读什么**：按官方书籍章节对应的 notebooks 顺序阅读。
- **适合练习**：完成小型 GPT 实现，解释张量形状、causal mask、损失函数和采样策略。
- **版本与状态**：这是收录书籍的官方配套代码；代码项目与书籍是不同类型的资源。
- **关注度快照**：106,205 Stars；未归档；最近推送 2026-10-02T14:55:52Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-19"></a>

<!-- resource: PRJ-19 -->
### CleanRL

- **官方仓库**：[vwxyzjn/cleanrl](https://github.com/vwxyzjn/cleanrl)；[README](https://github.com/vwxyzjn/cleanrl/blob/master/README.md)。
- **分类 / 难度 / 路线**：模型训练与算法实践 / 中级 → 进阶 / 算法。
- **前置知识**：MDP、PyTorch、PPO 或 SAC。
- **推荐理由**：通过单文件实现追踪强化学习算法从公式到 rollout、更新与日志的路径。
- **先读什么**：先读 README / 官方 docs，再读 PPO 或 SAC 的单文件脚本。
- **适合练习**：跑一个小环境的 PPO 实验，报告至少三个随机种子、评估回报与配置。
- **版本与状态**：作为研究实现参考；实际训练未在本合集制作过程中执行。
- **关注度快照**：10,508 Stars；未归档；最近推送 2026-04-20T10:57:15Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。

<a id="prj-20"></a>

<!-- resource: PRJ-20 -->
### Stable-Baselines3

- **官方仓库**：[DLR-RM/stable-baselines3](https://github.com/DLR-RM/stable-baselines3)；[README](https://github.com/DLR-RM/stable-baselines3/blob/master/README.md)。
- **分类 / 难度 / 路线**：模型训练与算法实践 / 中级 / 算法。
- **前置知识**：Python、Gymnasium、强化学习基本概念。
- **推荐理由**：用成熟实现建立基线，再与自己或 CleanRL 的实现比较。
- **先读什么**：先读 README 和官方 getting started / RL tips 文档。
- **适合练习**：训练一个策略基线，用独立评估环境比较 PPO 与 SAC 的适用条件。
- **版本与状态**：不同算法对应不同动作空间；比较前核对环境、预算和评估协议。
- **关注度快照**：13,875 Stars；未归档；最近推送 2026-09-09T14:05:40Z（UTC）。
- **核查 / 运行**：2026-10-08；仓库身份、元数据与 README 已核对；本地运行未验证。
