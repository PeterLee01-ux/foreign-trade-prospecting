# 竞品客户挖掘工作流

## 适用场景
用户想找到竞品公司现有的客户，或找到与已知目标公司类似的潜在客户。

## 重要规则

1. **每次调用 Snov.io 查找邮箱前，必须停下来让用户输入模糊查找关键词**，等用户确认后再继续。
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

### 第一步：调研竞品
使用 Snov.io get_company_info 获取竞品公司信息：
- 获取行业、规模、所在地
- 获取关联域名

### 第二步：找同类公司
使用 Snov.io domain_search，按竞品的行业 + 所在地搜索：
- 例如："在迪拜找与 acme.com 同行业的公司"
- 返回：同类公司列表

### 第三步：【暂停点】发现联系人前确认关键词

**在此步骤必须停下来**，向用户展示：
- 找到的同类公司列表
- 当前使用的职位关键词列表
- 询问用户：是否使用预设关键词继续，还是需要增删修改？

等用户确认后再继续。

### 第四步：找出它们的客户/供应商
对每家公司：
1. 使用 Snov.io domain_prospects 查找关键联系人
2. 使用确认后的关键词列表筛选 job_position（模糊匹配）
3. **每公司最多取 4 个联系人**

### 第五步：查找邮箱
使用 Snov.io find_email 查找邮箱（每公司最多 4 个）

### 第六步：反向供应链分析
对已知竞品：
1. 获取公司信息（行业、规模）
2. 搜索互补行业的公司
3. 示例：如果竞品做 LED 驱动器，就找购买 LED 驱动器的公司
   （照明制造商、汽车供应商、电子分销商）

### 第七步：LinkedIn 深度挖掘
1. 使用 snovio_enrich_linkedin 补充竞品员工信息（按需使用，控制点数）
2. 查看关联网络和合作伙伴
3. 识别合作伙伴公司、供应商、分销商

### 第八步：生成目标清单

| 公司 | 行业 | 为何是目标 | 关键联系人 | 职位 | 邮箱 | 命中关键词 |
|------|------|-----------|-----------|------|------|-----------|

## 示例流程

用户："谁在从 AcmeLED.com 采购？帮我找他们的客户。"

1. get_company_info -> AcmeLED：LED 照明制造商，50-200 人，深圳
2. domain_search -> 目标市场（美国/阿联酋）同类 LED 制造商
3. **【暂停】展示同类公司列表和预设关键词，让用户确认**
4. domain_prospects -> 用预设关键词筛选（每公司最多 4 人）
5. find_email -> 验证 -> 输出目标清单
