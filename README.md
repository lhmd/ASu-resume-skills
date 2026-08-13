# ASu Resume Skills

<div align="center">
  <img src="assets/asu-circle.png" width="180" height="180" alt="ASu Resume Skills 图标">
  <h3>阿酥式高密度履历生成 × 证据优先简历审计</h3>
  <p>一个负责把真实经历写得 Scope 很大，一个负责逐条检查到底大到哪里。</p>
</div>

[![Build with CODEX](https://img.shields.io/badge/Build%20with-CODEX-245579?style=for-the-badge&logo=openai&logoColor=white)](https://chatgpt.com/codex)
[![GitHub Stars](https://img.shields.io/github/stars/Claycui828/ASu-resume-skills?style=for-the-badge)](https://github.com/Claycui828/ASu-resume-skills/stargazers)
[![MIT License](https://img.shields.io/badge/License-MIT-D97757?style=for-the-badge)](LICENSE)

| Skill | 用途 | 主要交付 |
| --- | --- | --- |
| `$asu-resume-skill` | 阿酥式履历生成 | 来源映射 JSON、自包含 HTML、A4 PDF、小红书配文 |
| `$asu-resume-audit-skill` | 简历证据审计 | 原子主张、证据矩阵、夸大模式、HTML/PDF 审计报告 |

## 安装

把下面这段直接发给 Codex：

```text
请从这个 GitHub 仓库安装插件，并启用 asu-resume-skill 与 asu-resume-audit-skill：
https://github.com/Claycui828/ASu-resume-skills
```

安装完成后建议新建一个 Codex 对话，让 Skill 列表重新加载。也可以显式调用：

```text
$asu-resume-skill 读取我的经历，查学校官方 Title，生成 Owner、0→1 和大 Scope 的中文技术履历。

$asu-resume-audit-skill 审计这份简历里的角色强度、Scope 外扩、指标口径和规划时态。
```

## `$asu-resume-skill`：高密度履历生成

它会完整读取用户提供的简历、飞书文档、截图和项目材料，然后完成：

- 用学校官网、教育主管部门或正式高校联盟核验学校 Title；
- 把真实项目拆成 Data / Model / Training / Serving / Agent / Eval 技术链；
- 为独立负责或主要负责的模块生成边界明确的 Owner、0→1 与架构演进叙事；
- 区分模块 Owner、策略架构 Owner、系统级共建者与规划中方向；
- 输出可截图的中文 HTML、2–3 页 A4 PDF 与小红书配文；
- 用来源标记和指标重算阻止不存在的学历、项目、指标和成果进入成品。

典型用法：

```text
$asu-resume-skill

请读取我的晋升材料和现有简历，保留真实学校、公司、部门和指标。
学校要查官方 Title；项目要有模块级 Owner、0→1、技术链和大 Scope；
最终输出 HTML、PDF 和发布配文。
```

### 打招呼示例

参考招聘聊天截图的长气泡表达，但使用不包含真实求职者信息的原创演示界面：

<img src="assets/greeting-example.png" width="390" alt="阿酥式打招呼示例">

## `$asu-resume-audit-skill`：证据优先审计

它不会用“学校不够有名”“项目听起来太大”直接推断造假，而是把每一段拆成可核验的原子主张：

- 学校、学籍、合作项目和学位授予方；
- Contributor、Maintainer、Core Author、Owner、Lead 的角色强度；
- 个人产物、全系统架构、团队结果与个人归因；
- 用户数、转化率、Precision、AUC、延迟与 Benchmark 口径；
- “最年轻、首个、第一”等缺少比较全集的最高级；
- 已交付结果与当前方向、计划、探索之间的时态边界。

每条主张只使用一个状态：`已证实`、`部分证实`、`存在直接矛盾`、`缺乏支持` 或 `暂不可核验`。

典型用法：

```text
$asu-resume-audit-skill

请审计这份简历，逐条检查学校 Title、Owner、0→1、核心作者、项目指标和时间线，
生成证据矩阵、自包含 HTML 和 PDF；不要把未经证实的质疑写成事实。
```

## 两个 Skill 如何配合

1. 用生成 Skill 建立来源映射，输出高密度履历；
2. 用审计 Skill 把强表述拆成角色、范围、结果和因果四类主张；
3. 对审计报告中的高风险项补设计文档、代码所有权、评审记录、指标看板或学历凭证；
4. 将补强后的边界回写简历，再生成最终 HTML/PDF。

```text
真实经历
   ↓
学校 Title + Owner/0→1 + 技术链 + 大 Scope
   ↓
原子主张 + 证据等级 + 夸大模式
   ↓
可发布履历 / 可复核审计报告
```

## 事实边界

- 强表达必须限定到真实模块，不能把参与升级成整个项目 Owner；
- `0→1` 必须说明“0”指新服务、新训练链路还是新策略节点；
- 公司、项目 Star、团队收入和团队指标不会自动成为个人成果；
- 内部指标缺少评测集、分母、时间窗口或看板时，审计结果保持暂不可核验；
- 规划中的 Coding Agent、Memory、Compaction 等方向不能写成已上线收益；
- 审计只描述现有证据，不评价人格，也不把没有公开证据等同于虚假；
- 不要将含姓名、电话、邮箱、内部链接或雇主敏感数据的示例直接提交到公开仓库。

## 文件结构

```text
ASu-resume-skills/
├── .codex-plugin/
│   └── plugin.json
├── skills/
│   ├── asu-resume-skill/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   ├── assets/
│   │   ├── references/
│   │   └── scripts/
│   └── asu-resume-audit-skill/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── assets/
│       ├── references/
│       └── scripts/
├── assets/
│   ├── asu-circle.png
│   ├── greeting-example.html
│   └── greeting-example.png
├── examples/
│   ├── resume-data.example.json
│   └── audit-report.example.json
├── LICENSE
└── README.md
```

## 素材与关系说明

头像 `assets/asu-circle.png` 取自 [Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) 的公开 assets，依据其 MIT License 使用。聊天示例为本仓库重新制作，不复用原截图中的个人信息。

本仓库是社区制作的非官方工具，与头像人物、相关博主、其雇主及参考仓库作者不存在隶属、授权、背书或合作关系。

## 开源协议

代码以 [MIT License](LICENSE) 发布。头像素材的来源和关系说明见上一节。
