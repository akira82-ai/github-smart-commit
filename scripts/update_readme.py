#!/usr/bin/env python3
"""
智能更新 README.md
支持多种风格：赛博朋克、标准格式、Badges、极简格式
"""

import re
import sys
from datetime import datetime
from pathlib import Path


def detect_readme_style(content):
    """检测 README 风格"""
    # 检测赛博朋克风格的特征
    cyberpunk_patterns = [
        r"╔═+╗",  # ASCII 框架
        r"║.*║",
        r"╚═+╝",
        r"系统状态：",
        r"System Status:",
        r"版本：v\d+\.\d+\.\d+",
        r"Version: v\d+\.\d+\.\d+"
    ]

    # 检测标准格式
    standard_patterns = [
        r"^# \w+",  # 有标题
        r"##\s+Version",
        r"##\s+版本",
        r"##\s+Installation",
        r"##\s+安装"
    ]

    # 检测 Badges 格式
    badges_patterns = [
        r"!\[.*\]\(https://img\.shields\.io",  # Shields badges
        r"!\[.*\]\(https://badge\.fury\.io",   # Fury badges
        r"version.*badge",
        r"badge.*version"
    ]

    cyberpunk_score = sum(1 for pattern in cyberpunk_patterns if re.search(pattern, content, re.MULTILINE))
    standard_score = sum(1 for pattern in standard_patterns if re.search(pattern, content, re.MULTILINE))
    badges_score = sum(1 for pattern in badges_patterns if re.search(pattern, content, re.MULTILINE))

    if cyberpunk_score >= 3:
        return "cyberpunk"
    elif badges_score >= 2:
        return "badges"
    elif standard_score >= 2:
        return "standard"
    else:
        return "minimal"


def update_badges_readme(content, new_version, analysis):
    """更新 Badges 格式的 README"""
    updated = content

    # 更新版本号 badges（常见格式）
    # 格式 1: ![version](https://img.shields.io/badge/version-X.X.X-blue)
    updated = re.sub(
        r"(https://img\.shields\.io/badge/version-)[\d.]+",
        f"\\g<1>{new_version}",
        updated
    )

    # 格式 2: ![Version](https://badge.fury.io/gh/user/repo)
    updated = re.sub(
        r"(badge\.fury\.io/[^/]+/)[\d.]+",
        f"\\g<1>{new_version}",
        updated
    )

    # 更新标题中的版本号
    updated = re.sub(
        r"(Version\s*[：:]\s*)v?[\d.]+",
        f"\\1v{new_version}",
        updated,
        flags=re.IGNORECASE
    )

    # 更新日期
    today = datetime.now().strftime("%Y-%m-%d")
    updated = re.sub(
        r"(Last\s+Updated\s*[：:]\s*)\d{4}-\d{2}-\d{2}",
        f"\\1{today}",
        updated,
        flags=re.IGNORECASE
    )

    return updated


def update_standard_readme(content, new_version, analysis):
    """更新标准格式的 README"""
    updated = content

    # 更新版本号部分（常见格式）
    patterns = [
        r"(##?\s*Version\s*[：:]\s*)v?[\d.]+",
        r"(##?\s*版本\s*[：:]\s*)v?[\d.]+",
        r"(##?\s*Current\s+Version\s*[：:]\s*)v?[\d.]+",
        r"(##?\s*当前版本\s*[：:]\s*)v?[\d.]+",
        r"(\*\*Version:\*\*)\s*v?[\d.]+",
        r"(\*\*版本:\*\*)\s*v?[\d.]+"
    ]

    for pattern in patterns:
        updated = re.sub(
            pattern,
            f"\\g<1> v{new_version}",
            updated,
            flags=re.IGNORECASE
        )

    # 更新日期
    today = datetime.now().strftime("%Y-%m-%d")
    date_patterns = [
        r"(##?\s*Last\s+Updated?\s*[：:]\s*)\d{4}-\d{2}-\d{2}",
        r"(##?\s*最后更新\s*[：:]\s*)\d{4}-\d{2}-\d{2}",
        r"(\*\*Last\s+Updated?:\*\*)\s*\d{4}-\d{2}-\d{2}",
        r"(\*\*最后更新:\*\*)\s*\d{4}-\d{2}-\d{2}"
    ]

    for pattern in date_patterns:
        updated = re.sub(
            pattern,
            f"\\g<1>{today}",
            updated,
            flags=re.IGNORECASE
        )

    return updated


