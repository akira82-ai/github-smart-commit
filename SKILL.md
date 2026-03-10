---
name: github-smart-commit
description: |
  智能 GitHub 提交助手。当用户说"提交 GitHub"、"push to github"、"提交代码"、"commit and push"、"推送到 GitHub"、"上传代码"、"sync to github"时自动触发。

  自动分析代码变更，智能更新 README.md 和版本号，生成美观的 Conventional Commits 格式提交消息（带 emoji），并在用户确认后提交推送。

  功能完整：
  - 加载项目配置（支持 .smart-commit.json）
  - 分析代码变更（调用 analyze_changes.py）
  - 检查并更新 README.md（调用 update_readme.py）
  - 检查并更新版本号（调用 update_version.py）
  - 提供 commit 消息模板选择
  - 生成 commit 消息（调用 generate_commit.py）
  - 显示完整预览
  - 使用 AskUserQuestion 请求确认
  - 执行 git add、commit、push
version: 2.0.0
allowed-tools: Bash, Read, AskUserQuestion
author: Claude Code
---

# 🚀 GitHub 智能提交助手

## 核心优势

| 特性 | 说明 |
|-----|------|
| 🤖 智能分析 | 自动分析代码变更类型和影响范围 |
| 📝 文档更新 | 智能更新 README.md 版本号和日期 |
| 🔢 版本管理 | 自动更新项目版本号（支持多种项目类型）|
| 💬 美观消息 | 生成 Conventional Commits + Gitmoji 格式 |
| ✅ 确认流程 | 显示完整预览，用户确认后执行 |
| 🌐 多语言 | 支持中英文双语 |
| 🎨 模板选择 | 支持多种 commit 消息模板 |
| ⚙️ 配置支持 | 支持项目级和全局配置 |

## 触发短语

**中文**：
- "提交 GitHub"
- "提交代码"
- "推送到 GitHub"
- "上传代码"
- "同步到 GitHub"

**英文**：
- "push to github"
- "commit and push"
- "sync to github"
- "upload code"
- "submit to github"

## 执行流程

### 步骤 1：环境检查

检查 Git 仓库状态：

```bash
# 检查是否为 git 仓库
git rev-parse --is-inside-work-tree

# 检查是否有待提交的变更
git status --porcelain

# 检查大文件（> 10MB）
find . -type f -size +10M -not -path "./.git/*"
```

**错误处理**：
- 如果不是 Git 仓库 → 提示用户初始化 git，结束技能
- 如果没有变更 → 提示工作区干净，结束技能
- 如果发现大文件 → 警告并建议使用 Git LFS，询问是否继续

### 步骤 2：加载配置

加载项目配置（按优先级）：

```bash
# 项目级配置
if [ -f ".smart-commit.json" ]; then
    config_file=".smart-commit.json"
    config_level="project"
# 全局配置
elif [ -f "$HOME/.smart-commit.json" ]; then
    config_file="$HOME/.smart-commit.json"
    config_level="global"
# 默认配置
else
    config_level="default"
fi
```

**默认配置**：
```json
{
  "language": "en",
  "auto_update_readme": true,
  "auto_update_version": true,
  "auto_update_changelog": false,
  "always_show_template_choice": true,
  "commit_message_template": null,
  "readme_style": "auto",
  "version_scheme": "semver",
  "include_issue_refs": true,
  "max_files_in_commit": 10
}
```

使用 Bash 命令合并配置（使用 jq 工具）：

```bash
if [ "$config_level" != "default" ]; then
    # 读取用户配置并合并默认值
    config=$(jq -s '.[0] * .[1]' <<< "{}" "$config_file")
else
    # 使用默认配置
    config='{"language":"en","auto_update_readme":true,"auto_update_version":true,"auto_update_changelog":false,"always_show_template_choice":true,"commit_message_template":null}'
fi
```

### 步骤 3：分析代码变更

运行分析脚本：

```bash
python3 ~/.claude/skills/github-smart-commit/scripts/analyze_changes.py
```

