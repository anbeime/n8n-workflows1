#!/usr/bin/env python3
"""
中英文翻译模块
用于将中文搜索词转换为英文进行搜索
"""

# 常用服务和工具的中英文映射
SERVICE_TRANSLATIONS = {
    # 通讯工具
    "电报": "telegram",
    "微信": "wechat",
    "钉钉": "dingtalk",
    "飞书": "feishu",
    "邮件": "email gmail outlook",
    "邮箱": "email gmail outlook",
    "短信": "sms twilio",
    "消息": "message slack discord",
    
    # AI服务
    "人工智能": "ai openai anthropic",
    "智能": "ai gpt",
    "聊天机器人": "chatbot ai",
    "机器人": "bot",
    "语音": "voice audio speech",
    "图像": "image vision dalle",
    "视频": "video",
    
    # 数据存储
    "数据库": "database postgresql mysql mongodb",
    "表格": "sheet airtable google",
    "云盘": "drive google dropbox",
    "文件": "file storage",
    "存储": "storage",
    
    # 开发工具
    "代码": "code github",
    "仓库": "repository github gitlab",
    "部署": "deploy",
    "测试": "test",
    "监控": "monitor",
    
    # 业务功能
    "客户": "customer crm",
    "订单": "order",
    "支付": "payment stripe paypal",
    "发票": "invoice",
    "销售": "sales",
    "营销": "marketing",
    "推广": "promotion advertising",
    
    # 社交媒体
    "社交": "social media",
    "推特": "twitter x",
    "脸书": "facebook",
    "领英": "linkedin",
    "抖音": "tiktok",
    "油管": "youtube",
    "红书": "xiaohongshu",
    
    # 工作流概念
    "自动化": "automation automate",
    "工作流": "workflow",
    "触发": "trigger webhook",
    "定时": "schedule cron",
    "手动": "manual",
    "复杂": "complex",
    "简单": "simple low",
    
    # 数据操作
    "同步": "sync synchronize",
    "备份": "backup",
    "导入": "import",
    "导出": "export",
    "转换": "convert transform",
    "处理": "process",
    "分析": "analyze analytics",
    
    # 通知提醒
    "通知": "notification alert",
    "提醒": "reminder alert",
    "警报": "alert",
    "报告": "report",
    
    # 项目管理
    "任务": "task",
    "项目": "project",
    "看板": "kanban trello",
    "问题": "issue jira",
    "文档": "document notion",
    
    # 电商
    "商店": "shop shopify woocommerce",
    "产品": "product",
    "库存": "inventory stock",
    "购物车": "cart",
    
    # 时间相关
    "每天": "daily",
    "每周": "weekly",
    "每月": "monthly",
    "定期": "periodic schedule",
    "实时": "realtime",
    
    # 其他常用词
    "创建": "create",
    "更新": "update",
    "删除": "delete",
    "获取": "get fetch",
    "发送": "send",
    "接收": "receive",
    "生成": "generate",
    "上传": "upload",
    "下载": "download",
}

# 触发器类型翻译
TRIGGER_TRANSLATIONS = {
    "定时": "Scheduled",
    "计划": "Scheduled",
    "webhook": "Webhook",
    "钩子": "Webhook",
    "手动": "Manual",
    "复杂": "Complex",
}

# 复杂度翻译
COMPLEXITY_TRANSLATIONS = {
    "简单": "low",
    "低": "low",
    "中等": "medium",
    "中": "medium",
    "复杂": "high",
    "高": "high",
}

def translate_chinese_to_english(query: str) -> str:
    """
    将中文搜索词转换为英文
    支持混合中英文输入
    """
    if not query:
        return query
    
    # 转换为小写以便匹配
    query_lower = query.lower()
    translated_parts = []
    
    # 检查每个中文词汇并翻译
    for cn_word, en_words in SERVICE_TRANSLATIONS.items():
        if cn_word in query:
            # 如果找到中文词，添加对应的英文词
            translated_parts.append(en_words)
            # 从原查询中移除已翻译的中文
            query = query.replace(cn_word, "")
    
    # 保留原始查询中的英文和数字部分
    remaining = query.strip()
    if remaining:
        translated_parts.insert(0, remaining)
    
    # 组合所有翻译结果
    result = " ".join(translated_parts).strip()
    
    return result if result else query


def translate_filter_chinese_to_english(filter_value: str, filter_type: str = "trigger") -> str:
    """
    翻译过滤器值（如触发器类型、复杂度）
    """
    if filter_type == "trigger":
        return TRIGGER_TRANSLATIONS.get(filter_value, filter_value)
    elif filter_type == "complexity":
        return COMPLEXITY_TRANSLATIONS.get(filter_value, filter_value)
    return filter_value


def get_chinese_label(english_value: str, label_type: str = "trigger") -> str:
    """
    将英文标签转换为中文显示
    用于前端展示
    """
    # 反向映射
    if label_type == "trigger":
        reverse_map = {v: k for k, v in TRIGGER_TRANSLATIONS.items()}
        return reverse_map.get(english_value, english_value)
    elif label_type == "complexity":
        reverse_map = {v: k for k, v in COMPLEXITY_TRANSLATIONS.items()}
        return reverse_map.get(english_value, english_value)
    
    return english_value


# 常用服务的中文名称映射
SERVICE_NAME_CN = {
    "telegram": "Telegram/电报",
    "wechat": "微信",
    "email": "邮件",
    "gmail": "Gmail",
    "slack": "Slack",
    "discord": "Discord",
    "openai": "OpenAI/人工智能",
    "google": "谷歌",
    "drive": "云盘",
    "sheet": "表格",
    "airtable": "Airtable",
    "database": "数据库",
    "postgresql": "PostgreSQL",
    "mongodb": "MongoDB",
    "github": "GitHub",
    "gitlab": "GitLab",
    "notion": "Notion",
    "trello": "Trello",
    "jira": "Jira",
    "shopify": "Shopify",
    "stripe": "Stripe",
    "paypal": "PayPal",
    "youtube": "YouTube",
    "facebook": "Facebook",
    "twitter": "Twitter/X",
    "linkedin": "LinkedIn",
    "tiktok": "TikTok/抖音",
}


def add_chinese_hint(text: str) -> str:
    """
    为英文服务名添加中文提示
    例如: "Telegram" -> "Telegram (电报)"
    """
    text_lower = text.lower()
    for en_key, cn_name in SERVICE_NAME_CN.items():
        if en_key in text_lower and "/" in cn_name:
            # 只返回中文部分作为提示
            cn_part = cn_name.split("/")[-1]
            return f"{text} ({cn_part})"
    return text
