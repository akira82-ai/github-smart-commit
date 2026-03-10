#!/usr/bin/env python3
"""
交互式 Commit 消息编辑器
"""

import json
import re
import sys
import tempfile
from pathlib import Path


def validate_commit_message(message):
    """
    验证 commit 消息格式
    返回 (is_valid, warnings)
    """
    warnings = []

    # 检查是否为空
    if not message or not message.strip():
        return False, ["Commit 消息不能为空"]

    lines = message.strip().split("\n")
    subject = lines[0].strip()

    # 检查 subject 长度
    if len(subject) > 72:
        warnings.append(f"Subject 行过长（{len(subject)} 字符），建议不超过 72 字符")

    # 检查是否有 conventional commit 格式
    conventional_pattern = r"^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\(.+\))?\!?:"
    if not re.match(conventional_pattern, subject):
        warnings.append("建议使用 Conventional Commits 格式（如 feat: add feature）")

    # 检查是否以句号结尾
    if subject.endswith("."):
        warnings.append("Subject 行不应以句号结尾")

    # 检查空行分隔
    if len(lines) > 1 and lines[1].strip():
        warnings.append("Subject 和 body 之间应该有空行分隔")

    return True, warnings


def format_commit_message_preview(message):
    """格式化 commit 消息预览"""
    lines = message.strip().split("\n")

    preview = []
    preview.append("┌" + "─" * 76 + "┐")

    for i, line in enumerate(lines[:20]):  # 最多显示 20 行
        # 截断过长的行
        display_line = line[:76] if len(line) > 76 else line
        preview.append("│ " + display_line.ljust(76) + " │")

    if len(lines) > 20:
        preview.append("│ " + "... (更多内容)".ljust(76) + " │")

    preview.append("└" + "─" * 76 + "┘")

    return "\n".join(preview)


def apply_template(template, analysis):
    """应用模板变量替换"""
    if not template:
        return None

    # 可用的变量
    variables = {
        "{{type}}": analysis.get("type", "chore"),
        "{{scope}}": analysis.get("scope", ""),
        "{{emoji}}": analysis.get("emoji", "🔧"),
        "{{version}}": analysis.get("new_version", ""),
        "{{description}}": "Code updates"
    }

    result = template
    for key, value in variables.items():
        result = result.replace(key, str(value))

    return result


def interactive_editor(initial_message, analysis=None):
    """
    交互式编辑器
    返回编辑后的消息
    """
    print("\n" + "=" * 78)
    print("✏️  交互式 Commit 消息编辑器")
    print("=" * 78)
    print("\n当前 Commit 消息：")
    print(format_commit_message_preview(initial_message))
    print("")

    # 验证当前消息
    is_valid, warnings = validate_commit_message(initial_message)
    if warnings:
        print("⚠️  警告：")
        for warning in warnings:
            print(f"  - {warning}")
        print("")

    # 显示选项
    while True:
        print("\n可用操作：")
        print("  [1] 保持原消息")
        print("  [2] 在终端编辑消息")
        print("  [3] 使用自定义模板")
        print("  [4] 快速修改 subject 行")
        print("  [5] 验证并确认")
        print("")

        try:
            choice = input("请选择操作 [1-5]: ").strip()

            if choice == "1":
                return initial_message

            elif choice == "2":
                # 使用临时文件和系统编辑器
                with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
                    f.write(initial_message)
                    temp_path = f.name

                print(f"\n📝 打开编辑器: {temp_path}")
                print("   保存并关闭编辑器以继续...\n")

                # 尝试使用系统编辑器
                editor = Path.home() / ".smart-commit-editor"
                import os
                editor_cmd = os.environ.get('EDITOR', 'nano')

                try:
                    import subprocess
                    subprocess.call([editor_cmd, temp_path])
                    edited_message = Path(temp_path).read_text(encoding='utf-8')
                    Path(temp_path).unlink()  # 删除临时文件

                    print("\n✏️  编辑后的消息：")
                    print(format_commit_message_preview(edited_message))
                    initial_message = edited_message
                except Exception as e:
                    print(f"错误：无法打开编辑器：{e}", file=sys.stderr)
                    if Path(temp_path).exists():
                        Path(temp_path).unlink()

            elif choice == "3":
                template = input("请输入模板（使用 {{type}}, {{scope}}, {{emoji}} 等变量）: ").strip()
                if template:
                    new_message = apply_template(template, analysis or {})
                    if new_message:
                        print(f"\n应用模板后的消息：")
                        print(format_commit_message_preview(new_message))
                        initial_message = new_message

            elif choice == "4":
                current_subject = initial_message.split("\n")[0]
                new_subject = input(f"当前 Subject: {current_subject}\n新的 Subject: ").strip()
                if new_subject:
                    lines = initial_message.split("\n")
                    lines[0] = new_subject
                    initial_message = "\n".join(lines)
                    print(f"\n更新后的消息：")
                    print(format_commit_message_preview(initial_message))

            elif choice == "5":
                is_valid, warnings = validate_commit_message(initial_message)
                if is_valid:
                    if warnings:
                        print("\n⚠️  仍有警告：")
                        for warning in warnings:
                            print(f"  - {warning}")
                        confirm = input("\n是否仍要使用此消息？(y/N): ").strip().lower()
                        if confirm == 'y':
                            return initial_message
                    else:
                        print("\n✅ Commit 消息格式正确！")
                        return initial_message
                else:
                    print("\n❌ Commit 消息无效，请继续编辑")

        except KeyboardInterrupt:
            print("\n\n操作已取消")
            return None
        except Exception as e:
            print(f"\n错误：{e}", file=sys.stderr)


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("Usage: edit_commit.py <commit_message> [analysis_json]", file=sys.stderr)
        print("\n或者：", file=sys.stderr)
        print("  echo <commit_message> | edit_commit.py", file=sys.stderr)
        sys.exit(1)

    # 读取初始消息
    initial_message = sys.argv[1]

    # 读取 analysis（可选）
    analysis = None
    if len(sys.argv) > 2:
        try:
            analysis = json.loads(sys.argv[2])
        except json.JSONDecodeError:
            pass

    # 启动交互式编辑器
    final_message = interactive_editor(initial_message, analysis)

    if final_message:
        print("\n" + "=" * 78)
        print("✅ 最终 Commit 消息：")
        print("=" * 78)
        print(final_message)
        print("=" * 78)
    else:
        print("\n❌ 编辑已取消", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
