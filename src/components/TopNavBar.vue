<template>
  <nav class="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <div class="flex items-center">
          <router-link to="/" class="flex items-center space-x-2">
            <div class="w-8 h-8 bg-primary-600 rounded-lg flex items-center justify-center">
              <span class="text-white font-bold text-lg">S</span>
            </div>
            <span class="text-xl font-bold text-gray-900">SmartEdu</span>
          </router-link>
        </div>

        <!-- Navigation Links -->
        <div class="hidden md:flex items-center space-x-8">
          <router-link
            v-for="item in navItems"
            :key="item.name"
            :to="item.path"
            class="text-gray-600 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200"
            :class="{ 'text-primary-600 bg-primary-50': isActive(item.path) }"
          >
            {{ item.name }}
          </router-link>
        </div>

        <!-- User Menu -->
        <div class="flex items-center space-x-4">
          <!-- Messages Icon -->
          <router-link
            to="/messages"
            class="relative p-2 text-gray-600 hover:text-primary-600 transition-colors duration-200"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
            </svg>
            <span
              v-if="unreadCount > 0"
              class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center"
            >
              {{ unreadCount > 99 ? '99+' : unreadCount }}
            </span>
          </router-link>

          <!-- User Avatar -->
          <div v-if="userStore.isAuthenticated" class="relative">
            <button
              @click="toggleUserMenu"
              class="flex items-center space-x-2 text-gray-700 hover:text-primary-600 transition-colors duration-200"
            >
              <img
                :src="userStore.currentUser?.avatar || '/default-avatar.png'"
                :alt="userStore.currentUser?.username"
                class="w-8 h-8 rounded-full object-cover"
              />
              <span class="hidden sm:block text-sm font-medium">
                {{ userStore.currentUser?.username }}
              </span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            <!-- User Dropdown Menu -->
            <div
              v-if="showUserMenu"
              class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-50 border border-gray-200"
            >
              <router-link
                to="/profile"
                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
              >
                个人主页
              </router-link>
              <router-link
                to="/resume"
                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
              >
                我的简历
              </router-link>
              <router-link
                to="/launch-team"
                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
              >
                发起组队
              </router-link>
              <hr class="my-1" />
              <button
                @click="handleLogout"
                class="block w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
              >
                退出登录
              </button>
            </div>
          </div>

          <!-- Login Button -->
          <div v-else class="flex items-center space-x-2">
            <router-link
              to="/login"
              class="text-gray-600 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200"
            >
              登录
            </router-link>
            <router-link
              to="/register"
              class="btn-primary text-sm"
            >
              注册
            </router-link>
          </div>
        </div>

        <!-- Mobile menu button -->
        <div class="md:hidden">
          <button
            @click="toggleMobileMenu"
            class="text-gray-600 hover:text-primary-600 p-2"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile menu -->
      <div v-if="showMobileMenu" class="md:hidden">
        <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3 border-t border-gray-200">
          <router-link
            v-for="item in navItems"
            :key="item.name"
            :to="item.path"
            class="text-gray-600 hover:text-primary-600 block px-3 py-2 rounded-md text-base font-medium"
            :class="{ 'text-primary-600 bg-primary-50': isActive(item.path) }"
            @click="showMobileMenu = false"
          >
            {{ item.name }}
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'

const route = useRoute()
const userStore = useUserStore()

const showUserMenu = ref(false)
const showMobileMenu = ref(false)
const unreadCount = ref(0)

const navItems = [
  { name: '首页', path: '/' },
  { name: '组队大厅', path: '/team-hall' },
  { name: '我的', path: '/profile' },
  { name: '发起组队', path: '/launch-team' },
]

const isActive = (path: string) => {
  return route.path === path
}

const toggleUserMenu = () => {
  showUserMenu.value = !showUserMenu.value
}

const toggleMobileMenu = () => {
  showMobileMenu.value = !showMobileMenu.value
}

const handleLogout = async () => {
  try {
    await userStore.logout()
    showUserMenu.value = false
  } catch (error) {
    console.error('Logout failed:', error)
  }
}

// 点击外部关闭菜单
const handleClickOutside = (event: Event) => {
  const target = event.target as HTMLElement
  if (!target.closest('.relative')) {
    showUserMenu.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  // 这里应该获取未读消息数量
  unreadCount.value = 3 // 模拟数据
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script> 