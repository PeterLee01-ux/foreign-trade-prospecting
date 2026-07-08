# 邮箱验证工作流

## 适用场景
用户有一个邮箱列表，需要验证哪些是有效的、可投递的。

## 环境搭建：check-if-email-exists（本地 Docker）

### 首次部署
运行：bash scripts/setup_check_email.sh
或手动执行：
docker run -d --name reacher -p 8080:8080 reacherhq/backend:latest

### 验证服务是否运行
curl http://localhost:8080/health

## 三种验证方式（按推荐顺序）

### 方式一：check-if-email-exists（本地、无限制、最快）
curl "http://localhost:8080/v0/check_email?email=test@example.com"

返回字段说明：
- is_reachable：valid（有效）| invalid（无效）| risky（有风险）| unknown（未知）
- mx：是否找到 MX 邮件交换记录
- smtp：SMTP 握手结果
- syntax：格式是否合法
- misc：catch_all（全域接受）、disposable（一次性邮箱）、role_account（公共邮箱）

### 方式二：Prospector（免费版每天 50 次）
单个验证：prospector verify_email
批量验证（最多 25 个）：prospector verify_emails_batch

返回：status（valid/invalid/unknown）、score（0-100）、mx_host、catch_all

### 方式三：Snov.io（付费额度）
使用 snovio_verify_emails 批量验证，返回详细的投递数据。

## 批量验证流程

1. 将所有待验证邮箱汇入列表
2. 数量不超过 50 个：优先用 prospector verify_emails_batch（免费）
3. 数量超过 50 个：用 check-if-email-exists（本地无限制）
4. 需要详细投递数据分析：用 Snov.io

### 使用自带脚本
python scripts/validate_emails.py --input emails.txt --output results.csv

## 结果解读

| 状态 | 处理方式 |
|------|---------|
| valid / reachable | 安全，可直接发送 |
| risky | 可能退信，重要客户可尝试 |
| invalid / unreachable | 从列表中删除 |
| catch_all | 域名接受所有邮件，谨慎测试 |
| disposable | 一次性临时邮箱，删除 |
| role_account | info@/sales@ 类公共邮箱，参与度低，相关则保留 |

## 验证完成后

1. 在 Snov.io 列表中标记已验证邮箱
2. 计算有效率 = 有效数 / 总数
3. 向用户报告结果摘要
4. 建议下一步：对有效邮箱开始开发，对无效邮箱重新搜索
