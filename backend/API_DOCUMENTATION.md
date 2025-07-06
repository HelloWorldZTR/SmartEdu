# SmartEdu API 文档

## 基础信息

- **基础URL**: `http://localhost:8000/api/`
- **认证方式**: JWT Token
- **内容类型**: `application/json`

## 认证

### 获取Token
```http
POST /api/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

### 刷新Token
```http
POST /api/token/refresh/
Content-Type: application/json

{
    "refresh": "your_refresh_token"
}
```

## 用户模块 (users)

### 用户注册
```http
POST /api/register/
Content-Type: application/json

{
    "username": "newuser",
    "email": "user@example.com",
    "password": "password123",
    "first_name": "张",
    "last_name": "三"
}
```

### 用户登录
```http
POST /api/login/
Content-Type: application/json

{
    "username": "username",
    "password": "password"
}
```

### 用户登出
```http
POST /api/logout/
Authorization: Bearer <token>
```

### 获取用户信息
```http
GET /api/user/info/
Authorization: Bearer <token>
```

### 更新用户信息
```http
PUT /api/user/info/
Authorization: Bearer <token>
Content-Type: application/json

{
    "first_name": "新名字",
    "last_name": "新姓氏",
    "school": "清华大学",
    "department": "计算机系"
}
```

### 获取用户简历
```http
GET /api/user/resume/
Authorization: Bearer <token>
```

### 更新用户简历
```http
PUT /api/user/resume/
Authorization: Bearer <token>
Content-Type: application/json

{
    "education": [
        {
            "school": "清华大学",
            "major": "计算机科学与技术",
            "degree": "本科",
            "graduation_year": 2024
        }
    ],
    "skills": ["Python", "Django", "Vue.js"],
    "projects": [
        {
            "name": "项目名称",
            "description": "项目描述",
            "role": "开发者"
        }
    ],
    "self_evaluation": "自我评价"
}
```

### 获取用户统计
```http
GET /api/user/stats/
Authorization: Bearer <token>
```

## 分类模块 (categories)

### 获取分类列表
```http
GET /api/categories/
```

### 获取分类详情
```http
GET /api/categories/{id}/
```

## 项目模块 (projects)

### 获取项目列表
```http
GET /api/projects/
Query Parameters:
- page: 页码
- pageSize: 每页数量
- category: 分类ID
- skills: 技能数组
- targetAudience: 目标受众 (school/department/national)
```

### 获取项目详情
```http
GET /api/projects/{id}/
```

### 创建项目
```http
POST /api/projects/
Authorization: Bearer <token>
Content-Type: application/json

{
    "title": "项目标题",
    "description": "项目描述",
    "targetAudience": "school",
    "tags": ["标签1", "标签2"],
    "jobs": [
        {
            "title": "岗位标题",
            "description": "岗位描述",
            "requiredSkills": ["技能1", "技能2"],
            "headcount": 2,
            "salary": {
                "min": 5000,
                "max": 8000,
                "currency": "CNY"
            }
        }
    ]
}
```

### 更新项目
```http
PUT /api/projects/{id}/
Authorization: Bearer <token>
Content-Type: application/json

{
    "title": "新标题",
    "description": "新描述"
}
```

### 删除项目
```http
DELETE /api/projects/{id}/
Authorization: Bearer <token>
```

### 申请岗位
```http
POST /api/projects/{project_id}/jobs/{job_id}/apply/
Authorization: Bearer <token>
Content-Type: application/json

{
    "resumeId": 1,
    "note": "申请说明"
}
```

### 获取项目申请
```http
GET /api/projects/{project_id}/applications/
Authorization: Bearer <token>
```

### 处理申请
```http
PATCH /api/projects/{project_id}/applications/{application_id}/
Authorization: Bearer <token>
Content-Type: application/json

