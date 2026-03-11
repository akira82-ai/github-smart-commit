#!/usr/bin/env python3
"""
智能分类模块
将代码变更归类到不同类别：核心改进、新增功能、文档、配置等
"""

import re
from pathlib import Path


def categorize_changes(analysis, language="zh"):
    """
    智能分类变更内容

    根据文件路径、变更类型、文件内容分析，
    将变更归类到：核心改进、新增功能、文档、配置等

    Args:
        analysis: analyze_changes.py 的输出结果
        language: "zh" 或 "en"

    Returns:
        分类字典：
        {
            "core_improvements": [],
            "new_features": [],
            "bug_fixes": [],
            "documentation": [],
            "configuration": [],
            "testing": [],
            "performance": [],
            "breaking_changes": [],
            "other": []
        }
    """
    categories = {
        "core_improvements": [],
        "new_features": [],
        "bug_fixes": [],
        "documentation": [],
        "configuration": [],
        "testing": [],
        "performance": [],
        "breaking_changes": [],
        "other": []
    }

    change_type = analysis.get("type", "")
    modified_files = analysis.get("modified_files", [])
    added_files = analysis.get("added_files", [])
    deleted_files = analysis.get("deleted_files", [])
    is_breaking = analysis.get("is_breaking", False)

    # 所有文件列表
    all_files = list(zip(
        modified_files + added_files + deleted_files,
        ["modified"] * len(modified_files) +
        ["added"] * len(added_files) +
        ["deleted"] * len(deleted_files)
    ))

    # 如果是破坏性变更，添加到 breaking_changes
    if is_breaking:
        categories["breaking_changes"].append({
            "type": "breaking",
            "description": get_breaking_description(language),
            "files": [f[0] for f in all_files]
        })

    # 分类每个文件
    for filepath, change_status in all_files:
        category = classify_file(filepath, change_type, change_status)
        if category:
            categories[category].append({
                "file": filepath,
                "status": change_status,
                "description": describe_change(filepath, change_status, change_type, language)
            })

    return categories


def classify_file(filepath, change_type, change_status):
    """
    对单个文件进行分类

    Returns:
        类别名称字符串
    """
    filename = filepath.lower()
    path_parts = Path(filepath).parts

    # 文档类
    doc_patterns = [
        r"\.md$", r"readme", r"changelog", r"contributing",
        r"license", r"docs/", r"documentation/"
    ]
    if any(re.search(p, filename) for p in doc_patterns):
        return "documentation"

    # 配置类
    config_patterns = [
        r"config", r"\.json$", r"\.yaml$", r"\.yml$",
        r"\.toml$", r"\.xml$", r"\.env", r"settings",
        r"\.conf$", r"\.ini$"
    ]
    if any(re.search(p, filename) for p in config_patterns):
        return "configuration"

    # i18n 国际化相关
    if "i18n" in filename or "locale" in filename or "lang" in filename:
        return "configuration"

    # 测试类
    test_patterns = [
        r"test", r"spec", r"__tests__", r"\.test\.",
        r"\.spec\.", r"mock", r"fixture"
    ]
    if any(re.search(p, filename) for p in test_patterns):
        return "testing"

    # 性能优化相关
    perf_patterns = [
        r"cache", r"optimize", r"performance", r"lazy"
    ]
    if any(re.search(p, filename) for p in perf_patterns):
        return "performance"

    # 生成器、分析器、工具等核心模块
    if any(keyword in filename for keyword in ["generate", "analyze", "parser", "builder", "compiler"]):
        if change_type == "refactor":
            return "core_improvements"
        elif change_type == "feat":
            return "new_features"

    # 分类、路由等核心代码
    if path_parts and path_parts[0] in ["src", "lib", "core", "app", "scripts"]:
        if change_type == "feat":
            return "new_features"
        elif change_type == "refactor":
            return "core_improvements"
        elif change_type == "fix":
            return "bug_fixes"

    # 根据变更类型判断
    if change_type == "feat":
        return "new_features"
    elif change_type == "fix":
        return "bug_fixes"
    elif change_type == "refactor":
        return "core_improvements"

    # 默认归类到 other
    return "other"


