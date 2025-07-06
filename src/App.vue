<template>
  <ErrorBoundary>
    <div id="app" class="min-h-screen bg-gray-50">
      <router-view />
    </div>
  </ErrorBoundary>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import ErrorBoundary from '@/components/ErrorBoundary.vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

// 初始化用户认证状态
onMounted(async () => {
  const token = localStorage.getItem('token')
  if (token) {
    try {
      await userStore.fetchCurrentUser()
    } catch (error) {
      console.error('Failed to fetch current user:', error)
      // 如果获取用户信息失败，清除token
      localStorage.removeItem('token')
      localStorage.removeItem('refreshToken')
    }
  }
})
</script> 