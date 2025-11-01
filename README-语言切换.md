# N8N 工作流浏览器 - 中英文语言切换功能

## 功能说明

已成功为首页添加中英文语言切换功能！用户可以在界面上自由切换中英文显示。

## 新增功能

### 1. 语言切换按钮
- 位置：控制栏右上角，主题切换按钮旁边
- 显示：
  - 英文界面时显示 "中文"
  - 中文界面时显示 "English"

### 2. 完整的界面翻译

#### 页面标题和描述
- 标题：⚡ N8N Workflow Documentation / ⚡ N8N 工作流文档
- 副标题：Lightning-fast workflow browser with instant search / 闪电般快速的工作流浏览器，支持即时搜索

#### 统计信息
- Total / 总数
- Active / 活跃
- Total Nodes / 总节点数
- Integrations / 集成服务

#### 搜索和筛选
- 搜索框提示：Search workflows... / 搜索工作流...
- 触发器筛选：Trigger / 触发器
  - All Types / 所有类型
  - Webhook / Webhook钩子
  - Scheduled / 定时计划
  - Manual / 手动触发
  - Complex / 复杂流程
- 复杂度筛选：Complexity / 复杂度
  - All Levels / 所有级别
  - Low (≤5 nodes) / 低 (≤5个节点)
  - Medium (6-15 nodes) / 中 (6-15个节点)
  - High (16+ nodes) / 高 (16+个节点)
- 分类筛选：Category / 分类
  - All Categories / 所有分类
- Active only / 仅活跃

#### 状态信息
- Loading workflows... / 正在加载工作流...
- Please wait while we fetch your workflow data / 请稍候，正在获取工作流数据
- Error Loading Workflows / 工作流加载错误
- Something went wrong. Please try again. / 出现错误，请重试。
- Retry / 重试
- No workflows found / 未找到工作流
- Try adjusting your search terms or filters / 尝试调整搜索词或筛选条件

#### 工作流卡片
- X nodes / X 个节点
- Integrations (X) / 集成服务 (X)

#### 工作流详情模态框
- Workflow Details / 工作流详情
- Description / 描述
- Statistics / 统计
  - Status / 状态
  - Active / 活跃
  - Inactive / 未激活
  - Trigger / 触发器
  - Complexity / 复杂度
  - Nodes / 节点数
  - Category / 分类
- Integrations / 集成服务
- No integrations found / 未找到集成服务
- Actions / 操作
  - 📥 Download JSON / 📥 下载JSON
  - 📄 View JSON / 📄 查看JSON
  - 📊 View Diagram / 📊 查看流程图
- Workflow JSON / 工作流JSON
- Workflow Diagram / 工作流流程图
- 📋 Copy / 📋 复制
- ✅ Copied! / ✅ 已复制!

#### 搜索结果统计
- 英文：X workflows found for "query" in "category"
- 中文：共找到 X 个工作流（搜索"query"，分类"category"）

#### 按钮
- Load More / 加载更多
- Zoom In / 放大
- Zoom Out / 缩小
- Reset Zoom / 重置缩放

## 技术实现

### 1. 国际化 (i18n) 系统
```javascript
// 翻译字典
const i18n = {
  en: { /* 英文翻译 */ },
  zh: { /* 中文翻译 */ }
};

// 翻译函数
function t(key) {
  return i18n[currentLang][key] || i18n.en[key] || key;
}
```

### 2. 语言状态管理
- 使用 `localStorage` 保存用户的语言偏好
- 默认语言：英文 (en)
- 支持的语言：英文 (en) / 中文 (zh)

### 3. 动态更新机制
```javascript
// 更新所有界面文本
function updateUILanguage() {
  // 更新标题、标签、按钮等所有文本元素
}

// 切换语言
function toggleLanguage() {
  currentLang = currentLang === 'en' ? 'zh' : 'en';
  localStorage.setItem('language', currentLang);
  updateUILanguage();
}
```

### 4. 集成到 WorkflowApp
- 工作流卡片渲染时根据当前语言显示
- 搜索结果统计根据语言格式化
- 模态框内容根据语言显示
- 按钮文本自动切换

## 使用方法

### 启动服务器
```bash
python api_server.py --port 8003
```

### 访问地址
浏览器打开：http://localhost:8003

### 切换语言
1. 点击页面右上角的语言切换按钮
2. 界面会立即切换到对应语言
3. 语言偏好会自动保存，下次访问时自动恢复

## 中文搜索支持

虽然工作流数据都是英文，但系统已经集成了中文翻译功能：

### 支持的中文搜索词
- **通讯工具**：电报、微信、钉钉、飞书、邮件、短信等
- **AI服务**：人工智能、聊天机器人、机器人等
- **数据存储**：数据库、表格、云盘等
- **开发工具**：代码、编程、测试等
- **业务流程**：客服、销售、市场等

### 示例
- 搜索 "电报" → 自动翻译为 "telegram" 进行搜索
- 搜索 "人工智能" → 自动翻译为 "ai openai anthropic" 进行搜索
- 搜索 "邮件自动化" → 自动翻译为 "email gmail outlook automation" 进行搜索

## 特性总结

✅ **完整的中英文界面**
✅ **一键切换语言**
✅ **自动保存语言偏好**
✅ **所有界面元素全部翻译**
✅ **实时更新，无需刷新页面**
✅ **支持中文搜索（自动翻译）**
✅ **响应式设计，支持移动端**

## 浏览器兼容性

- Chrome/Edge (推荐)
- Firefox
- Safari
- 支持 localStorage 和 ES6+ 的现代浏览器

## 未来改进方向

1. 添加更多语言支持（如日语、韩语等）
2. 支持工作流名称和描述的本地化
3. 添加语言自动检测功能
4. 优化翻译质量和覆盖范围

---

**开发时间**：2025-11-01
**版本**：1.0.0
**状态**：✅ 已完成
