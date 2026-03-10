#!/bin/bash

# Git Commit 模板安装脚本
# 用于配置 Git 使用 .gitmessage 作为默认 commit 模板

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_FILE="$SCRIPT_DIR/.gitmessage"

# 检查模板文件是否存在
if [ ! -f "$TEMPLATE_FILE" ]; then
    echo "❌ 错误：找不到模板文件 $TEMPLATE_FILE"
    exit 1
fi

# 复制到用户主目录
echo "📋 安装 Git Commit 模板..."
cp "$TEMPLATE_FILE" "$HOME/.gitmessage"

# 配置 Git 使用模板
git config --global commit.template "$HOME/.gitmessage"

echo "✅ 安装完成！"
echo ""
echo "现在每次执行 'git commit' 时，都会看到这个模板"
echo ""
echo "─────────────────────────────────────"
echo "📝 使用方法"
echo "─────────────────────────────────────"
echo "1. 正常提交代码："
echo "   git add ."
echo "   git commit"
echo ""
echo "2. 会自动打开编辑器显示模板"
echo "3. 按照模板格式填写提交信息"
echo "4. 保存并退出即可完成提交"
echo ""
echo "💡 提示：删除以 # 开头的注释行"
echo ""
echo "如需卸载，运行："
echo "  git config --global --unset commit.template"
echo "  rm ~/.gitmessage"
