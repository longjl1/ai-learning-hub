# 核查记录与首版验收

[返回首页](README.md) · [贡献指南](CONTRIBUTING.md)

核查日期：**2026-10-08（Asia/Hong_Kong）**。首版来源使用项目官方仓库、arXiv / 正式发表页面、大学课程站点与作者 / 出版社 / 官方文档。此页保存核查依据和限制；资源的学习说明只在四类详情页维护。

## 核查范围与数量

| 分类 | 主条目数量 | 本轮确认内容 | 未在本轮完成 |
| --- | ---: | --- | --- |
| 项目 | 20 | GitHub 仓库身份、Stars、归档状态、最近推送、README 说明 | 安装、运行、部署与 API 兼容性验证 |
| 论文 | 35 | 原文题名、arXiv v1 年份、摘要与可找到的发表 / 作者材料入口 | 全文逐页评审、全部正式发表映射、训练复现 |
| 课程 | 15 | 所选版本、官网及视频 / 讲义 / 作业的公开入口或限制说明 | 所有视频播放、全部文件下载、作业执行与提交 |
| 书籍 / 文档 | 10 | 6 本书版本与获取方式、4 项滚动文档入口 | 全文下载回读、库 / SDK 安装与示例运行 |
| **合计** | **80** | 首页与 Roadmap 只引用这些条目 | 远端 GitHub 发布 |

「已读取」表示本轮取得并阅读了页面或 README 文本；「官方提供」表示官方页面列出材料入口；「待核查」表示尚未取得足够证据。访问抓取失败与资料不公开不是同一结论。本轮未运行 20 个外部项目，也未对 35 篇论文执行复现。

## 项目来源快照

数据通过 GitHub 连接器读取官方仓库 API 与 README。以下 Stars 和 pushed_at 是核查当次快照，不是 2026 年增长统计。所有入选仓库在 API 中 archived=false；其中 nanoGPT 明确弃用，说明未归档不能代表持续维护。

