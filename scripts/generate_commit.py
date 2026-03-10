#!/usr/bin/env python3
"""
生成美观的 Commit 消息
格式：<emoji> <type>(<scope>): <subject>
"""

import json
import re
import sys
from datetime import datetime


def generate_commit_message(analysis, custom_message=None, language="en"):
    """
    生成 commit 消息

    Args:
        analysis: analyze_changes.py 的输出结果
        custom_message: 用户自定义的 commit 消息（可选）
        language: "en" 或 "zh"，决定 commit 消息语言

    Returns:
        完整的 commit 消息字符串
    """
    if custom_message:
        # 如果用户提供了自定义消息，直接使用
        return custom_message

    # 生成 subject
    emoji = analysis.get("emoji", "🔧")
    change_type = analysis.get("type", "chore")
    scope = analysis.get("scope", "")
    is_breaking = analysis.get("is_breaking", False)

    # 智能生成 subject
    subject = generate_smart_subject(analysis, emoji, change_type, scope, is_breaking, language)

    # 构建 body
    body_parts = []

    # 添加详细变更描述
    change_description = generate_change_description(analysis, language)
    if change_description:
        body_parts.append(change_description)
        body_parts.append("")

    # 添加修改的文件列表（精简版）
    modified_files = analysis.get("modified_files", [])
    added_files = analysis.get("added_files", [])
    deleted_files = analysis.get("deleted_files", [])

    if modified_files or added_files or deleted_files:
        body_parts.append("Modified files:" if language == "en" else "修改的文件：")
        for file in modified_files[:8]:  # 最多显示 8 个
            body_parts.append(f"  {file}")
        for file in added_files[:5]:
            body_parts.append(f"  + {file}")
        for file in deleted_files[:3]:
            body_parts.append(f"  - {file}")

        total_files = len(modified_files) + len(added_files) + len(deleted_files)
        shown_files = min(8, len(modified_files)) + min(5, len(added_files)) + min(3, len(deleted_files))
        if total_files > shown_files:
            body_parts.append(f"  ... and {total_files - shown_files} more files")
        body_parts.append("")

    # 构建 footer
    footer_parts = []

    # 破坏性变更警告
    if is_breaking:
        if language == "zh":
            footer_parts.append("⚠️ 破坏性变更：此更新包含不兼容的 API 变更")
        else:
            footer_parts.append("⚠️ BREAKING CHANGE: This update contains breaking changes")
        footer_parts.append("")

    # 关联的 issues/PRs（从 branch 名称或文件内容推断）
    refs = extract_issue_references(analysis)
    if refs:
        footer_parts.append(f"Refs: {', '.join(refs)}")
        footer_parts.append("")

    # Claude 署名
    footer_parts.append("Co-Authored-By: Claude Sonnet 4.6 (1M context) <noreply@anthropic.com>")

    # 组合完整消息
    commit_message = subject
    if body_parts:
        commit_message += "\n\n" + "\n".join(body_parts)
    if footer_parts:
        commit_message += "\n" + "\n".join(footer_parts)

    return commit_message


def generate_smart_subject(analysis, emoji, change_type, scope, is_breaking, language):
    """智能生成 subject"""
    # 确定变更类型的描述词
    type_descriptions = {
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

    action = type_descriptions[language].get(change_type, "Update")

    # 提取主要影响的模块或文件
    modified_files = analysis.get("modified_files", [])
    added_files = analysis.get("added_files", [])
    deleted_files = analysis.get("deleted_files", [])

    all_files = modified_files + added_files + deleted_files
    target = ""

    if all_files:
        # 获取最主要的文件或目录
        main_file = all_files[0]

        # 如果是路径，提取最后部分
        if "/" in main_file:
            parts = main_file.split("/")
            # 尝试获取有意义的文件名或目录名
            for part in reversed(parts):
                if part and part not in ["src", "lib", "app", "index", "main"]:
                    target = part
                    break
            if not target and parts:
                target = parts[-1]
        else:
            target = main_file

        # 去掉文件扩展名（除非是配置文件）
        if "." in target and not target.endswith((".json", ".yaml", ".yml", ".toml", ".md")):
            target = target.rsplit(".", 1)[0]

    # 构建 subject
    if scope and target:
        subject = f"{emoji} {change_type}({scope}): {action} {target}"
    elif scope:
        subject = f"{emoji} {change_type}({scope}): {action}"
    elif target:
        subject = f"{emoji} {change_type}: {action} {target}"
    else:
        subject = f"{emoji} {change_type}: {action.lower()}"

    # 添加破坏性变更标记
    if is_breaking:
        subject += " !"

    return subject


def generate_change_description(analysis, language):
    """生成变更描述"""
    modified_files = analysis.get("modified_files", [])
    added_files = analysis.get("added_files", [])
    deleted_files = analysis.get("deleted_files", [])

    if not modified_files and not added_files and not deleted_files:
        return ""

    lines = []

    # 统计信息
    if language == "zh":
        if added_files:
            lines.append(f"• 新增 {len(added_files)} 个文件")
        if deleted_files:
            lines.append(f"• 删除 {len(deleted_files)} 个文件")
        if modified_files:
            lines.append(f"• 修改 {len(modified_files)} 个文件")
    else:
        if added_files:
            lines.append(f"• Add {len(added_files)} new files")
        if deleted_files:
            lines.append(f"• Remove {len(deleted_files)} files")
        if modified_files:
            lines.append(f"• Modify {len(modified_files)} files")

    return "\n".join(lines)


def extract_issue_references(analysis):
    """从分析结果中提取 issue/PR 引用"""
    refs = set()

    # 从文件名中查找 issue 编号（如 fix-123, feature-456）
    all_files = (
        analysis.get("modified_files", []) +
        analysis.get("added_files", []) +
        analysis.get("deleted_files", [])
    )

    for file_path in all_files:
        # 查找 #123 格式
        matches = re.findall(r"#(\d+)", file_path)
        refs.update(matches)

        # 查找 issue-123, fix-123 等格式
        matches = re.findall(r"(?:issue|fix|feat|bug)[-_]?(\d+)", file_path, re.IGNORECASE)
        refs.update(matches)

    # 从 diff 统计中查找（如果有的话）
    stat_summary = analysis.get("stat_summary", "")
    matches = re.findall(r"#(\d+)", stat_summary)
    refs.update(matches)

    return sorted(refs, key=int) if refs else []


def main():
    """主函数"""
    # 从 stdin 读取 analysis 结果
    try:
        analysis = json.load(sys.stdin)
    except json.JSONDecodeError:
        print(json.dumps({"error": "无效的 JSON 输入"}), file=sys.stderr)
        sys.exit(1)

    # 生成 commit 消息
    commit_message = generate_commit_message(analysis)

    # 输出结果
    print(commit_message)


if __name__ == "__main__":
    main()
