import { apiClient } from './index'
import type { Project, Application, PaginatedResponse, ApiResponse } from '@/types'

export const projectApi = {
  // 项目列表
  getProjects: (params?: {
    page?: number
    pageSize?: number
    category?: string
    skills?: string[]
    targetAudience?: string
  }) => apiClient.get<PaginatedResponse<Project>>('/projects', params),

  // 项目详情
  getProjectById: (id: number) => apiClient.get<Project>(`/projects/${id}`),

  // 创建项目
  createProject: (projectData: {
    title: string
    description: string
    targetAudience: 'school' | 'department' | 'national'
    tags: string[]
    jobs: {
      title: string
      description: string
      requiredSkills: string[]
      headcount: number
      salary?: {
        min: number
        max: number
        currency: string
      }
    }[]
  }) => apiClient.post<ApiResponse<Project>>('/projects', projectData),

  // 更新项目
  updateProject: (id: number, projectData: Partial<Project>) =>
    apiClient.put<ApiResponse<Project>>(`/projects/${id}`, projectData),

  // 删除项目
  deleteProject: (id: number) => apiClient.delete(`/projects/${id}`),

  // 申请岗位
  applyToJob: (
    projectId: number,
    jobId: number,
    applicationData: {
      resumeId: number
      note?: string
    }
  ) =>
    apiClient.post<Application>(
      `/projects/${projectId}/jobs/${jobId}/apply`,
      applicationData
    ),

  // 获取项目申请
  getProjectApplications: (projectId: number) =>
    apiClient.get<Application[]>(`/projects/${projectId}/applications`),

  // 处理申请
  handleApplication: (
    projectId: number,
    applicationId: number,
    action: 'accept' | 'reject'
  ) =>
    apiClient.patch<Application>(
      `/projects/${projectId}/applications/${applicationId}`,
      { action }
    ),

  // 收藏项目
  favoriteProject: (projectId: number) =>
    apiClient.post(`/projects/${projectId}/favorite`),

  // 取消收藏
  unfavoriteProject: (projectId: number) =>
    apiClient.delete(`/projects/${projectId}/favorite`),

  // 获取收藏的项目
  getFavoriteProjects: () =>
    apiClient.get<Project[]>('/projects/favorites'),

  // 搜索项目
  searchProjects: (query: string) =>
    apiClient.get<PaginatedResponse<Project>>('/projects/search', { q: query }),
} 