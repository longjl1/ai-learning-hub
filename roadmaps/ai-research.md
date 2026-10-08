# Roadmap · ML / DL / RL 算法研究

[返回首页](../README.md) · [Agent 应用开发路线](agent-development.md)

目标：能理解模型与算法，设计可信的实验，再完成范围明确的论文复现。先做基础模型和小规模训练，再按兴趣进入多模态或 RL。资源是可选学习路径，不要求逐项读完。

## 路线总览

| 阶段 | 核心能力 | 阶段产出 |
| --- | --- | --- |
| 1 · 数学 / ML | 线性代数、概率、梯度、统计学习 | 基础模型与数据评估报告 |
| 2 · PyTorch / DL | 自动微分、训练循环、网络与泛化 | 小型神经网络训练 |
| 3 · Transformer 与训练 | 注意力、分词、语言建模、训练预算 | 小型 Transformer |
| 4A · 多模态 | 视觉表示、对比学习或扩散 | 专题实验 |
| 4B · RL | MDP、价值函数、策略优化与探索 | PPO / SAC 实验 |
| 5 · 论文复现 | 研究问题、对照、消融与误差分析 | 可复现报告 |

阶段 4A 与 4B 至少选择一个分支。已有研究经验可直接选论文，通过阶段 5 的清单检查基础是否充分。

## 1 · 数学与机器学习

