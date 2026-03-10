---
name: github-smart-commit
description: |
  智能 GitHub 提交助手。当用户说"提交 GitHub"、"push to github"、"提交代码"、"commit and push"、"推送到 GitHub"、"上传代码"、"sync to github"时自动触发。

  自动分析代码变更，智能更新 README.md 和版本号，生成美观的 Conventional Commits 格式提交消息（带 emoji），并在用户确认后提交推送。
version: 1.0.0
allowed-tools: Bash, Read, Write, Edit, AskUserQuestion
author: Claude Code
---

# 🚀 GitHub 智能提交助手

## 核心特性

| 特性 | 说明 |
|-----|------|
| 🤖 智能分析 | 自动分析代码变更类型和影响范围 |
| 📝 文档更新 | 智能更新 README.md 版本号和日期 |
| 🔢 版本管理 | 自动更新项目版本号（支持多种项目类型）|
| 💬 美观消息 | 生成 Conventional Commits + Gitmoji 格式 |
| ✅ 确认流程 | 显示完整预览，用户确认后执行 |
| 🌐 多语言 | 支持中英文 README 格式 |

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

## 工作流程

### 步骤 1：环境检查
- 检查是否为 git 仓库
- 检查是否有待提交的变更
- 检查大文件（> 10MB）

### 步骤 2：分析代码变更
使用 `scripts/analyze_changes.py` 分析：
- 变更类型（feat/fix/refactor/docs 等）
- 影响范围（scope）
- 版本升级类型（major/minor/patch）
- 选择合适的 gitmoji

### 步骤 3：智能更新 README.md
使用 `scripts/update_readme.py` 更新：
- 顶部版本号（ASCII 框架中）
- 底部版本号（系统信息框中）
- 更新日期
- 核心模块进度条（新功能）
- 关键特性列表（新功能）
- 开发路线图

**支持的 README 风格**：
- 赛博朋克风格（带 ASCII 框架）

### 步骤 4：自动更新版本号
使用 `scripts/update_version.py` 更新：
- Node.js：`package.json`
- Python Poetry：`pyproject.toml`
- Python Setup：`setup.py`
- Rust：`Cargo.toml`
- Go：`go.mod`

**版本升级规则（SemVer）**：
- **major**：破坏性变更（BREAKING CHANGE）
- **minor**：新功能（feat）
- **patch**：bug 修复（fix）、文档、样式、重构等

### 步骤 5：生成美观的 Commit 消息
使用 `scripts/generate_commit.py` 生成：

**格式**：
```
<emoji> <type>(<scope>): <subject>

<body>

<footer>
```

**示例**：
```
✨ feat(auth): add OAuth 2.0 authentication support

Implement OAuth 2.0 authentication flow with support for:
- Google OAuth provider
- GitHub OAuth provider
- Token refresh mechanism

Modified files:
- src/auth/oauth.py
- src/auth/providers/google.py
- src/auth/providers/github.py
- tests/test_oauth.py

Co-Authored-By: Claude Sonnet 4.6 (1M context) <noreply@anthropic.com>
```

### 步骤 6：显示预览并请求确认
显示完整预览：
- 代码变更分析
- 将要更新的文件
- Commit 消息
- 将执行的操作

使用 `AskUserQuestion` 请求确认：
- 选项 1：确认执行
- 选项 2：取消
- 选项 3：修改 commit 消息

### 步骤 7：执行提交和推送
1. 更新 README.md（如果需要）
2. 更新版本号（如果需要）
3. `git add` 变更文件
4. `git commit` 提交
5. `git push origin <branch>` 推送到远程

## 错误处理

| 错误类型 | 处理策略 |
|---------|---------|
| 不是 Git 仓库 | 提示初始化 git |
| 没有变更 | 提示工作区干净 |
| README 格式不标准 | 跳过自动更新，发出警告 |
| 推送失败 | 提示 pull 或解决冲突 |
| 大文件 | 警告并建议使用 Git LFS |

## 使用示例

### 场景 1：基础使用
```
用户：提交 GitHub
助手：[分析变更] → [显示预览] → [请求确认] → [执行提交]
```

### 场景 2：修改 commit 消息
```
用户：提交 GitHub
助手：[显示预览]
用户：[选择"修改 commit 消息"]
助手：[请输入新的 commit 消息]
用户：[输入自定义消息]
助手：[使用自定义消息提交]
```

### 场景 3：取消提交
```
用户：提交 GitHub
助手：[显示预览]
用户：[选择"取消"]
助手：已取消提交操作
```

## 技术依赖

- Python 3.7+
- Git 2.0+
- 标准库：json, re, pathlib, datetime

## 配置文件

- `references/gitmoji-map.json`：Gitmoji emoji 映射表
- `references/readme-template-cyberpunk-zh.md`：赛博朋克风格中文模板
- `references/readme-template-cyberpunk-en.md`：赛博朋克风格英文模板

## 注意事项

1. **README 更新**：只支持赛博朋克风格的 README，其他风格会跳过更新
2. **版本号更新**：自动检测项目类型，如果无法识别会跳过
3. **推送前确认**：所有操作都会先显示预览，用户确认后才执行
4. **破坏性变更**：如果检测到 BREAKING CHANGE，会自动升级 major 版本

## 开发路线图

- [x] v1.0.0：核心功能（代码分析、commit 生成、提交推送）
- [ ] v1.1.0：README 智能更新
- [ ] v1.2.0：版本号自动更新
- [ ] v1.3.0：支持更多项目类型
- [ ] v2.0.0：自定义配置支持
