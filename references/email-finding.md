# 邮箱查找工作流

## 适用场景
用户需要查找特定公司联系人的邮箱地址，或在目标行业/地区内寻找潜在客户。

## 重要规则

1. **每次调用 Snov.io 查找邮箱前，必须停下来让用户输入模糊查找关键词**，等用户确认后再继续。不得自动生成关键词。
2. **每个公司最多查 4 个邮箱**，严格控制 Snov.io 点数消耗。

## 预设职位查找关键词

使用预设关键词列表（见 SKILL.md 全局规则），模糊匹配 job_position。
默认包含：president, chief, chair, director, GM, partner, CEO, head,
procurement, purchas, sourc, buyer, vendor, supplier, supply。

用户可在暂停点增删修改。


## 操作步骤

### 第一步：明确目标
与用户确认：
- 目标公司域名还是行业关键词？
- 需要对接什么职位？（默认使用预设关键词，可增删）
- 国家/地区范围？
- 预计需要多少家公司？

### 第二步：域名搜索（用户未提供具体域名时）
使用 Snov.io domain_search 查找公司域名。若失败（403/429/空结果），报告用户并询问是否换关键词重试：
- 输入：公司名称或关键词
- 返回：域名、公司信息、行业、所在地

### 第三步：发现域名下的联系人
使用 Snov.io domain_prospects：
- domain：来自第二步的域名
- job_position：使用预设关键词列表做模糊匹配
- 可选过滤：location（所在城市/国家）

### 第四步：【暂停点】确认查找关键词

**⛔ PAUSE — NEVER proceed without user confirmation.**，向用户展示：
- 当前目标公司列表
- 当前使用的职位关键词列表
- 询问用户：是否使用预设关键词继续，还是需要增删修改？

等用户确认后再继续。

### 第五步：查找邮箱地址

使用 Snov.io find_email：
- 输入：first_name + last_name + domain
- 返回：邮箱地址 + 信心评分

**限制规则：每个公司最多查找 4 个邮箱。**
优先选关键词命中数多、信心度高的联系人。

### 第六步：备选方案 — 用 Prospector 免费查找
当 Snov.io 额度不足时，使用 prospector find_emails：
- 输入：domain + contact_name（可选）
- 返回：最佳邮箱 + 信心度 + 备选邮箱
- Prospector 免费版每天 50 次，不消耗 Snov.io 点数

### 第七步：验证找到的邮箱
跳转到 email-verification.md 进行验证。

### 第八步：呈现结果
以表格形式输出：
| 姓名 | 职位 | 公司 | 邮箱 | 信心度 | 命中关键词 | 来源 |

## 常见错误 & 自救

| 错误 | 原因 | 解决 |
|------|------|------|
| Snov.io 返回空 | 域名错误或没有匹配联系人 | 检查域名拼写，换行业关键词搜索 |
| Snov.io 403 | API Key 无效或过期 | 让用户去 Snov.io 重新获取 Key |
| Snov.io 429 | 请求频率超限 | 等待 60 秒后重试 |
| find_email 无结果 | 联系人姓名与实际不匹配 | 尝试不同姓名格式（first.last / flast） |
| Prospector 报错 | Node.js 未安装或版本低于 18 | 检查：node --version，需 >=18 |
| Docker 连不上 | Reacher 容器未启动 | 运行 bash scripts/setup_check_email.sh |
| domain_prospects 无结果 | 公司太小或无公开联系人 | 换 LinkedIn 手动查找，或换更大公司 |
