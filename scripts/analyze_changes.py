#!/usr/bin/env python3
"""
分析 Git 代码变更
- 变更类型（feat/fix/refactor/docs 等）
- 影响范围（scope）
- 版本升级类型（major/minor/patch）
- 选择合适的 gitmoji
"""

import json
import re
import subprocess
import sys
from pathlib import Path

# 支持直接运行和模块导入
try:
    from . import utils
except ImportError:
    import utils


def run_git_command(cmd):
    """执行 git 命令"""
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


def get_git_diff():
    """获取 git diff 信息"""
    diff = run_git_command("git diff HEAD")
    stat = run_git_command("git diff --stat HEAD")
    status = run_git_command("git status --porcelain")

    return {
        "diff": diff or "",
        "stat": stat or "",
        "status": status or ""
    }


def analyze_change_type(diff_info):
    """
    分析变更类型
    返回：{
        "type": "feat|fix|refactor|docs|style|test|chore",
        "scope": "模块名称",
        "version_bump": "major|minor|patch",
        "emoji": "✨",
        "is_breaking": false
    }
    """
    diff = diff_info["diff"].lower()
    stat = diff_info["stat"].lower()
    status = diff_info["status"]

    # 检测破坏性变更
    is_breaking = (
        "breaking change" in diff or
        "breaking:" in diff or
        "!" in diff or  # Conventional Commits 的 ! 标记
        any("break" in line for line in diff.split("\n")[:20])  # 前20行
    )

    # 解析修改的文件列表
    modified_files = []
    added_files = []
    deleted_files = []

    for line in status.split("\n"):
        if not line.strip():
            continue
        file_status = line[0]
        file_path = line[3:] if len(line) > 3 else line[1:]
        modified_files.append(file_path)

        if file_status == "A":
            added_files.append(file_path)
        elif file_status == "D":
            deleted_files.append(file_path)

    # 智能分析变更类型
    change_type = analyze_change_type_intelligent(
        diff, stat, modified_files, added_files, deleted_files
    )

    # 确定版本升级类型
    if is_breaking:
        version_bump = "major"
    elif change_type == "feat":
        version_bump = "minor"
    else:
        version_bump = "patch"

    # 选择 emoji
    emoji_map_path = Path(__file__).parent.parent / "references" / "gitmoji-map.json"
    with open(emoji_map_path, "r", encoding="utf-8") as f:
        emoji_map = json.load(f)

    emoji = emoji_map.get(change_type, "🔧")
    if is_breaking:
        emoji = emoji_map.get("breaking", "💥")

    # 智能提取 scope
    scope = extract_scope_intelligent(modified_files, added_files, deleted_files)

    return {
        "type": change_type,
        "scope": scope,
        "version_bump": version_bump,
        "emoji": emoji,
        "is_breaking": is_breaking,
        "modified_files": modified_files,
        "added_files": added_files,
        "deleted_files": deleted_files,
        "stat_summary": stat
    }


