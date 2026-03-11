# Commit 消息格式增强功能

## 概述

github-smart-commit 技能现在支持多种 commit 消息格式，包括简洁格式和详细的分类格式。

## 格式类型

### 1. Simple 格式（默认）

简洁的列表格式，每个文件一行描述。

**示例**：
```
✨ feat(core): 添加认证功能

• 新增 2 个文件
• 修改 3 个文件

添加新功能，增强系统能力

  + src/auth.py - 认证模块
  + tests/test_auth.py - 测试用例
  ~ src/api/user.py - API 接口

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

### 2. Detailed 格式（详细分类）

类似 CHANGELOG 的详细格式，包含智能分类。

**示例**：
```
✨ feat(core): 完整实现智能分类功能

添加新功能，增强系统能力

**新增功能**：
✅ scripts/categorization.py - 智能分类模块
✅ scripts/generate_commit.py - Commit 消息生成器

**配置变更**：
- scripts/config.py - 配置管理系统
- scripts/i18n.py - 国际化文本映射

修改的文件：
  scripts/config.py (10 行)
  scripts/i18n.py

新增的文件：
  scripts/categorization.py (+50 行)

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

## 配置选项

在项目根目录创建 `.smart-commit.json` 文件：

```json
{
  "language": "zh",

  "commit_message_format": "detailed",
  "include_categorization": true,
  "show_line_changes": true,
  "show_emoji_bullets": true
}
```

### 配置说明

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `commit_message_format` | string | `"simple"` | 消息格式：`simple`、`detailed` 或 `compact` |
| `include_categorization` | boolean | `false` | 是否启用智能分类（详细格式） |
| `show_line_changes` | boolean | `false` | 是否显示代码行数变化 |
| `show_emoji_bullets` | boolean | `false` | 是否使用 emoji 作为列表符号 |
| `include_file_stats` | boolean | `true` | 是否包含文件统计 |
| `max_files_in_summary` | number | `10` | 摘要中最多显示的文件数 |

## 分类说明

详细格式会将变更自动分类到以下类别：

- **核心改进**：重构、架构变更
- **新增功能**：新功能、新模块
- **修复问题**：Bug 修复
- **新增文档**：文档相关文件
- **配置变更**：配置文件修改
- **测试完善**：测试文件
- **性能优化**：性能相关优化
- **破坏性变更**：不兼容变更说明

## 使用示例

### 启用详细格式

1. 创建 `.smart-commit.json`：
```bash
cp .smart-commit.json.detailed.example .smart-commit.json
```

2. 正常使用技能：
```
"提交代码" 或 "commit and push"
```

### 切换回简单格式

编辑 `.smart-commit.json`：
```json
{
  "commit_message_format": "simple"
}
```

## 向后兼容性

✅ 完全向后兼容：
- 默认使用简单格式
- 现有配置文件继续有效
- 函数签名保持兼容

## 测试

运行测试脚本验证功能：

```bash
cd /Users/agiray/.claude/skills/github-smart-commit/scripts
python3 test_generate.py
```

## 实现细节

### 新增文件

- `scripts/categorization.py` - 智能分类模块
- `.smart-commit.json.detailed.example` - 详细格式配置示例
- `scripts/test_generate.py` - 测试脚本

### 修改文件

- `scripts/config.py` - 扩展配置系统
- `scripts/i18n.py` - 增强国际化支持
- `scripts/generate_commit.py` - 重构生成逻辑

## 开发说明

### 分类规则

文件分类基于以下规则：

1. **文件路径匹配**：根据路径判断（docs/、config/、src/等）
2. **变更类型匹配**：feat → 新增功能、fix → 修复问题等
3. **文件名模式**：特殊文件的特殊处理
4. **代码行数统计**：从 git diff --stat 提取

### 扩展分类

如需添加新的分类或修改分类规则，编辑 `scripts/categorization.py` 中的：
- `classify_file()` - 分类逻辑
- `describe_change()` - 描述生成
