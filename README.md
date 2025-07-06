# SmartEdu - 智能教育组队平台

一个基于Vue 3 + TypeScript + Tailwind CSS的现代化组队平台，专为大学生设计，支持项目招募、简历投递、经验分享等功能。

## 技术栈

- **前端框架**: Vue 3 + TypeScript
- **构建工具**: Vite
- **状态管理**: Pinia
- **路由管理**: Vue Router 4
- **UI框架**: Tailwind CSS
- **HTTP客户端**: Axios
- **日期处理**: Day.js
- **通知组件**: Vue Toastification

## 功能特性

- 🏠 **首页**: 轮播图展示、动态分类标签、内容推荐
- 👥 **组队大厅**: 项目浏览、筛选、收藏
- 📋 **项目详情**: 详细信息、岗位申请、简历投递
- 👤 **个人主页**: 用户信息、经历展示、等级积分
- 🚀 **发起组队**: 创建项目、设置岗位、发布招募
- 💬 **消息中心**: 私信沟通、系统通知
- 📄 **简历管理**: 简历编辑、一键投递、申请历史
- 🔧 **管理后台**: 内容审核、用户管理、系统配置
- 🏷️ **动态分类**: 支持后台动态添加和管理分类标签
- 📊 **API驱动**: 所有数据通过RESTful API获取，支持实时更新
- 🛡️ **错误处理**: 完善的错误页面和错误边界，提供友好的用户体验

## 快速开始

### 环境要求

- Node.js >= 16.0.0
- npm >= 8.0.0

### 一键启动

```bash
# 克隆项目
git clone <repository-url>
cd smartedu-team-app

# 使用启动脚本（推荐）
chmod +x start.sh
./start.sh

# 或手动启动
npm install
npm run dev
```

访问 http://localhost:3000 查看应用

### 环境配置

复制环境变量文件：
```bash
cp env.example .env
```

根据需要修改 `.env` 文件中的配置。

### 构建生产版本

```bash
npm run build
```

### 代码检查

```bash
npm run lint
npm run type-check
```

## 项目结构

```
src/
├── api/                 # API接口层
│   ├── index.ts        # API基础配置
│   ├── user.ts         # 用户相关API
│   ├── project.ts      # 项目相关API
│   ├── home.ts         # 首页数据API
│   └── category.ts     # 分类管理API
├── components/         # 通用组件
│   ├── TopNavBar.vue   # 顶部导航栏
│   ├── CarouselBanner.vue # 轮播图
│   ├── CategoryTabs.vue   # 分类标签
│   ├── CompetitionCard.vue # 比赛卡片
│   ├── ProjectCard.vue     # 项目卡片
│   ├── ShareCard.vue       # 分享卡片
│   ├── Sidebar.vue         # 侧边栏
│   ├── ErrorBoundary.vue   # 错误边界组件
│   └── CustomSelect.vue    # 自定义下拉选择器
├── stores/            # 状态管理
│   ├── user.ts        # 用户状态
│   └── project.ts     # 项目状态
├── types/             # TypeScript类型定义
│   └── index.ts       # 全局类型
├── utils/             # 工具函数
│   ├── date.ts        # 日期处理
│   └── error.ts       # 错误处理工具
├── views/             # 页面组件
│   ├── HomePage.vue   # 首页
│   ├── TeamHallPage.vue # 组队大厅
│   ├── TeamDetailPage.vue # 项目详情
│   ├── ProfilePage.vue    # 个人主页
│   ├── LaunchTeamPage.vue # 发起组队
│   ├── MessageCenter.vue  # 消息中心
│   ├── MyResumePage.vue   # 简历管理
│   ├── AdminDashboard.vue # 管理后台
│   ├── ErrorPage.vue      # 错误页面
│   └── TestErrorPage.vue  # 错误测试页面
├── router/            # 路由配置
│   └── index.ts       # 路由定义
├── style.css          # 全局样式
├── main.ts           # 应用入口
└── App.vue           # 根组件
```

## 后端API文档

### 基础信息

- **Base URL**: `/api`
- **认证方式**: Bearer Token (JWT)
- **响应格式**: JSON

### 通用响应格式

```typescript
interface ApiResponse<T> {
  success: boolean
  data: T
  message?: string
}

interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  pageSize: number
  totalPages: number
}
```

### 1. 用户认证 API

