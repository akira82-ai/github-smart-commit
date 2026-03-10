#!/usr/bin/env python3
"""
自动生成 CHANGELOG.md
遵循 Keep a Changelog 格式
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path


def generate_changelog_entry(analysis, version, commit_hash, language="en"):
    """
    生成单个版本的 CHANGELOG 条目

    Args:
        analysis: analyze_changes.py 的输出
        version: 版本号
        commit_hash: commit hash（用于链接）
        language: "en" 或 "zh"

    Returns:
        CHANGELOG 条目字符串
    """
    change_type = analysis.get("type", "chore")
    is_breaking = analysis.get("is_breaking", False)

    # 日期
    today = datetime.now().strftime("%Y-%m-%d")

    # 标题
    if language == "zh":
        title = f"## [{version}] - {today}"
    else:
        title = f"## [{version}] - {today}"

    # 变更类型映射到 Keep a Changelog 分类
    category_mapping = {
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

    category = category_mapping[language].get(change_type, "Changed" if language == "en" else "变更")

    # 生成变更条目
    entry_lines = [title, ""]

    # 添加破坏性变更警告
    if is_breaking:
        if language == "zh":
            entry_lines.append("### ⚠️ 破坏性变更")
        else:
            entry_lines.append("### ⚠️ Breaking Changes")
        entry_lines.append("")

    # 添加分类
    entry_lines.append(f"### {category}")
    entry_lines.append("")

    # 生成描述
    description = generate_changelog_description(analysis, commit_hash, language)
    entry_lines.append(description)
    entry_lines.append("")

    return "\n".join(entry_lines)


def generate_changelog_description(analysis, commit_hash, language):
    """生成变更描述"""
    modified_files = analysis.get("modified_files", [])
    added_files = analysis.get("added_files", [])
    deleted_files = analysis.get("deleted_files", [])
    scope = analysis.get("scope", "")

    # 提取关键文件/模块
    key_files = []
    if added_files:
        key_files.extend(added_files[:3])
    if modified_files:
        key_files.extend(modified_files[:2])

    # 生成简短描述
    if language == "zh":
        if scope:
            desc = f"- 更新 `{scope}` 模块"
        else:
            desc = "- 代码更新"

        # 添加文件列表
        if key_files:
            files_str = ", ".join([f"`{f}`" for f in key_files[:5]])
            desc += f"：{files_str}"

        # 添加更多文件指示
        total_files = len(added_files) + len(modified_files) + len(deleted_files)
        if total_files > 5:
            desc += f" 及其他 {total_files - 5} 个文件"

    else:
        if scope:
            desc = f"- Update `{scope}` module"
        else:
            desc = "- Code updates"

        # 添加文件列表
        if key_files:
            files_str = ", ".join([f"`{f}`" for f in key_files[:5]])
            desc += f": {files_str}"

        # 添加更多文件指示
        total_files = len(added_files) + len(modified_files) + len(deleted_files)
        if total_files > 5:
            desc += f" and {total_files - 5} more files"

    # 添加 commit 链接
    if commit_hash:
        short_hash = commit_hash[:7]
        if language == "zh":
            desc += f" ([{short_hash}](/commits/{commit_hash}))"
        else:
            desc += f" ([{short_hash}](/commits/{commit_hash}))"

    return desc


def update_changelog(changelog_path, new_entry, language="en"):
    """
    更新 CHANGELOG.md 文件

    Args:
        changelog_path: CHANGELOG.md 文件路径
        new_entry: 新的 CHANGELOG 条目
        language: "en" 或 "zh"

    Returns:
        更新后的内容
    """
    # 如果文件不存在，创建新文件
    if not changelog_path.exists():
        if language == "zh":
            header = "# 变更日志\n\n本文档记录项目的所有重要变更。\n\n"
        else:
            header = "# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n"
        return header + new_entry

    # 读取现有内容
    content = changelog_path.read_text(encoding="utf-8")

    # 在第一个版本条目之前插入新条目
    # 查找第一个 "## [" 的位置
    match = re.search(r"##\s+\[", content)
    if match:
        # 在第一个版本条目前插入
        insert_pos = match.start()
        updated = content[:insert_pos] + new_entry + "\n" + content[insert_pos:]
    else:
        # 没有版本条目，添加到文件末尾
        updated = content + "\n" + new_entry

    return updated


def main():
    """主函数"""
    if len(sys.argv) < 4:
        print("Usage: generate_changelog.py <changelog_path> <version> <analysis_json> [commit_hash] [language]", file=sys.stderr)
        sys.exit(1)

    changelog_path = Path(sys.argv[1])
    version = sys.argv[2]
    language = sys.argv[4] if len(sys.argv) > 4 else "en"
    commit_hash = sys.argv[5] if len(sys.argv) > 5 else ""

    # 读取 analysis
    try:
        analysis = json.loads(sys.argv[3])
    except json.JSONDecodeError:
        print("错误：无效的 JSON 输入", file=sys.stderr)
        sys.exit(1)

    # 生成新的 CHANGELOG 条目
    new_entry = generate_changelog_entry(analysis, version, commit_hash, language)

    # 更新 CHANGELOG.md
    updated_content = update_changelog(changelog_path, new_entry, language)

    # 写回文件
    changelog_path.write_text(updated_content, encoding="utf-8")

    # 输出结果
    print(json.dumps({
        "status": "success",
        "version": version,
        "changelog_file": str(changelog_path),
        "entry_preview": new_entry.split("\n")[0]  # 只返回标题作为预览
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