**输出**（JSON）：
```json
{
  "type": "feat",
  "scope": "auth",
  "version_bump": "minor",
  "emoji": "✨",
  "is_breaking": false,
  "modified_files": ["src/auth/oauth.py"],
  "added_files": ["src/auth/providers/google.py"],
  "deleted_files": [],
  "stat_summary": " 1 file changed, 20 insertions(+)"
}
```

**保存结果到变量**：
```bash
analysis=$(python3 ~/.claude/skills/github-smart-commit/scripts/analyze_changes.py)

# 提取关键字段
change_type=$(echo "$analysis" | jq -r '.type')
scope=$(echo "$analysis" | jq -r '.scope')
version_bump=$(echo "$analysis" | jq -r '.version_bump')
emoji=$(echo "$analysis" | jq -r '.emoji')
is_breaking=$(echo "$analysis" | jq -r '.is_breaking')
```

### 步骤 4：检查并更新 README.md

**条件**：
- README.md 文件存在
- 配置中 `auto_update_readme` 不为 `false`

**执行**：
```bash
# 检查 README.md 是否存在
if [ -f "README.md" ] && [ "$(echo "$config" | jq -r '.auto_update_readme')" != "false" ]; then
    # 获取当前版本号
    if [ -f "package.json" ]; then
        current_version=$(cat package.json | jq -r '.version')
    elif [ -f "pyproject.toml" ]; then
        current_version=$(grep -oP 'version\s*=\s*"\K[^"]+' pyproject.toml)
    else
        current_version="1.0.0"
    fi

    # 计算新版本号
    if [ "$version_bump" == "major" ]; then
        new_version=$(echo "$current_version" | awk -F. '{print $1+1".0.0"}')
    elif [ "$version_bump" == "minor" ]; then
        new_version=$(echo "$current_version" | awk -F. '{print $1"."$2+1".0"}')
    else
        new_version=$(echo "$current_version" | awk -F. '{print $1"."$2"."$3+1}')
    fi

    # 更新 README
    python3 ~/.claude/skills/github-smart-commit/scripts/update_readme.py README.md "$new_version" "$analysis"

    echo "✓ README.md 已更新到版本 v$new_version"
fi
```

**错误处理**：
- 如果 README 格式不支持 → 输出警告，跳过更新
- 如果更新失败 → 输出错误信息，询问是否继续

### 步骤 5：检查并更新版本号

**条件**：
- 配置中 `auto_update_version` 不为 `false`

**执行**：
```bash
if [ "$(echo "$config" | jq -r '.auto_update_version')" != "false" ]; then
    # 获取项目根目录
    project_dir=$(git rev-parse --show-toplevel)

    # 调用更新脚本
    version_update=$(python3 ~/.claude/skills/github-smart-commit/scripts/update_version.py "$project_dir" "$version_bump")

    old_version=$(echo "$version_update" | jq -r '.old_version')
    new_version=$(echo "$version_update" | jq -r '.new_version')
    project_type=$(echo "$version_update" | jq -r '.project_type')

    echo "✓ 版本号已更新: $old_version → $new_version ($project_type)"
fi
```

**错误处理**：
- 如果无法识别项目类型 → 输出警告，跳过更新
- 如果更新失败 → 输出错误信息，询问是否继续

### 步骤 6：选择 Commit 消息模板

**条件**：
- 配置中 `always_show_template_choice` 不为 `false`，或
- 用户明确要求选择模板

**使用 AskUserQuestion 提供选项**：

```python
AskUserQuestion(
    questions=[{
        "question": "请选择 commit 消息模板：",
        "header": "模板选择",
        "multiSelect": false,
        "options": [
            {
                "label": "智能生成（推荐）",
                "description": "基于代码分析自动生成完整消息（包含文件列表和变更说明）"
            },
            {
                "label": "简洁模式",
                "description": "只有 type 和 subject，无 body（适合快速提交）"
            },
            {
                "label": "详细模式",
                "description": "包含完整的文件列表和变更说明（适合重要更新）"
            },
            {
                "label": "手动编辑",
                "description": "在编辑器中打开自定义编辑"
            }
        ]
    }]
)
```

**模板说明**：

