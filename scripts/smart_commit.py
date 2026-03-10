#!/usr/bin/env python3
"""
GitHub Smart Commit 主工作流程
实现完整的确认流程
"""

import json
import subprocess
import sys
from pathlib import Path


def run_command(cmd):
    """执行命令并返回输出"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return None


def load_project_config():
    """加载项目配置"""
    script_dir = Path(__file__).parent
    config_script = script_dir / "config.py"

    try:
        result = subprocess.run(
            f"python3 {config_script} load",
            shell=True,
            capture_output=True,
            text=True,
            check=True,
            timeout=5
        )
        # 解析 JSON 输出（跳过第一行"配置级别"）
        lines = result.stdout.strip().split("\n")
        if len(lines) > 1:
            config = json.loads("\n".join(lines[1:]))
            return config
    except Exception as e:
        print(f"警告：加载配置失败，使用默认配置：{e}", file=sys.stderr)

    # 默认配置
    return {
        "language": "en",
        "auto_update_readme": True,
        "auto_update_changelog": True,
        "auto_update_version": True,
        "include_issue_refs": True,
        "max_files_in_commit": 10
    }


def analyze_changes():
    """分析代码变更"""
    script_dir = Path(__file__).parent
    analyze_script = script_dir / "analyze_changes.py"

    output = run_command(f"python3 {analyze_script}")
    if output:
        try:
            return json.loads(output)
        except json.JSONDecodeError:
            return None
    return None


def preview_operations(analysis, config, new_version=None):
    """生成操作预览"""
    preview_lines = []
    preview_lines.append("=" * 60)
    preview_lines.append("📋 GitHub Smart Commit 预览")
    preview_lines.append("=" * 60)
    preview_lines.append("")

    # 1. 变更分析
    preview_lines.append("📊 变更分析：")
    preview_lines.append(f"  类型: {analysis.get('type', 'unknown')}")
    preview_lines.append(f"  范围: {analysis.get('scope', 'N/A') or 'N/A'}")
    preview_lines.append(f"  版本升级: {analysis.get('version_bump', 'patch')}")
    preview_lines.append(f"  破坏性变更: {'是' if analysis.get('is_breaking') else '否'}")
    preview_lines.append("")

    # 2. 文件统计
    added_files = analysis.get('added_files', [])
    modified_files = analysis.get('modified_files', [])
    deleted_files = analysis.get('deleted_files', [])

    preview_lines.append("📁 文件变更：")
    preview_lines.append(f"  新增: {len(added_files)} 个文件")
    preview_lines.append(f"  修改: {len(modified_files)} 个文件")
    preview_lines.append(f"  删除: {len(deleted_files)} 个文件")

    # 显示前 5 个文件
    if added_files or modified_files or deleted_files:
        preview_lines.append("")
        preview_lines.append("  主要文件：")
        for f in (added_files + modified_files)[:5]:
            prefix = "+" if f in added_files else ("-" if f in deleted_files else " ")
            preview_lines.append(f"    {prefix} {f}")

    preview_lines.append("")

    # 3. 将要执行的操作
    preview_lines.append("🔧 将要执行的操作：")

    if new_version and config.get('auto_update_version'):
        preview_lines.append(f"  ✓ 更新版本号: → v{new_version}")

    if config.get('auto_update_readme'):
        preview_lines.append("  ✓ 更新 README.md")

    if config.get('auto_update_changelog'):
        if new_version:
            preview_lines.append(f"  ✓ 更新 CHANGELOG.md (版本 {new_version})")
        else:
            preview_lines.append("  ✓ 更新 CHANGELOG.md")

    preview_lines.append("  ✓ Git add 变更文件")
    preview_lines.append("  ✓ Git commit 提交")
    preview_lines.append("  ✓ Git push 推送")
    preview_lines.append("")

    preview_lines.append("=" * 60)

    return "\n".join(preview_lines)


def generate_commit_message_preview(analysis, config):
    """生成 commit 消息预览"""
    script_dir = Path(__file__).parent
    generate_script = script_dir / "generate_commit.py"

    # 准备输入
    analysis_json = json.dumps(analysis)

    try:
        # 使用 stdin 传递数据
        process = subprocess.Popen(
            ['python3', str(generate_script)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=analysis_json, timeout=10)

        if process.returncode == 0 and stdout:
            return stdout.strip()
        else:
            print(f"警告：生成 commit 消息时出错：{stderr}", file=sys.stderr)
            return None
    except Exception as e:
        print(f"警告：生成 commit 消息失败：{e}", file=sys.stderr)
        return None


def main():
    """主函数"""
    print("🚀 GitHub Smart Commit 启动中...")
    print("")

    # 1. 加载配置
    config = load_project_config()

    # 2. 分析变更
    print("📊 正在分析代码变更...")
    analysis = analyze_changes()

    if not analysis:
        print("❌ 错误：无法分析代码变更", file=sys.stderr)
        sys.exit(1)

    if "error" in analysis:
        print(f"❌ 错误：{analysis['error']}", file=sys.stderr)
        sys.exit(1)

    # 3. 如果需要，更新版本号
    new_version = None
    if config.get('auto_update_version'):
        print("🔢 正在更新版本号...")
        script_dir = Path(__file__).parent
        version_script = script_dir / "update_version.py"

        bump_type = analysis.get('version_bump', 'patch')
        output = run_command(f"python3 {version_script} . {bump_type}")

        if output:
            try:
                version_info = json.loads(output)
                new_version = version_info.get('new_version')
                print(f"  版本号: → v{new_version}")
            except:
                pass

    # 4. 生成 commit 消息
    print("💬 正在生成 commit 消息...")
    commit_message = generate_commit_message_preview(analysis, config)

    if not commit_message:
        print("❌ 错误：无法生成 commit 消息", file=sys.stderr)
        sys.exit(1)

    # 5. 显示预览
    print("")
    print(preview_operations(analysis, config, new_version))
    print("")
    print("💬 Commit 消息预览：")
    print("-" * 60)
    print(commit_message)
    print("-" * 60)
    print("")

    # 6. 这里应该调用 AskUserQuestion，但在脚本模式下我们使用简单的输入
    print("❓ 是否继续执行？")
    print("  [1] 是，执行提交")
    print("  [2] 取消")
    print("  [3] 修改 commit 消息")
    print("")

    # 注意：在实际使用中，这里会由 SKILL.md 中的 AskUserQuestion 接管
    print("✅ 预览完成！在实际使用中，这里会显示确认对话框。")
    print("")
    print("预览数据已保存，可以传递给 SKILL.md 使用：")
    print(json.dumps({
        "analysis": analysis,
        "config": config,
        "new_version": new_version,
        "commit_message": commit_message
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
