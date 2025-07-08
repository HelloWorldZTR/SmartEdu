import { apiClient } from './index'
import type { Competition, Project, Share } from '@/types'

// 分页响应类型
interface PaginatedResponse<T> {
  count: number
  next: string | null
  previous: string | null
  results: T[]
}

// 轮播图类型
export interface Banner {
  id: number
  title: string
  image: string
  description?: string
  link?: string
  order: number
  isActive?: boolean
  is_active?: boolean
  created_at?: string
}

// 公告类型
export interface Announcement {
  id: number
  title: string
  content: string
  type: 'system' | 'competition' | 'project'
  announcement_type?: 'system' | 'competition' | 'project'
  isImportant?: boolean
  is_important?: boolean
  createdAt?: string
  created_at?: string
}

export const homeApi = {
  // 获取轮播图
  getBanners: () => apiClient.get<PaginatedResponse<Banner>>('/home/banners'),

  // 获取比赛列表
  getCompetitions: (params?: { limit?: number; category?: string }) =>
    apiClient.get<PaginatedResponse<Competition>>('/home/competitions', params),

  // 获取项目列表
  getProjects: (params?: { limit?: number; status?: string }) =>
    apiClient.get<PaginatedResponse<Project>>('/home/projects', params),

  // 获取分享列表
  getShares: (params?: { limit?: number; category?: string }) =>
    apiClient.get<PaginatedResponse<Share>>('/home/shares', params),

  // 获取公告列表
  getAnnouncements: (params?: { limit?: number; type?: string }) =>
    apiClient.get<PaginatedResponse<Announcement>>('/home/announcements', params),

  // // 获取首页统计数据
  // getHomeStats: () => apiClient.get('/home/stats'),

  // 获取标签
  getTags: () => apiClient.get<PaginatedResponse<string>>('/tags'),

  // 获取话题
  getTopics: () => apiClient.get<PaginatedResponse<{
    id: number
    title: string
    tag: string
    count: number
  }>>('/topics'),
} 