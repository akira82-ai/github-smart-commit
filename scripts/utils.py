#!/usr/bin/env python3
"""
通用工具函数
"""

import re
from datetime import datetime
from typing import Dict, List, Tuple
from pathlib import Path
import json


# 预编译的正则表达式
class Patterns:
    """常用正则表达式模式（预编译以提高性能）"""

    # 版本号模式
    VERSION_PATTERNS = [
        re.compile(r"(Version\s*[：:]\s*)v?([\d.]+)", re.IGNORECASE),
        re.compile(r"(##?\s*Version\s*[：:]\s*)v?([\d.]+)", re.IGNORECASE),
        re.compile(r"(##?\s*Current\s+Version\s*[：:]\s*)v?([\d.]+)", re.IGNORECASE),
        re.compile(r"(##?\s*当前版本\s*[：:]\s*)v?([\d.]+)", re.IGNORECASE),
        re.compile(r"(\*\*Version:\*\*)\s*v?([\d.]+)", re.IGNORECASE),
        re.compile(r"(\*\*版本:\*\*)\s*v?([\d.]+)", re.IGNORECASE),
        re.compile(r"(版本[：:]\s*)v?([\d.]+)", re.IGNORECASE),
        re.compile(r"(https://img\.shields\.io/badge/version-)([\d.]+)", re.IGNORECASE),
        re.compile(r"(badge\.fury\.io/[^/]+/)([\d.]+)", re.IGNORECASE),
    ]

    # 日期模式
    DATE_PATTERNS = [
        re.compile(r"(##?\s*Last\s+Updated?\s*[：:]\s*)(\d{4}-\d{2}-\d{2})", re.IGNORECASE),
        re.compile(r"(##?\s*最后更新\s*[：:]\s*)(\d{4}-\d{2}-\d{2})", re.IGNORECASE),
        re.compile(r"(\*\*Last\s+Updated?:\*\*)\s*(\d{4}-\d{2}-\d{2})", re.IGNORECASE),
        re.compile(r"(\*\*最后更新:\*\*)\s*(\d{4}-\d{2}-\d{2})", re.IGNORECASE),
        re.compile(r"(最后更新[：:]\s*)(\d{4}-\d{2}-\d{2})", re.IGNORECASE),
        re.compile(r"(Last Updated[：:]\s*)(\d{4}-\d{2}-\d{2})", re.IGNORECASE),
    ]

    # README 风格检测（预编译）
    CYBERPUNK_PATTERNS = [
        re.compile(r"╔═+╗"),
        re.compile(r"║.*║"),
        re.compile(r"╚═+╝"),
        re.compile(r"系统状态："),
        re.compile(r"System Status:"),
        re.compile(r"版本：v\d+\.\d+\.\d+"),
        re.compile(r"Version: v\d+\.\d+\.\d+")
    ]

    STANDARD_PATTERNS = [
        re.compile(r"^# \w+"),
        re.compile(r"##\s+Version"),
        re.compile(r"##\s+版本"),
        re.compile(r"##\s+Installation"),
        re.compile(r"##\s+安装")
    ]

    BADGES_PATTERNS = [
        re.compile(r"!\[.*\]\(https://img\.shields\.io"),
        re.compile(r"!\[.*\]\(https://badge\.fury\.io"),
        re.compile(r"version.*badge"),
        re.compile(r"badge.*version")
    ]


# 文件类型常量
class FileTypes:
    """文件扩展名和路径常量"""

    CONFIG_EXTENSIONS = (".json", ".yaml", ".yml", ".toml", ".md")
    COMMON_ROOTS = ["src", "lib", "app", "dist", "build", "test", "tests"]
    IGNORED_PARTS = ["src", "lib", "app", "index", "main"]


def get_today() -> str:
    """获取今天的日期字符串 (YYYY-MM-DD)"""
    return datetime.now().strftime("%Y-%m-%d")


def get_build_date() -> str:
    """获取构建日期字符串 (YYYYMMDD)"""
    return datetime.now().strftime("%Y%m%d")


def extract_files_from_analysis(analysis: Dict) -> Tuple[List[str], List[str], List[str]]:
    """
    从分析结果中提取文件列表

    Args:
        analysis: 分析结果字典

    Returns:
        (modified_files, added_files, deleted_files)
    """
    return (
        analysis.get("modified_files", []),
        analysis.get("added_files", []),
        analysis.get("deleted_files", [])
    )


def replace_version(content: str, new_version: str) -> str:
    """
    在文本中替换版本号

    Args:
        content: 原始内容
        new_version: 新版本号

    Returns:
        替换后的内容
    """
    updated = content

    for pattern in Patterns.VERSION_PATTERNS:
        updated = pattern.sub(
            lambda m: f"{m.group(1)}{new_version}",
            updated
        )

    return updated


def replace_date(content: str, new_date: str = None) -> str:
    """
    在文本中替换日期

    Args:
        content: 原始内容
        new_date: 新日期字符串，默认为今天

    Returns:
        替换后的内容
    """
    if new_date is None:
        new_date = get_today()

    updated = content

    for pattern in Patterns.DATE_PATTERNS:
        updated = pattern.sub(
            lambda m: f"{m.group(1)}{new_date}",
            updated
        )

    return updated


def sanitize_filename(filename: str) -> str:
    """
    清理文件名：移除扩展名（除非是配置文件）

    Args:
        filename: 文件名

    Returns:
        清理后的文件名
    """
    if "." in filename and not filename.endswith(FileTypes.CONFIG_EXTENSIONS):
        return filename.rsplit(".", 1)[0]
    return filename


def extract_target_from_files(files: List[str]) -> str:
    """
    从文件列表中提取主要目标

    Args:
        files: 文件路径列表

    Returns:
        提取的目标名称
    """
    if not files:
        return ""

    main_file = files[0]

    # 如果是路径，提取最后部分
    if "/" in main_file:
        parts = main_file.split("/")
        for part in reversed(parts):
            if part and part not in FileTypes.IGNORED_PARTS:
                target = part
                break
        else:
            target = parts[-1] if parts else main_file
    else:
        target = main_file

    return sanitize_filename(target)


def read_json_file(path: Path) -> dict:
    """
    读取 JSON 文件

    Args:
        path: 文件路径

    Returns:
        JSON 数据字典
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json_file(path: Path, data: dict, indent: int = 2) -> None:
    """
    写入 JSON 文件

    Args:
        path: 文件路径
        data: 要写入的数据
        indent: 缩进空格数
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)