1. **智能生成（默认）**：
```
<emoji> <type>(<scope>): <subject>

<body>

<files>

Co-Authored-By: Claude Sonnet 4.6 (1M context) <noreply@anthropic.com>
```

2. **简洁模式**：
```
<emoji> <type>(<scope>): <subject>
```

3. **详细模式**：
```
<emoji> <type>(<scope>): <subject>

## 变更详情
- 新增 X 个文件
- 修改 Y 个文件
- 删除 Z 个文件

## 完整文件列表
<all_files>

Co-Authored-By: Claude Sonnet 4.6 (1M context) <noreply@anthropic.com>
```

### 步骤 7：生成 Commit 消息

**基础消息生成**：

```bash
# 生成基础消息
commit_message=$(echo "$analysis" | python3 ~/.claude/skills/github-smart-commit/scripts/generate_commit.py)

# 根据模板选项调整
case $template_choice in
    1)  # 智能生成（完整）
        # 使用 generate_commit.py 的完整输出
        ;;
    2)  # 简洁模式
        # 只保留 subject 行
        commit_message=$(echo "$commit_message" | head -1)
        ;;
    3)  # 详细模式
        # 包含更多文件详情（使用完整输出）
        ;;
    4)  # 手动编辑
        # 打开编辑器
        temp_file=$(mktemp)
        echo "$commit_message" > "$temp_file"
        ${EDITOR:-vim} "$temp_file"
        commit_message=$(cat "$temp_file")
        rm "$temp_file"
        ;;
esac
```

**自定义模板支持**：

如果配置中指定了 `commit_message_template`，使用自定义模板：

```bash
custom_template=$(echo "$config" | jq -r '.commit_message_template')
if [ "$custom_template" != "null" ] && [ -n "$custom_template" ]; then
    # 使用自定义模板
    commit_message=$(eval echo "$custom_template")
fi
```

### 步骤 8：显示完整预览

**展示内容**：

```bash
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 变更统计"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 变更类型
echo "类型: $emoji $change_type"
if [ -n "$scope" ]; then
    echo "范围: $scope"
fi

# 版本升级
echo "版本升级: $version_bump"
if [ "$is_breaking" == "true" ]; then
    echo "⚠️  破坏性变更"
fi

# 文件统计
modified_count=$(echo "$analysis" | jq -r '.modified_files | length')
added_count=$(echo "$analysis" | jq -r '.added_files | length')
deleted_count=$(echo "$analysis" | jq -r '.deleted_files | length')

echo "文件变更: +$added_count ~$modified_count -$deleted_count"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📝 Commit 消息预览"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "$commit_message"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📄 将要更新的文件"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 显示将要提交的文件
git status --short

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔧 将要执行的操作"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1. git add ."
current_branch=$(git branch --show-current)
echo "2. git commit -m <commit_message>"
echo "3. git push origin $current_branch"
echo ""
```

### 步骤 9：请求用户确认

**使用 AskUserQuestion 提供选项**：

```python
AskUserQuestion(
    questions=[{
        "question": "是否执行提交和推送？",
        "header": "确认操作",
        "multiSelect": false,
        "options": [
            {
                "label": "确认提交",
                "description": "执行完整的 add、commit、push 操作"
            },
            {
                "label": "修改消息",
                "description": "重新编辑 commit 消息"
            },
            {
                "label": "更改模板",
                "description": "重新选择 commit 消息模板"
            },
            {
                "label": "取消操作",
                "description": "取消本次提交，保留所有变更"
            }
        ]
    }]
)
```

### 步骤 10：执行 Git 操作

**根据用户选择执行**：

```bash
case $user_choice in
    1)  # 确认提交
        # 添加所有变更文件
        git add .

        # 提交
        git commit -m "$commit_message"

        # 推送
        current_branch=$(git branch --show-current)
        git push origin "$current_branch"

        echo ""
        echo "✅ 提交成功！"
        echo "分支: $current_branch"
        echo "远程: origin"
        ;;

    2)  # 修改消息
        # 打开编辑器编辑消息
        temp_file=$(mktemp)
        echo "$commit_message" > "$temp_file"
        ${EDITOR:-vim} "$temp_file"
        commit_message=$(cat "$temp_file")
        rm "$temp_file"

        # 重新显示预览并确认
        # 回到步骤 8
        ;;

    3)  # 更改模板
        # 重新选择模板
        # 回到步骤 6
        ;;

    4)  # 取消操作
        echo "❌ 操作已取消"
        exit 0
        ;;
esac
```

