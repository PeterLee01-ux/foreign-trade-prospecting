# 客户分类整理工作流

## 适用场景
用户需要将已找到的客户按多维度分类归档，进行持续的客户管理。

## 使用 Snov.io 列表

### 创建新列表
使用 snovio_create_list：
- 命名规则："[国家]-[行业]-[日期]"
- 示例："US-LED_Importers-2026Q3"

### 添加客户到列表
使用 snovio_add_prospect：
- 必填：email、list_id
- 可选：name、company、position、phone、custom_fields

### 推荐自定义字段

| 字段名 | 类型 | 可选值 |
|-------|------|--------|
| lead_source | 文本 | snovio、linkedin、referral、exhibition |
| whatsapp_active | 布尔 | true / false |
| email_verified | 布尔 | true / false |
| outreach_stage | 文本 | new、contacted、replied、meeting、deal、closed |
| response_status | 文本 | none、interested、not_interested、wrong_contact |
| priority | 文本 | high、medium、low |
| last_follow_up | 日期 | YYYY-MM-DD |
| notes | 文本 | 自由文本 |

## 分类整理操作

### 按行业分类
1. 获取列表中的所有客户
2. 按公司行业字段分组
3. 创建子列表或按行业打标签

### 按回复状态分类
1. 按 response_status 自定义字段筛选客户
2. 优先级排序：有兴趣 > 无回复 > 无意向
3. 对"有兴趣"：立即安排跟进
4. 对"无意向"：移入培育列表（3 个月后重新联系）

### 按国家/地区分类
1. 按所在地对客户分组
2. 创建按国家划分的子列表
3. 根据时区调整触达时间

### 清理无效客户
1. 找出 3 次跟进无回复的客户
2. 移入"冷却"列表
3. 6 个月后换新角度重新尝试

## 每周回顾流程
1. 查看营销数据（snovio_get_campaign_analytics）
2. 更新最近联系人的回复状态
3. 将"有兴趣"的客户移入活跃跟进
4. 向用户报告：本周新增客户、回复数、预约会议数