{
    "action": "accept"  // 或 "reject"
}
```

### 收藏项目
```http
POST /api/projects/{project_id}/favorite/
Authorization: Bearer <token>
```

### 取消收藏
```http
DELETE /api/projects/{project_id}/favorite/
Authorization: Bearer <token>
```

### 获取收藏的项目
```http
GET /api/projects/favorites/
Authorization: Bearer <token>
```

### 搜索项目
```http
GET /api/projects/search/
Query Parameters:
- q: 搜索关键词
```

## 比赛模块 (competitions)

### 获取比赛列表
```http
GET /api/competitions/
```

### 获取比赛详情
```http
GET /api/competitions/{id}/
```

## 分享模块 (shares)

### 获取分享列表
```http
GET /api/shares/
```

### 获取分享详情
```http
GET /api/shares/{id}/
```

### 创建分享
```http
POST /api/shares/
Authorization: Bearer <token>
Content-Type: application/json

{
    "title": "分享标题",
    "content": "分享内容",
    "category": 1,
    "tech_stack": ["技术1", "技术2"]
}
```

### 更新分享
```http
PUT /api/shares/{id}/
Authorization: Bearer <token>
Content-Type: application/json

{
    "title": "新标题",
    "content": "新内容"
}
```

### 删除分享
```http
DELETE /api/shares/{id}/
Authorization: Bearer <token>
```

## 聊天模块 (chat)

### 获取对话列表
```http
GET /api/messages/conversations/
Authorization: Bearer <token>
```

### 获取对话详情
```http
GET /api/messages/conversations/{conversation_id}/
Authorization: Bearer <token>
```

### 发送消息
```http
POST /api/messages/send/
Authorization: Bearer <token>
Content-Type: application/json

{
    "conversation": 1,
    "content": "消息内容",
    "message_type": "text"
}
```

### 获取通知列表
```http
GET /api/notifications/
Authorization: Bearer <token>
```

### 标记通知为已读
```http
PATCH /api/notifications/{notification_id}/read/
Authorization: Bearer <token>
```

## 首页模块 (home)

### 获取轮播图
```http
GET /api/home/banners/
```

### 获取首页比赛
```http
GET /api/home/competitions/
Query Parameters:
- limit: 限制数量
- category: 分类
```

### 获取首页项目
```http
GET /api/home/projects/
Query Parameters:
- limit: 限制数量
- status: 状态
```

### 获取首页分享
```http
GET /api/home/shares/
Query Parameters:
- limit: 限制数量
- category: 分类
```

### 获取公告列表
```http
GET /api/home/announcements/
Query Parameters:
- limit: 限制数量
- type: 公告类型
```

### 获取热门标签
```http
GET /api/home/hot-tags/
```

### 获取首页统计
```http
GET /api/home/stats/
```

## 管理员模块 (admin_dashboard)

### 获取举报列表
```http
GET /api/admin/reports/
Authorization: Bearer <token>
Query Parameters:
- type: 举报类型
- status: 状态
```

### 获取举报详情
```http
GET /api/admin/reports/{id}/
Authorization: Bearer <token>
```

### 处理举报
```http
PUT /api/admin/reports/{id}/
Authorization: Bearer <token>
Content-Type: application/json

{
    "status": "approved",
    "admin_note": "处理说明"
}
```

### 获取管理员统计
```http
GET /api/admin/stats/
Authorization: Bearer <token>
```

## 响应格式

### 成功响应
```json
{
    "id": 1,
    "title": "示例标题",
    "created_at": "2024-01-01T00:00:00Z"
}
```

### 分页响应
```json
{
    "count": 100,
    "next": "http://localhost:8000/api/projects/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "项目1"
        },
        {
            "id": 2,
            "title": "项目2"
        }
    ]
}
```

### 错误响应
```json
{
    "error": "错误信息",
    "detail": "详细错误描述"
}
```

## 状态码

- `200` - 成功
- `201` - 创建成功
- `400` - 请求错误
- `401` - 未认证
- `403` - 权限不足
- `404` - 资源不存在
- `500` - 服务器错误

## Django Admin

访问 `http://localhost:8000/admin/` 可以进入Django管理界面，管理所有数据模型。

### 主要管理功能：

1. **用户管理** - 管理用户账户、简历、统计信息
2. **项目管理** - 管理项目、岗位、申请、收藏
3. **分类管理** - 管理各种分类
4. **比赛管理** - 管理比赛信息
5. **分享管理** - 管理用户分享
6. **聊天管理** - 管理对话和消息
7. **首页管理** - 管理轮播图、公告、热门标签等
8. **举报管理** - 处理用户举报

所有模型都已配置了合适的列表显示、过滤器、搜索功能和字段分组。 