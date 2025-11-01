# ⚡ N8N Workflow Browser

一个功能强大的 N8N 工作流浏览器，支持中英文双语界面、全文搜索、分类筛选和可视化流程图展示。

[English](#english) | [中文](#中文)

---

## 中文

### 📖 项目简介

本项目是一个 **N8N 工作流集合浏览器**，收集了来自 n8n 官网、社区论坛及网络公开资源的 **4800+ 个工作流**。提供了一个现代化的 Web 界面，让您可以快速搜索、浏览和下载这些工作流。

### ✨ 主要特性

#### 🌍 **中英文双语支持**
- ✅ 一键切换中英文界面
- ✅ 所有界面元素完整翻译
- ✅ 支持中文搜索（自动翻译）
- ✅ 语言偏好自动保存

#### 🔍 **强大的搜索功能**
- 全文搜索（名称、描述、集成服务）
- 支持中文关键词搜索
- 实时搜索结果展示
- 搜索结果高亮显示

#### 🎯 **智能筛选**
- 按触发器类型筛选（Webhook、定时、手动等）
- 按复杂度筛选（低、中、高）
- 按分类筛选
- 仅显示活跃工作流

#### 📊 **可视化展示**
- Mermaid 流程图自动生成
- 工作流结构可视化
- 支持缩放和平移
- 节点关系清晰展示

#### 🎨 **现代化界面**
- 响应式设计，支持移动端
- 深色/浅色主题切换
- 流畅的动画效果
- 优雅的卡片布局

#### ⚡ **高性能**
- SQLite FTS5 全文搜索引擎
- 亚秒级搜索响应
- 分页加载优化
- 智能缓存机制

### 🚀 快速开始

#### 1. 安装依赖

```bash
pip install -r requirements.txt
```

#### 2. 启动服务器

```bash
# 默认端口 8000
python api_server.py

# 或指定端口
python api_server.py --port 8003
```

#### 3. 访问界面

浏览器打开：`http://localhost:8000`

首次启动会自动索引所有工作流文件（约需 1-2 分钟）。

### 📁 项目结构

```
n8n-workflows1-main/
├── workflows/              # 工作流 JSON 文件
├── static/                 # 静态文件
│   ├── index.html         # 主界面（支持中英文）
│   └── demo-cn.html       # 中文演示页面
├── api_server.py          # FastAPI 后端服务
├── workflow_db.py         # 数据库管理
├── i18n_translator.py     # 翻译模块
├── requirements.txt       # Python 依赖
└── README.md             # 项目说明
```

### 🎯 使用场景

1. **学习参考**：浏览各种 N8N 工作流实现案例
2. **快速开发**：搜索并下载符合需求的工作流模板
3. **工作流管理**：集中管理和浏览大量工作流
4. **技术研究**：分析工作流结构和设计模式

### 📝 工作流使用方法

#### 导入工作流到 N8N

1. 在浏览器中找到需要的工作流
2. 点击 "下载 JSON" 按钮
3. 打开 N8N 编辑器
4. 点击右上角菜单 → "Import workflow"
5. 选择下载的 JSON 文件
6. 点击导入

⚠️ **注意**：导入后需要配置相关凭证和 Webhook 地址才能正常运行。

### 🌐 部署指南

本项目支持多种部署方式：

- **GitHub Pages**（静态展示）
- **Vercel**（推荐，支持完整功能）
- **Railway**（简单快速）
- **Render**（稳定可靠）
- **Docker**（自托管）

详细部署说明请查看 [deploy-github-pages.md](deploy-github-pages.md)

### 🛠️ 技术栈

- **后端**：Python 3.9+, FastAPI, SQLite FTS5
- **前端**：原生 JavaScript, HTML5, CSS3
- **可视化**：Mermaid.js
- **搜索**：全文搜索 + 中文翻译
- **国际化**：自定义 i18n 系统

### 📊 数据统计

- 📦 工作流总数：**4834 个**
- 🔥 活跃工作流：**4818 个**
- 🔌 集成服务：**680+ 种**
- 🌐 支持语言：**中文 / English**

### 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 📄 开源协议

本项目采用 MIT 协议开源。

### 🙏 致谢

- N8N 官方及社区
- 所有贡献工作流的开发者
- 开源社区的支持

---

## English

### 📖 Project Introduction

This is an **N8N Workflow Browser** with a collection of **4800+ workflows** from n8n official website, community forums, and public resources. It provides a modern web interface for quickly searching, browsing, and downloading these workflows.

### ✨ Key Features

#### 🌍 **Bilingual Support (Chinese/English)**
- ✅ One-click language switching
- ✅ Complete UI translation
- ✅ Chinese keyword search (auto-translation)
- ✅ Language preference persistence

#### 🔍 **Powerful Search**
- Full-text search (name, description, integrations)
- Chinese keyword support
- Real-time results
- Search highlighting

#### 🎯 **Smart Filtering**
- Filter by trigger type (Webhook, Scheduled, Manual, etc.)
- Filter by complexity (Low, Medium, High)
- Filter by category
- Active workflows only

#### 📊 **Visualization**
- Auto-generated Mermaid diagrams
- Workflow structure visualization
- Zoom and pan support
- Clear node relationships

#### 🎨 **Modern UI**
- Responsive design (mobile-friendly)
- Dark/light theme toggle
- Smooth animations
- Elegant card layout

#### ⚡ **High Performance**
- SQLite FTS5 full-text search
- Sub-second search response
- Pagination optimization
- Smart caching

### 🚀 Quick Start

#### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 2. Start Server

```bash
# Default port 8000
python api_server.py

# Or specify port
python api_server.py --port 8003
```

#### 3. Access Interface

Open browser: `http://localhost:8000`

First startup will auto-index all workflows (takes 1-2 minutes).

### 🌐 Deployment

Supports multiple deployment options:

- **GitHub Pages** (static demo)
- **Vercel** (recommended, full features)
- **Railway** (simple & fast)
- **Render** (stable & reliable)
- **Docker** (self-hosted)

See [deploy-github-pages.md](deploy-github-pages.md) for details.

### 🛠️ Tech Stack

- **Backend**: Python 3.9+, FastAPI, SQLite FTS5
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Visualization**: Mermaid.js
- **Search**: Full-text search + Chinese translation
- **i18n**: Custom internationalization system

### 📊 Statistics

- 📦 Total Workflows: **4834**
- 🔥 Active Workflows: **4818**
- 🔌 Integrations: **680+**
- 🌐 Languages: **Chinese / English**

### 🤝 Contributing

Issues and Pull Requests are welcome!

### 📄 License

MIT License

---

**Version**: 1.0.0  
**Last Updated**: 2025-11-01  
**Status**: ✅ Production Ready
