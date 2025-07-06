import { apiClient } from './index'
import type { Category } from '@/types'

export const categoryApi = {
  // 获取所有分类
  getCategories: () => apiClient.get<Category[]>('/categories'),

  // 根据类型获取分类
  getCategoriesByType: (type: string) => 
    apiClient.get<Category[]>(`/categories?type=${type}`),

  // 获取活跃的分类
  getActiveCategories: () => 
    apiClient.get<Category[]>('/categories?isActive=true'),

  // 创建分类（管理员）
  createCategory: (categoryData: Omit<Category, 'id'>) =>
    apiClient.post<Category>('/categories', categoryData),

  // 更新分类（管理员）
  updateCategory: (id: string, categoryData: Partial<Category>) =>
    apiClient.put<Category>(`/categories/${id}`, categoryData),

  // 删除分类（管理员）
  deleteCategory: (id: string) =>
    apiClient.delete(`/categories/${id}`),
} 