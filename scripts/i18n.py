#!/usr/bin/env python3
"""
国际化模块
统一管理所有中英文文本映射
"""

# 变更类型描述
TYPE_DESCRIPTIONS = {
    "en": {
        "feat": "Add",
        "fix": "Fix",
        "refactor": "Refactor",
        "docs": "Update",
        "style": "Style",
        "test": "Test",
        "chore": "Update",
        "perf": "Optimize",
        "ci": "Update CI",
        "build": "Update build"
    },
    "zh": {
        "feat": "添加",
        "fix": "修复",
        "refactor": "重构",
        "docs": "更新",
        "style": "优化样式",
        "test": "测试",
        "chore": "更新",
        "perf": "优化",
        "ci": "更新 CI",
        "build": "更新构建"
    }
}

# CHANGELOG 分类
CHANGELOG_CATEGORIES = {
    "en": {
        "feat": "Added",
        "fix": "Fixed",
        "refactor": "Changed",
        "perf": "Changed",
        "docs": "Changed",
        "style": "Changed",
        "test": "Changed",
        "ci": "Changed",
        "build": "Changed",
        "chore": "Changed",
        "security": "Security"
    },
    "zh": {
        "feat": "新增",
        "fix": "修复",
        "refactor": "变更",
        "perf": "优化",
        "docs": "文档",
        "style": "样式",
        "test": "测试",
        "ci": "CI",
        "build": "构建",
        "chore": "其他",
        "security": "安全"
    }
}

# 文件统计描述
FILE_STATS = {
    "en": {
        "added": "• Add {count} new files",
        "deleted": "• Remove {count} files",
        "modified": "• Modify {count} files",
        "more_files": "  ... and {count} more files",
        "modified_files_header": "Modified files:"
    },
    "zh": {
        "added": "• 新增 {count} 个文件",
        "deleted": "• 删除 {count} 个文件",
        "modified": "• 修改 {count} 个文件",
        "more_files": "  ... 以及其他 {count} 个文件",
        "modified_files_header": "修改的文件："
    }
}

# 破坏性变更警告
BREAKING_WARNING = {
    "en": "⚠️ BREAKING CHANGE: This update contains breaking changes",
    "zh": "⚠️ 破坏性变更：此更新包含不兼容的 API 变更"
}

# CHANGELOG 标题
CHANGELOG_HEADERS = {
    "en": {
        "title": "Changelog",
        "description": "All notable changes to this project will be documented in this file.",
        "breaking": "### ⚠️ Breaking Changes",
        "default_category": "Changed",
        "default_desc": "- Code updates",
        "update_module": "- Update `{scope}` module"
    },
    "zh": {
        "title": "变更日志",
        "description": "本文档记录项目的所有重要变更。",
        "breaking": "### ⚠️ 破坏性变更",
        "default_category": "变更",
        "default_desc": "- 代码更新",
        "update_module": "- 更新 `{scope}` 模块"
    }
}


def get_text(mapping, language, key, fallback=None, **kwargs):
    """
    获取本地化文本

    Args:
        mapping: 文本映射字典
        language: "en" 或 "zh"
        key: 键名
        fallback: 如果键不存在时的回退值
        **kwargs: 格式化参数

    Returns:
        本地化文本字符串
    """
    lang_mapping = mapping.get(language, mapping.get("en", {}))
    text = lang_mapping.get(key, fallback or key)

    if kwargs:
        return text.format(**kwargs)
    return text