## 错误处理

### 推送失败

```bash
if ! git push origin "$current_branch" 2>&1; then
    echo ""
    echo "⚠️  推送失败！可能的原因："
    echo "1. 远程有新提交，需要先 pull"
    echo "2. 网络连接问题"
    echo "3. 认证失败"
    echo ""
    echo "建议操作："
    echo "  git pull --rebase origin $current_branch"
    echo "  git push origin $current_branch"
    exit 1
fi
```

### Pre-commit 钩子失败

```bash
if ! git commit -m "$commit_message" 2>&1; then
    echo ""
    echo "⚠️  提交失败！pre-commit 钩子检查未通过。"
    echo ""
    echo "选项："
    echo "1. 修复问题后重试"
    echo "2. 使用 --no-verify 跳过钩子（不推荐）"
    exit 1
fi
```

## 配置文件

### 项目级配置

在项目根目录创建 `.smart-commit.json`：

```json
{
  "$schema": "./config-schema.json",
  "_comment": "GitHub Smart Commit 项目配置",
  "language": "zh",
  "auto_update_readme": true,
  "auto_update_version": true,
  "auto_update_changelog": false,
  "always_show_template_choice": true,
  "commit_message_template": null,
  "readme_style": "auto",
  "version_scheme": "semver",
  "include_issue_refs": true,
  "max_files_in_commit": 10
}
```

### 全局配置

在用户主目录创建 `~/.smart-commit.json`：

```json
{
  "_comment": "GitHub Smart Commit 全局配置",
  "language": "en",
  "auto_update_readme": true,
  "auto_update_version": true,
  "always_show_template_choice": false
}
```

### 配置优先级

1. 项目级配置（`.smart-commit.json`）
2. 全局配置（`~/.smart-commit.json`）
3. 默认配置

## 完成提示

```
✅ GitHub 智能提交完成！

提交信息：
  类型: ✨ feat(auth)
  分支: main
  远程: origin

更新内容：
  ✓ README.md → v1.1.0
  ✓ package.json → v1.1.0

Commit 消息：
  ✨ feat(auth): add OAuth 2.0 authentication support

  Implement OAuth 2.0 authentication flow with support for:
  - Google OAuth provider
  - GitHub OAuth provider
  - Token refresh mechanism

  Modified files:
    src/auth/oauth.py
    src/auth/providers/google.py

  Co-Authored-By: Claude Sonnet 4.6 (1M context) <noreply@anthropic.com>
```

## 技术依赖

- Python 3.7+
- Git 2.0+
- jq（用于 JSON 处理，可选）

## 脚本路径

所有脚本位于：`~/.claude/skills/github-smart-commit/scripts/`

- `analyze_changes.py` - 代码变更分析
- `generate_commit.py` - Commit 消息生成
- `update_readme.py` - README 更新
- `update_version.py` - 版本号更新
- `config.py` - 配置管理
- `utils.py` - 工具函数
- `i18n.py` - 国际化支持

## 参考文件

- `references/gitmoji-map.json` - Gitmoji 映射表
- `references/readme-template-cyberpunk-zh.md` - 赛博朋克风格中文模板
- `references/readme-template-cyberpunk-en.md` - 赛博朋克风格英文模板

## 开发路线图

- [x] v1.0.0：核心功能（代码分析、commit 生成、提交推送）
- [x] v1.1.0：README 智能更新
- [x] v1.2.0：版本号自动更新
- [x] v1.3.0：支持更多项目类型
- [x] v2.0.0：完整配置支持和模板选择
- [ ] v2.1.0：CHANGELOG 自动更新
- [ ] v2.2.0：预提交和后提交钩子支持
- [ ] v3.0.0：多机器学习和 AI 增强功能