**前置知识**：Python；不足时先学 [CS50P](../resources/courses.md#crs-01)。

**主资源**：按薄弱点选 [MIT 18.06](../resources/courses.md#crs-03)、[Harvard STAT 110](../resources/courses.md#crs-02)、[Mathematics for Machine Learning](../resources/books-and-docs.md#bok-01)。ML 主课从 [MIT 6.036](../resources/courses.md#crs-05) 与 [Stanford CS229](../resources/courses.md#crs-06) 中选一门；实践参考 [ISLP](../resources/books-and-docs.md#bok-02)。

**任务**：用 NumPy 实现线性回归与逻辑回归，再与成熟实现比较。固定训练、验证、测试划分，记录预处理、损失、预测指标和超参数选择依据。

**验收**：能够解释梯度、过拟合、正则化、交叉验证和数据泄漏；用多数类或常数预测等简单基线说明模型是否有效；不使用测试集选择超参数。

## 2 · PyTorch 与深度学习

**前置知识**：阶段 1；理解矩阵计算、链式法则与分类损失。

**主资源**：[PyTorch Tutorials](../resources/books-and-docs.md#bok-07) + [Dive into Deep Learning](../resources/books-and-docs.md#bok-03) 或 [Understanding Deep Learning](../resources/books-and-docs.md#bok-04)。短课可选 [MIT 6.S191](../resources/courses.md#crs-07)。

**任务**：训练 MLP 与一个小型 CNN，比较模型规模、优化器或正则化中的一个变量。保存数据版本、依赖、随机种子、训练日志和检查点。

**验收**：能解释 Autograd、梯度清零、训练 / 推理模式和学习率；记录训练与验证曲线，分析一次失败或过拟合案例。先选小数据和小模型，按实验需要再增加硬件。

## 3 · Transformer 与语言模型训练

**前置知识**：阶段 2；理解序列数据、嵌入和概率建模。

**主资源**：[Attention Is All You Need](../papers/README.md#pap-01) → [LLMs from Scratch](../projects/README.md#prj-18)；课程选 [CS224n](../resources/courses.md#crs-09)，准备系统训练时再进入 [CS336](../resources/courses.md#crs-10)。[CS25](../resources/courses.md#crs-11) 作为专题讲座补充。

**任务**：实现 Tokenizer、因果注意力和小型语言模型，完成一次受预算约束的训练。按原始文档划分训练与验证数据后再分块，检查重复文本，记录参数量、Token 数、步数、耗时和验证损失。

**验收**：说明掩码与位置编码的作用，检查预测目标是否正确移位，避免看到未来 Token；同一验证设置下比较至少两种模型或训练配置。[nanoGPT](../projects/README.md#prj-17) 可作为历史代码参考，README 已说明弃用状态。

**后续选读**：

- 预训练与规模：[BERT](../papers/README.md#pap-02)、[GPT-3](../papers/README.md#pap-03)、[T5](../papers/README.md#pap-04)、[Scaling Laws](../papers/README.md#pap-05)、[Chinchilla](../papers/README.md#pap-06)。
- 效率与稀疏模型：[LoRA](../papers/README.md#pap-07)、[QLoRA](../papers/README.md#pap-08)、[FlashAttention](../papers/README.md#pap-09)、[Switch Transformers](../papers/README.md#pap-13)。
- 对齐与推理：[InstructGPT](../papers/README.md#pap-14)、[DPO](../papers/README.md#pap-16)、[DeepSeekMath](../papers/README.md#pap-17)、[DeepSeek-V3](../papers/README.md#pap-18)、[DeepSeek-R1](../papers/README.md#pap-19)。先区分监督微调、偏好优化与 RL，再阅读近期报告。

## 4A · 多模态分支

**前置知识**：阶段 2–3；选择一个专题，无需同时学习所有生成与表示方法。

**主资源**：[CS231n](../resources/courses.md#crs-08)，论文依兴趣选 [ViT](../papers/README.md#pap-10)、[CLIP](../papers/README.md#pap-12) 或 [DDPM](../papers/README.md#pap-11)。

**任务**：选一个小规模实验，例如 ViT 与 CNN 分类对照、CLIP 图文检索，或小图像扩散模型。固定数据划分与评估方法，把模型权重推理和从头训练分别说明。

**验收**：设置适当基线，报告至少一个与任务匹配的指标和失败样例；说明数据规模、预训练权重、计算预算与论文原设定的差异。使用预训练 CLIP 做检索不等于复现原始预训练。

## 4B · 强化学习分支

**前置知识**：阶段 1–2；概率、期望、MDP 与 Bellman 方程。

**主资源**：[Reinforcement Learning: An Introduction 第二版](../resources/books-and-docs.md#bok-06) 与 [CS234](../resources/courses.md#crs-12)。实现参考 [CleanRL](../projects/README.md#prj-19) 或 [Stable-Baselines3](../projects/README.md#prj-20)；深入课程从 [CS224R](../resources/courses.md#crs-13) 和 [CS285](../resources/courses.md#crs-14) 中选一门。

**任务**：先完成表格型方法，再读 [PPO](../papers/README.md#pap-29) 与 [SAC](../papers/README.md#pap-30)。用支持连续动作的同一环境（如 Pendulum）进行 PPO / SAC 实验，匹配总环境交互预算，至少运行 3 个随机种子，单独进行评估回合并报告均值与离散程度。

**验收**：解释 on-policy / off-policy、优势估计、熵项、Replay Buffer 与动作空间限制；正确处理 episode 终止与时间截断；不把单次最好结果当作整体结论。记录软件版本、评估策略和训练 / 评估环境配置。

**后续选读**：[TD3](../papers/README.md#pap-31) 补充连续控制；[AlphaZero](../papers/README.md#pap-32)、[MuZero](../papers/README.md#pap-33) 阅读搜索与模型；[DreamerV3](../papers/README.md#pap-34) 阅读世界模型；[Decision Transformer](../papers/README.md#pap-35) 阅读离线序列建模。有限硬件先复现一个核心机制或小任务，不要求复制原始大规模结果。

## 5 · 论文复现

**前置知识**：完成阶段 1–3，并掌握所选专题。选择有明确实验问题和可获得数据 / 代码的论文。

**任务**：定义一个可检验的问题，例如「LoRA 的秩如何影响同一任务的效果与可训练参数量」或「相同环境交互预算下 PPO / SAC 的学习曲线有什么差异」。先跑基线，再改一个变量，最后做消融与误差分析。

**验收与报告结构**：

1. **问题与范围**：论文标题、首次公开年份、所复现的具体结论；区分完整复现、部分复现和概念演示。
2. **来源与设置**：论文版本、作者代码或第三方实现身份、固定提交 / 依赖、数据与模型许可、数据划分、硬件与预算。
3. **对照与实验**：基线、超参数选择、随机种子、训练步数；尽量保持比较双方预算与预处理一致。
4. **结果与证据**：原论文数字、复现数字、均值与变化范围、训练曲线及失败案例。无法对齐的设置明确注明。
5. **分析与复现入口**：一个主要消融、差异原因、限制、运行命令、配置和可获取的产物。

作者公开权重、伪代码、评测数据或推理示例的情况，均在 [论文详情](../papers/README.md) 分别标注；这些材料不一定包含完整训练代码。

想把模型能力做成产品，可接着进入 [Agent 应用开发路线](agent-development.md) 的 RAG、工具和评估阶段。
