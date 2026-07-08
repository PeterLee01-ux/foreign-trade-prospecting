# 公司背景调查工作流

## 适用场景
用户在联系目标公司之前需要了解：
- 公司规模、行业、营收
- 关键决策人
- 近期动态和发展情况

## 重要规则

1. **每次调用 Snov.io 查找邮箱前，必须停下来让用户确认模糊查找关键词**，等用户确认后再继续。
2. **每个公司最多查 4 个邮箱**，严格控制 Snov.io 点数消耗。

## 预设模糊查找关键词

以下为预设的职位关键词，采用模糊匹配（包含即命中）。
查找联系人时使用此列表作为默认过滤条件，用户可在暂停点增删修改：

**默认职位关键词（模糊匹配）：**
```
president, chief, chair, director, general manager, GM, partner,
CEO, head, procurement, purchas, sourc, buyer, vendor, supplier, supply
```

匹配逻辑：
- 输入 "purchas" 可匹配 "Purchasing Manager"、"Purchase Director" 等
- 输入 "sourc" 可匹配 "Sourcing Manager"、"Global Sourcing" 等
- 输入 "chief" 可匹配 "Chief Executive Officer"、"Chief Operating Officer" 等
- 不区分大小写

## 操作步骤

### 第一步：基础公司信息
使用 Snov.io domain_search 或 get_company_info：
- 输入：公司域名（如 acme.com）
- 返回：公司名称、行业、规模范围、所在地、电话、关联域名

### 第二步：LinkedIn 信息补充
使用 Snov.io enrich_linkedin：
- 输入：关键员工的 LinkedIn 个人主页链接
- 返回：当前职位、公司、所在地、技能
- 注意：按需使用，避免无差别消耗点数

### 第三步：【暂停点】确认查找关键词

**在此步骤必须停下来**，向用户展示：
- 公司基本信息
- 当前预设关键词列表（如用户之前未修改，使用默认列表）
- 询问用户：是否使用预设关键词继续，还是需要增删修改？

等用户确认后再继续。

### 第四步：发现关键联系人
使用 Snov.io domain_prospects：
- 输入：域名
- 使用确认后的关键词列表筛选 job_position（模糊匹配）
- **每公司最多取 4 个联系人**
- 优先取关键词命中数多的联系人

### 第五步：查找邮箱
使用 Snov.io find_email（每公司最多 4 个）

### 第六步：关联公司
使用 Snov.io domain_search 查找：
- 同行业公司
- 同地区公司
- 关联/姊妹公司

### 第七步：生成背景调查报告

输出格式建议：

## 公司：[名称]
- 官网：[域名]
- 行业：[行业]
- 规模：[员工数范围]
- 所在地：[城市，国家]
- 电话：[如有]

### 关键联系人
| 姓名 | 职位 | 邮箱 | LinkedIn | 命中关键词 |
|------|------|------|----------|-----------|

### 关联公司
列出相关公司及关联方式

### 开发建议
基于调研给出个性化建议

## 快捷命令

快速调研时直接问 Snov.io：
- "获取 domain.com 的公司信息"
- "查找 domain.com 的采购岗位联系人"
- "查找迪拜与 domain.com 类似的公司"
