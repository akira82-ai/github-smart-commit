#!/usr/bin/env python3
"""
配置管理系统
支持项目级和全局配置
"""

import json
import sys
from pathlib import Path


DEFAULT_CONFIG = {
    "language": "en",  # en 或 zh
    "auto_update_readme": True,
    "auto_update_changelog": True,
    "auto_update_version": True,
    "include_issue_refs": True,
    "max_files_in_commit": 10,
    "commit_message_template": None,  # 自定义模板
    "changelog_format": "keep-a-changelog",  # keep-a-changelog 或 custom
    "readme_style": "auto",  # auto, cyberpunk, standard, badges, minimal
    "version_scheme": "semver",  # semver 或 custom
    "pre_commit_hooks": [],  # 预提交钩子列表
    "post_commit_hooks": []  # 后提交钩子列表
}


def find_config_file(project_dir=None):
    """
    查找配置文件
    优先级：项目级 > 全局级 > 默认配置
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # 查找项目级配置
    project_config = project_dir / ".smart-commit.json"
    if project_config.exists():
        return project_config, "project"

    # 查找全局配置
    home_config = Path.home() / ".smart-commit.json"
    if home_config.exists():
        return home_config, "global"

    return None, "default"


def load_config(project_dir=None):
    """
    加载配置
    返回合并后的配置字典
    """
    config_file, level = find_config_file(project_dir)

    if level == "default":
        return DEFAULT_CONFIG.copy(), "default"

    try:
        with open(config_file, "r", encoding="utf-8") as f:
            user_config = json.load(f)

        # 合并配置（用户配置覆盖默认配置）
        merged_config = DEFAULT_CONFIG.copy()
        merged_config.update(user_config)

        return merged_config, level

    except json.JSONDecodeError as e:
        print(f"错误：配置文件格式无效：{e}", file=sys.stderr)
        return DEFAULT_CONFIG.copy(), "error"


def create_config_template(output_path=None):
    """
    创建配置文件模板
    """
    template = {
        "$schema": "https://raw.githubusercontent.com/username/github-smart-commit/main/config-schema.json",
        "_comment": "GitHub Smart Commit 配置文件",
        "language": "en",
        "auto_update_readme": True,
        "auto_update_changelog": True,
        "auto_update_version": True,
        "include_issue_refs": True,
        "max_files_in_commit": 10,
        "commit_message_template": None,
        "changelog_format": "keep-a-changelog",
        "readme_style": "auto",
        "version_scheme": "semver",
        "pre_commit_hooks": [],
        "post_commit_hooks": []
    }

    if output_path:
        output_path = Path(output_path)
    else:
        output_path = Path.cwd() / ".smart-commit.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(template, f, indent=2, ensure_ascii=False)
        f.write("\n")

    return output_path


def validate_config(config):
    """
    验证配置的有效性
    返回 (is_valid, errors)
    """
    errors = []

    # 验证 language
    if config.get("language") not in ["en", "zh"]:
        errors.append("language 必须是 'en' 或 'zh'")

    # 验证布尔值
    bool_keys = [
        "auto_update_readme",
        "auto_update_changelog",
        "auto_update_version",
        "include_issue_refs"
    ]
    for key in bool_keys:
        if key in config and not isinstance(config[key], bool):
            errors.append(f"{key} 必须是布尔值")

    # 验证数字
    if "max_files_in_commit" in config:
        if not isinstance(config["max_files_in_commit"], int) or config["max_files_in_commit"] < 1:
            errors.append("max_files_in_commit 必须是正整数")

    # 验证 changelog_format
    if config.get("changelog_format") not in ["keep-a-changelog", "custom"]:
        errors.append("changelog_format 必须是 'keep-a-changelog' 或 'custom'")

    # 验证 readme_style
    valid_styles = ["auto", "cyberpunk", "standard", "badges", "minimal"]
    if config.get("readme_style") not in valid_styles:
        errors.append(f"readme_style 必须是以下之一：{', '.join(valid_styles)}")

    # 验证 version_scheme
    if config.get("version_scheme") not in ["semver", "custom"]:
        errors.append("version_scheme 必须是 'semver' 或 'custom'")

    # 验证钩子列表
    for key in ["pre_commit_hooks", "post_commit_hooks"]:
        if key in config and not isinstance(config[key], list):
            errors.append(f"{key} 必须是列表")

    return len(errors) == 0, errors


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("Usage: config.py <command> [args]", file=sys.stderr)
        print("Commands:", file=sys.stderr)
        print("  init [path]     创建配置文件模板", file=sys.stderr)
        print("  load [path]     加载并显示配置", file=sys.stderr)
        print("  validate [path] 验证配置文件", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        config_path = create_config_template(output_path)
        print(f"✓ 配置文件已创建：{config_path}")

    elif command == "load":
        project_dir = sys.argv[2] if len(sys.argv) > 2 else None
        config, level = load_config(project_dir)
        print(f"配置级别: {level}")
        print(json.dumps(config, indent=2, ensure_ascii=False))

    elif command == "validate":
        config_path = sys.argv[2] if len(sys.argv) > 2 else None
        if config_path:
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
        else:
            config, _ = load_config()

        is_valid, errors = validate_config(config)
        if is_valid:
            print("✓ 配置文件有效")
        else:
            print("✗ 配置文件无效：", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
            sys.exit(1)

    else:
        print(f"未知命令：{command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
