#!/usr/bin/env python3
"""
生成美观的 Commit 消息
格式：<emoji> <type>(<scope>): <subject>
"""

import json
import sys

from . import i18n
from . import utils


def generate_commit_message(analysis, custom_message=None, language="zh"):
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
        return custom_message

    emoji = analysis.get("emoji", "🔧")
    change_type = analysis.get("type", "chore")
    scope = analysis.get("scope", "")
    is_breaking = analysis.get("is_breaking", False)

    # 生成 subject
    subject = generate_smart_subject(analysis, emoji, change_type, scope, is_breaking, language)

    # 构建 body
    body_parts = []

    # 添加详细变更描述
    change_description = generate_change_description(analysis, language)
    if change_description:
        body_parts.append(change_description)
        body_parts.append("")

    # 添加修改的文件列表（精简版）
    modified_files, added_files, deleted_files = utils.extract_files_from_analysis(analysis)

    if modified_files or added_files or deleted_files:
        header = i18n.get_text(i18n.FILE_STATS, language, "modified_files_header")
        body_parts.append(header)
        for file in modified_files[:8]:
            body_parts.append(f"  {file}")
        for file in added_files[:5]:
            body_parts.append(f"  + {file}")
        for file in deleted_files[:3]:
            body_parts.append(f"  - {file}")

        total_files = len(modified_files) + len(added_files) + len(deleted_files)
        shown_files = min(8, len(modified_files)) + min(5, len(added_files)) + min(3, len(deleted_files))
        if total_files > shown_files:
            more_text = i18n.get_text(i18n.FILE_STATS, language, "more_files", count=total_files - shown_files)
            body_parts.append(more_text)
        body_parts.append("")

    # 构建 footer
    footer_parts = []

    if is_breaking:
        warning = i18n.get_text(i18n.BREAKING_WARNING, language, "breaking")
        footer_parts.append(warning)
        footer_parts.append("")

    # Claude 署名
    footer_parts.append("Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>")

    # 组合完整消息
    commit_message = subject
    if body_parts:
        commit_message += "\n\n" + "\n".join(body_parts)
    if footer_parts:
        commit_message += "\n" + "\n".join(footer_parts)

    return commit_message


def generate_smart_subject(analysis, emoji, change_type, scope, is_breaking, language):
    """智能生成 subject"""
    action = i18n.get_text(i18n.TYPE_DESCRIPTIONS, language, change_type, "Update")

    modified_files, added_files, deleted_files = utils.extract_files_from_analysis(analysis)

    all_files = modified_files + added_files + deleted_files
    target = utils.extract_target_from_files(all_files) if all_files else ""

    # 构建 subject
    if scope and target:
        subject = f"{emoji} {change_type}({scope}): {action} {target}"
    elif scope:
        subject = f"{emoji} {change_type}({scope}): {action}"
    elif target:
        subject = f"{emoji} {change_type}: {action} {target}"
    else:
        subject = f"{emoji} {change_type}: {action.lower()}"

    if is_breaking:
        subject += " !"

    return subject


def generate_change_description(analysis, language):
    """生成变更描述"""
    modified_files, added_files, deleted_files = utils.extract_files_from_analysis(analysis)

    if not modified_files and not added_files and not deleted_files:
        return ""

    lines = []

    if added_files:
        lines.append(i18n.get_text(i18n.FILE_STATS, language, "added", count=len(added_files)))
    if deleted_files:
        lines.append(i18n.get_text(i18n.FILE_STATS, language, "deleted", count=len(deleted_files)))
    if modified_files:
        lines.append(i18n.get_text(i18n.FILE_STATS, language, "modified", count=len(modified_files)))

    return "\n".join(lines)


def main():
    """主函数"""
    try:
        analysis = json.load(sys.stdin)
    except json.JSONDecodeError:
        print(json.dumps({"error": "无效的 JSON 输入"}), file=sys.stderr)
        sys.exit(1)

    commit_message = generate_commit_message(analysis)
    print(commit_message)


if __name__ == "__main__":
    main()
