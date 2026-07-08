# 地域精准筛选工作流

## 适用场景
用户需要按特定国家、地区或城市精准锁定目标客户。

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


## 支持的国家代码（美国及中东重点）

| 国家 | 代码 | Snov.io 筛选值 |
|------|------|---------------|
| 美国 | US | location: "United States" |
| 阿联酋 | AE | location: "United Arab Emirates" |
| 沙特阿拉伯 | SA | location: "Saudi Arabia" |
| 卡塔尔 | QA | location: "Qatar" |
| 科威特 | KW | location: "Kuwait" |
| 阿曼 | OM | location: "Oman" |
| 巴林 | BH | location: "Bahrain" |
| 约旦 | JO | location: "Jordan" |
| 埃及 | EG | location: "Egypt" |

美国还可按州筛选：CA（加州）、TX（德州）、NY（纽约）、FL（佛州）、IL（伊利诺伊）等。

## 操作步骤

### 第一步：定义地域 + 行业筛选条件
与用户确认：
- 国家：（如 United States）
- 州/省：（如 California）
- 城市：（如 Los Angeles）
- 行业：（如 LED 照明进口商）

### 第二步：带地域的域名搜索
使用 Snov.io domain_search：
- 将行业关键词 + 地域组合搜索
- 示例："LED lighting California"、"electronics distributor Dubai"

### 第三步：【暂停点】确认查找关键词

**在此步骤必须停下来**，向用户展示：
- 搜索到的目标公司列表
- 当前筛选条件（国家/地区/行业）
- 当前使用的职位关键词列表
- 询问用户：是否使用预设关键词继续，还是需要增删修改？

等用户确认后再继续。

### 第四步：联系人筛选
使用 Snov.io domain_prospects：
- domain：来自第二步的结果
- job_position：使用确认后的关键词列表做模糊匹配
- location：进一步缩小地域范围
- **每公司最多取 4 个联系人**

### 第五步：查找邮箱
使用 Snov.io find_email 查找邮箱（每公司最多 4 个）

### 第六步：城市级别精准定位
1. 先用"国家 + 行业"进行宽泛搜索
2. 然后在 domain_prospects 结果中按城市名筛选
3. 或在 prospector 搜索时附加城市关键词

### 第七步：按时区优化发送时间

| 地区 | UTC 偏移 | 最佳发送时间（当地时间） |
|------|---------|----------------------|
| 美国东部（纽约） | UTC-5 | 上午 9-11 点 |
| 美国中部 | UTC-6 | 上午 9-11 点 |
| 美国西部（加州） | UTC-8 | 上午 9-11 点 |
| 阿联酋/迪拜 | UTC+4 | 上午 9-11 点 |
| 沙特阿拉伯 | UTC+3 | 上午 9-11 点 |
| 卡塔尔 | UTC+3 | 上午 9-11 点 |

邮件和 WhatsApp 消息应在对方工作时间到达。

## 示例

用户："找加州做户外用品的批发商"

1. 翻译：California、outdoor/sporting goods、wholesalers/distributors
2. Snov.io domain_search："outdoor sporting goods wholesaler California"
3. **【暂停】展示找到的公司和预设关键词，让用户确认**
4. Snov.io domain_prospects：用预设关键词 + 地域筛选（每公司最多 4 人）
5. find_email -> 验证 -> 输出（附带时区提醒）