def analyze_change_type_intelligent(diff, stat, modified_files, added_files, deleted_files):
    """智能分析变更类型"""
    # 预编译正则表达式以提高性能
    file_patterns = {
        "docs": [re.compile(p, re.IGNORECASE) for p in [r"\.md$", r"docs/", r"README", r"CHANGELOG", r"LICENSE"]],
        "test": [re.compile(p, re.IGNORECASE) for p in [r"test", r"spec", r"__tests__", r"\.test\.", r"\.spec\."]],
        "style": [re.compile(p, re.IGNORECASE) for p in [r"\.css$", r"\.scss$", r"\.sass$", r"\.less$", r"style/"]],
        "ci": [re.compile(p, re.IGNORECASE) for p in [r"\.github/", r"\.gitlab-ci\.yml", r"\travis\.yml", r"jenkins"]],
        "build": [re.compile(p, re.IGNORECASE) for p in [r"webpack", r"vite", r"rollup", r"\.babelrc", r"tsconfig"]],
    }

    # 使用 itertools.chain 避免列表拼接
    from itertools import chain
    all_files = chain(modified_files, added_files, deleted_files)

    for change_type, patterns in file_patterns.items():
        for pattern in patterns:
            if any(pattern.search(file) for file in all_files):
                return change_type

    # 优先级 2：检查 diff 内容中的关键词（更智能的匹配）
    content_keywords = {
        "feat": [
            re.compile(r"add\s+\w+\s+function", re.IGNORECASE),
            re.compile(r"implement\s+\w+", re.IGNORECASE),
            re.compile(r"new\s+\w+", re.IGNORECASE),
            re.compile(r"create\s+\w+", re.IGNORECASE),
            re.compile(r"\+\s*class\s+\w+", re.IGNORECASE),
            re.compile(r"\+\s*def\s+\w+", re.IGNORECASE),
            re.compile(r"\+\s*function\s+\w+", re.IGNORECASE)
        ],
        "fix": [
            re.compile(r"fix\s+\w+", re.IGNORECASE),
            re.compile(r"bug\s*\w*\s*fix", re.IGNORECASE),
            re.compile(r"resolve\s+\w+", re.IGNORECASE),
            re.compile(r"patch\s+\w+", re.IGNORECASE),
            re.compile(r"issue\s+\d+", re.IGNORECASE)
        ],
        "refactor": [
            re.compile(r"refactor", re.IGNORECASE),
            re.compile(r"restructure", re.IGNORECASE),
            re.compile(r"reorganize", re.IGNORECASE),
            re.compile(r"extract\s+\w+", re.IGNORECASE),
            re.compile(r"simplify", re.IGNORECASE)
        ],
        "perf": [
            re.compile(r"optimize", re.IGNORECASE),
            re.compile(r"performance", re.IGNORECASE),
            re.compile(r"speed\s+up", re.IGNORECASE),
            re.compile(r"cache", re.IGNORECASE),
            re.compile(r"lazy", re.IGNORECASE)
        ],
        "security": [
            re.compile(r"security", re.IGNORECASE),
            re.compile(r"vulnerability", re.IGNORECASE),
            re.compile(r"xss", re.IGNORECASE),
            re.compile(r"injection", re.IGNORECASE),
            re.compile(r"csrf", re.IGNORECASE)
        ]
    }

    for change_type, patterns in content_keywords.items():
        for pattern in patterns:
            if pattern.search(diff):
                return change_type

    # 优先级 3：检查是否有大量文件删除（可能是清理）
    if len(deleted_files) > len(added_files) * 2:
        return "chore"

    # 优先级 4：检查是否有新增文件（倾向于 feat）
    if len(added_files) > len(modified_files):
        return "feat"

    # 默认返回 chore
    return "chore"


def extract_scope_intelligent(modified_files, added_files, deleted_files):
    """智能提取 scope"""
    if not modified_files and not added_files:
        return ""

    # 使用 itertools.chain 避免列表拼接
    from itertools import chain
    all_files = chain(modified_files, added_files)
    scopes = []

    for file_path in all_files:
        parts = Path(file_path).parts

        # 使用 utils 模块中的常量
        if parts and parts[0] in utils.FileTypes.COMMON_ROOTS:
            if len(parts) > 1:
                scopes.append(parts[1])
        elif parts:
            scopes.append(parts[0])

    # 统计最常见的 scope
    if scopes:
        from collections import Counter
        most_common = Counter(scopes).most_common(1)
        if most_common:
            # 只有当某个 scope 出现超过 50% 时才使用
            scope, count = most_common[0]
            if count >= len(list(all_files)) * 0.5:
                return scope

    return ""


def main():
    """主函数"""
    # 检查是否为 git 仓库
    if not run_git_command("git rev-parse --is-inside-work-tree"):
        print(json.dumps({"error": "不是 Git 仓库"}), file=sys.stderr)
        sys.exit(1)

    # 检查是否有变更
    status = run_git_command("git status --porcelain")
    if not status:
        print(json.dumps({"error": "没有待提交的变更"}), file=sys.stderr)
        sys.exit(1)

    # 获取 diff 信息
    diff_info = get_git_diff()

    # 分析变更类型
    analysis = analyze_change_type(diff_info)

    # 输出 JSON 结果
    print(json.dumps(analysis, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
