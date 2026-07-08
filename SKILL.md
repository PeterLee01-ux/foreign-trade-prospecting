---
name: foreign-trade-prospecting
description: >
  B2B foreign trade customer acquisition. Single keyword match triggers:
  find company email, verify email, check WhatsApp, company research,
  customer organization, competitor mining, geo-filter prospects,
  email outreach. Targets US, Middle East, Europe, global markets.
  NOT for: CRM, accounting, translation, product design, general chat.
---

# 外贸获客助手

## 触发规则（精确匹配）

**自动激活** 当用户消息包含以下任一关键词：
找客户、找邮箱、查邮箱、验证邮箱、邮箱验证、WhatsApp、公司背景、客户分类、
竞品挖掘、地域筛选、开发信、外发邮件、SMTP 配置、Email Finder

**不激活** 当用户消息是：闲聊、翻译、写代码、记账、产品设计、国内电商、个人邮件

## 硬性规则（违反即停止）

### R1：所有 Snov.io 调用前必须暂停
**NEVER call Snov.io find_email or domain_prospects without pausing first.**
展示目标公司和预设关键词 → 等用户输入关键词确认 → 再继续。

### R2：每公司最多 4 个邮箱
`find_email` per company limit = 4. 超过就截断，报告用户 "共 N 人，取前 4 个"。

### R3：发邮件前必须暂停
展示邮件正文和附件 → 等用户确认 → 再发送。
**NEVER send email without user approval of content.**

### R4：SMTP 一问一答
配置 SMTP 时每次只问一个问题，等回答后再问下一个。不能一次性问多个。

### R5：验证优先
查到的邮箱必须先验证再用。优先 check-if-email-exists（免费）> Prospector（50次/天）> Snov.io（付费）。

## 工具选择优先级

| 任务 | 首选工具 | 备选 |
|------|---------|------|
| 找公司邮箱 | Snov.io find_email | Prospector find_emails（免费） |
| 验证邮箱（≤50个） | Prospector verify_emails_batch | check-if-email-exists |
| 验证邮箱（>50个） | check-if-email-exists | — |
| 查 WhatsApp | mcp-whatsapp is_on_whatsapp | — |
| 公司信息 | Snov.io get_company_info | — |
| 发邮件 | mcp-email-server send_email | — |
| 客户管理 | Snov.io list tools | — |

## 预设职位关键词（模糊匹配）

```
president, chief, chair, director, general manager, GM, partner,
CEO, head, procurement, purchas, sourc, buyer, vendor, supplier, supply
```

## 工作流路由

| 用户说 | 读这个文件 | 涉及工具 |
|--------|-----------|---------|
| 找邮箱/查联系方式 | email-finding.md | Snov.io, Prospector |
| 验证邮箱/清洗列表 | email-verification.md | Prospector, check-if-email-exists, Snov.io |
| WhatsApp/发消息 | whatsapp-tools.md | mcp-whatsapp |
| 公司背景/调研 | company-research.md | Snov.io |
| 全套开发流程 | outreach-workflow.md | 全部 |
| 客户分类/整理 | customer-organization.md | Snov.io lists |
| 竞品/挖客户 | competitor-mining.md | Snov.io |
| 按国家城市筛选 | geo-filtering.md | Snov.io |
| SMTP配置/发邮件 | email-sending.md | mcp-email-server |

## 首次使用检查

1. Snov.io API Key 是否已配置？未配置则暂停索要。
2. Docker 是否运行？未运行则提示安装。
3. WhatsApp 是否已扫码配对？未配对则提示启动 mcp-whatsapp。
