import { apiClient } from './index'
import type { User, Resume } from '@/types'

export const userApi = {
  // 用户认证
  login: (email: string, password: string) =>
    apiClient.post<{ user: User; token: string }>('/auth/login', {
      email,
      password,
    }),

  register: (userData: {
    username: string
    email: string
    password: string
    school: string
    department: string
  }) =>
    apiClient.post<{ user: User; token: string }>('/auth/register', userData),

  logout: () => apiClient.post('/auth/logout'),

  // 用户信息
  getCurrentUser: () => apiClient.get<User>('/user/me'),

  updateProfile: (profileData: Partial<User>) =>
    apiClient.put<User>('/user/profile', profileData),

  getUserById: (id: number) => apiClient.get<User>(`/user/${id}`),

  // 简历相关
  getResume: () => apiClient.get<Resume>('/user/resume'),

  updateResume: (resumeData: Partial<Resume>) =>
    apiClient.put<Resume>('/user/resume', resumeData),

  // 用户统计
  getUserStats: (userId: number) =>
    apiClient.get(`/user/${userId}/stats`),

  // 用户项目
  getUserProjects: (userId: number) =>
    apiClient.get(`/user/${userId}/projects`),

  // 用户申请
  getUserApplications: (userId: number) =>
    apiClient.get(`/user/${userId}/applications`),
} 