# 邮箱查找工作流

## 适用场景
用户需要查找特定公司联系人的邮箱地址，或在目标行业/地区内寻找潜在客户。

## 重要规则

1. **每次调用 Snov.io 查找邮箱前，必须停下来让用户输入模糊查找关键词**，等用户确认后再继续。不得自动生成关键词。
2. **每个公司最多查 4 个邮箱**，严格控制 Snov.io 点数消耗。

## 预设职位查找关键词（模糊匹配）

查找联系人时使用以下关键词过滤 job_position，采用模糊匹配（包含即命中）。
用户可在暂停点增删修改：

```
president, chief, chair, director, general manager, GM, partner,
CEO, head, procurement, purchas, sourc, buyer, vendor, supplier, supply
```

匹配逻辑：
- "purchas" 命中 "Purchasing Manager"、"Purchase Director"
- "sourc" 命中 "Sourcing Manager"、"Global Sourcing"
- "chief" 命中 "Chief Executive Officer"、"Chief Operating Officer"
- "director" 命中 "Director of Sales"、"Marketing Director"
- 不区分大小写


## 操作步骤

### 第一步：明确目标
与用户确认：
- 目标公司域名还是行业关键词？
- 需要对接什么职位？（默认使用预设关键词，可增删）
- 国家/地区范围？
- 预计需要多少家公司？

### 第二步：域名搜索（用户未提供具体域名时）
使用 Snov.io domain_search 查找公司域名：
- 输入：公司名称或关键词
- 返回：域名、公司信息、行业、所在地

### 第三步：发现域名下的联系人
使用 Snov.io domain_prospects：
- domain：来自第二步的域名
- job_position：使用预设关键词列表做模糊匹配
- 可选过滤：location（所在城市/国家）

### 第四步：【暂停点】确认查找关键词

**在此步骤必须停下来**，向用户展示：
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
