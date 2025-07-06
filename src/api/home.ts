import { apiClient } from './index'
import type { Competition, Project, Share } from '@/types'

// 轮播图类型
export interface Banner {
  id: number
  title: string
  image: string
  link: string
  order: number
  isActive: boolean
}

// 公告类型
export interface Announcement {
  id: number
  title: string
  content: string
  type: 'system' | 'competition' | 'project'
  isImportant: boolean
  createdAt: string
}

export const homeApi = {
  // 获取轮播图
  getBanners: () => apiClient.get<Banner[]>('/home/banners'),

  // 获取比赛列表
  getCompetitions: (params?: { limit?: number; category?: string }) =>
    apiClient.get<Competition[]>('/home/competitions', params),

  // 获取项目列表
  getProjects: (params?: { limit?: number; status?: string }) =>
    apiClient.get<Project[]>('/home/projects', params),

  // 获取分享列表
  getShares: (params?: { limit?: number; category?: string }) =>
    apiClient.get<Share[]>('/home/shares', params),

  // 获取公告列表
  getAnnouncements: (params?: { limit?: number; type?: string }) =>
    apiClient.get<Announcement[]>('/home/announcements', params),

  // 获取首页统计数据
  getHomeStats: () => apiClient.get('/home/stats'),

  // 获取热门标签
  getHotTags: () => apiClient.get<string[]>('/home/hot-tags'),
} 