#### 1.1 用户登录
```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

**响应**:
```json
{
  "success": true,
  "data": {
    "user": {
      "id": 1,
      "username": "张三",
      "email": "user@example.com",
      "avatar": "https://example.com/avatar.jpg",
      "school": "清华大学",
      "department": "计算机系",
      "level": 5,
      "points": 1200,
      "skills": ["Vue.js", "Python"],
      "interests": ["AI", "Web开发"],
      "createdAt": "2024-01-01T00:00:00Z"
    },
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
}
```

#### 1.2 用户注册
```http
POST /api/auth/register
Content-Type: application/json

{
  "username": "张三",
  "email": "user@example.com",
  "password": "password123",
  "school": "清华大学",
  "department": "计算机系"
}
```

#### 1.3 用户登出
```http
POST /api/auth/logout
Authorization: Bearer <token>
```

### 2. 用户信息 API

#### 2.1 获取当前用户信息
```http
GET /api/user/me
Authorization: Bearer <token>
```

#### 2.2 更新用户资料
```http
PUT /api/user/profile
Authorization: Bearer <token>
Content-Type: application/json

{
  "username": "新用户名",
  "bio": "个人简介",
  "skills": ["Vue.js", "React", "Python"],
  "interests": ["AI", "Web开发", "机器学习"]
}
```

#### 2.3 获取指定用户信息
```http
GET /api/user/{id}
```

#### 2.4 获取用户统计信息
```http
GET /api/user/{id}/stats
```

#### 2.5 获取用户项目
```http
GET /api/user/{id}/projects
```

#### 2.6 获取用户申请记录
```http
GET /api/user/{id}/applications
```

### 3. 简历管理 API

#### 3.1 获取用户简历
```http
GET /api/user/resume
Authorization: Bearer <token>
```

#### 3.2 更新用户简历
```http
PUT /api/user/resume
Authorization: Bearer <token>
Content-Type: application/json

{
  "education": [
    {
      "school": "清华大学",
      "major": "计算机科学与技术",
      "degree": "本科",
      "startDate": "2020-09-01",
      "endDate": "2024-07-01",
      "gpa": 3.8
    }
  ],
  "skills": ["Vue.js", "React", "Python", "机器学习"],
  "projects": [
    {
      "name": "智能校园导航系统",
      "role": "前端开发",
      "description": "基于Vue3的校园导航应用",
      "startDate": "2023-09-01",
      "endDate": "2024-01-01",
      "result": "获得校级一等奖",
      "link": "https://github.com/example/project"
    }
  ],
  "selfEvaluation": "热爱编程，擅长前端开发..."
}
```

### 4. 项目管理 API

#### 4.1 获取项目列表
```http
GET /api/projects?page=1&pageSize=10&category=AI&skills[]=Vue.js&targetAudience=school
```

**查询参数**:
- `page`: 页码 (默认: 1)
- `pageSize`: 每页数量 (默认: 10)
- `category`: 项目分类
- `skills[]`: 技能标签数组
- `targetAudience`: 目标受众 (school/department/national)

#### 4.2 获取项目详情
```http
GET /api/projects/{id}
```

#### 4.3 创建项目
```http
POST /api/projects
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "智能校园导航系统",
  "description": "基于AI的校园导航应用，提供最优路径规划",
  "targetAudience": "school",
  "tags": ["AI", "导航", "Vue.js"],
  "jobs": [
    {
      "title": "前端开发工程师",
      "description": "负责Vue3前端开发",
      "requiredSkills": ["Vue.js", "TypeScript", "Tailwind CSS"],
      "headcount": 2,
      "salary": {
        "min": 3000,
        "max": 5000,
        "currency": "CNY"
      }
    },
    {
      "title": "后端开发工程师",
      "description": "负责Python后端开发",
      "requiredSkills": ["Python", "FastAPI", "PostgreSQL"],
      "headcount": 1
    }
  ]
}
```

#### 4.4 更新项目
```http
PUT /api/projects/{id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "更新后的项目标题",
  "description": "更新后的项目描述"
}
```

#### 4.5 删除项目
```http
DELETE /api/projects/{id}
Authorization: Bearer <token>
```

#### 4.6 申请岗位
```http
POST /api/projects/{projectId}/jobs/{jobId}/apply
Authorization: Bearer <token>
Content-Type: application/json

