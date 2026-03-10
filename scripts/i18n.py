#!/usr/bin/env python3
"""
国际化模块
统一管理所有中英文文本映射
"""

# 变更类型描述（符合 Conventional Commits 规范）
TYPE_DESCRIPTIONS = {
    "en": {
        "feat": "Add",
        "fix": "Fix",
        "refactor": "Refactor",
        "docs": "Update",
        "style": "Fix style in",
        "test": "Add tests for",
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
        "style": "调整样式",
        "test": "添加测试",
        "chore": "更新",
        "perf": "优化",
        "ci": "更新 CI",
        "build": "更新构建"
    }
}

# 文件统计描述（简洁格式）
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
    "en": "BREAKING CHANGE: This update contains breaking changes",
    "zh": "⚠️ 破坏性变更：此更新包含不兼容的 API 变更"
}

# 变更详细描述模板
CHANGE_DESCRIPTIONS = {
    "en": {
        "feat": {
            "default": "Add new functionality",
            "auth": "Implement authentication and authorization",
            "api": "Add new API endpoint",
            "ui": "Add new UI component"
        },
        "fix": {
            "default": "Fix reported issue",
            "bug": "Fix bug in functionality",
            "crash": "Fix crash issue"
        },
        "refactor": {
            "default": "Refactor code structure",
            "simplify": "Simplify implementation",
            "performance": "Improve code performance"
        },
        "docs": {
            "default": "Update documentation",
            "readme": "Update README",
            "api": "Update API documentation"
        }
    },
    "zh": {
        "feat": {
            "default": "添加新功能",
            "auth": "实现身份认证和授权",
            "api": "添加新的 API 接口",
            "ui": "添加新的 UI 组件"
        },
        "fix": {
            "default": "修复已报告的问题",
            "bug": "修复功能缺陷",
            "crash": "修复崩溃问题"
        },
        "refactor": {
            "default": "重构代码结构",
            "simplify": "简化实现逻辑",
            "performance": "优化代码性能"
        },
        "docs": {
            "default": "更新文档",
            "readme": "更新 README 文档",
            "api": "更新 API 文档"
        }
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
