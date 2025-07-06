import { apiClient } from './index'
import type { Share, PaginatedResponse, ApiResponse } from '@/types'

export const shareApi = {
  // 获取分享列表
  getShares: (params?: {
    page?: number
    pageSize?: number
    category?: string
  }) => apiClient.get<PaginatedResponse<Share>>('/shares', params),

  // 获取分享详情
  getShareById: (id: number) => apiClient.get<Share>(`/shares/${id}`),

  // 创建分享
  createShare: (shareData: {
    title: string
    content: string
    category: string
    techStack: string[]
  }) => apiClient.post<ApiResponse<Share>>('/shares', shareData),

  // 更新分享
  updateShare: (id: number, shareData: Partial<Share>) =>
    apiClient.put<ApiResponse<Share>>(`/shares/${id}`, shareData),

  // 删除分享
  deleteShare: (id: number) => apiClient.delete<ApiResponse<void>>(`/shares/${id}`),

  // 点赞分享
  likeShare: (id: number) => apiClient.post(`/shares/${id}/like`),

  // 取消点赞
  unlikeShare: (id: number) => apiClient.delete(`/shares/${id}/like`),
} 