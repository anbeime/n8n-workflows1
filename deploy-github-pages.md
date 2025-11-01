# GitHub Pages 部署指南

## 🚀 部署到 GitHub Pages

### 方案一：静态前端 + GitHub Pages（推荐用于展示）

#### 步骤 1：准备静态数据

```bash
# 1. 生成静态数据文件
python -c "
from workflow_db import WorkflowDatabase
import json

db = WorkflowDatabase()
# 获取所有工作流
all_workflows = []
page = 1
while True:
    workflows, total = db.search_workflows(query='', page=page, per_page=100)
    if not workflows:
        break
    all_workflows.extend(workflows)
    page += 1

# 保存到 JSON 文件
with open('static/data/workflows.json', 'w', encoding='utf-8') as f:
    json.dump({
        'workflows': all_workflows,
        'total': len(all_workflows)
    }, f, ensure_ascii=False, indent=2)

# 保存统计信息
stats = db.get_stats()
with open('static/data/stats.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)
"

# 2. 创建数据目录
mkdir -p static/data
```

#### 步骤 2：创建 GitHub 仓库

```bash
# 1. 初始化 Git 仓库
git init

# 2. 添加 .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
*.db
*.db-journal

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# 项目特定
workflows.db
*.log
EOF

# 3. 添加所有文件
git add .

# 4. 提交
git commit -m "Initial commit: N8N Workflow Browser with i18n support"

# 5. 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/YOUR_USERNAME/n8n-workflows-browser.git

# 6. 推送到 GitHub
git push -u origin main
```

#### 步骤 3：配置 GitHub Pages

1. 进入 GitHub 仓库设置
2. 找到 "Pages" 部分
3. Source 选择 "Deploy from a branch"
4. Branch 选择 "main" 分支，目录选择 "/static"
5. 保存设置

⚠️ **限制**：GitHub Pages 只能托管静态内容，无法运行 Python 后端，因此无法实时搜索和更新数据。

---

### 方案二：完整部署（推荐用于生产环境）

使用支持 Python 的托管服务：

#### 2.1 Vercel 部署

1. **安装 Vercel CLI**
```bash
npm install -g vercel
```

2. **创建 vercel.json**
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api_server.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "api_server.py"
    },
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/static/index.html"
    }
  ]
}
```

3. **部署**
```bash
vercel --prod
```

#### 2.2 Railway 部署

1. **创建 railway.json**
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python api_server.py --port $PORT",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

2. **创建 Procfile**
```
web: python api_server.py --port $PORT
```

3. **部署到 Railway**
- 访问 https://railway.app
- 连接 GitHub 仓库
- 选择项目并部署

#### 2.3 Render 部署

1. **创建 render.yaml**
```yaml
services:
  - type: web
    name: n8n-workflows-browser
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python api_server.py --port $PORT"
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.0
```

2. **部署到 Render**
- 访问 https://render.com
- 连接 GitHub 仓库
- 创建 Web Service
- 自动检测并部署

#### 2.4 PythonAnywhere 部署

1. 访问 https://www.pythonanywhere.com
2. 上传项目文件
3. 配置 WSGI 文件
4. 设置虚拟环境和依赖
5. 重启 Web 应用

---

### 方案三：Docker 部署（最灵活）

#### 创建 Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 索引工作流（首次运行时）
RUN python -c "from workflow_db import WorkflowDatabase; db = WorkflowDatabase(); db.index_all_workflows()"

# 暴露端口
EXPOSE 8000

# 启动服务
CMD ["python", "api_server.py", "--port", "8000"]
```

#### 创建 docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./workflows.db:/app/workflows.db
    environment:
      - WORKFLOW_DB_PATH=/app/workflows.db
    restart: unless-stopped
```

#### 部署命令

```bash
# 构建镜像
docker build -t n8n-workflows-browser .

# 运行容器
docker run -d -p 8000:8000 --name n8n-browser n8n-workflows-browser

# 或使用 docker-compose
docker-compose up -d
```

---

## 📝 推送到 GitHub 的完整步骤

### 1. 准备工作

```bash
# 确保在项目根目录
cd "c:\D\工作流n8n-coze-dify\n8n工作流\n8n-workflows1-main"

# 检查 Git 状态
git status
```

### 2. 创建必要的配置文件

创建 `.gitignore`：
```
__pycache__/
*.pyc
*.db
*.db-journal
.env
venv/
node_modules/
.DS_Store
*.log
```

创建 `README.md`（项目说明）

### 3. 初始化并推送

```bash
# 如果还没有初始化 Git
git init

# 添加所有文件
git add .

# 提交
git commit -m "feat: Add N8N Workflow Browser with Chinese/English i18n support"

# 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/YOUR_USERNAME/n8n-workflows-browser.git

# 创建主分支
git branch -M main

# 推送
git push -u origin main
```

---

## 🌟 推荐部署方案对比

| 方案 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| **GitHub Pages** | 免费、简单、稳定 | 仅静态内容，无后端 | 展示用途 |
| **Vercel** | 免费、自动部署、CDN | 有使用限制 | 中小型项目 |
| **Railway** | 简单、支持数据库 | 免费额度有限 | 快速原型 |
| **Render** | 免费层可用、稳定 | 冷启动较慢 | 个人项目 |
| **Docker** | 最灵活、可自托管 | 需要服务器 | 生产环境 |

---

## 🔥 快速开始（推荐 Vercel）

```bash
# 1. 安装 Vercel CLI
npm install -g vercel

# 2. 登录 Vercel
vercel login

# 3. 初始化项目
vercel

# 4. 部署
vercel --prod
```

部署后，您将获得一个类似 `https://n8n-workflows-browser.vercel.app` 的网址。

---

## ⚠️ 注意事项

1. **数据库文件**：
   - 不要将 `workflows.db` 推送到 GitHub（已在 .gitignore 中排除）
   - 部署时需要重新索引或上传预构建的数据库

2. **安全性**：
   - 确保没有敏感信息（API密钥、凭证等）
   - 检查工作流文件中的敏感数据

3. **性能**：
   - 4800+ 工作流的数据库较大，首次索引需要时间
   - 考虑使用缓存或预构建数据

4. **成本**：
   - GitHub Pages: 免费
   - Vercel/Railway/Render: 有免费层
   - 自托管: 需要服务器成本

---

## 📚 相关资源

- [GitHub Pages 文档](https://docs.github.com/en/pages)
- [Vercel 部署指南](https://vercel.com/docs)
- [Railway 文档](https://docs.railway.app)
- [Render 文档](https://render.com/docs)
- [Docker 文档](https://docs.docker.com)

---

**推荐路径**：
1. 先推送到 GitHub（代码托管）
2. 使用 Vercel 部署（快速上线）
3. 如需更多控制，考虑 Docker 自托管

祝您部署顺利！🚀
