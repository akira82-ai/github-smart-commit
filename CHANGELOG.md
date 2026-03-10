# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-03-10

### Added

- ✅ 完整的配置系统支持（项目级和全局配置）
- ✅ Commit 消息模板选择功能
  - 智能生成（推荐）
  - 简洁模式
  - 详细模式
  - 手动编辑
- ✅ README.md 自动更新集成
  - 支持多种 README 风格（cyberpunk、standard、badges、minimal）
  - 自动检测风格并更新
- ✅ 版本号自动更新集成
  - 支持 Node.js、Python、Rust、Go、Ruby、PHP、Java
  - 自动检测项目类型
- ✅ 使用 AskUserQuestion 的完整确认流程
  - 模板选择
  - 预览确认
  - 修改消息
  - 取消操作
- ✅ 完整的错误处理和用户提示
- ✅ 配置文件示例（`.smart-commit.json.example`）
- ✅ 完整的 README.md 文档
- ✅ CHANGELOG.md 文件

### Changed

- 🔄 重写 SKILL.md，从描述性文档改为完整的实现指南
- 🔄 优化工作流程，增加配置加载和模板选择步骤
- 🔄 改进错误处理，提供更友好的错误提示

### Fixed

- 🐛 修复缺少 README 更新的问题
- 🐛 修复缺少版本号更新的问题
- 🐛 修复缺少模板选择的问题
- 🐛 修复缺少用户确认流程的问题

### Technical Details

**实现的关键功能**：

1. **配置系统**：
   - 项目级配置（`.smart-commit.json`）
   - 全局配置（`~/.smart-commit.json`）
   - 默认配置合并
   - 配置验证

2. **README 更新**：
   - 调用 `update_readme.py` 脚本
   - 自动检测 README 风格
   - 更新版本号和日期
   - 支持多种风格

3. **版本号更新**：
   - 调用 `update_version.py` 脚本
   - 自动检测项目类型
   - 根据变更类型升级版本号（major/minor/patch）
   - 支持多种项目类型

4. **模板选择**：
   - 使用 AskUserQuestion 提供选项
   - 4 种模板类型
   - 支持自定义模板
   - 手动编辑模式

5. **用户确认流程**：
   - 显示完整预览
   - 变更统计
   - Commit 消息预览
   - 将要更新的文件列表
   - 将要执行的操作
   - 多选项确认

6. **错误处理**：
   - Git 仓库检查
   - 变更文件检查
   - 大文件警告
   - 推送失败处理
   - Pre-commit 钩子失败处理

## [1.0.0] - 2025-03-10

### Added

- 🎉 初始版本
- ✅ 代码变更分析
- ✅ Commit 消息生成
- ✅ Git 提交和推送
- ✅ Gitmoji 支持
- ✅ Conventional Commits 格式

### Missing Features (在 v2.0.0 中已实现)

- ❌ 配置系统
- ❌ README 自动更新
- ❌ 版本号自动更新
- ❌ 模板选择
- ❌ 用户确认流程

## 未来计划

### [2.1.0] - 计划中

- CHANGELOG 自动更新
- 支持更多 Commit 消息格式
- 改进 AI 分析能力

### [2.2.0] - 计划中

- 预提交钩子支持
- 后提交钩子支持
- 自定义钩子脚本

### [3.0.0] - 计划中

- 多机器学习和 AI 增强功能
- 智能建议系统
- 自动分类和标签

---

**注意**：版本 2.0.0 是一个重大更新，完全重写了 SKILL.md 并实现了所有计划中的功能。
