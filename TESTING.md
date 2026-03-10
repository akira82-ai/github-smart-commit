# GitHub Smart Commit 测试指南

本文档描述如何测试 `github-smart-commit` 技能的完整功能。

## 前提条件

1. ✅ 技能已安装到 `~/.claude/skills/github-smart-commit/`
2. ✅ 测试项目是一个 Git 仓库
3. ✅ 有远程仓库配置

## 测试场景

### 场景 1：新功能提交（feat）

**目的**：验证新功能类型的变更检测和版本升级

**步骤**：

1. 创建或修改一个文件：
```bash
echo "# New Feature" >> feature.txt
```

2. 触发技能：
```
提交代码
```

3. **验证点**：
   - ✅ 正确识别为 `feat` 类型
   - ✅ 显示模板选择界面
   - ✅ Commit 消息包含 `✨` emoji
   - ✅ 版本号 minor 升级（1.0.0 → 1.1.0）
   - ✅ README.md 版本号已更新（如果存在）
   - ✅ 成功推送到远程

**预期输出**：
```
📊 变更统计
类型: ✨ feat
范围: (空)
版本升级: minor

📝 Commit 消息
✨ feat: add new feature

Modified files:
  feature.txt
```

---

### 场景 2：Bug 修复提交（fix）

**目的**：验证 bug 修复类型的变更检测

**步骤**：

1. 修改文件，包含 "fix" 关键词：
```bash
echo "# Fix bug" >> fix.txt
```

2. 触发技能：
```
push to github
```

3. **验证点**：
   - ✅ 正确识别为 `fix` 类型
   - ✅ Commit 消息包含 `🐛` emoji
   - ✅ 版本号 patch 升级（1.1.0 → 1.1.1）
   - ✅ README.md 版本号已更新

---

### 场景 3：文档更新（docs）

**目的**：验证文档类型的变更检测

**步骤**：

1. 修改 README.md 或文档文件：
```bash
echo "# Documentation update" >> README.md
```

2. 触发技能：
```
推送到 GitHub
```

3. **验证点**：
   - ✅ 正确识别为 `docs` 类型
   - ✅ Commit 消息包含 `📝` emoji
   - ✅ 版本号 patch 升级
   - ✅ 不升级 minor 版本

---

### 场景 4：无 README 项目

**目的**：验证在无 README 项目中的行为

**步骤**：

1. 在临时目录创建新项目：
```bash
mkdir /tmp/test-no-readme
cd /tmp/test-no-readme
git init
echo "# Test" > test.txt
```

2. 触发技能：
```
提交代码
```

3. **验证点**：
   - ✅ 跳过 README 更新
   - ✅ 显示友好提示（不显示错误）
   - ✅ 不影响其他功能
   - ✅ 仍然能正常提交

---

### 场景 5：配置文件测试

**目的**：验证配置文件的加载和使用

**步骤**：

1. 创建配置文件：
```bash
cat > .smart-commit.json << EOF
{
  "language": "zh",
  "auto_update_readme": false,
  "auto_update_version": true,
  "always_show_template_choice": false
}
EOF
```

2. 修改文件：
```bash
echo "# Config test" >> test.txt
```

3. 触发技能：
```
提交 GitHub
```

4. **验证点**：
   - ✅ 配置正确加载
   - ✅ README 未被更新（`auto_update_readme: false`）
   - ✅ 版本号仍然更新（`auto_update_version: true`）
   - ✅ 不显示模板选择（`always_show_template_choice: false`）
   - ✅ Commit 消息语言为中文（`language: zh`）

---

### 场景 6：模板选择测试

**目的**：验证各种 commit 消息模板

**步骤**：

1. 修改文件：
```bash
echo "# Template test" >> test.txt
```

2. 触发技能并选择不同模板：
```
提交代码
```

3. **测试各种模板**：

#### 模板 1：智能生成（推荐）
**验证点**：
   - ✅ 包含完整的 subject、body、files
   - ✅ 包含 Co-Authored-By 署名

#### 模板 2：简洁模式
**验证点**：
   - ✅ 只有 subject 行
   - ✅ 无 body 和 files

#### 模板 3：详细模式
**验证点**：
   - ✅ 包含完整的文件列表
   - ✅ 包含变更详情统计

#### 模板 4：手动编辑
**验证点**：
   - ✅ 打开编辑器
   - ✅ 可以自定义消息

---

### 场景 7：用户确认流程测试

**目的**：验证用户确认流程的各种选项

**步骤**：

1. 修改文件：
```bash
echo "# Confirm test" >> test.txt
```

2. 触发技能：
```
提交代码
```

3. **测试各种选项**：

#### 选项 1：确认提交
**验证点**：
   - ✅ 执行 git add
   - ✅ 执行 git commit
   - ✅ 执行 git push
   - ✅ 显示成功消息

#### 选项 2：修改消息
**验证点**：
   - ✅ 打开编辑器
   - ✅ 重新显示预览
   - ✅ 可以再次确认

#### 选项 3：更改模板
**验证点**：
   - ✅ 重新显示模板选择
   - ✅ 可以选择其他模板

#### 选项 4：取消操作
**验证点**：
   - ✅ 不执行任何操作
   - ✅ 保留所有变更
   - ✅ 显示取消消息

---

### 场景 8：错误处理测试

**目的**：验证各种错误情况的处理

#### 测试 8.1：不是 Git 仓库

```bash
cd /tmp
mkdir test-no-git
cd test-no-git
echo "# Test" > test.txt

# 触发技能
提交代码
```