{
  "resumeId": 1,
  "note": "我对这个项目很感兴趣，希望能加入团队"
}
```

#### 4.7 获取项目申请列表
```http
GET /api/projects/{id}/applications
Authorization: Bearer <token>
```

#### 4.8 处理申请
```http
PATCH /api/projects/{projectId}/applications/{applicationId}
Authorization: Bearer <token>
Content-Type: application/json

{
  "action": "accept" // 或 "reject"
}
```

#### 4.9 收藏项目
```http
POST /api/projects/{id}/favorite
Authorization: Bearer <token>
```

#### 4.10 取消收藏
```http
DELETE /api/projects/{id}/favorite
Authorization: Bearer <token>
```

#### 4.11 获取收藏的项目
```http
GET /api/projects/favorites
Authorization: Bearer <token>
```

#### 4.12 搜索项目
```http
GET /api/projects/search?q=关键词
```

### 5. 比赛管理 API

#### 5.1 获取比赛列表
```http
GET /api/competitions?page=1&pageSize=10&category=算法
```

#### 5.2 获取比赛详情
```http
GET /api/competitions/{id}
```

#### 5.3 创建比赛
```http
POST /api/competitions
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "蓝桥杯程序设计大赛",
  "organizer": "蓝桥杯组委会",
  "deadline": "2024-03-15",
  "tags": ["算法", "编程"],
  "description": "全国性的程序设计竞赛",
  "poster": "https://example.com/poster.jpg"
}
```

### 6. 分享管理 API

#### 6.1 获取分享列表
```http
GET /api/shares?category=CS&page=1&pageSize=10
```

#### 6.2 获取分享详情
```http
GET /api/shares/{id}
```

#### 6.3 创建分享
```http
POST /api/shares
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Vue3 + TypeScript 最佳实践",
  "content": "分享Vue3和TypeScript的使用经验...",
  "techStack": ["Vue3", "TypeScript", "Vite"],
  "category": "CS"
}
```

### 7. 消息管理 API

#### 7.1 获取聊天列表
```http
GET /api/messages/conversations
Authorization: Bearer <token>
```

#### 7.2 获取聊天记录
```http
GET /api/messages/conversations/{userId}
Authorization: Bearer <token>
```

#### 7.3 发送消息
```http
POST /api/messages/send
Authorization: Bearer <token>
Content-Type: application/json

