# 论文阅读清单：2017–2026

[返回首页](../README.md) · [算法路线](../roadmaps/ai-research.md) · [Agent 路线](../roadmaps/agent-development.md)

共 35 篇论文，按主题组织。这里的「首次公开年份」统一采用 **arXiv v1**，与会议 / 期刊发表年份分别记录；这不是对更早研讨会、草稿或博客首发时间的穷尽调查。2025–2026 年标为「近期研究」，其余为本路线的经典 / 代表性阅读。

**核查日期：2026-10-08。** 原文题名与 arXiv 记录已核对。中文说明是阅读指导；论文报告的实验结果不能直接推定到其他模型和部署环境。代码按作者来源辨认；完整训练代码、模型权重、推理示例和伪代码分别注明。

## 主题索引

| 条目 | 论文简称 | 首次公开 | 主题 | 路线 |
| --- | --- | --- | --- | --- |
| PAP-01 | [Attention Is All You Need](#pap-01) | 2017 | Transformer 与预训练 | 双路线 |
| PAP-02 | [BERT](#pap-02) | 2018 | Transformer 与预训练 | 算法 |
| PAP-03 | [GPT-3](#pap-03) | 2020 | Transformer 与预训练 | 双路线 |
| PAP-04 | [T5](#pap-04) | 2019 | Transformer 与预训练 | 算法 |
| PAP-05 | [Scaling Laws](#pap-05) | 2020 | Transformer 与预训练 | 算法 |
| PAP-06 | [Chinchilla](#pap-06) | 2022 | Transformer 与预训练 | 算法 |
| PAP-07 | [LoRA](#pap-07) | 2021 | 高效训练与多模态 | 双路线 |
| PAP-08 | [QLoRA](#pap-08) | 2023 | 高效训练与多模态 | 双路线 |
| PAP-09 | [FlashAttention](#pap-09) | 2022 | 高效训练与多模态 | 算法 |
| PAP-10 | [ViT](#pap-10) | 2020 | 高效训练与多模态 | 算法 |
| PAP-11 | [DDPM](#pap-11) | 2020 | 高效训练与多模态 | 算法 |
| PAP-12 | [CLIP](#pap-12) | 2021 | 高效训练与多模态 | 双路线 |
| PAP-13 | [Switch Transformers](#pap-13) | 2021 | 高效训练与多模态 | 算法 |
| PAP-14 | [InstructGPT](#pap-14) | 2022 | 对齐、推理与训练报告 | 双路线 |
| PAP-15 | [Chain-of-Thought](#pap-15) | 2022 | 对齐、推理与训练报告 | 双路线 |
| PAP-16 | [DPO](#pap-16) | 2023 | 对齐、推理与训练报告 | 算法 |
| PAP-17 | [DeepSeekMath](#pap-17) | 2024 | 对齐、推理与训练报告 | 算法 |
| PAP-18 | [DeepSeek-V3](#pap-18) | 2024 | 对齐、推理与训练报告 | 算法 |
| PAP-19 | [DeepSeek-R1](#pap-19) | 2025 · 近期研究 | 对齐、推理与训练报告 | 双路线 |
| PAP-20 | [RAG](#pap-20) | 2020 | RAG、Agent 与评估 | 双路线 |
| PAP-21 | [ReAct](#pap-21) | 2022 | RAG、Agent 与评估 | 双路线 |
| PAP-22 | [Toolformer](#pap-22) | 2023 | RAG、Agent 与评估 | 双路线 |
| PAP-23 | [Reflexion](#pap-23) | 2023 | RAG、Agent 与评估 | 双路线 |
| PAP-24 | [Voyager](#pap-24) | 2023 | RAG、Agent 与评估 | 双路线 |
| PAP-25 | [AutoGen](#pap-25) | 2023 | RAG、Agent 与评估 | Agent |
| PAP-26 | [SWE-agent](#pap-26) | 2024 | RAG、Agent 与评估 | Agent |
| PAP-27 | [GAIA](#pap-27) | 2023 | RAG、Agent 与评估 | 双路线 |
| PAP-28 | [Gaia2](#pap-28) | 2026 · 近期研究 | RAG、Agent 与评估 | 双路线 |
| PAP-29 | [PPO](#pap-29) | 2017 | 深度强化学习 | 算法 |
| PAP-30 | [SAC](#pap-30) | 2018 | 深度强化学习 | 算法 |
| PAP-31 | [TD3](#pap-31) | 2018 | 深度强化学习 | 算法 |
| PAP-32 | [AlphaZero](#pap-32) | 2017 | 深度强化学习 | 算法 |
| PAP-33 | [MuZero](#pap-33) | 2019 | 深度强化学习 | 算法 |
| PAP-34 | [DreamerV3](#pap-34) | 2023 | 深度强化学习 | 算法 |
| PAP-35 | [Decision Transformer](#pap-35) | 2021 | 深度强化学习 | 算法 |

## 年份索引

| arXiv v1 年份 | 阅读入口 |
| --- | --- |
| 2017 | [Attention Is All You Need](#pap-01)、[PPO](#pap-29)、[AlphaZero](#pap-32) |
| 2018 | [BERT](#pap-02)、[SAC](#pap-30)、[TD3](#pap-31) |
| 2019 | [T5](#pap-04)、[MuZero](#pap-33) |
| 2020 | [GPT-3](#pap-03)、[Scaling Laws](#pap-05)、[ViT](#pap-10)、[DDPM](#pap-11)、[RAG](#pap-20) |
| 2021 | [LoRA](#pap-07)、[CLIP](#pap-12)、[Switch Transformers](#pap-13)、[Decision Transformer](#pap-35) |
| 2022 | [Chinchilla](#pap-06)、[FlashAttention](#pap-09)、[InstructGPT](#pap-14)、[Chain-of-Thought](#pap-15)、[ReAct](#pap-21) |
| 2023 | [QLoRA](#pap-08)、[DPO](#pap-16)、[Toolformer](#pap-22)、[Reflexion](#pap-23)、[Voyager](#pap-24)、[AutoGen](#pap-25)、[GAIA](#pap-27)、[DreamerV3](#pap-34) |
| 2024 | [DeepSeekMath](#pap-17)、[DeepSeek-V3](#pap-18)、[SWE-agent](#pap-26) |
| 2025 | [DeepSeek-R1](#pap-19) |
| 2026 | [Gaia2](#pap-28) |

2017–2026 是收录窗口，不收录 2017 年之前的 DQN 等基础论文；这类概念由课程与教材补足。没有每年数量配额，2025 / 2026 的覆盖分别为 R1 / Gaia2。

<a id="pap-01"></a>

<!-- resource: PAP-01 -->
### Attention Is All You Need

**Attention Is All You Need**

- **原文**：[arXiv:1706.03762](https://arxiv.org/abs/1706.03762)。
- **首次公开 / 发表信息**：2017（arXiv v1）；[NeurIPS 2017](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)。
- **难度 / 路线 / 标签**：中级 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：线性代数、神经网络、序列建模。
- **核心问题**：如何高效建模序列之间的依赖？
- **主要贡献**：以注意力为核心构建 encoder-decoder Transformer，使用多头注意力、位置编码与前馈层。
- **推荐理由**：后续 LLM 与大量视觉模型的共同基础；先弄清张量形状和 mask。
- **阅读衔接**：先读 PyTorch 基础；再读 BERT、GPT-3。
- **作者代码 / 材料**：[tensorflow/tensor2tensor](https://github.com/tensorflow/tensor2tensor)；原始 Transformer 相关实现；仓库已归档。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-02"></a>

<!-- resource: PAP-02 -->
### BERT

**BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding**

- **原文**：[arXiv:1810.04805](https://arxiv.org/abs/1810.04805)。
- **首次公开 / 发表信息**：2018（arXiv v1）；[NAACL 2019](https://aclanthology.org/N19-1423/)。
- **难度 / 路线 / 标签**：中级 / 算法 / 经典 / 代表性阅读。
- **前置知识**：Transformer、预训练与微调。
- **核心问题**：怎样通过双向上下文预训练学习可迁移的语言表示？
- **主要贡献**：使用 masked language modeling 等目标训练双向 Transformer encoder，再微调到下游任务。
- **推荐理由**：理解 encoder 型预训练和 decoder 型生成模型的差异。
- **阅读衔接**：Attention Is All You Need；对照 GPT-3。
- **作者代码 / 材料**：[google-research/bert](https://github.com/google-research/bert)；官方 TensorFlow 代码与预训练模型；仓库已归档。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-03"></a>

<!-- resource: PAP-03 -->
### GPT-3

**Language Models are Few-Shot Learners**

- **原文**：[arXiv:2005.14165](https://arxiv.org/abs/2005.14165)。
- **首次公开 / 发表信息**：2020（arXiv v1）；[NeurIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html)。
- **难度 / 路线 / 标签**：中级 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：自回归语言模型、Transformer、评估。
- **核心问题**：模型能否仅凭上下文示例完成新任务？
- **主要贡献**：研究大规模自回归语言模型在 zero-shot、one-shot 和 few-shot 条件下的表现。
- **推荐理由**：理解 in-context learning，并区分上下文示例与参数微调。
- **阅读衔接**：Attention Is All You Need；再读 Scaling Laws。
- **作者代码 / 材料**：[openai/gpt-3](https://github.com/openai/gpt-3)；官方评估数据与样例入口；已归档，非完整 GPT-3 训练代码。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-04"></a>

<!-- resource: PAP-04 -->
### T5

**Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer**

- **原文**：[arXiv:1910.10683](https://arxiv.org/abs/1910.10683)。
- **首次公开 / 发表信息**：2019（arXiv v1）；[JMLR 21(140), 2020](https://www.jmlr.org/papers/v21/20-074.html)。
- **难度 / 路线 / 标签**：中级 / 算法 / 经典 / 代表性阅读。
- **前置知识**：Transformer、迁移学习、预训练。
- **核心问题**：不同 NLP 任务如何用统一接口训练和评估？
- **主要贡献**：以 text-to-text 框架比较预训练目标、数据、模型和迁移策略，形成 T5。
- **推荐理由**：学习统一任务接口和系统性的预训练实验设计。
- **阅读衔接**：Attention Is All You Need、BERT。
- **作者代码 / 材料**：[google-research/text-to-text-transfer-transformer](https://github.com/google-research/text-to-text-transfer-transformer)；作者官方 T5 实现与模型入口。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-05"></a>

<!-- resource: PAP-05 -->
### Scaling Laws

**Scaling Laws for Neural Language Models**

- **原文**：[arXiv:2001.08361](https://arxiv.org/abs/2001.08361)。
- **首次公开 / 发表信息**：2020（arXiv v1）；arXiv 预印本；会议 / 期刊信息待核查。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：语言模型训练、损失、对数图、实验设计。
- **核心问题**：模型规模、数据量与计算预算怎样影响语言模型损失？
- **主要贡献**：用经验幂律分析规模与性能关系，讨论受计算预算约束的训练选择。
- **推荐理由**：建立预算意识；结论需要结合后续 Chinchilla 的实验设置一起看。
- **阅读衔接**：GPT-3；再读 Chinchilla。
- **作者代码 / 材料**：未确认公开的作者完整训练实现；保留论文原文。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-06"></a>

<!-- resource: PAP-06 -->
### Chinchilla

**Training Compute-Optimal Large Language Models**

- **原文**：[arXiv:2203.15556](https://arxiv.org/abs/2203.15556)。
- **首次公开 / 发表信息**：2022（arXiv v1）；[NeurIPS 2022（会议页面题名为 An empirical analysis of compute-optimal large language model training）](https://proceedings.neurips.cc/paper_files/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract.html)。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：Scaling Laws、训练 token、计算预算。
- **核心问题**：固定计算预算下应怎样分配模型参数和训练数据？
- **主要贡献**：通过训练规模实验分析 compute-optimal 配比，提出 Chinchilla 的训练配置。
- **推荐理由**：用于比较数据不足与模型过大两类问题，不把经验配比直接当通用公式。
- **阅读衔接**：Scaling Laws；联系 CS336 的 scaling 作业。
- **作者代码 / 材料**：未确认公开的完整 Chinchilla 训练代码；论文和计算配比分析是主要入口。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-07"></a>

<!-- resource: PAP-07 -->
### LoRA

**LoRA: Low-Rank Adaptation of Large Language Models**

- **原文**：[arXiv:2106.09685](https://arxiv.org/abs/2106.09685)。
- **首次公开 / 发表信息**：2021（arXiv v1）；[ICLR 2022（会议入口当前需要浏览器验证）](https://openreview.net/forum?id=nZeVKeeFYf9)。
- **难度 / 路线 / 标签**：中级 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：矩阵运算、反向传播、微调。
- **核心问题**：如何减少适配大模型时需要训练的参数？
- **主要贡献**：冻结原始权重，用低秩矩阵表示可训练的权重增量。
- **推荐理由**：理解参数高效微调，并检查秩、目标层和合并权重的影响。
- **阅读衔接**：Transformer、基础微调；再读 QLoRA。
- **作者代码 / 材料**：[microsoft/LoRA](https://github.com/microsoft/LoRA)；作者 loralib 实现；完整论文训练配置仍需按原文核对。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-08"></a>

<!-- resource: PAP-08 -->
### QLoRA

**QLoRA: Efficient Finetuning of Quantized LLMs**

- **原文**：[arXiv:2305.14314](https://arxiv.org/abs/2305.14314)。
- **首次公开 / 发表信息**：2023（arXiv v1）；[NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract.html)。
- **难度 / 路线 / 标签**：进阶 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：LoRA、量化、GPU 显存。
- **核心问题**：如何在更小显存预算下微调大型模型？
- **主要贡献**：结合量化基座与低秩适配，并使用 NF4、double quantization 和 paged optimizers。
- **推荐理由**：看懂显存从哪里节省，以及量化与优化器带来的运行条件。
- **阅读衔接**：LoRA；先理解参数、梯度与优化器状态的显存。
- **作者代码 / 材料**：[artidoro/qlora](https://github.com/artidoro/qlora)；作者官方训练实现；当前依赖和硬件兼容性未运行验证。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-09"></a>

<!-- resource: PAP-09 -->
### FlashAttention

**FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness**

- **原文**：[arXiv:2205.14135](https://arxiv.org/abs/2205.14135)。
- **首次公开 / 发表信息**：2022（arXiv v1）；[NeurIPS 2022](https://papers.neurips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html)。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：注意力、GPU 内存层次、性能分析。
- **核心问题**：怎样减少注意力计算的显存读写和中间存储？
- **主要贡献**：通过 IO-aware tiling 和重计算实现精确注意力，降低 HBM 访问和存储开销。
- **推荐理由**：连接算法复杂度与硬件性能；它不是通过稀疏近似改变注意力定义。
- **阅读衔接**：Attention Is All You Need；CS336 systems。
- **作者代码 / 材料**：[Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)；作者维护实现包含后续版本；复现原论文要核对版本。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-10"></a>

<!-- resource: PAP-10 -->
### ViT

**An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale**

- **原文**：[arXiv:2010.11929](https://arxiv.org/abs/2010.11929)。
- **首次公开 / 发表信息**：2020（arXiv v1）；[ICLR 2021（arXiv 标注 camera-ready；年份对应版本）](https://arxiv.org/abs/2010.11929)。
- **难度 / 路线 / 标签**：中级 / 算法 / 经典 / 代表性阅读。
- **前置知识**：Transformer、图像分类、卷积网络基础。
- **核心问题**：图像能否通过 patch 序列直接交给 Transformer？
- **主要贡献**：将图像切分为 patch 并嵌入，用 Transformer 学习图像表示，即 ViT。
- **推荐理由**：理解 token 化、归纳偏置与预训练规模的关系。
- **阅读衔接**：Attention Is All You Need；CS231n。
- **作者代码 / 材料**：[google-research/vision_transformer](https://github.com/google-research/vision_transformer)；作者官方 ViT 模型与训练 / 微调相关代码。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-11"></a>

<!-- resource: PAP-11 -->
### DDPM

**Denoising Diffusion Probabilistic Models**

- **原文**：[arXiv:2006.11239](https://arxiv.org/abs/2006.11239)。
- **首次公开 / 发表信息**：2020（arXiv v1）；[NeurIPS 2020](https://proceedings.neurips.cc/paper_files/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html)。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：概率、生成模型、神经网络。
- **核心问题**：如何通过逐步去噪学习图像生成分布？
- **主要贡献**：建立前向加噪与反向去噪过程，并讨论简化训练目标与生成。
- **推荐理由**：作为扩散模型入口，先推导训练目标，再观察采样过程。
- **阅读衔接**：基础概率、生成模型；CS231n 生成模型部分。
- **作者代码 / 材料**：[hojonathanho/diffusion](https://github.com/hojonathanho/diffusion)；作者原始实现；不是当前常用工具库的统一接口。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-12"></a>

<!-- resource: PAP-12 -->
### CLIP

**Learning Transferable Visual Models From Natural Language Supervision**

- **原文**：[arXiv:2103.00020](https://arxiv.org/abs/2103.00020)。
- **首次公开 / 发表信息**：2021（arXiv v1）；[ICML 2021](https://proceedings.mlr.press/v139/radford21a)。
- **难度 / 路线 / 标签**：中级 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：图像编码器、文本编码器、对比学习。
- **核心问题**：能否从图文配对中学习可迁移的视觉表示？
- **主要贡献**：使用图文对比学习训练 CLIP，并以文本标签构造 zero-shot 分类。
- **推荐理由**：理解多模态对齐和文本驱动检索的基础。
- **阅读衔接**：Transformer、ViT；对比学习基础。
- **作者代码 / 材料**：[openai/CLIP](https://github.com/openai/CLIP)；官方模型与推理代码；不能等同于完整预训练管线。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-13"></a>

<!-- resource: PAP-13 -->
### Switch Transformers

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity**

- **原文**：[arXiv:2101.03961](https://arxiv.org/abs/2101.03961)。
- **首次公开 / 发表信息**：2021（arXiv v1）；[JMLR 23(120), 2022](https://www.jmlr.org/papers/v23/21-0998.html)。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：Transformer、分布式训练、MoE。
- **核心问题**：如何扩大模型容量，同时控制每个 token 的计算开销？
- **主要贡献**：简化稀疏专家路由并讨论负载、通信与训练稳定性。
- **推荐理由**：区分总参数量与每次激活参数量，衔接后续 MoE 报告。
- **阅读衔接**：Transformer、T5；CS336 的 MoE 部分。
- **作者代码 / 材料**：[JMLR 链接的 MoE 实现](https://github.com/tensorflow/mesh/blob/master/mesh_tensorflow/transformer/moe.py)；JMLR 官方代码链接指向 mesh_tensorflow/transformer/moe.py。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-14"></a>

<!-- resource: PAP-14 -->
### InstructGPT

**Training language models to follow instructions with human feedback**

- **原文**：[arXiv:2203.02155](https://arxiv.org/abs/2203.02155)。
- **首次公开 / 发表信息**：2022（arXiv v1）；[NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf)。
- **难度 / 路线 / 标签**：进阶 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：自回归模型、SFT、PPO。
- **核心问题**：怎样使模型输出更符合人类对指令回答的偏好？
- **主要贡献**：结合示范数据、偏好排序和强化学习微调形成 InstructGPT 流程。
- **推荐理由**：理解 SFT、奖励模型和策略优化各自的作用与数据来源。
- **阅读衔接**：GPT-3、PPO；再读 DPO。
- **作者代码 / 材料**：未确认公开的原始 InstructGPT 完整训练实现；第三方 RLHF 教程须另标。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-15"></a>

<!-- resource: PAP-15 -->
### Chain-of-Thought

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models**

- **原文**：[arXiv:2201.11903](https://arxiv.org/abs/2201.11903)。
- **首次公开 / 发表信息**：2022（arXiv v1）；[NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract.html)。
- **难度 / 路线 / 标签**：中级 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：few-shot prompting、任务评估。
- **核心问题**：中间推理示例是否有助于模型完成多步任务？
- **主要贡献**：研究带有中间推理步骤的示例提示对算术、常识和符号推理任务的影响。
- **推荐理由**：作为 ReAct 与推理模型的前置阅读，并检查任务、模型和提示条件。
- **阅读衔接**：GPT-3；再读 ReAct。
- **作者代码 / 材料**：以原文示例和附录为提示复现实验入口；独立官方训练代码待核查。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-16"></a>

<!-- resource: PAP-16 -->
### DPO

**Direct Preference Optimization: Your Language Model is Secretly a Reward Model**

- **原文**：[arXiv:2305.18290](https://arxiv.org/abs/2305.18290)。
- **首次公开 / 发表信息**：2023（arXiv v1）；[NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/file/a85b405ed65c6477a4fe8302b5e06ce7-Paper-Conference.pdf)。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：SFT、偏好数据、概率、RLHF。
- **核心问题**：能否直接使用偏好数据优化策略，而不单独训练奖励模型？
- **主要贡献**：在特定偏好与策略假设下，把优化目标转为可直接训练的分类式损失。
- **推荐理由**：对照 PPO-based RLHF 的数据、目标与工程复杂度。
- **阅读衔接**：InstructGPT；理解 reference policy 与 KL 约束。
- **作者代码 / 材料**：[eric-mitchell/direct-preference-optimization](https://github.com/eric-mitchell/direct-preference-optimization)；作者 reference implementation。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-17"></a>

<!-- resource: PAP-17 -->
### DeepSeekMath

**DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models**

- **原文**：[arXiv:2402.03300](https://arxiv.org/abs/2402.03300)。
- **首次公开 / 发表信息**：2024（arXiv v1）；arXiv 技术报告；会议 / 期刊信息待核查。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：语言模型训练、数学评估、PPO。
- **核心问题**：数学能力如何受预训练数据与后训练策略影响？
- **主要贡献**：讨论数学数据构建与训练，并提出 Group Relative Policy Optimization（GRPO）。
- **推荐理由**：把数据、SFT 和 RL 分开分析，作为 R1 的方法前置。
- **阅读衔接**：PPO、InstructGPT；再读 DeepSeek-R1。
- **作者代码 / 材料**：[deepseek-ai/DeepSeek-Math](https://github.com/deepseek-ai/DeepSeek-Math)；官方模型与使用入口；完整原始 RL 训练代码的公开情况待核查。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-18"></a>

<!-- resource: PAP-18 -->
### DeepSeek-V3

**DeepSeek-V3 Technical Report**

- **原文**：[arXiv:2412.19437](https://arxiv.org/abs/2412.19437)。
- **首次公开 / 发表信息**：2024（arXiv v1）；arXiv 技术报告；会议 / 期刊信息待核查。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：MoE、注意力、分布式训练、预训练。
- **核心问题**：大型 MoE 的架构、训练效率与后训练如何协同？
- **主要贡献**：报告 MLA、MoE 训练、负载平衡与低精度训练等设计和实验。
- **推荐理由**：作为完整训练系统案例，分别看架构、数据、计算和评估。
- **阅读衔接**：Switch Transformers、FlashAttention；CS336。
- **作者代码 / 材料**：[deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3)；官方权重与推理示例；未声称包含完整预训练数据和训练管线。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-19"></a>

<!-- resource: PAP-19 -->
### DeepSeek-R1

**DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning**

- **原文**：[arXiv:2501.12948](https://arxiv.org/abs/2501.12948)。
- **首次公开 / 发表信息**：2025（arXiv v1）；[Nature 645:633–638, 2025（arXiv journal reference 已确认）](https://arxiv.org/abs/2501.12948)。
- **难度 / 路线 / 标签**：进阶 / 双路线 / 近期研究。
- **前置知识**：DeepSeekMath、RL、SFT、推理评估。
- **核心问题**：大规模强化学习怎样影响语言模型的推理行为？
- **主要贡献**：比较 R1-Zero 与含冷启动、多阶段训练的 R1，并提供蒸馏模型。
- **推荐理由**：连接经典 RL 与 LLM 后训练；不要把模型权重公开等同于完整训练可复现。
- **阅读衔接**：DeepSeekMath、PPO、InstructGPT。
- **作者代码 / 材料**：[deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)；官方模型 / 权重 / 使用说明；完整训练管线待核查。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-20"></a>

<!-- resource: PAP-20 -->
### RAG

**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**

- **原文**：[arXiv:2005.11401](https://arxiv.org/abs/2005.11401)。
- **首次公开 / 发表信息**：2020（arXiv v1）；[NeurIPS 2020（arXiv accepted 注释）](https://arxiv.org/abs/2005.11401)。
- **难度 / 路线 / 标签**：中级 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：检索、embedding、seq2seq 模型。
- **核心问题**：怎样让生成模型利用可检索的外部知识？
- **主要贡献**：结合参数化生成模型与非参数化文档检索，研究知识密集任务中的生成。
- **推荐理由**：区分原论文联合建模与今天应用层的检索拼接流程。
- **阅读衔接**：T5、检索基础；再做知识库问答。
- **作者代码 / 材料**：[facebookresearch/fairseq](https://github.com/facebookresearch/fairseq)；官方相关 RAG 实现位于 examples/rag；仓库已归档。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-21"></a>

<!-- resource: PAP-21 -->
### ReAct

**ReAct: Synergizing Reasoning and Acting in Language Models**

- **原文**：[arXiv:2210.03629](https://arxiv.org/abs/2210.03629)。
- **首次公开 / 发表信息**：2022（arXiv v1）；[ICLR 2023（arXiv camera-ready 注释）](https://arxiv.org/abs/2210.03629)。
- **难度 / 路线 / 标签**：中级 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：CoT、工具调用、环境反馈。
- **核心问题**：如何让模型在推理与外部行动之间循环？
- **主要贡献**：交错生成推理与动作，并利用观察结果修正后续步骤。
- **推荐理由**：从单次生成走向 Agent 反馈循环的关键阅读。
- **阅读衔接**：Chain-of-Thought、工具调用；再读 Reflexion。
- **作者代码 / 材料**：[ysymyth/ReAct](https://github.com/ysymyth/ReAct)；作者官方实现；原文同时链接 react-lm.github.io。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-22"></a>

<!-- resource: PAP-22 -->
### Toolformer

**Toolformer: Language Models Can Teach Themselves to Use Tools**

- **原文**：[arXiv:2302.04761](https://arxiv.org/abs/2302.04761)。
- **首次公开 / 发表信息**：2023（arXiv v1）；[NeurIPS 2023](https://proceedings.nips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html)。
- **难度 / 路线 / 标签**：进阶 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：语言模型训练、API、数据过滤。
- **核心问题**：模型怎样学习何时调用工具、传入什么参数和使用返回值？
- **主要贡献**：构造和筛选工具调用示例，将工具使用融入语言建模训练。
- **推荐理由**：区分训练得到的工具能力与提示词层的工具协议。
- **阅读衔接**：GPT-3、工具调用；对照 ReAct。
- **作者代码 / 材料**：未确认公开的作者完整 Toolformer 训练实现；社区实现不标为官方。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-23"></a>

<!-- resource: PAP-23 -->
### Reflexion

**Reflexion: Language Agents with Verbal Reinforcement Learning**

- **原文**：[arXiv:2303.11366](https://arxiv.org/abs/2303.11366)。
- **首次公开 / 发表信息**：2023（arXiv v1）；[NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html)。
- **难度 / 路线 / 标签**：中级 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：ReAct、评估、记忆。
- **核心问题**：Agent 怎样利用任务失败反馈改善下一次尝试？
- **主要贡献**：将反馈转成文本反思并保存到 episodic memory，影响后续行动。
- **推荐理由**：学习反馈和记忆设计；这里的 verbal RL 并非通常意义上的梯度更新。
- **阅读衔接**：ReAct；对照 PPO 的参数优化。
- **作者代码 / 材料**：[noahshinn/reflexion](https://github.com/noahshinn/reflexion)；作者仓库已从原文中的旧账号路径重定向到当前路径。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-24"></a>

<!-- resource: PAP-24 -->
### Voyager

**Voyager: An Open-Ended Embodied Agent with Large Language Models**

- **原文**：[arXiv:2305.16291](https://arxiv.org/abs/2305.16291)。
- **首次公开 / 发表信息**：2023（arXiv v1）；arXiv 预印本；会议 / 期刊信息待核查。
- **难度 / 路线 / 标签**：进阶 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：ReAct、代码执行、环境反馈。
- **核心问题**：Agent 如何在开放环境中积累技能并探索新任务？
- **主要贡献**：结合自动课程、可执行技能库和基于反馈的迭代提示，应用于 Minecraft。
- **推荐理由**：作为长期技能积累案例，辨认技能存储、检索与重用。
- **阅读衔接**：ReAct、Reflexion；环境与程序接口。
- **作者代码 / 材料**：[MineDojo/Voyager](https://github.com/MineDojo/Voyager)；作者项目代码；模型、游戏和环境版本需按文档配置。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-25"></a>

<!-- resource: PAP-25 -->
### AutoGen

**AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation**

- **原文**：[arXiv:2308.08155](https://arxiv.org/abs/2308.08155)。
- **首次公开 / 发表信息**：2023（arXiv v1）；arXiv 预印本；会议 / 期刊信息待核查。
- **难度 / 路线 / 标签**：中级 / Agent / 经典 / 代表性阅读。
- **前置知识**：LLM API、工具调用、流程控制。
- **核心问题**：怎样通过可编程对话组织多个 Agent 协作？
- **主要贡献**：提出可配置的 Agent、对话模式和人类 / 工具参与方式。
- **推荐理由**：作为多 Agent 框架的历史方法阅读，比较职责划分与固定工作流。
- **阅读衔接**：ReAct；与 Microsoft Agent Framework 的当前工作流对照。
- **作者代码 / 材料**：[microsoft/autogen](https://github.com/microsoft/autogen)；历史官方代码；当前 README 标注 maintenance mode，新用户指向 Microsoft Agent Framework。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-26"></a>

<!-- resource: PAP-26 -->
### SWE-agent

**SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering**

- **原文**：[arXiv:2405.15793](https://arxiv.org/abs/2405.15793)。
- **首次公开 / 发表信息**：2024（arXiv v1）；[NeurIPS 2024（作者官方仓库说明）](https://github.com/SWE-agent/SWE-agent)。
- **难度 / 路线 / 标签**：进阶 / Agent / 经典 / 代表性阅读。
- **前置知识**：ReAct、Git、终端、测试。
- **核心问题**：怎样的计算机接口更有利于编码 Agent 完成修改任务？
- **主要贡献**：围绕浏览、编辑、执行等操作设计 Agent-Computer Interface 并评估软件工程任务。
- **推荐理由**：理解工具接口设计如何影响行为，而不仅是换模型。
- **阅读衔接**：ReAct；Git diff、单元测试与环境隔离。
- **作者代码 / 材料**：[SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent)；作者官方代码；当前 README 和原文项目网站均可用于核对。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-27"></a>

<!-- resource: PAP-27 -->
### GAIA

**GAIA: a benchmark for General AI Assistants**

- **原文**：[arXiv:2311.12983](https://arxiv.org/abs/2311.12983)。
- **首次公开 / 发表信息**：2023（arXiv v1）；会议 / 期刊信息待核查；当前以 arXiv 与官方数据集为依据。
- **难度 / 路线 / 标签**：中级 / 双路线 / 经典 / 代表性阅读。
- **前置知识**：Agent、工具、任务评估。
- **核心问题**：如何评估综合使用推理、浏览和多模态工具的助手？
- **主要贡献**：提供需组合多种能力完成的真实任务基准。
- **推荐理由**：从产品演示转向明确任务、答案与评估协议。
- **阅读衔接**：ReAct；基础评估设计。
- **作者代码 / 材料**：官方数据与排行榜：[gaia-benchmark/GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA)；访问或下载按数据集要求操作。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-28"></a>

<!-- resource: PAP-28 -->
### Gaia2

**Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments**

- **原文**：[arXiv:2602.11964](https://arxiv.org/abs/2602.11964)。
- **首次公开 / 发表信息**：2026（arXiv v1）；[ICLR 2026 Oral（arXiv accepted 注释）](https://arxiv.org/abs/2602.11964)。
- **难度 / 路线 / 标签**：进阶 / 双路线 / 近期研究。
- **前置知识**：GAIA、Agent 状态、异步事件。
- **核心问题**：Agent 怎样应对独立变化、带时间约束的异步环境？
- **主要贡献**：提出动态评估环境与行动验证，支持研究反馈、时间约束和多 Agent 协作。
- **推荐理由**：把静态问答评估扩展到长期行动过程；先读 GAIA 再比较变化。
- **阅读衔接**：GAIA、ReAct；异步工具与事件循环。
- **作者代码 / 材料**：[facebookresearch/meta-agents-research-environments](https://github.com/facebookresearch/meta-agents-research-environments)；Meta 官方 ARE 平台 README 明确提供 Gaia2 运行入口；不是同名社区仓库。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-29"></a>

<!-- resource: PAP-29 -->
### PPO

**Proximal Policy Optimization Algorithms**

- **原文**：[arXiv:1707.06347](https://arxiv.org/abs/1707.06347)。
- **首次公开 / 发表信息**：2017（arXiv v1）；arXiv 预印本；会议 / 期刊信息待核查。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：MDP、策略梯度、优势估计。
- **核心问题**：怎样约束策略更新幅度并保持实现相对简单？
- **主要贡献**：提出 clipped surrogate 等策略优化目标，支持重复利用一批采样进行更新。
- **推荐理由**：读懂 rollout、advantage 和策略更新；同时衔接 RLHF。
- **阅读衔接**：Sutton & Barto 的策略梯度部分；CS234。
- **作者代码 / 材料**：[openai/baselines](https://github.com/openai/baselines)；作者机构相关实现；对照 CleanRL 的 PPO 单文件实现，区分版本。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-30"></a>

<!-- resource: PAP-30 -->
### SAC

**Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor**

- **原文**：[arXiv:1801.01290](https://arxiv.org/abs/1801.01290)。
- **首次公开 / 发表信息**：2018（arXiv v1）；[ICML 2018（arXiv 注释）](https://arxiv.org/abs/1801.01290)。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：MDP、actor-critic、off-policy、熵。
- **核心问题**：怎样同时优化回报与策略熵，并利用 replay buffer？
- **主要贡献**：将最大熵目标与随机 actor-critic 结合，用于连续控制。
- **推荐理由**：理解探索、温度参数与样本复用；与 PPO 做不同策略的数据流比较。
- **阅读衔接**：策略梯度、Q-learning；CS234 / CS285。
- **作者代码 / 材料**：[haarnoja/sac](https://github.com/haarnoja/sac)；作者原始 SAC 实现；后续实现可能采用不同版本。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-31"></a>

<!-- resource: PAP-31 -->
### TD3

**Addressing Function Approximation Error in Actor-Critic Methods**

- **原文**：[arXiv:1802.09477](https://arxiv.org/abs/1802.09477)。
- **首次公开 / 发表信息**：2018（arXiv v1）；[ICML 2018（arXiv accepted 注释）](https://arxiv.org/abs/1802.09477)。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：DDPG、actor-critic、Q 函数估计。
- **核心问题**：怎样缓解 actor-critic 中价值过估计和误差累积？
- **主要贡献**：TD3 结合双 critic、延迟策略更新与目标策略平滑。
- **推荐理由**：通过机制对照理解连续控制的稳定性问题。
- **阅读衔接**：Q-learning、确定性策略梯度；对照 SAC。
- **作者代码 / 材料**：[sfujim/TD3](https://github.com/sfujim/TD3)；作者 PyTorch 实现。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-32"></a>

<!-- resource: PAP-32 -->
### AlphaZero

**Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm**

- **原文**：[arXiv:1712.01815](https://arxiv.org/abs/1712.01815)。
- **首次公开 / 发表信息**：2017（arXiv v1）；当前收录 2017 arXiv 版本；后续正式发表版本对应关系待核查。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：MDP、策略 / 价值网络、MCTS。
- **核心问题**：怎样通过自我对弈学习棋类策略，而非依赖人类棋谱？
- **主要贡献**：AlphaZero 将神经网络、搜索与自我对弈结合，应用于多种棋类。
- **推荐理由**：理解 search、训练目标与自生成数据的相互作用。
- **阅读衔接**：Sutton & Barto、MCTS；再读 MuZero。
- **作者代码 / 材料**：未确认公开的作者完整 AlphaZero 训练实现；第三方复现应另标。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-33"></a>

<!-- resource: PAP-33 -->
### MuZero

**Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model**

- **原文**：[arXiv:1911.08265](https://arxiv.org/abs/1911.08265)。
- **首次公开 / 发表信息**：2019（arXiv v1）；[Nature 588:604–609, 2020（arXiv DOI 与期刊页）](https://www.nature.com/articles/s41586-020-03051-4)。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：AlphaZero、MCTS、模型学习。
- **核心问题**：能否用学习到的环境表示进行规划，而不依赖已知规则？
- **主要贡献**：MuZero 学习表示、动力学及预测函数，并在隐空间中进行搜索。
- **推荐理由**：理解 world model 用于规划时需要保留哪些信息。
- **阅读衔接**：AlphaZero、模型式 RL；再读 DreamerV3。
- **作者代码 / 材料**：arXiv 原文附 pseudocode.py 等补充材料；伪代码不等于完整训练实现。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-34"></a>

<!-- resource: PAP-34 -->
### DreamerV3

**Mastering Diverse Domains through World Models**

- **原文**：[arXiv:2301.04104](https://arxiv.org/abs/2301.04104)。
- **首次公开 / 发表信息**：2023（arXiv v1）；[Nature 2025；期刊版本题名为 Mastering diverse control tasks through world models（出版页自动抓取受限）](https://www.nature.com/articles/s41586-025-08744-2)。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：模型式 RL、潜变量、actor-critic。
- **核心问题**：能否用一套世界模型学习配置适应不同任务领域？
- **主要贡献**：DreamerV3 通过世界模型和想象轨迹训练策略，并提出提升尺度适应性的设计。
- **推荐理由**：与 MuZero 比较：世界模型用于搜索还是策略训练。
- **阅读衔接**：MDP、模型式 RL、MuZero；CS285。
- **作者代码 / 材料**：[danijar/dreamerv3](https://github.com/danijar/dreamerv3)；作者官方实现；当前代码与 2023 初版配置须分别核对。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。

<a id="pap-35"></a>

<!-- resource: PAP-35 -->
### Decision Transformer

**Decision Transformer: Reinforcement Learning via Sequence Modeling**

- **原文**：[arXiv:2106.01345](https://arxiv.org/abs/2106.01345)。
- **首次公开 / 发表信息**：2021（arXiv v1）；[NeurIPS 2021](https://proceedings.neurips.cc/paper_files/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html)。
- **难度 / 路线 / 标签**：进阶 / 算法 / 经典 / 代表性阅读。
- **前置知识**：Transformer、离线 RL、轨迹数据。
- **核心问题**：强化学习任务能否表达为条件序列建模？
- **主要贡献**：用 return-to-go、状态与动作序列训练 Transformer，生成目标回报条件下的行动。
- **推荐理由**：比较序列建模与 Bellman 更新路线，以及离线数据分布的影响。
- **阅读衔接**：Attention Is All You Need、MDP、离线 RL。
- **作者代码 / 材料**：[kzl/decision-transformer](https://github.com/kzl/decision-transformer)；作者官方实现。
- **核查日期**：2026-10-08；原文已核对，未执行论文复现；未确认字段按上文标注。
