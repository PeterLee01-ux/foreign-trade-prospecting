# 速查表 — 外贸获客助手

## 一句话匹配

| 用户说 | 跳到 |
|--------|------|
| 找邮箱 | email-finding.md |
| 验证邮箱 | email-verification.md |
| WhatsApp | whatsapp-tools.md |
| 公司调研 | company-research.md |
| 全套开发 | outreach-workflow.md |
| 客户分类 | customer-organization.md |
| 竞品挖掘 | competitor-mining.md |
| 地域筛选 | geo-filtering.md |
| 发邮件 | email-sending.md |

## 硬性规则速记

1. **暂停**：调 Snov.io 前必须暂停让用户确认关键词
2. **4 个上限**：每公司最多 4 个邮箱
3. **发邮件暂停**：正文+附件必须用户确认
4. **SMTP 一问一答**：每轮只问一个问题
5. **先验证再用**：邮箱先验证再发送

## 工具速选

| 任务 | 用谁 |
|------|------|
| 找邮箱 | Snov.io find_email |
| 验证邮箱 <50 | Prospector（免费） |
| 验证邮箱 >50 | check-if-email-exists（Docker） |
| 查 WhatsApp | mcp-whatsapp is_on_whatsapp |
| 公司信息 | Snov.io get_company_info |
| 发邮件 | mcp-email-server |

## 暂停点一览

| 位置 | 等什么 |
|------|--------|
| 查邮箱前 | 用户确认职位关键词 |
| 发邮件前 | 用户上传附件+输入正文 |
| SMTP 配置 | 一问一答填 5 个配置项 |
| SMTP 测试后 | 用户确认收到测试邮件 |
| 主送/抄送 | 用户确认分配方案 |

## 常见失败 & 自救

| 失败 | 原因 | 解决 |
|------|------|------|
| Snov.io 403 | API Key 无效 | 让用户重新提供 |
| Snov.io 429 | 超限 | 等 60 秒重试 |
| SMTP 连不上 | 密码错/端口封 | 检查 App Password，换 587 端口 |
| Docker 未运行 | 没启 Reacher | 运行 setup_check_email.sh |
| WhatsApp 断连 | 20 天过期 | 重新扫码配对 |
