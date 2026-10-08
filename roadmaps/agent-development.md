# Roadmap · Agent 应用开发

[返回首页](../README.md) · [算法研究路线](ai-research.md)

目标：从能调用模型的问答应用，逐步做出有知识检索、工具、状态管理、评估与恢复能力的 Agent。按阶段产出推进；已经满足验收标准的阶段可以跳过。每阶段选一套主资源，其他资料用于补充，不要求读完全部清单。

## 路线总览

| 阶段 | 核心能力 | 阶段产出 |
| --- | --- | --- |
| 1 · Python / API | 文件、HTTP、JSON、异常与测试 | 可测试的命令行工具 |
| 2 · LLM 基础 | 消息、Token、上下文、结构化输出 | 问答应用 |
| 3 · RAG | 摄取、分块、检索、引用与评估 | 知识库助手 |
| 4 · 工具与 MCP | 工具 Schema、协议角色、错误与边界 | 工具助手 |
| 5 · 工作流与多 Agent | 状态、分支、持久化、人工介入 | 可恢复的多步骤 Agent |
| 6 · 评估与部署 | 任务集、追踪、预算与服务运行 | 可评估的 Agent 与部署说明 |

## 1 · Python / API

**前置知识**：无需 AI 经验。已有 Python 基础则直接完成小任务检验。

**主资源**：[CS50P](../resources/courses.md#crs-01)。按需补充 [CS50 AI](../resources/courses.md#crs-04) 的搜索与知识表示；它对 Python 经验的要求高于 CS50P。

**任务**：写一个读取 JSON 输入、调用 HTTP 接口并保存结果的命令行程序。模型凭据从环境变量读取；把 API 调用封装成独立函数，使正常结果、超时和无效返回可以分别验证。

**验收**：能够解释请求与响应、处理超时及 JSON 格式错误，写清安装和运行命令；提供一次正常调用和两类失败案例的记录。

## 2 · LLM 基础：问答应用

**前置知识**：阶段 1；了解客户端调用和异步任务的基本概念。

**主资源**：[LLMs from Scratch](../projects/README.md#prj-18) 的分词与注意力部分、[Transformers 文档](../resources/books-and-docs.md#bok-08)。理论补充 [Attention Is All You Need](../papers/README.md#pap-01) 与 [Chain-of-Thought](../papers/README.md#pap-15)；此阶段无需完整预训练模型。

**任务**：做一个支持多轮对话、结构化结果和上下文限制的问答应用。明确模型、提示模板、输入截断策略及费用 / Token 记录。

**验收**：准备至少 10 个固定问题，检查结果格式、空输入、长输入和模型请求失败；能区分提示修改与模型能力变化。不把模型生成的推理描述当作事实核验。

## 3 · RAG：知识库助手

**前置知识**：阶段 2；理解文档、向量、相似度与检索的基本概念。

**主资源**：[RAG 论文](../papers/README.md#pap-20) + [LlamaIndex](../projects/README.md#prj-12) 或 [Haystack](../projects/README.md#prj-13)，二选一。想先观察完整平台，可参考 [Dify](../projects/README.md#prj-10) 或 [RAGFlow](../projects/README.md#prj-11)。

**任务**：把一批允许使用的文档做成带引用的知识库助手，保留文件名、页码或章节、分块编号和原文。构建至少 20 个问答样例，其中包含知识库没有答案的问题。

**验收**：分别报告检索命中与回答质量；对比至少两种分块或检索配置；引用能回到支持回答的具体原文，未检索到证据时明确表达不确定性。把开发集与最终评估集分开，避免用测试问题调提示。

## 4 · 工具调用与 MCP：工具助手

**前置知识**：阶段 2；阶段 3 可并行补齐。会定义类型、参数和返回结果。

**主资源**：[MCP 官方文档](../resources/books-and-docs.md#bok-09)、[ReAct](../papers/README.md#pap-21)、[nanobot](../projects/README.md#prj-03)。想练习严格结构化输入输出可选 [PydanticAI](../projects/README.md#prj-08)。

**任务**：接入一个只读检索工具和一个计算工具，再实现一个本地 MCP Server。定义工具参数、超时、失败返回和调用次数上限，记录从用户目标到工具结果的执行路径。

**验收**：工具返回无效数据时能够终止或重试；不把工具内容中的指令直接当作系统指令。若加入修改数据或发送消息的工具，明确人工确认点，并用模拟输入验证确认前不会执行写入。

## 5 · 工作流与多 Agent

**前置知识**：阶段 4；理解状态机和任务分解。

**主资源**：[LangGraph 项目](../projects/README.md#prj-04) 与 [官方文档](../resources/books-and-docs.md#bok-10)。参考完整系统时，在 [DeerFlow 2.0](../projects/README.md#prj-02)、[OpenClaw](../projects/README.md#prj-01)、[Microsoft Agent Framework](../projects/README.md#prj-07) 中选一个。专题课选 [Berkeley LLM Agents](../resources/courses.md#crs-15)。

**任务**：先实现单 Agent 的「规划 → 检索 → 整理 → 检查」工作流，加入检查点与人工介入，再挑一个子任务尝试拆成多个 Agent。保留相同输入与模型配置，比较单 Agent 与多 Agent 的完成率、耗时和 Token 使用。

**验收**：中断后能从已保存状态恢复，避免重复执行具有外部影响的操作；说明增加子 Agent 带来的实际收益与成本。不要仅凭 Agent 数量判断系统能力。

**延伸选读**：[smolagents](../projects/README.md#prj-05)、[CrewAI](../projects/README.md#prj-06)、[Agno](../projects/README.md#prj-09) 的编排思路；[AutoGen 论文](../papers/README.md#pap-25) 用作历史研究阅读，其项目已进入维护模式。

## 6 · 评估与部署：可评估的 Agent

**前置知识**：阶段 3–5 的实践产出；会读取日志、配置运行环境。

**主资源**：[Langfuse](../projects/README.md#prj-16)、[GAIA](../papers/README.md#pap-27)、[Gaia2](../papers/README.md#pap-28)。浏览器或软件工程任务可参考 [Browser Use](../projects/README.md#prj-14)、[SWE-agent](../papers/README.md#pap-26) 和 [OpenHands](../projects/README.md#prj-15)，这些扩展不是必修项。

**任务**：把已有 Agent 形成一个可评估的小服务。准备至少 30 个目标明确的任务，包含正常案例、缺失信息、工具失败和长任务；定义成功标准，记录工具轨迹、耗时、Token 和人工介入次数。

**验收**：固定模型与配置，重复评估并保存失败案例；至少与一个简单基线比较。提供启动说明、依赖版本、配置样例、停止方法、失败恢复与评估报告。若实际发布到服务器，单独记录目标环境、健康检查和真实请求结果；本合集提供的文档核查不等于部署完成。

## 最终交付清单

- 可运行的问答、知识库和工具能力，或整合后的一个应用。
- 资源与数据来源说明，含文档引用和模型 / 依赖版本。
- 评估任务、判断规则、基线对比、失败案例与调用追踪。
- 人工确认节点、重试 / 超时 / 调用预算与恢复说明。
- 新使用者可遵循的运行文档；实际部署验证另记。

想深入模型训练与 RL 对齐，再进入 [算法研究路线](ai-research.md) 的 Transformer、对齐和强化学习分支。