**验证点**：
   - ✅ 显示友好错误提示
   - ✅ 建议初始化 git
   - ✅ 结束技能

#### 测试 8.2：没有变更

```bash
cd /tmp/test-no-git
git init
git add .
git commit -m "Initial commit"

# 触发技能
提交代码
```

**验证点**：
   - ✅ 显示工作区干净提示
   - ✅ 结束技能

#### 测试 8.3：大文件警告

```bash
# 创建大于 10MB 的文件
dd if=/dev/zero of=large.bin bs=1M count=11

# 触发技能
提交代码
```

**验证点**：
   - ✅ 显示大文件警告
   - ✅ 建议 Git LFS
   - ✅ 询问是否继续

---

### 场景 9：不同项目类型测试

**目的**：验证不同项目类型的版本号更新

#### 测试 9.1：Node.js 项目

```bash
mkdir /tmp/test-nodejs
cd /tmp/test-nodejs
git init
cat > package.json << EOF
{
  "name": "test-project",
  "version": "1.0.0"
}
EOF
echo "# Test" > test.txt

# 触发技能
提交代码
```

**验证点**：
   - ✅ 检测为 Node.js 项目
   - ✅ package.json 版本号更新
   - ✅ JSON 格式保持正确

#### 测试 9.2：Python 项目

```bash
mkdir /tmp/test-python
cd /tmp/test-python
git init
cat > pyproject.toml << EOF
[tool.poetry]
name = "test-project"
version = "1.0.0"
EOF
echo "# Test" > test.txt

# 触发技能
提交代码
```

**验证点**：
   - ✅ 检测为 Python 项目
   - ✅ pyproject.toml 版本号更新

---

### 场景 10：README 风格检测测试

**目的**：验证不同 README 风格的检测和更新

#### 测试 10.1：赛博朋克风格

```bash
# 使用赛博朋克风格的 README
cat > README.md << 'EOF'
╔══════════════════════════════════════════════════════════════╗
║                    My Project v1.0.0                         ║
║                    Build: 20250310                           ║
╚══════════════════════════════════════════════════════════════╝
EOF
```

**验证点**：
   - ✅ 检测为 cyberpunk 风格
   - ✅ 正确更新版本号和构建日期

#### 测试 10.2：标准格式

```bash
cat > README.md << 'EOF'
# My Project

Version: 1.0.0
Updated: 2025-03-10
EOF
```

**验证点**：
   - ✅ 检测为 standard 风格
   - ✅ 正确更新版本号和日期

#### 测试 10.3：极简格式

```bash
cat > README.md << 'EOF'
# My Project

A simple project.
EOF
```

**验证点**：
   - ✅ 检测为 minimal 风格
   - ✅ 跳过版本号更新（无明显版本号）

---

## 测试清单

使用以下清单确保所有功能都已测试：

### 核心功能
- [ ] 代码变更分析（feat/fix/docs/refactor 等）
- [ ] Commit 消息生成
- [ ] Git 提交和推送
- [ ] Emoji 和 Gitmoji 支持
- [ ] Conventional Commits 格式

### 新增功能（v2.0.0）
- [ ] 配置文件加载
- [ ] README 自动更新
- [ ] 版本号自动更新
- [ ] 模板选择
- [ ] 用户确认流程
- [ ] 错误处理

### 项目类型支持
- [ ] Node.js (package.json)
- [ ] Python (pyproject.toml)
- [ ] Python (setup.py)
- [ ] Rust (Cargo.toml)
- [ ] Go (go.mod)
- [ ] Ruby (Gemfile)
- [ ] PHP (composer.json)
- [ ] Java (pom.xml)

### README 风格支持
- [ ] Cyberpunk
- [ ] Standard
- [ ] Badges
- [ ] Minimal

### Commit 模板
- [ ] 智能生成（推荐）
- [ ] 简洁模式
- [ ] 详细模式
- [ ] 手动编辑

### 错误处理
- [ ] 非 Git 仓库
- [ ] 无变更
- [ ] 大文件警告
- [ ] 推送失败
- [ ] Pre-commit 钩子失败

## 测试报告模板

```markdown
## 测试报告

**测试日期**：2025-03-10
**测试人员**：[姓名]
**技能版本**：v2.0.0

### 测试结果

| 场景 | 状态 | 备注 |
|------|------|------|
| 场景 1：新功能提交 | ✅/❌ | |
| 场景 2：Bug 修复提交 | ✅/❌ | |
| 场景 3：文档更新 | ✅/❌ | |
| 场景 4：无 README 项目 | ✅/❌ | |
| 场景 5：配置文件测试 | ✅/❌ | |
| 场景 6：模板选择测试 | ✅/❌ | |
| 场景 7：用户确认流程测试 | ✅/❌ | |
| 场景 8：错误处理测试 | ✅/❌ | |
| 场景 9：不同项目类型测试 | ✅/❌ | |
| 场景 10：README 风格检测测试 | ✅/❌ | |

### 发现的问题

1. [问题描述]

### 建议

1. [改进建议]
```

## 自动化测试

未来可以添加自动化测试脚本：

```bash
#!/bin/bash
# test-github-smart-commit.sh

echo "开始测试 GitHub Smart Commit 技能..."

# 运行所有测试场景
for scenario in scenario-*.sh; do
    echo "运行测试场景: $scenario"
    bash "$scenario"
done

echo "测试完成！"
```

---

**注意**：在测试过程中，建议使用测试仓库而不是生产仓库，以避免意外提交。
