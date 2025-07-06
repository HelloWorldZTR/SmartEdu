// 用户相关类型
export interface User {
  id: number
  username: string
  email: string
  avatar?: string
  school: string
  department: string
  bio?: string
  level: number
  points: number
  skills: string[]
  interests: string[]
  createdAt: string
}

// 分类相关类型
export interface Category {
  id: string
  name: string
  type: 'competitions' | 'projects' | 'shares'
  order: number
  isActive: boolean
}

// 项目相关类型
export interface Project {
  id: number
  title: string
  description: string
  creator: User
  targetAudience: 'school' | 'department' | 'national'
  tags: string[]
  jobs: Job[]
  status: 'recruiting' | 'in_progress' | 'completed'
  createdAt: string
  updatedAt: string
}

// 岗位相关类型
export interface Job {
  id: number
  title: string
  description: string
  requiredSkills: string[]
  required_skills?: string[]
  headcount: number
  salary?: {
    min: number
    max: number
    currency: string
  }
  salary_min?: number
  salary_max?: number
  salary_currency?: string
  applications: Application[]
}

// 申请相关类型
export interface Application {
  id: number
  applicant: User
  job: Job
  resume: Resume
  status: 'pending' | 'accepted' | 'rejected'
  note?: string
  appliedAt: string
}

// 简历相关类型
export interface Resume {
  id: number
  user: User
  education: Education[]
  skills: string[]
  projects: ProjectExperience[]
  selfEvaluation: string
  updatedAt: string
}

// 教育经历
export interface Education {
  school: string
  major: string
  degree: string
  startDate: string
  endDate?: string
  gpa?: number
}

// 项目经验
export interface ProjectExperience {
  name: string
  role: string
  description: string
  startDate: string
  endDate?: string
  result?: string
  link?: string
}

// 比赛相关类型
export interface Competition {
  id: number
  title: string
  organizer: string
  deadline: string
  tags: string[]
  description: string
  poster?: string
}

// 分享相关类型
export interface Share {
  id: number
  title: string
  author: User
  content: string
  techStack: string[]
  category: 'AI' | 'CS' | 'EE'
  publishedAt: string
}

// 消息相关类型
export interface Message {
  id: number
  sender: User
  receiver: User
  content: string
  type: 'text' | 'image' | 'file'
  sentAt: string
  readAt?: string
}

// 系统通知
export interface Notification {
  id: number
  type: 'application' | 'project_update' | 'system'
  title: string
  content: string
  isRead: boolean
  createdAt: string
}

// API响应类型
export interface ApiResponse<T> {
  success: boolean
  data: T
  message?: string
}

// JWT Token响应类型
export interface JWTResponse {
  access: string
  refresh: string
}

export interface PaginatedResponse<T> {
  count: number
  next: string | null
  previous: string | null
  results: T[]
} 