{
  "receiverId": 2,
  "content": "你好，我对你的项目很感兴趣",
  "type": "text"
}
```

#### 7.4 获取系统通知
```http
GET /api/notifications?page=1&pageSize=10
Authorization: Bearer <token>
```

#### 7.5 标记通知为已读
```http
PATCH /api/notifications/{id}/read
Authorization: Bearer <token>
```

### 8. 分类管理 API

#### 8.1 获取所有分类
```http
GET /api/categories
```

#### 8.2 根据类型获取分类
```http
GET /api/categories?type=shares
```

#### 8.3 获取活跃分类
```http
GET /api/categories?isActive=true
```

#### 8.4 创建分类（管理员）
```http
POST /api/categories
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "新分类",
  "type": "shares", // competitions, projects, shares
  "order": 1,
  "isActive": true
}
```

#### 8.5 更新分类（管理员）
```http
PUT /api/categories/{id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "更新后的分类名",
  "order": 2,
  "isActive": false
}
```

#### 8.6 删除分类（管理员）
```http
DELETE /api/categories/{id}
Authorization: Bearer <token>
```

### 9. 首页数据 API

#### 9.1 获取轮播图
```http
GET /api/home/banners
```

**响应示例**:
```json
[
  {
    "id": 1,
    "title": "蓝桥杯程序设计大赛",
    "image": "/banners/lanqiao.jpg",
    "link": "/competition/1",
    "order": 1,
    "isActive": true
  }
]
```

#### 9.2 获取首页比赛列表
```http
GET /api/home/competitions?limit=10&category=算法
```

**查询参数**:
- `limit`: 返回数量限制 (默认: 10)
- `category`: 比赛分类

#### 9.3 获取首页项目列表
```http
GET /api/home/projects?limit=10&status=recruiting
```

**查询参数**:
- `limit`: 返回数量限制 (默认: 10)
- `status`: 项目状态 (recruiting/in_progress/completed)

#### 9.4 获取首页分享列表
```http
GET /api/home/shares?limit=20&category=AI
```

**查询参数**:
- `limit`: 返回数量限制 (默认: 20)
- `category`: 分享分类 (AI/CS/EE)

#### 9.5 获取首页公告列表
```http
GET /api/home/announcements?limit=5&type=system
```

**查询参数**:
- `limit`: 返回数量限制 (默认: 5)
- `type`: 公告类型 (system/competition/project)

**响应示例**:
```json
[
  {
    "id": 1,
    "title": "平台功能更新通知",
    "content": "新增了更多功能，欢迎体验！",
    "type": "system",
    "isImportant": true,
    "createdAt": "2024-01-15T10:00:00Z"
  }
]
```

#### 9.6 获取热门标签
```http
GET /api/home/hot-tags
```

**响应示例**:
```json
["#蓝桥杯", "#互联网+", "#数模竞赛", "#AI", "#Vue.js"]
```

#### 9.7 获取首页统计数据
```http
GET /api/home/stats
```

**响应示例**:
```json
{
  "totalUsers": 1000,
  "totalProjects": 50,
  "totalCompetitions": 10,
  "hotTopics": [
    {
      "id": 1,
      "title": "Vue3 组合式API最佳实践",
      "tag": "Vue3",
      "count": 156
    }
  ]
}
```

### 10. 管理后台 API

#### 10.1 获取举报内容列表
```http
GET /api/admin/reports?status=pending&page=1&pageSize=10
Authorization: Bearer <token>
```

#### 10.2 处理举报
```http
PATCH /api/admin/reports/{id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "action": "approve", // 或 "reject"
  "reason": "处理原因"
}
```

#### 10.3 获取用户统计
```http
GET /api/admin/stats/users
Authorization: Bearer <token>
```

#### 10.4 获取项目统计
```http
GET /api/admin/stats/projects
Authorization: Bearer <token>
```

#### 10.5 获取待审核项目
```http
GET /api/admin/projects/pending?page=1&pageSize=10
Authorization: Bearer <token>
```

#### 10.6 审核项目
```http
PATCH /api/admin/projects/{id}/review
Authorization: Bearer <token>
Content-Type: application/json

{
  "action": "approve", // 或 "reject"
  "reason": "审核意见"
}
```

### 错误处理

所有API在发生错误时都会返回以下格式：

```json
{
  "success": false,
  "message": "错误描述",
  "code": "ERROR_CODE"
}
```

常见错误码：
- `400`: 请求参数错误
- `401`: 未授权访问
- `403`: 权限不足
- `404`: 资源不存在
- `422`: 数据验证失败
- `500`: 服务器内部错误

### 认证说明

1. 用户登录后获取JWT token
2. 在后续请求中，在请求头中添加：`Authorization: Bearer <token>`
3. token过期时，服务器返回401状态码
4. 前端自动清除token并跳转到登录页

## 开发指南

### 代码规范

- 使用ESLint进行代码检查
- 使用Prettier进行代码格式化
- 遵循Vue 3组合式API最佳实践
- 使用TypeScript进行类型检查

### 组件开发

- 组件使用组合式API
- Props使用TypeScript接口定义
- 事件使用defineEmits声明
- 样式使用Tailwind CSS类名

### 状态管理

- 使用Pinia进行状态管理
- Store按功能模块划分
- 异步操作使用try-catch处理错误
- 计算属性用于派生状态

### API调用

- 使用封装的apiClient进行HTTP请求
- 统一错误处理，包括网络错误和服务器错误
- 请求拦截器自动添加token
- 响应拦截器处理401错误
- 使用Promise.allSettled处理并发请求
- 网络错误时显示默认数据，确保用户体验

### 错误处理

- 使用ErrorBoundary组件捕获组件渲染错误
- 统一的错误页面显示不同类型的错误
- 支持404、403、500、网络错误等多种错误类型
- 自动跳转到错误页面处理API错误
- 提供重试、返回首页等操作选项
- 开发环境显示详细错误信息

## 部署说明

### 环境变量

创建`.env`文件：

```env
VITE_API_BASE_URL=http://localhost:8000/api
VITE_APP_TITLE=SmartEdu
```

### 生产构建

```bash
npm run build
```

构建产物在`dist`目录中。

### Nginx配置

```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /path/to/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://backend-server:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 贡献指南

1. Fork项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

