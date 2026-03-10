# Git Commit 消息示例

本文档提供了符合 Conventional Commits 规范的中文 commit 消息示例。

## 基础示例

### 功能开发
```bash
feat: 添加用户认证功能

实现 JWT 认证，支持登录、注册、登出功能
- 添加登录页面
- 实现token刷新机制
- 添加权限验证中间件

Closes #123
```

### Bug 修复
```bash
fix: 修复用户登录时密码验证错误的问题

密码比较时未使用 bcrypt，导致明文比较失败
现在使用 bcrypt.compare() 进行验证

Fixes #456
```

### 重构
```bash
refactor(core): 简化架构，删除冗余代码

将重复的验证逻辑提取到公共模块
移除未使用的工具函数
优化文件结构
```

### 文档更新
```bash
docs: 更新 README 安装说明

添加 Windows 系统的安装步骤
补充常见问题解答部分
```

### 性能优化
```bash
perf(api): 优化数据库查询性能

- 为 user_id 字段添加索引
- 使用 join 替代多次查询
- 添加查询结果缓存

查询速度提升 80%
```

## 破坏性变更

### 带详细说明
```bash
feat!: 重构 API 响应格式

BREAKING CHANGE: API 响应格式从 {data: {...}} 改为 {...}，
前端需要相应调整数据获取方式

迁移指南：见 docs/migration-guide.md
```

### 带迁移说明
```bash
chore!: 移除 Node 16 支持

BREAKING CHANGE: 最低 Node 版本提升到 18.0.0
使用了 Node 18+ 的原生 fetch API

影响：
- 所有用户需要升级到 Node 18+
- CI/CD 环境需要更新 Node 版本
```

## 复杂场景

### 完整的功能提交
```bash
feat(payment): 集成支付宝支付接口

实现扫码支付和移动支付功能
- 添加支付宝 SDK 集成
- 实现支付回调处理
- 添加支付订单管理
- 完善支付状态查询

测试账号：test@example.com / 123456
文档：docs/payment/alipay.md

Refs #789
Co-authored-by: 张三 <zhangsan@example.com>
```

### 多人协作
```bash
feat(ui): 添加暗黑模式支持

根据系统设置自动切换主题
支持手动切换亮/暗模式
添加主题切换动画效果

Co-authored-by: 李四 <lisi@example.com>
Co-authored-by: 王五 <wangwu@example.com>
Reviewed-by: Team Lead
```

### Bug 修复详细说明
```bash
fix(api): 修复并发请求导致的竞态条件问题

问题：
当用户快速连续点击时，多个请求同时发出，
后端可能收到旧的请求覆盖新的请求

解决方案：
- 引入请求 ID 追踪最新请求
- 忽略非最新请求的响应
- 添加请求防抖（300ms）

影响范围：所有表单提交操作

Fixes #234
```

## 不同类型的对比

### 同一功能的不同提交类型

```bash
# 新功能
feat: 添加商品搜索功能

实现商品关键词搜索
支持模糊匹配和高级筛选

# 修复 bug
fix: 修复搜索结果不准确的 bug

修复了排序逻辑错误
现在按相关性正确排序

# 重构（功能不变）
refactor(search): 优化搜索算法，提升查询速度

使用更高效的搜索算法
保持功能和接口不变

# 性能优化
perf(search): 添加搜索结果缓存

响应时间从 500ms 降至 50ms
使用 Redis 缓存热门搜索结果

# 文档
docs: 添加搜索功能使用文档

编写 API 文档
添加使用示例

# 测试
test(search): 添加搜索功能的单元测试

覆盖主要搜索场景
测试边界条件

# 样式调整
style(search): 优化搜索框样式

调整宽度和间距
统一配色方案

# 构建相关
build: 升级 webpack 到 5.x 版本

提升构建速度
减小打包体积

# CI 配置
ci: 添加 GitHub Actions 自动化测试流程

每次提交自动运行测试
支持多版本测试
```

## 实用技巧

### 带 Issue 链接
```bash
fix: 修复首页加载缓慢的问题

优化图片加载，添加懒加载
压缩静态资源

Fixes #123
Related to #456
```

### 回退提交
```bash
revert: 回退 "feat: 添加实验性功能"

该功能存在性能问题，需要重新设计

Refs: abc123, def456
```

### 带 Breaking Change 的详细说明
```bash
feat(auth)!: 认证系统升级

BREAKING CHANGE: 认证方式从 Session 改为 Token

变更内容：
1. 移除 /api/auth/login 端点
2. 新增 /api/auth/token 获取 token
3. 所有 API 请求需携带 Authorization header

前端修改示例：
```javascript
// 旧方式
fetch('/api/data', {
  credentials: 'include'
})

// 新方式
fetch('/api/data', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
})
```

迁移期：2周（截止 2026-03-24）
文档：docs/migration/auth-v2.md
```

## 最佳实践

### ✅ 好的提交消息

```bash
# 标题简洁有力
feat: 添加用户头像上传
fix: 修复登录后跳转错误
docs: 更新 API 文档

# 正文说明原因
fix: 修复登录验证失败

之前的密码验证逻辑有误，使用了错误的加密方式
现在使用 bcrypt 统一处理
```

### ❌ 不好的提交消息

```bash
# 太模糊
fix: 修复 bug
update: 更新代码
change: 改了一些东西

# 太冗长
feat: 添加了一个非常非常非常非常非常非常非常非常非常非常长的标题

# 缺少上下文
fix: 修复问题
# （应该说明是什么问题、为什么修复、怎么修复的）

# 混合多个变更
feat: 添加认证功能和修复登录 bug 和优化样式
# （应该拆分成多个提交）
```

### 使用 Co-authored-by

```bash
feat: 添加导出功能

实现 Excel 和 PDF 导出
支持自定义模板

Co-authored-by: 小明 <xiaoming@example.com>
```

## 规范总结

### 标题格式
- 不超过 50 个字符
- 使用祈使语气（"添加"不是"添加了"）
- 首字母小写（中文无此要求）
- 不以句号结尾
- 格式：`<类型>(<范围>): <描述>`

### 正文格式
- 每行不超过 72 个字符
- 解释 what 和 why，不是 how
- 使用空行分隔不同段落
- 可以列出要点

### 页脚格式
- 放置相关 issue 引用
- 添加 Co-authored-by 信息
- 标记破坏性变更

## 参考资源

- [Conventional Commits](https://www.conventionalcommits.org/zh-hans/)
- [Commitlint](https://commitlint.js.org/)
- [如何写好 Git Commit Message](https://cbea.ms/git-commit/)
