import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { User } from '@/types'
import { userApi } from '@/api/user'

export const useUserStore = defineStore('user', () => {
  const currentUser = ref<User | null>(null)
  const isAuthenticated = ref(false)
  const isLoading = ref(false)

  // 计算属性
  const userLevel = computed(() => currentUser.value?.level || 0)
  const userPoints = computed(() => currentUser.value?.points || 0)
  const userSkills = computed(() => currentUser.value?.skills || [])

  // Actions
  const login = async (email: string, password: string) => {
    try {
      isLoading.value = true
      const response = await userApi.login(email, password)
      
      // 保存JWT token - response现在是直接的token对象
      localStorage.setItem('token', response.access)
      localStorage.setItem('refreshToken', response.refresh)
      
      // 获取用户信息
      const userResponse = await userApi.getCurrentUser()
      currentUser.value = userResponse
      isAuthenticated.value = true
      
      return response
    } catch (error) {
      throw error
    } finally {
      isLoading.value = false
    }
  }

  const logout = async () => {
    try {
      await userApi.logout()
    } catch (error) {
      console.error('Logout error:', error)
    } finally {
      // 清除token和用户信息
      localStorage.removeItem('token')
      localStorage.removeItem('refreshToken')
      currentUser.value = null
      isAuthenticated.value = false
    }
  }

  const register = async (userData: {
    username: string
    email: string
    password: string
    school: string
    department: string
  }) => {
    try {
      isLoading.value = true
      const response = await userApi.register(userData)
      
      // 注册成功后，用户需要登录
      // 这里可以选择自动登录或者跳转到登录页
      currentUser.value = response.data
      isAuthenticated.value = true
      
      return response
    } catch (error) {
      throw error
    } finally {
      isLoading.value = false
    }
  }

  const updateProfile = async (profileData: Partial<User>) => {
    try {
      isLoading.value = true
      const response = await userApi.updateProfile(profileData)
      currentUser.value = response.data
      return response
    } catch (error) {
      throw error
    } finally {
      isLoading.value = false
    }
  }

  const fetchCurrentUser = async () => {
    try {
      isLoading.value = true
      const response = await userApi.getCurrentUser()
      currentUser.value = response
      isAuthenticated.value = true
      return response
    } catch (error) {
      currentUser.value = null
      isAuthenticated.value = false
      throw error
    } finally {
      isLoading.value = false
    }
  }

  return {
    // State
    currentUser,
    isAuthenticated,
    isLoading,
    
    // Getters
    userLevel,
    userPoints,
    userSkills,
    
    // Actions
    login,
    logout,
    register,
    updateProfile,
    fetchCurrentUser
  }
}) 