def describe_change(filepath, change_status, change_type, language):
    """
    描述文件变更

    Returns:
        描述字符串
    """
    filename = Path(filepath).name.lower()
    path_parts = Path(filepath).parts

    # 特殊文件的描述
    special_files = {
        "readme.md": "项目说明文档",
        "changelog.md": "变更日志",
        "package.json": "项目配置和依赖",
        "tsconfig.json": "TypeScript 配置",
        "webpack.config.js": "构建配置",
        ".gitignore": "Git 忽略规则",
        ".env.example": "环境变量示例",
        "dockerfile": "Docker 配置",
        "docker-compose.yml": "Docker Compose 配置"
    }

    if filename in special_files:
        return special_files[filename]

    # 根据脚本文件名判断
    if filename == "config.py":
        return "配置管理系统"
    elif filename == "i18n.py":
        return "国际化文本映射"
    elif filename == "generate_commit.py":
        return "Commit 消息生成器"
    elif filename == "analyze_changes.py":
        return "代码变更分析器"
    elif filename == "categorization.py":
        return "智能分类模块"
    elif filename == "update_readme.py":
        return "README 更新器"
    elif filename == "update_version.py":
        return "版本号更新器"
    elif filename == "utils.py":
        return "工具函数库"

    # 根据路径和文件名判断
    # 认证相关
    if "auth" in filename or "login" in filename or "oauth" in filename:
        if "provider" in filename:
            return "OAuth 提供商"
        elif "session" in filename:
            return "会话管理"
        return "认证模块"

    # API 相关
    if "api" in filename:
        if "user" in filename:
            return "用户 API"
        return "API 接口"

    # 数据库相关
    if "db" in filename or "database" in filename or "query" in filename:
        return "数据库操作"

    # UI 相关
    if "ui" in filename or "component" in filename or "view" in filename:
        return "UI 组件"

    # 工具类
    if "util" in filename or "helper" in filename or "tool" in filename:
        return "工具函数"

    # 生成器、分析器类
    if "generate" in filename or "gen" in filename or "builder" in filename:
        return "生成器"
    elif "analyze" in filename or "analysis" in filename or "parser" in filename:
        return "分析器"
    elif "manager" in filename:
        return "管理器"

    # 测试相关
    if "test" in filename:
        if change_status == "added":
            return "测试用例"
        return "测试代码"

    # 配置相关
    if "config" in filename or "setting" in filename:
        return "配置管理"

    # 文档类
    if any(doc in filename for doc in ["readme", "contributing", "changelog", "license"]):
        if change_status == "added":
            return "添加项目文档"
        elif change_status == "modified":
            return "更新文档说明"

    # Git 配置
    if ".gitmessage" in filename or "gitignore" in filename:
        return "Git 模板"

    # 脚本类
    if filename.endswith(".sh"):
        if "install" in filename:
            return "安装脚本"
        elif "build" in filename:
            return "构建脚本"
        return "Shell 脚本"

    # Python 脚本
    if filename.endswith(".py"):
        # 根据所在目录判断
        if path_parts and "scripts" in path_parts:
            return "脚本模块"
        return "Python 模块"

    # 配置文件
    if any(ext in filename for ext in [".json", ".yaml", ".yml", ".toml", ".xml"]):
        if "example" in filename or "sample" in filename:
            return "配置示例"
        return "配置文件"

    # 示例/模板文件
    if "example" in filename or "template" in filename or "sample" in filename:
        return "示例文件"

    # 默认返回文件类型
    if change_status == "added":
        return "新文件"
    elif change_status == "modified":
        return "更新"
    return "变更"


def get_breaking_description(language):
    """获取破坏性变更的描述"""
    descriptions = {
        "zh": "此更新包含不兼容的 API 变更，请注意迁移",
        "en": "This update contains incompatible API changes"
    }
    return descriptions.get(language, descriptions["zh"])


def extract_line_changes(analysis):
    """
    从 git diff --stat 中提取代码行数变化

    解析格式：
    filename | 5 ++++---
    filename | 10 +++++-----

    Returns:
        {filename: (added, deleted)} 字典
    """
    stat_summary = analysis.get("stat_summary", "")
    line_changes = {}

    for line in stat_summary.split("\n"):
        if "|" not in line:
            continue

        parts = line.split("|")
        if len(parts) < 2:
            continue

        filename = parts[0].strip()
        changes = parts[1].strip()

        # 解析行数变化
        # 格式：5 ++++--- 或 10 +++++-----
        added = changes.count("+")
        deleted = changes.count("-")

        if added > 0 or deleted > 0:
            line_changes[filename] = (added, deleted)

    return line_changes


def get_total_line_changes(line_changes):
    """
    获取总行数变化

    Returns:
        (total_added, total_deleted) 元组
    """
    total_added = sum(changes[0] for changes in line_changes.values())
    total_deleted = sum(changes[1] for changes in line_changes.values())
    return (total_added, total_deleted)


def generate_smart_summary(analysis, categories, language):
    """
    智能生成总体说明（第一段）

    例如："完整实现 GitHub Smart Commit 技能的所有计划功能："

    Returns:
        总体说明字符串
    """
    change_type = analysis.get("type", "")
    scope = analysis.get("scope", "")

    # 统计各类别数量
    category_counts = {
        cat: len(items) for cat, items in categories.items()
        if items and cat != "breaking_changes"
    }

    if not category_counts:
        # 没有具体分类，使用默认描述
        default_desc = {
            "zh": "更新代码",
            "en": "Update code"
        }
        return default_desc.get(language, "Update code")

    # 根据主要类别生成描述
    main_category = max(category_counts, key=category_counts.get)

    summaries = {
        "zh": {
            "new_features": f"添加新功能，增强系统能力",
            "core_improvements": f"重构代码结构，提升可维护性",
            "bug_fixes": f"修复已知问题，提升稳定性",
            "documentation": f"更新项目文档",
            "configuration": f"更新配置文件",
            "testing": f"完善测试覆盖",
            "performance": f"优化性能，提升响应速度"
        },
        "en": {
            "new_features": "Add new features to enhance system capabilities",
            "core_improvements": "Refactor code structure for better maintainability",
            "bug_fixes": "Fix known issues and improve stability",
            "documentation": "Update project documentation",
            "configuration": "Update configuration files",
            "testing": "Improve test coverage",
            "performance": "Optimize performance for better response time"
        }
    }

    return summaries.get(language, summaries["zh"]).get(
        main_category,
        "更新代码"
    )


def main():
    """测试主函数"""
    import json
    import sys

    # 测试数据
    test_analysis = {
        "type": "feat",
        "scope": "core",
        "is_breaking": False,
        "modified_files": ["src/auth.py", "README.md"],
        "added_files": ["src/api/user.py", "tests/test_auth.py"],
        "deleted_files": [],
        "stat_summary": "src/auth.py | 10 +++++-----\nREADME.md | 5 +++---"
    }

    categories = categorize_changes(test_analysis, "zh")
    print(json.dumps(categories, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