| 条目 / 官方元数据 | Stars | pushed_at（UTC） | 归档 | README blob SHA |
| --- | ---: | --- | --- | --- |
| [PRJ-01](projects/README.md#prj-01) · [openclaw/openclaw](https://api.github.com/repos/openclaw/openclaw) | 391,625 | 2026-10-08T08:27:37Z | 否 | `cf37326bfe36929d79f90be549be3ec6ac1a0434` |
| [PRJ-02](projects/README.md#prj-02) · [bytedance/deer-flow](https://api.github.com/repos/bytedance/deer-flow) | 83,493 | 2026-10-08T06:24:51Z | 否 | `40c777e4f984a1ff5f88135a920addf8530aea4c` |
| [PRJ-03](projects/README.md#prj-03) · [HKUDS/nanobot](https://api.github.com/repos/HKUDS/nanobot) | 48,856 | 2026-10-08T07:31:17Z | 否 | `e789b42afa4b05c2ca194da7b690d188c6c96af2` |
| [PRJ-04](projects/README.md#prj-04) · [langchain-ai/langgraph](https://api.github.com/repos/langchain-ai/langgraph) | 42,877 | 2026-10-08T07:26:46Z | 否 | `97c31e9cb4d8fe56be8d768ce3eb5e22400e897e` |
| [PRJ-05](projects/README.md#prj-05) · [huggingface/smolagents](https://api.github.com/repos/huggingface/smolagents) | 29,729 | 2026-10-06T18:35:07Z | 否 | `7c8af38d981a563add56db76b10cde810e010690` |
| [PRJ-06](projects/README.md#prj-06) · [crewAIInc/crewAI](https://api.github.com/repos/crewAIInc/crewAI) | 59,445 | 2026-10-08T06:03:59Z | 否 | `4a5360ad587a35625684747157881558c6acae1d` |
| [PRJ-07](projects/README.md#prj-07) · [microsoft/agent-framework](https://api.github.com/repos/microsoft/agent-framework) | 14,000 | 2026-10-08T08:33:37Z | 否 | `d8ea282064ff70d99f3dde1a793802270e1cf24c` |
| [PRJ-08](projects/README.md#prj-08) · [pydantic/pydantic-ai](https://api.github.com/repos/pydantic/pydantic-ai) | 20,481 | 2026-10-08T04:00:32Z | 否 | `5c92efbcdb40ca35c9effdd7986cdfea40d0312a` |
| [PRJ-09](projects/README.md#prj-09) · [agno-agi/agno](https://api.github.com/repos/agno-agi/agno) | 42,610 | 2026-10-08T08:26:04Z | 否 | `2813f35fa7620ff7d95465d853d7b0a6ee2c00b4` |
| [PRJ-10](projects/README.md#prj-10) · [langgenius/dify](https://api.github.com/repos/langgenius/dify) | 158,079 | 2026-10-08T08:17:32Z | 否 | `2dd55a942f63ad30a433813bebfbccb955198b72` |
| [PRJ-11](projects/README.md#prj-11) · [infiniflow/ragflow](https://api.github.com/repos/infiniflow/ragflow) | 91,808 | 2026-10-08T08:05:28Z | 否 | `694cd3465ff17abfa4c7953783e9e1ee156010e1` |
| [PRJ-12](projects/README.md#prj-12) · [run-llama/llama_index](https://api.github.com/repos/run-llama/llama_index) | 52,436 | 2026-10-06T19:11:28Z | 否 | `572527a8f5293bcf001366da01e51549280ff2e0` |
| [PRJ-13](projects/README.md#prj-13) · [deepset-ai/haystack](https://api.github.com/repos/deepset-ai/haystack) | 26,694 | 2026-10-07T16:35:09Z | 否 | `afa079b2a7e90e815fdaf9b09edcd7ad010e3e91` |
| [PRJ-14](projects/README.md#prj-14) · [browser-use/browser-use](https://api.github.com/repos/browser-use/browser-use) | 117,441 | 2026-10-07T18:42:14Z | 否 | `faaa2e193cdba137cfec568a258470b278c43ba5` |
| [PRJ-15](projects/README.md#prj-15) · [OpenHands/OpenHands](https://api.github.com/repos/OpenHands/OpenHands) | 90,247 | 2026-10-08T06:02:25Z | 否 | `9748057acf5110b0c4c5641ac990f17f2c923f13` |
| [PRJ-16](projects/README.md#prj-16) · [langfuse/langfuse](https://api.github.com/repos/langfuse/langfuse) | 35,514 | 2026-10-08T08:28:09Z | 否 | `3c4ad5773b846b6b1c16355640ebd87ff031f92e` |
| [PRJ-17](projects/README.md#prj-17) · [karpathy/nanoGPT](https://api.github.com/repos/karpathy/nanoGPT) | 63,630 | 2025-11-12T19:52:34Z | 否 | `67ef634ff4797037e72b2919c2af1fb33dbd4fe5` |
| [PRJ-18](projects/README.md#prj-18) · [rasbt/LLMs-from-scratch](https://api.github.com/repos/rasbt/LLMs-from-scratch) | 106,205 | 2026-10-02T14:55:52Z | 否 | `4703bc5afc86803540abd6cbc465d635aa3eb5e8` |
| [PRJ-19](projects/README.md#prj-19) · [vwxyzjn/cleanrl](https://api.github.com/repos/vwxyzjn/cleanrl) | 10,508 | 2026-04-20T10:57:15Z | 否 | `109427f99fcaad614e991719cc202fa4850dd444` |
| [PRJ-20](projects/README.md#prj-20) · [DLR-RM/stable-baselines3](https://api.github.com/repos/DLR-RM/stable-baselines3) | 13,875 | 2026-09-09T14:05:40Z | 否 | `66d20f64a092c5af9a5e24b8430d7e2025c42a44` |

README 使用核查时默认分支的文件内容，SHA 为该文件的 Git blob SHA，用来辨认本次内容，不是 commit SHA。详情页的默认分支链接会继续变化；本地合集没有保存外部仓库的完整源码或部署环境。

### 本轮发现的版本与状态变化

- [DeerFlow 官方 README](https://github.com/bytedance/deer-flow#readme)：当前按 2.0 Super Agent Harness 介绍；原 Deep Research 1.x 位于 main-1.x 分支。
- [nanoGPT 官方 README](https://github.com/karpathy/nanoGPT#readme)：标示自 2025 年 11 月弃用并指向后继项目；首版保留其历史代码学习用途。
- [OpenHands 官方 README](https://github.com/OpenHands/OpenHands#readme)：当前主分支介绍 Agent Canvas beta。原 All-Hands-AI 路径迁移到 OpenHands 组织，旧版本教程须核对。
- [AutoGen 官方 README](https://github.com/microsoft/autogen#readme)：维护模式，新用户推荐 Microsoft Agent Framework。AutoGen 只作为已收录论文的历史材料，不另计一个项目。
- [LlamaIndex 官方 README](https://github.com/run-llama/llama_index#readme)：当前说明强调文档解析 / 提取，框架仍有摄取与查询组件；条目同时记录当前定位与 RAG 学习用途。
- [Reflexion 作者仓库](https://github.com/noahshinn/reflexion)：旧作者账号路径重定向到当前 noahshinn 路径；正文采用当前路径。
- [Gaia2 官方 ARE 仓库](https://github.com/facebookresearch/meta-agents-research-environments)：README 明确列出 Gaia2，采用 meta-agents-research-environments 规范仓库名。

## 论文题名、年份与发表依据

所有原文入口已读取，年份统一取 arXiv v1。正式发表信息来自 arXiv Comments / Journal reference / DOI、官方 proceedings 或作者官方仓库说明，分别标在详情。没有正式会议字段不表示论文未发表；以下仍保留待核查项。

| 论文条目 | arXiv v1 年份 / 原文 | 发表依据或待核查项 |
| --- | --- | --- |
| [Attention Is All You Need](papers/README.md#pap-01) | [2017 · 1706.03762](https://arxiv.org/abs/1706.03762) | [NeurIPS 2017](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html) |
| [BERT](papers/README.md#pap-02) | [2018 · 1810.04805](https://arxiv.org/abs/1810.04805) | [NAACL 2019](https://aclanthology.org/N19-1423/) |
| [GPT-3](papers/README.md#pap-03) | [2020 · 2005.14165](https://arxiv.org/abs/2005.14165) | [NeurIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) |
| [T5](papers/README.md#pap-04) | [2019 · 1910.10683](https://arxiv.org/abs/1910.10683) | [JMLR 21(140), 2020](https://www.jmlr.org/papers/v21/20-074.html) |
| [Scaling Laws](papers/README.md#pap-05) | [2020 · 2001.08361](https://arxiv.org/abs/2001.08361) | arXiv 预印本；会议 / 期刊信息待核查 |
| [Chinchilla](papers/README.md#pap-06) | [2022 · 2203.15556](https://arxiv.org/abs/2203.15556) | [NeurIPS 2022（会议页面题名为 An empirical analysis of compute-optimal large language model training）](https://proceedings.neurips.cc/paper_files/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract.html) |
| [LoRA](papers/README.md#pap-07) | [2021 · 2106.09685](https://arxiv.org/abs/2106.09685) | [ICLR 2022（会议入口当前需要浏览器验证）](https://openreview.net/forum?id=nZeVKeeFYf9) |
| [QLoRA](papers/README.md#pap-08) | [2023 · 2305.14314](https://arxiv.org/abs/2305.14314) | [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract.html) |
| [FlashAttention](papers/README.md#pap-09) | [2022 · 2205.14135](https://arxiv.org/abs/2205.14135) | [NeurIPS 2022](https://papers.neurips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html) |
| [ViT](papers/README.md#pap-10) | [2020 · 2010.11929](https://arxiv.org/abs/2010.11929) | [ICLR 2021（arXiv 标注 camera-ready；年份对应版本）](https://arxiv.org/abs/2010.11929) |
| [DDPM](papers/README.md#pap-11) | [2020 · 2006.11239](https://arxiv.org/abs/2006.11239) | [NeurIPS 2020](https://proceedings.neurips.cc/paper_files/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html) |
| [CLIP](papers/README.md#pap-12) | [2021 · 2103.00020](https://arxiv.org/abs/2103.00020) | [ICML 2021](https://proceedings.mlr.press/v139/radford21a) |
| [Switch Transformers](papers/README.md#pap-13) | [2021 · 2101.03961](https://arxiv.org/abs/2101.03961) | [JMLR 23(120), 2022](https://www.jmlr.org/papers/v23/21-0998.html) |
| [InstructGPT](papers/README.md#pap-14) | [2022 · 2203.02155](https://arxiv.org/abs/2203.02155) | [NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf) |
| [Chain-of-Thought](papers/README.md#pap-15) | [2022 · 2201.11903](https://arxiv.org/abs/2201.11903) | [NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract.html) |
| [DPO](papers/README.md#pap-16) | [2023 · 2305.18290](https://arxiv.org/abs/2305.18290) | [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/file/a85b405ed65c6477a4fe8302b5e06ce7-Paper-Conference.pdf) |
| [DeepSeekMath](papers/README.md#pap-17) | [2024 · 2402.03300](https://arxiv.org/abs/2402.03300) | arXiv 技术报告；会议 / 期刊信息待核查 |
| [DeepSeek-V3](papers/README.md#pap-18) | [2024 · 2412.19437](https://arxiv.org/abs/2412.19437) | arXiv 技术报告；会议 / 期刊信息待核查 |
| [DeepSeek-R1](papers/README.md#pap-19) | [2025 · 2501.12948](https://arxiv.org/abs/2501.12948) | [Nature 645:633–638, 2025（arXiv journal reference 已确认）](https://arxiv.org/abs/2501.12948) |
| [RAG](papers/README.md#pap-20) | [2020 · 2005.11401](https://arxiv.org/abs/2005.11401) | [NeurIPS 2020（arXiv accepted 注释）](https://arxiv.org/abs/2005.11401) |
| [ReAct](papers/README.md#pap-21) | [2022 · 2210.03629](https://arxiv.org/abs/2210.03629) | [ICLR 2023（arXiv camera-ready 注释）](https://arxiv.org/abs/2210.03629) |
| [Toolformer](papers/README.md#pap-22) | [2023 · 2302.04761](https://arxiv.org/abs/2302.04761) | [NeurIPS 2023](https://proceedings.nips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html) |
| [Reflexion](papers/README.md#pap-23) | [2023 · 2303.11366](https://arxiv.org/abs/2303.11366) | [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html) |
| [Voyager](papers/README.md#pap-24) | [2023 · 2305.16291](https://arxiv.org/abs/2305.16291) | arXiv 预印本；会议 / 期刊信息待核查 |
| [AutoGen](papers/README.md#pap-25) | [2023 · 2308.08155](https://arxiv.org/abs/2308.08155) | arXiv 预印本；会议 / 期刊信息待核查 |
| [SWE-agent](papers/README.md#pap-26) | [2024 · 2405.15793](https://arxiv.org/abs/2405.15793) | [NeurIPS 2024（作者官方仓库说明）](https://github.com/SWE-agent/SWE-agent) |
| [GAIA](papers/README.md#pap-27) | [2023 · 2311.12983](https://arxiv.org/abs/2311.12983) | 会议 / 期刊信息待核查；当前以 arXiv 与官方数据集为依据 |
| [Gaia2](papers/README.md#pap-28) | [2026 · 2602.11964](https://arxiv.org/abs/2602.11964) | [ICLR 2026 Oral（arXiv accepted 注释）](https://arxiv.org/abs/2602.11964) |
| [PPO](papers/README.md#pap-29) | [2017 · 1707.06347](https://arxiv.org/abs/1707.06347) | arXiv 预印本；会议 / 期刊信息待核查 |
| [SAC](papers/README.md#pap-30) | [2018 · 1801.01290](https://arxiv.org/abs/1801.01290) | [ICML 2018（arXiv 注释）](https://arxiv.org/abs/1801.01290) |
| [TD3](papers/README.md#pap-31) | [2018 · 1802.09477](https://arxiv.org/abs/1802.09477) | [ICML 2018（arXiv accepted 注释）](https://arxiv.org/abs/1802.09477) |
| [AlphaZero](papers/README.md#pap-32) | [2017 · 1712.01815](https://arxiv.org/abs/1712.01815) | 当前收录 2017 arXiv 版本；后续正式发表版本对应关系待核查 |
| [MuZero](papers/README.md#pap-33) | [2019 · 1911.08265](https://arxiv.org/abs/1911.08265) | [Nature 588:604–609, 2020（arXiv DOI 与期刊页）](https://www.nature.com/articles/s41586-020-03051-4) |
| [DreamerV3](papers/README.md#pap-34) | [2023 · 2301.04104](https://arxiv.org/abs/2301.04104) | [Nature 2025；期刊版本题名为 Mastering diverse control tasks through world models（出版页自动抓取受限）](https://www.nature.com/articles/s41586-025-08744-2) |
| [Decision Transformer](papers/README.md#pap-35) | [2021 · 2106.01345](https://arxiv.org/abs/2106.01345) | [NeurIPS 2021](https://proceedings.neurips.cc/paper_files/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html) |

### 作者材料核查与限制

作者材料入口与其公开内容类型详见各论文条目。已读取相关仓库的官方 API / README，或原文及出版社的材料链接；存在仓库不代表有完整论文训练管线。

- BERT、原始 Transformer 相关 tensor2tensor、GPT-3 配套仓库和 fairseq 已归档；保留历史入口，不标作活跃默认选择。
- GPT-3、CLIP 与 DeepSeek 报告的入口可能主要提供评测材料、模型权重或推理用法；不声称已公开完整训练数据和流程。
- MuZero 的 arXiv 补充材料包括伪代码；GAIA 提供数据 / 排行榜；CoT 可从原文示例与附录开始。三者不统一写成「完整训练代码」。
- 未确认 Scaling Laws、Chinchilla、InstructGPT、Toolformer、AlphaZero 的完整作者训练实现；CoT 独立代码、DeepSeekMath / R1 完整原始训练管线仍待核查。
- LoRA 的 OpenReview 页面需要浏览器验证；DreamerV3 的 Nature 出版页自动抓取受限。正文保留证据来源与访问限制，不将抓取失败写成论文不存在。
- Chinchilla 与 DreamerV3 的期刊 / 会议题名和 arXiv 题名不同；T5、MuZero、DreamerV3 的首次公开年份早于正式发表年份；DeepSeek-V3 按 2024 年 arXiv v1 记录。

## 课程材料入口核查

以下「公开」表示官网提供公开入口，未逐段播放或逐份执行。具体 URL、前置知识与访问限制见课程条目。

| 条目 / 版本 | 视频 | 讲义 | 作业 |
| --- | --- | --- | --- |
| [CRS-01 · CS50’s Introduction to Programming with Python](resources/courses.md#crs-01)：OCW 在线版；2026-10-08 快照（官网未锁定一个学期编号） | 官方按周列出公开 Lecture / Shorts；未逐段播放。 | 各周 Notes / Slides 由课程页面进入。 | 官方 Problem Sets；提交反馈与证书另有注册要求。 |
| [CRS-02 · Statistics 110: Probability](resources/courses.md#crs-02)：作者公开学习站点；2026-10-08 快照，录播具体年份待核查 | 官网列出 YouTube 公开录播与 edX 入口。 | 官网 Handouts 与教材入口；部分材料需要沿教材页面阅读。 | 已读取 Strategic Practice and Homework 页面，提供公开题目与解答入口 |
| [CRS-03 · 18.06 Linear Algebra](resources/courses.md#crs-03)：Spring 2010，MIT OCW 归档版 | OCW 提供公开录播；实际录制于 Fall 1999，资料归档为 Spring 2010 | 官网学习材料和阅读说明。 | OCW 提供题目与解答入口。 |
| [CRS-04 · CS50’s Introduction to Artificial Intelligence with Python](resources/courses.md#crs-04)：OCW 在线版；2026-10-08 快照 | 官方七周课程列出公开讲座。 | 每周 Notes / Slides 由主题页面进入。 | 官方项目任务；反馈与提交要求见官网。 |
| [CRS-05 · 6.036 Introduction to Machine Learning](resources/courses.md#crs-05)：Fall 2020，MIT OCW / Open Learning Library 归档入口 | 课程资料由 Open Learning Library 分发；当前视频子入口待核查。 | 官网确认免费材料；讲义具体子入口待核查。 | OLL 练习入口与反馈可用性待核查；无须注册即可浏览的说明来自官网。 |
| [CRS-06 · CS229 Machine Learning](resources/courses.md#crs-06)：Stanford Engineering Everywhere 公开归档版；录制年份待核查 | SEE 页面提供逐讲 Watch Online 入口。 | SEE 页面提供 Lecture Handouts；与当前学期资料分开。 | SEE 页面提供 Assignments；原练习含 Matlab / Octave 环境。 |
| [CRS-07 · 6.S191 Introduction to Deep Learning](resources/courses.md#crs-07)：2026 官方公开版 | 官方 2026 课程日程列出各讲公开视频。 | 各讲 Slides 公开列出。 | 日程提供 Lab 入口；未执行 notebook。 |
| [CRS-08 · CS231n Deep Learning for Computer Vision](resources/courses.md#crs-08)：Spring 2026 讲义 / 作业；录播采用官网链接的往年公开版本 | 官网提供往年 YouTube；2026 视频限已选课学生的 Canvas。 | 2026 日程公开各讲 Slides 与阅读材料。 | 2026 作业说明公开；提交与评分需要课程身份。 |
| [CRS-09 · CS224n Natural Language Processing with Deep Learning](resources/courses.md#crs-09)：Winter 2026 讲义 / 作业；2024 官方公开录播 | 官网明确列出免费 2024 全套录播；2026 视频需要 Canvas 登录。 | 2026 日程和 Slides 公开列出。 | 官方 Coursework / assignments 入口公开；评分系统另需身份。 |
| [CRS-10 · CS336 Language Modeling from Scratch](resources/courses.md#crs-10)：Spring 2026；另提供 Spring 2025 官方归档 | 官网提供 YouTube playlist；本轮未成功抓取播放列表内容，全集覆盖待核查 | 2026 日程提供讲义、代码或 PDF；2025 归档可单独查阅。 | 官网列出五项公开 GitHub 作业：Basics、Systems、Scaling、Data、Alignment and Reasoning RL。 |
| [CRS-11 · CS25 Transformers United](resources/courses.md#crs-11)：V6 / Spring 2026 日程；公开录播包含往期精选 | 官网 Recordings 提供精选公开讲座；不假设覆盖所有当期讲座。 | 部分讲座日程提供 Slides；覆盖以每讲入口为准。 | 研讨课程；官网说明唯一课堂作业为每周出席，无统一编程作业。 |
| [CRS-12 · CS234 Reinforcement Learning](resources/courses.md#crs-12)：Winter 2026 公开讲义 / 作业 | 已核查 materials 页的讲义；本轮未确认 2026 公开录播入口。 | Lecture Materials 提供公开 Slides 与补充阅读。 | Assignments 页面公开题目与相关文件；提交评分要求见官网。 |
| [CRS-13 · CS224R Deep Reinforcement Learning](resources/courses.md#crs-13)：Spring 2025 公开自学版本；2026 页面作更新参考 | 2026 官网明确提供 Spring 2025 公开录播；2026 课堂视频位于 Canvas。 | 2025 归档列出讲义和阅读材料。 | 2025 日程公开作业入口；以该版材料为一套，不混用 2026 截止日期。 |
| [CRS-14 · CS285 Deep Reinforcement Learning](resources/courses.md#crs-14)：Spring 2026 讲义 / 作业；Fall 2023 公开录播 | 官网明确链接 Fall 2023 公开录播；未逐段播放 | 官网逐讲列出 PDF，已读取第一讲 PDF | 官网列出作业，已读取 HW1 PDF 与 starter code 入口；未执行 |
| [CRS-15 · CS194/294-196 Large Language Model Agents](resources/courses.md#crs-15)：Fall 2024，Berkeley RDI 公开课程版 | 日程的 Edited Video 为 YouTube 公开入口；Original Recording 为校内平台。 | 日程提供各讲 Slides 与论文。 | 公开 syllabus、阅读与项目要求；课程提交渠道需注册，不承诺公开自动评分。 |

课程材料的事实核查主要读官网目录和入口；CS50P、CS50 AI、MIT 18.06 和 STAT 110 的作业 / 练习页面已直接读取。CS285 已读取第一讲 PDF 与 2026 HW1 PDF，题目包含官方 starter code 链接；未运行作业。

## 书籍版本与获取依据

| 资源 | 收录版本 | 依据 / 限制 |
| --- | --- | --- |
| [Mathematics for Machine Learning](resources/books-and-docs.md#bok-01) | 2020 年 Cambridge University Press 版；在线勘误持续更新 | [作者官网与下载入口](https://mml-book.github.io/)；已读取作者页面的出版年份、下载与内容说明。 |
| [An Introduction to Statistical Learning with Applications in Python](resources/books-and-docs.md#bok-02) | Python 版，2023 年；区别于 R 版的出版年份 | [官方 Python Labs](https://intro-stat-learning.github.io/ISLP/)；已读取官方 Python 版介绍与配套实验入口；未运行所有实验。 |
| [Dive into Deep Learning](resources/books-and-docs.md#bok-03) | 2023 年 Cambridge University Press 版；在线版持续更新，核查时页面标示 1.0.3 | [作者在线教材与出版 BibTeX](https://d2l.ai/)；已读取官网内容目录与 2023 年出版记录；未执行全部代码。 |
| [Understanding Deep Learning](resources/books-and-docs.md#bok-04) | 2023 年 MIT Press 版（2023-12-05 出版） | [出版社：年份与 Open Access](https://mitpress.mit.edu/9780262377102/understanding-deep-learning/) · [作者配套仓库](https://github.com/udlbook/udlbook)；已核对出版社年份、开放访问说明与作者仓库目录；全文文件可下载性待核查。 |
| [Build a Large Language Model (From Scratch)](resources/books-and-docs.md#bok-05) | 2024 年 Manning 版（2024 年 9 月出版） | [作者官方代码](https://github.com/rasbt/LLMs-from-scratch) · [本合集项目条目](projects/README.md#prj-18)；已核对出版社出版时间和官方代码入口；未复现书中完整训练。 |
| [Reinforcement Learning: An Introduction](resources/books-and-docs.md#bok-06) | 第二版，2018 年 MIT Press 版；不采用 1998 年第一版 | [出版社：第二版与 Open Access](https://mitpress.mit.edu/9780262039246/reinforcement-learning/)；已读取出版社说明；作者站访问与全文文件可下载性待核查。 |
| [PyTorch Tutorials](resources/books-and-docs.md#bok-07) | 持续更新；页面快照 2026-10-08，使用时按实际安装的 PyTorch 版本选择文档 | [官方教程](https://docs.pytorch.org/tutorials/)；已读取官方教程入口；示例执行与版本兼容性未验证。 |
| [Hugging Face Transformers Documentation](resources/books-and-docs.md#bok-08) | 持续更新；页面快照 2026-10-08，不固定库版本 | [官方文档](https://huggingface.co/docs/transformers/index)；已读取官方入口；具体模型下载、库安装与示例执行未验证。 |
| [Model Context Protocol Documentation](resources/books-and-docs.md#bok-09) | 持续更新；页面快照 2026-10-08；实现时另记录使用的协议版本 | [官方入门文档](https://modelcontextprotocol.io/docs/getting-started/intro)；已读取官方介绍；协议 / SDK 兼容性与服务运行未验证。 |
| [LangGraph Documentation](resources/books-and-docs.md#bok-10) | Python OSS 文档；持续更新，页面快照 2026-10-08 | [官方 Python OSS 文档](https://docs.langchain.com/oss/python/langgraph/overview) · [本合集项目条目](projects/README.md#prj-04)；已读取官方入口与职责说明；未运行工作流。 |

Reinforcement Learning 作者站在本轮 HTTP 与 HTTPS 均超时，改由 MIT Press 官方页面确认第二版与 Open Access 入口；正文保留作者 URL 并标记访问待核查。Understanding Deep Learning 作者站未解析出完整文本，出版社的 2023 年出版与 Open Access 说明已读取，作者仓库包含 Notebooks 与 Slides。两者均未确认全文 PDF 的实际下载回读。

## 尚待补齐的来源核查

- **发表映射**：Scaling Laws、DeepSeekMath、DeepSeek-V3、Voyager、AutoGen、GAIA、PPO，以及 2017 AlphaZero 与后续正式发表版本的对应关系。原文题名与首次公开年份已核对。
- **课程深层入口**：MIT 6.036 的 Open Learning Library 深层视频、讲义与作业入口；CS336 全部录播的覆盖与播放；CS234 2026 公开录播；STAT 110 / CS229 录播具体年份。已提供官网入口，待核查不等同于没有材料。
- **全文与代码**：上述两本书的 PDF 下载回读；论文完整训练代码的公开范围；所有外部项目与课程代码的运行兼容性。

## 本地验收

| 检查 | 状态 |
| --- | --- |
| 80 个独立主条目，20 / 35 / 15 / 10 分类计数 | 通过，2026-10-08 |
| 唯一编号与官方主链接、索引和年份一致 | 通过，80 个唯一编号与官方主链接 |
| 相对链接、显式锚点、基本 Markdown 结构 | 通过，329 个相对链接与锚点；表格、围栏、字段与空白正常 |
| Markdown 渲染与页面排版 | 通过本地 GFM 渲染；9 页结构检查，首页桌面 / 手机及条目截图抽查 |
| 外部项目运行 / 论文复现 | 本轮未执行 |
| 远端 GitHub 发布与远端展示 | 本轮未执行；目标仓库尚未确定 |

校验命令：`python3 scripts/check_catalog.py`。脚本不请求网络；它只检查本地资源结构、数量、去重、索引、相对链接与锚点、必填字段、表格、代码围栏和空白。外部链接的来源阅读与访问限制按此页记录，不声称全部视频或下载链接已成功打开。

本地预览使用 marked 的 GFM 模式与独立的无头浏览器，9 页均正常生成表格与标题；4 类详情页分别生成 20 / 35 / 15 / 10 个资源锚点，未发现页面整体横向溢出。已抽查首页桌面 / 手机、论文和书籍详情截图。样式用于接近 GitHub 阅读布局；尚未验证实际 GitHub 远端渲染。313 个外部链接引用通过语法提取，访问证据与未确认事项以上文为准。
