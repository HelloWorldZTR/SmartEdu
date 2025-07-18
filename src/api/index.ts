import axios from 'axios'
import type { ApiResponse } from '@/types'
import { handleApiError, navigateToError } from '@/utils/error'

// 创建axios实例
const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// 请求拦截器
api.interceptors.request.use(
  (config) => {
    // 从localStorage获取token
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器
api.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    // 处理网络错误
    if (error.code === 'ECONNREFUSED' || error.code === 'ERR_NETWORK') {
      console.error('Network error:', error.message)
      // 网络错误时跳转到错误页面
      const errorInfo = handleApiError(error)
      navigateToError(errorInfo)
    }
    
    if (error.response?.status === 401) {
      // 清除token并跳转到登录页
      localStorage.removeItem('token')
      window.location.href = '/login'
    } else if (error.response?.status >= 500) {
      // 服务器错误时跳转到错误页面
      const errorInfo = handleApiError(error)
      navigateToError(errorInfo)
    }
    
    return Promise.reject(error)
  }
)

// 通用API方法
export const apiClient = {
  get: <T>(url: string, params?: any): Promise<T> =>
    api.get(url, { params }).then(res => res.data),
    
  post: <T>(url: string, data?: any): Promise<ApiResponse<T>> =>
    api.post(url, data).then(res => res.data),
    
  // 用于JWT token等直接返回数据的API
  postRaw: <T>(url: string, data?: any): Promise<T> =>
    api.post(url, data).then(res => res.data),
    
  put: <T>(url: string, data?: any): Promise<ApiResponse<T>> =>
    api.put(url, data).then(res => res.data),
    
  delete: <T>(url: string): Promise<ApiResponse<T>> =>
    api.delete(url).then(res => res.data),
    
  patch: <T>(url: string, data?: any): Promise<ApiResponse<T>> =>
    api.patch(url, data).then(res => res.data),
}

export default api 