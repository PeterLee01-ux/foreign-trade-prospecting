# 邮件发送工作流

## 适用场景
用户已有验证通过的邮箱列表和邮件内容，需要逐封发送开发邮件。

## SMTP 配置（首次使用必须逐项填写）

**在此必须暂停，一问一答，每次只问一个问题，等用户回答后再问下一个。**

### 问题一：邮件服务商
向用户提问：
"你用什么邮箱发送？请选择：
1. Gmail（个人/Google Workspace）
2. Outlook/Hotmail
3. 企业邮箱（阿里企业邮、腾讯企业邮、网易企业邮）
4. 其他自建邮件服务器"

根据用户回答，给出对应的 SMTP 配置提示：

| 服务商 | SMTP 服务器 | 端口 | 加密 |
|--------|------------|------|------|
| Gmail | smtp.gmail.com | 465 | SSL |
| Outlook | smtp-mail.outlook.com | 587 | STARTTLS |
| 阿里企业邮 | smtp.mxhichina.com | 465 | SSL |
| 腾讯企业邮 | smtp.exmail.qq.com | 465 | SSL |
| 网易企业邮 | smtp.ym.163.com | 465 | SSL |

### 问题二：发件邮箱地址
向用户提问：
"请输入你的发件邮箱地址（完整的 email，例如：sales@centidiffuser.com）："

记录为 SMTP_USER。

### 问题三：邮箱密码/应用专用密码
向用户提问：
"请输入邮箱密码。注意：如果是 Gmail 或 Outlook，需要在邮箱设置中生成'应用专用密码（App Password）'，
不能用登录密码。以下是获取方式：

- Gmail：Google 账号 > 安全性 > 两步验证 > 应用专用密码
- Outlook：Microsoft 账号 > 安全性 > 应用专用密码
- 企业邮箱：一般直接用登录密码即可"

记录为 SMTP_PASS。

### 问题四：发件人显示名称
向用户提问：
"发件人显示名称是什么？（收件人看到的发件人名字，例如：Sales Team | CentiDiffuser LTD）"

记录为 SMTP_FROM_NAME。

### 问题五：确认并发送测试邮件

汇总展示配置：

| 配置项 | 值 |
|--------|-----|
| SMTP 服务器 | [用户输入] |
| 端口 | [自动匹配] |
| 加密方式 | [自动匹配] |
| 发件邮箱 | [用户输入] |
| 显示名称 | [用户输入] |

向用户提问：
"以上配置是否正确？确认后我将发送一封测试邮件到你的发件邮箱。"

用户确认后，使用 mcp-email-server send_email 发送测试邮件：
- To：发件邮箱自身
- Subject：SMTP Test — CentiDiffuser LTD
- Body：This is a test email to verify SMTP configuration. If you receive this, the setup is working.

### 问题六：【暂停点】确认测试结果

**测试邮件发送后，必须等待用户确认结果。**

向用户提问：
"测试邮件已发送。请检查收件箱（含垃圾邮件箱），收到测试邮件了吗？"
- 如果收到：SMTP 配置成功，继续正式发送
- 如果未收到：排查原因（密码错误/端口被封/服务商限制），重新配置

确认测试通过后，再继续正式发送。

## 发送开发邮件

### 准备工作
1. SMTP 配置已完成并测试通过
2. 邮件正文已由用户确认（见 outreach-workflow.md 第四阶段 P2）
3. 邮件附件已由用户上传

### 发送流程

对每家公司逐个发送：

1. 替换占位符：将正文中的 [First Name]、[Company Name] 等替换为实际值
2. 设置邮件头：
   - To：主送人
   - CC：抄送 3 人
   - Subject：替换 [Company Name] 和 [First Name]
3. 附加用户上传的附件
4. 通过 mcp-email-server send_email 发送
5. 每条发送间隔 3-5 秒，避免触发频率限制

使用 mcp-email-server 工具：
- send_email：发送邮件
- 参数：account_name、recipients（To+CC）、subject、body、attachments

### 发送后记录
- 发送时间
- 发送状态（成功/失败）
- 失败原因（如有）
- 在 Snov.io 列表中更新 outreach_stage 为 "contacted"
