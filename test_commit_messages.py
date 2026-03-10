#!/usr/bin/env python3
"""
测试 commit 消息生成效果
展示不同类型的 commit 消息格式
"""

import json
import subprocess
import sys


def test_commit_message(test_name, analysis):
    """测试单个 commit 消息"""
    print(f"\n{'='*60}")
    print(f"测试: {test_name}")
    print('='*60)

    result = subprocess.run(
        ['python3', 'scripts/generate_commit.py'],
        input=json.dumps(analysis),
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"错误: {result.stderr}")
        return False

    return True


def main():
    """主测试函数"""
    print("🧪 GitHub Smart Commit - 消息生成测试")
    print("使用中文 Conventional Commits 模板\n")

    tests = [
        ("功能开发 - 添加认证", {
            "type": "feat",
            "scope": "auth",
            "emoji": "✨",
            "is_breaking": False,
            "modified_files": ["src/auth/oauth.py"],
            "added_files": ["src/auth/providers/google.py", "src/auth/session.py"],
            "deleted_files": []
        }),

        ("Bug 修复 - API 问题", {
            "type": "fix",
            "scope": "api",
            "emoji": "🐛",
            "is_breaking": False,
            "modified_files": ["src/api/user.py"],
            "added_files": [],
            "deleted_files": []
        }),

        ("重构 - 简化架构", {
            "type": "refactor",
            "scope": "core",
            "emoji": "♻️",
            "is_breaking": False,
            "modified_files": ["src/core/utils.py", "src/core/helpers.py"],
            "added_files": ["src/core/common.py"],
            "deleted_files": []
        }),

        ("文档更新", {
            "type": "docs",
            "scope": "",
            "emoji": "📝",
            "is_breaking": False,
            "modified_files": ["README.md", "docs/api.md"],
            "added_files": [],
            "deleted_files": []
        }),

        ("性能优化", {
            "type": "perf",
            "scope": "database",
            "emoji": "⚡",
            "is_breaking": False,
            "modified_files": ["src/db/query.py"],
            "added_files": [],
            "deleted_files": []
        }),

        ("破坏性变更", {
            "type": "feat",
            "scope": "api",
            "emoji": "✨",
            "is_breaking": True,
            "modified_files": ["src/api/response.py"],
            "added_files": [],
            "deleted_files": ["src/api/legacy.py"]
        }),

        ("测试添加", {
            "type": "test",
            "scope": "auth",
            "emoji": "✅",
            "is_breaking": False,
            "modified_files": [],
            "added_files": ["tests/test_auth.py", "tests/test_oauth.py"],
            "deleted_files": []
        }),

        ("构建更新", {
            "type": "build",
            "scope": "",
            "emoji": "📦",
            "is_breaking": False,
            "modified_files": ["package.json", "webpack.config.js"],
            "added_files": [],
            "deleted_files": []
        })
    ]

    passed = 0
    failed = 0

    for test_name, analysis in tests:
        if test_commit_message(test_name, analysis):
            passed += 1
        else:
            failed += 1

    print(f"\n{'='*60}")
    print("测试总结")
    print('='*60)
    print(f"✅ 通过: {passed}")
    print(f"❌ 失败: {failed}")
    print(f"总计: {passed + failed}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
