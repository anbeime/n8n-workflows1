# 推送到 GitHub 快速指南

## 🚀 第一次推送到 GitHub

### 步骤 1：在 GitHub 上创建仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `n8n-workflows-browser` （或其他名称）
   - **Description**: `🌐 N8N Workflow Browser with 4800+ workflows, bilingual support (中英文)`
   - **Public** or **Private**: 根据需要选择
   - ⚠️ **不要**勾选 "Initialize this repository with a README"
3. 点击 "Create repository"

### 步骤 2：在本地推送代码

打开命令行，执行以下命令：

```bash
# 进入项目目录
cd "c:\D\工作流n8n-coze-dify\n8n工作流\n8n-workflows1-main"

# 初始化 Git 仓库（如果还没有初始化）
git init

# 添加所有文件
git add .

# 提交代码
git commit -m "feat: Initial commit - N8N Workflow Browser with i18n support"

# 设置主分支名称
git branch -M main

# 添加远程仓库（替换 YOUR_USERNAME 和 YOUR_REPO_NAME）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 推送代码
git push -u origin main
```

### 步骤 3：验证推送

访问你的 GitHub 仓库页面，确认文件已成功上传。

---

## 🌐 部署到 Vercel（推荐）

### 方法 1：通过 GitHub 自动部署（最简单）

1. 访问 https://vercel.com
2. 点击 "Sign Up" 或 "Log in"，使用 GitHub 账号登录
3. 点击 "Add New..." → "Project"
4. 导入你的 GitHub 仓库
5. 配置项目：
   - **Framework Preset**: Other
   - **Build Command**: 留空
   - **Output Directory**: `static`
   - **Install Command**: `pip install -r requirements.txt`
6. 点击 "Deploy"

✅ **完成！** Vercel 会自动构建并提供一个访问地址，如：
```
https://n8n-workflows-browser.vercel.app
```

### 方法 2：使用 Vercel CLI

```bash
# 安装 Vercel CLI
npm install -g vercel

# 登录 Vercel
vercel login

# 部署项目
cd "c:\D\工作流n8n-coze-dify\n8n工作流\n8n-workflows1-main"
vercel

# 生产环境部署
vercel --prod
```

---

## 🐳 Docker 部署

### 构建并运行

```bash
# 构建 Docker 镜像
docker build -t n8n-workflows-browser .

# 运行容器
docker run -d -p 8000:8000 --name n8n-browser n8n-workflows-browser

# 或使用 docker-compose
docker-compose up -d
```

### 访问应用

浏览器打开：`http://localhost:8000`

### 停止容器

```bash
# 使用 docker
docker stop n8n-browser
docker rm n8n-browser

# 使用 docker-compose
docker-compose down
```

---

## 🎯 部署到其他平台

### Railway

1. 访问 https://railway.app
2. 点击 "Start a New Project"
3. 选择 "Deploy from GitHub repo"
4. 选择你的仓库
5. Railway 会自动检测并部署

### Render

1. 访问 https://render.com
2. 点击 "New +" → "Web Service"
3. 连接你的 GitHub 仓库
4. 配置：
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python api_server.py --port $PORT`
5. 点击 "Create Web Service"

### Heroku

```bash
# 安装 Heroku CLI
# 访问 https://devcenter.heroku.com/articles/heroku-cli

# 登录
heroku login

# 创建应用
heroku create n8n-workflows-browser

# 推送代码
git push heroku main

# 打开应用
heroku open
```

---

## ⚠️ 重要提示

### 1. 数据库文件

数据库文件 `workflows.db` 已被 `.gitignore` 排除，**不会**推送到 GitHub。

**解决方案**：
- 首次部署时会自动重新索引工作流
- 或者手动上传预构建的数据库

### 2. 文件大小限制

GitHub 有 100MB 单文件限制，如果有大文件：

```bash
# 使用 Git LFS（Large File Storage）
git lfs install
git lfs track "*.db"
git add .gitattributes
git commit -m "Add Git LFS support"
```

### 3. 环境变量

如果需要设置环境变量（在 Vercel/Railway/Render 等平台）：

- `PORT`: 服务端口（通常由平台自动设置）
- `WORKFLOW_DB_PATH`: 数据库路径（可选）

---

## 📝 常用 Git 命令

```bash
# 查看状态
git status

# 添加文件
git add .

# 提交更改
git commit -m "描述信息"

# 推送到远程
git push

# 拉取最新代码
git pull

# 查看提交历史
git log

# 创建分支
git checkout -b feature-name

# 切换分支
git checkout main

# 合并分支
git merge feature-name
```

---

## 🎉 部署成功后的检查清单

- [ ] ✅ 代码已推送到 GitHub
- [ ] ✅ 可以访问部署的网站
- [ ] ✅ 搜索功能正常工作
- [ ] ✅ 中英文切换正常
- [ ] ✅ 工作流列表正确显示
- [ ] ✅ 详情页面可以正常打开
- [ ] ✅ 下载功能正常
- [ ] ✅ 流程图可以正常显示

---

## 🆘 常见问题

### Q: 推送时提示认证失败？
**A**: 使用 Personal Access Token 代替密码：
1. GitHub → Settings → Developer settings → Personal access tokens
2. 生成新 token
3. 使用 token 作为密码

### Q: Vercel 部署失败？
**A**: 检查：
1. `requirements.txt` 是否正确
2. Python 版本是否兼容（建议 3.9+）
3. 查看 Vercel 部署日志

### Q: 数据库没有数据？
**A**: 确保：
1. 工作流文件已上传
2. 首次启动会自动索引（需要 1-2 分钟）
3. 检查服务器日志

---

## 📞 需要帮助？

如有问题，请：
1. 查看 GitHub Issues
2. 提交新的 Issue
3. 联系项目维护者

---

**祝您部署顺利！** 🚀