def update_minimal_readme(content, new_version, analysis):
    """更新极简格式的 README（只更新明显的版本号和日期）"""
    updated = content

    # 更新明显的版本号模式
    updated = re.sub(
        r"(v?\d+\.\d+\.\d+)",
        f"v{new_version}",
        updated,
        count=1  # 只替换第一个
    )

    # 如果有日期，更新它
    today = datetime.now().strftime("%Y-%m-%d")
    updated = re.sub(
        r"\d{4}-\d{2}-\d{2}",
        today,
        updated,
        count=1
    )

    return updated


def update_cyberpunk_readme(content, new_version, analysis):
    """更新赛博朋克风格的 README"""
    updated = content
    today = datetime.now().strftime("%Y-%m-%d")
    build_date = datetime.now().strftime("%Y%m%d")

    # 1. 更新顶部 ASCII 框架中的版本号
    # 中文版本
    updated = re.sub(
        r"(版本：)v\d+\.\d+\.\d+",
        f"\\1v{new_version}",
        updated
    )
    # 英文版本
    updated = re.sub(
        r"(Version: )v\d+\.\d+\.\d+",
        f"\\1v{new_version}",
        updated
    )

    # 2. 更新构建日期
    # 中文版本
    updated = re.sub(
        r"(构建：)\d{8}",
        f"\\1{build_date}",
        updated
    )
    # 英文版本
    updated = re.sub(
        r"(Build: )\d{8}",
        f"\\1{build_date}",
        updated
    )

    # 3. 更新底部系统信息框中的版本号
    # 中文版本
    updated = re.sub(
        r"(版本\s*[：:]\s*)v?\d+\.\d+\.\d+",
        f"\\1v{new_version}",
        updated
    )

    # 4. 更新最后更新日期
    # 中文版本
    updated = re.sub(
        r"(最后更新[：:]\s*)\d{4}-\d{2}-\d{2}",
        f"\\1{today}",
        updated
    )
    # 英文版本
    updated = re.sub(
        r"(Last Updated[：:]\s*)\d{4}-\d{2}-\d{2}",
        f"\\1{today}",
        updated
    )

    # 5. 如果是新功能，添加到核心模块进度条（可选）
    if analysis.get("type") == "feat":
        # 这部分需要更智能的实现，暂时跳过
        pass

    return updated


def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("Usage: update_readme.py <readme_path> <new_version> [analysis_json]", file=sys.stderr)
        sys.exit(1)

    readme_path = Path(sys.argv[1])
    new_version = sys.argv[2]

    # 读取 analysis（可选）
    analysis = {}
    if len(sys.argv) > 3:
        import json
        try:
            analysis = json.loads(sys.argv[3])
        except json.JSONDecodeError:
            pass

    # 检查 README 是否存在
    if not readme_path.exists():
        print(f"错误：README 文件不存在：{readme_path}", file=sys.stderr)
        sys.exit(1)

    # 读取 README 内容
    content = readme_path.read_text(encoding="utf-8")

    # 检测风格
    style = detect_readme_style(content)

    print(f"检测到 README 风格: {style}", file=sys.stderr)

    # 根据风格选择更新函数
    update_functions = {
        "cyberpunk": update_cyberpunk_readme,
        "badges": update_badges_readme,
        "standard": update_standard_readme,
        "minimal": update_minimal_readme
    }

    update_func = update_functions.get(style)
    if not update_func:
        print(f"警告：不支持的 README 风格 '{style}'，跳过自动更新", file=sys.stderr)
        sys.exit(0)

    # 更新 README
    updated_content = update_func(content, new_version, analysis)

    # 检查是否有变化
    if updated_content == content:
        print("提示：README 内容无需更新", file=sys.stderr)
        sys.exit(0)

    # 写回文件
    readme_path.write_text(updated_content, encoding="utf-8")

    print(f"✓ README 已更新到版本 v{new_version}")
    print(f"  风格: {style}", file=sys.stderr)


if __name__ == "__main__":
    main()
