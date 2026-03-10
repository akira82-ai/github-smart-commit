# GitHub Smart Commit

智能 GitHub 提交助手，自动分析代码变更、更新版本号和文档，生成美观的 Conventional Commits 格式提交消息。

## 特性

- 🤖 **智能分析**：自动分析代码变更类型（feat/fix/refactor/docs 等）
- 📝 **文档更新**：智能更新 README.md 版本号和日期
- 🔢 **版本管理**：自动更新项目版本号（支持 Node.js、Python、Rust、Go 等）
- 💬 **美观消息**：生成 Conventional Commits + Gitmoji 格式
- ✅ **确认流程**：显示完整预览，用户确认后执行
- 🌐 **多语言**：支持中英文双语
- 🎨 **模板选择**：支持多种 commit 消息模板
- ⚙️ **配置支持**：支持项目级和全局配置

## 安装

### 1. 复制技能文件

将技能文件夹复制到 Claude Code 技能目录：

```bash
cp -r github-smart-commit ~/.claude/skills/
```

### 2. 验证安装

```bash
ls -la ~/.claude/skills/github-smart-commit/
```

应该看到以下文件：
- `SKILL.md` - 技能定义文件
- `scripts/` - Python 脚本目录
- `references/` - 参考文件目录

## 使用方法

### 触发技能

使用以下任一短语触发技能：

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

### 工作流程

1. **环境检查**：检查 Git 仓库状态和变更文件
2. **加载配置**：加载项目或全局配置
3. **分析变更**：分析代码变更类型和影响范围
4. **更新 README**：自动更新 README.md 版本号（如果存在）
5. **更新版本**：自动更新项目版本号
6. **选择模板**：选择 commit 消息模板
7. **生成消息**：生成美观的 commit 消息
8. **预览确认**：显示完整预览，等待用户确认
9. **执行提交**：执行 git add、commit、push

## 配置

### 项目级配置

在项目根目录创建 `.smart-commit.json`：

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

### 全局配置

在用户主目录创建 `~/.smart-commit.json`：

```bash
cp .smart-commit.json.example ~/.smart-commit.json
```

### 配置选项

| 选项 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `language` | string | `"en"` | 语言：`"en"` 或 `"zh"` |
| `auto_update_readme` | boolean | `true` | 自动更新 README.md |
| `auto_update_version` | boolean | `true` | 自动更新版本号 |
| `auto_update_changelog` | boolean | `false` | 自动更新 CHANGELOG |
| `always_show_template_choice` | boolean | `true` | 总是显示模板选择 |
| `commit_message_template` | string/null | `null` | 自定义 commit 消息模板 |
| `readme_style` | string | `"auto"` | README 风格：`"auto"`, `"cyberpunk"`, `"standard"`, `"badges"`, `"minimal"` |
| `version_scheme` | string | `"semver"` | 版本方案：`"semver"` 或 `"custom"` |
| `include_issue_refs` | boolean | `true` | 包含 issue 引用 |
| `max_files_in_commit` | number | `10` | commit 中最大文件数 |

## Commit 消息模板

### 智能生成（推荐）

```
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

### 简洁模式

```
✨ feat(auth): add OAuth 2.0 authentication support
```

### 详细模式

```
✨ feat(auth): add OAuth 2.0 authentication support

## 变更详情
- 新增 2 个文件
- 修改 1 个文件
- 删除 0 个文件

## 完整文件列表
  src/auth/oauth.py
  src/auth/providers/google.py
  src/auth/providers/github.py

Co-Authored-By: Claude Sonnet 4.6 (1M context) <noreply@anthropic.com>
```

## 支持的项目类型

### Node.js
- `package.json`

### Python
- `pyproject.toml` (Poetry)
- `setup.py` (Setuptools)

### Rust
- `Cargo.toml`

### Go
- `go.mod`

### Ruby
- `Gemfile`
- `*.gemspec`

### PHP
- `composer.json`

### Java
- `pom.xml`

## 版本升级规则

根据 SemVer 规范自动升级版本号：

| 变更类型 | 版本升级 | 示例 |
|----------|----------|------|
| **major** | 破坏性变更 | `1.0.0` → `2.0.0` |
| **minor** | 新功能 | `1.0.0` → `1.1.0` |
| **patch** | bug 修复、文档、重构 | `1.0.0` → `1.0.1` |

## 技术架构

```
SKILL.md (技能定义)
    ↓
scripts/
    ├── analyze_changes.py    # 代码变更分析
    ├── generate_commit.py    # Commit 消息生成
    ├── update_readme.py      # README 更新
    ├── update_version.py     # 版本号更新
    ├── config.py             # 配置管理
    ├── utils.py              # 工具函数
    └── i18n.py               # 国际化支持
    ↓
references/
    ├── gitmoji-map.json      # Gitmoji 映射表
    └── readme-templates/     # README 模板
```

## 依赖项

- Python 3.7+
- Git 2.0+
- jq（可选，用于 JSON 处理）

## 开发路线图

- [x] v1.0.0：核心功能（代码分析、commit 生成、提交推送）
- [x] v1.1.0：README 智能更新
- [x] v1.2.0：版本号自动更新
- [x] v1.3.0：支持更多项目类型
- [x] v2.0.0：完整配置支持和模板选择
- [ ] v2.1.0：CHANGELOG 自动更新
- [ ] v2.2.0：预提交和后提交钩子支持
- [ ] v3.0.0：多机器学习和 AI 增强功能

## 故障排除

### 技能未触发

确保技能文件在正确位置：
```bash
ls -la ~/.claude/skills/github-smart-commit/SKILL.md
```

### README 未更新

检查 README 风格是否支持：
```bash
python3 ~/.claude/skills/github-smart-commit/scripts/update_readme.py --help
```

### 版本号未更新

检查项目类型是否支持：
```bash
python3 ~/.claude/skills/github-smart-commit/scripts/update_version.py --help
```

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

## 作者

Claude Code

---

Made with ❤️ by Claude Sonnet 4.6 (1M context)
