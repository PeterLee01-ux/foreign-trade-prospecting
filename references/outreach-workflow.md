# 端到端客户开发全流程

## 适用场景
用户需要一个完整的开发流程：找客户 -> 验证联系方式 -> 发邮件 -> WhatsApp 跟进。

## 重要规则

1. **每次调用 Snov.io 查找邮箱前，必须停下来让用户输入模糊查找关键词**，等用户确认后再继续。
2. **每个公司最多查 4 个邮箱**，严格控制 Snov.io 点数消耗。
3. **发送开发邮件前，必须停下来让用户上传附件并输入邮件内容**，等用户确认后再发送。不得自动生成邮件内容。

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


## 完整流程

### 第一阶段：客户发现
1. 明确目标：行业、国家、公司规模、决策人职位
2. 使用 Snov.io domain_search 查找目标公司
3. 使用 Snov.io domain_prospects 查找每家公司下的联系人
4. 使用预设职位关键词做模糊匹配筛选

### 第二阶段：联系方式采集
1. **【暂停点】向用户展示目标公司列表和预设关键词，确认后再继续**
2. 使用 Snov.io find_email 为每个联系人查找邮箱（每公司最多 4 个）
3. 从公司信息和 LinkedIn 资料中收集电话号码
4. 跳转到 email-verification.md 验证邮箱
5. 跳转到 whatsapp-tools.md 检查 WhatsApp 状态

### 第三阶段：验证清洗
1. 用 check-if-email-exists（批量）或 prospector（小批量）验证所有邮箱
2. 检查所有号码的 WhatsApp 注册状态
3. 标记结果：邮箱已验证 / WhatsApp 活跃 / 两者都有 / 都没有

### 第四阶段：配置 SMTP 并发送开发邮件

#### 步骤一：【暂停点】SMTP 配置（首次使用）

跳转到 [email-sending.md](email-sending.md)，按一问一答方式引导用户填写：
- 邮件服务商类型
- 发件邮箱地址
- 邮箱密码/应用专用密码
- 发件人显示名称
- 发送测试邮件确认

配置完成后回到本流程继续。

#### 步骤二：【暂停点】准备邮件内容

#### 步骤一：【暂停点】准备邮件内容

**在此步骤必须停下来**，向用户展示：
- 待发送的目标联系人列表（姓名、公司、邮箱、职位）
- 提示用户上传邮件附件（产品目录、公司介绍 PDF 等）
- 提示用户输入邮件正文内容

等用户上传附件并输入正文内容、确认后，再继续发送。

#### 步骤二：确定主送和抄送

对每家公司，从 4 个邮箱中按规则分配：

**主送（To）— 选 1 个最高价值目标：**
按以下优先级排序，取排第一的：
1. 职位含 CEO / President / General Manager / Managing Director（最高决策者）
2. 职位含 procurement / purchas / sourc / buyer（采购负责人）
3. 职位含 director / VP / head（部门负责人）
4. 信心度最高的那个

**抄送（CC）— 其余 3 个邮箱全部抄送**

向用户展示分配结果并确认：
| 公司 | 主送 | 职位 | 抄送 1 | 抄送 2 | 抄送 3 |
|------|------|------|--------|--------|--------|

#### 步骤三：逐封发送

对每个目标公司：
1. 将邮件正文中的 [姓名]、[公司名] 等占位符替换为主送人的实际值
2. 附带用户上传的附件
3. To：主送人 / CC：其余 3 人
4. 发送邮件
5. 记录发送时间和状态

### 第五阶段：分层跟进
- 第 1 天：发送第一封开发邮件（用户确认内容后）
- 第 3 天：对未回复者发送跟进邮件
  - **【暂停点】同样需要用户确认跟进邮件内容**
- 第 5 天：对有 WhatsApp 的联系人发消息
  - **【暂停点】同样需要用户确认 WhatsApp 消息内容**
- 第 10 天：根据互动情况做最后一次跟进

### 第六阶段：追踪管理
1. 在 Snov.io 中为本轮开发创建专用列表
2. 添加所有客户并设置自定义字段：状态 / 最近联系 / 回复情况
3. 使用 Snov.io drip campaign 工具追踪打开、点击、回复
4. 每周：向用户汇报本轮开发统计数据

## 全流程暂停点汇总

| 序号 | 阶段 | 暂停原因 | 用户需提供 |
|------|------|---------|-----------|
| P1 | 第二阶段 | 确认目标公司和职位关键词 | 关键词确认或修改 |
| P2 | 第四阶段 | SMTP 邮件配置（首次使用） | SMTP 服务器、端口、账号、密码 |
| P3 | 第四阶段 | 准备第一封开发邮件 | 邮件正文 + 附件 |
| P4 | 第四阶段 | 确认主送/抄送分配 | 确认或调整主送人选 |
| P5 | 第五阶段 | 准备跟进邮件 | 跟进邮件正文 + 附件 |
| P6 | 第五阶段 | 准备 WhatsApp 消息 | 消息内容 |

## 开发前检查清单
- [ ] 已明确目标行业/国家
- [ ] 已建立客户列表（最少 20 个，建议 50-100 个）
- [ ] 用户已确认职位关键词和地域筛选条件
- [ ] 邮箱已验证
- [ ] WhatsApp 状态已检查
- [ ] 邮件附件已准备（产品目录、公司介绍等）
- [ ] 邮件正文已由用户确认
- [ ] WhatsApp 消息模板已由用户确认
- [ ] Snov.io 列表已创建
- [ ] 追踪已开启

## Email Template (English)

Subject: [First Name], commercial-grade scent diffuser for [Company Name]?

Hi [First Name],

I'm [Your Name] from CentiDiffuser LTD, a manufacturer of commercial HVAC
scent diffusion systems.

We focus on three things our clients care about most:

- Ultra-quiet operation: whisper-level noise, ideal for hotels, offices, retail
- Smart app control: full scheduling, zone management, real-time fragrance level monitoring
- Mesh auto-networking: deploy dozens of units across floors; they self-organize
  into a single managed mesh — zero manual pairing

Stable, proven, and already deployed across [Target Industry] clients globally.

I came across [Company Name] and thought there might be a fit.
Would you be open to a quick look at our spec sheet?

Best regards,
[Your Name]
[Title] | CentiDiffuser LTD
[WhatsApp/Phone]

---

## Placeholder Reference

| Placeholder | Replaced With |
|-------------|--------------|
| [First Name] | Contact's first name |
| [Company Name] | Company name |
| [Your Name] | User's name |
| CentiDiffuser LTD | Your company name |
| [Product/Service] | User's product or service |
| [Target Industry] | Target industry |
| [Title] | User's job title |
| [WhatsApp/Phone] | User's contact info |
| [personalized observation from research] | Auto-filled from company research |
