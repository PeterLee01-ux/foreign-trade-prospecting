---
name: foreign-trade-prospecting
description: >
  外贸客户开发全流程。查找公司邮箱、验证联系人、检查 WhatsApp 号码、
  公司背景调查、客户分类整理、竞品客户挖掘、按国家/地区/城市精准筛选。
  当用户想要：找海外客户、查找邮箱、验证邮箱、检查 WhatsApp、公司调研、
  客户整理、竞品分析、按地区筛选客户时使用（覆盖美国、中东及全球 B2B 市场）。
---

# 外贸获客助手
## ⚠️ 首次使用必读

**此 Skill 依赖 Snov.io API，需要用户自行注册并获取 API Key。**

1. 去 https://app.snov.io 注册账号
2. 进入 Account Settings > API
3. 获取 CLIENT_ID（App ID）和 CLIENT_SECRET（App Secret）
4. 首次运行本 Skill 时，会提示输入这两个值

**没有 API Key 则无法使用邮箱查找和域名搜索功能。**

其他工具均为免费/自托管，无需额外付费。


## 全局规则（所有工作流必须遵守）

1. **暂停确认关键词**：每次调用 Snov.io 查找邮箱前，**必须停下来**，向用户展示当前进展，
   让用户输入模糊查找关键词，等用户确认后再继续。不得自动生成关键词。
2. **每公司最多 4 个邮箱**：使用 Snov.io find_email 时，每个公司最多查找 4 个邮箱地址，
   严格控制点数消耗。优先选信心度最高、职位最相关的联系人。

## 快速开始

当用户要求查找客户、验证联系方式或执行外发流程时，先匹配对应的工作流，
然后跳转到相应的参考文件。

## 可用 MCP 工具

### 1. Snov.io（43 个工具）— 核心获客引擎
API 凭证需要用户自行配置。

**首次使用前，必须向用户索要 Snov.io API Key：**
- SNOVIO_CLIENT_ID（也称为 App ID）：从 Snov.io > Account Settings > API 获取
- SNOVIO_CLIENT_SECRET（也称为 App Secret）：同上
- 注册地址：https://snov.io（有免费额度）

如果用户未提供，暂停所有工作流，等用户输入后再继续。

核心工具：域名搜索、邮箱查找、邮箱验证、LinkedIn 补充、域名下的联系人发现、
公司信息查询、客户列表管理、邮件序列营销。

**点数控制**：每次邮箱查找消耗 Snov.io 点数。遵守全局规则第 1、2 条。

### 2. Prospector（6 个工具）— 免费自托管邮箱查找与验证
无需 API Key。通过 npx prospector-mcp 运行。
免费版：每天 50 次验证。升级：设置环境变量 PROSPECTOR_TIER=pro 或 business。

工具：单邮箱验证、批量验证（最多 25 个）、邮箱查找、域名检查、用量统计。
**不消耗 Snov.io 点数，优先用于验证和补充查找。**

### 3. check-if-email-exists — 本地 Docker 邮箱验证
启动命令：docker run -d --name reacher -p 8080:8080 reacherhq/backend:latest
调用方式：curl http://localhost:8080/v0/check_email?email=test@example.com

详见 references/email-verification.md。
**完全不消耗任何点数，优先用于批量验证。**

### 4. mcp-whatsapp（42 个工具）— WhatsApp 验证与消息
无需 API Key。扫码配对：http://127.0.0.1:8765/pair。
核心工具：is_on_whatsapp（批量验证号码）、send_message（发消息）、list_chats（聊天列表）。

### 5. mcp-email-server（270+ 星）— 邮件发送
通过 SMTP/IMAP 发送开发邮件。首次使用需配置 SMTP（见 email-sending.md）。
安装：uvx mcp-email-server@latest stdio
核心工具：send_email（发送邮件）、list_emails（查看收件箱）

## 工作流路由表

| 用户意图 | 参考文件 |
|---------|---------|
| 查找公司邮箱/联系方式 | references/email-finding.md |
| 验证/清洗邮箱列表 | references/email-verification.md |
| WhatsApp 验证/发消息 | references/whatsapp-tools.md |
| 公司背景调查 | references/company-research.md |
| 端到端客户开发全流程 | references/outreach-workflow.md |
| 客户分类整理 | references/customer-organization.md |
| 竞品客户挖掘 | references/competitor-mining.md |

| 配置 SMTP / 发送开发邮件 | [references/email-sending.md](references/email-sending.md) || 按国家/地区/城市精准筛选 | references/geo-filtering.md |

## 环境准备

首次使用前，确保：

1. check-if-email-exists Docker 容器已运行（见 email-verification.md）
2. mcp-whatsapp 守护进程已启动并完成手机扫码配对
3. Snov.io 凭证已在 MCP 配置中设置

## 脚本工具

- scripts/setup_check_email.sh — 一键启动 check-if-email-exists Docker 容器
- scripts/validate_emails.py — 通过本地 Docker API 批量验证邮箱

## 常用组合模式

### 查找并验证一条龙
1. 用 Snov.io domain_search 在目标公司查找联系人
2. **【暂停】展示联系人列表，让用户输入模糊查找关键词，确认后继续**
3. 用 Snov.io find_email 获取邮箱地址（每公司最多 4 个）
4. 用 prospector verify_emails_batch 或 check-if-email-exists 验证邮箱
5. 返回带有信心度评分的验证结果

### WhatsApp 触达准备
1. 从 Snov.io 收集电话号码
2. 用 mcp-whatsapp is_on_whatsapp 批量检查号码是否注册 WhatsApp
3. 对活跃号码使用 send_message 发送开发信
4. 在 Snov.io 列表中标记 WhatsApp 状态

### 地域精准筛选
1. 向用户确认目标国家/地区/城市 + 行业
2. 用 Snov.io domain_prospects 按位置过滤
3. **【暂停】展示筛选结果，让用户输入模糊查找关键词，确认后继续**
4. 查找邮箱（每公司最多 4 个）
5. 按职位/职能进一步缩小范围
6. 返回经过验证的目标联系人
