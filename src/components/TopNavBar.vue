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

        <!-- User Menu / Login -->
        <div class="flex items-center space-x-4">
          <!-- 登录/注册 或 头像 -->
          <div v-if="userStore.isAuthenticated" class="flex items-center space-x-2">
            <!-- 发布按钮下拉菜单 -->
            <div class="relative">
              <button
                @click="togglePublishMenu"
                class="p-2 text-gray-600 hover:text-primary-600 hover:bg-primary-50 rounded-full transition-colors duration-200"
                title="发布"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                </svg>
              </button>
              <!-- 发布下拉菜单 -->
              <div
                v-if="showPublishMenu"
                class="absolute right-0 mt-2 w-40 bg-white rounded-md shadow-lg py-1 z-50 border border-gray-200"
              >
                <router-link
                  to="/launch-team"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                  @click="showPublishMenu = false"
                >
                  发起组队
                </router-link>
                <router-link
                  to="/publish-share"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                  @click="showPublishMenu = false"
                >
                  发布分享
                </router-link>
              </div>
            </div>
            
            <!-- 用户头像 -->
            <div class="relative">
              <button
                @click="toggleUserMenu"
                class="flex items-center text-gray-700 hover:text-primary-600 transition-colors duration-200 rounded-xl overflow-hidden focus:outline-none focus:ring-2 focus:ring-primary-500"
                style="padding: 0;"
              >
                <div class="relative">
                  <img
                    :src="userStore.currentUser?.avatar || '/default-avatar.png'"
                    :alt="userStore.currentUser?.username"
                    class="w-9 h-9 rounded-xl object-cover border border-gray-200"
                  />
                  <!-- 未读消息红点 -->
                  <span
                    v-if="unreadCount > 0"
                    class="absolute -top-0.5 -right-0.5 bg-red-500 text-white text-xs rounded-full h-4 w-4 flex items-center justify-center border border-white"
                  >
                    {{ unreadCount > 99 ? '99+' : unreadCount }}
                  </span>
                </div>
              </button>
              <!-- User Dropdown Menu -->
              <div
                v-if="showUserMenu"
                class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-50 border border-gray-200"
              >
                <router-link
                  to="/profile"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                  @click="showUserMenu = false"
                >
                  个人主页
                </router-link>
                <router-link
                  to="/resume"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                  @click="showUserMenu = false"
                >
                  我的简历
                </router-link>
                <router-link
                  to="/messages"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 flex items-center justify-between"
                  @click="showUserMenu = false"
                >
                  <span>私信</span>
                  <span
                    v-if="unreadCount > 0"
                    class="bg-red-500 text-white text-xs rounded-full h-4 w-4 flex items-center justify-center"
                  >
                    {{ unreadCount > 99 ? '99+' : unreadCount }}
                  </span>
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
          </div>
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
          <div v-if="userStore.isAuthenticated" class="mt-2">
            <button
              @click="() => { goToProfile(); showMobileMenu = false }"
              class="flex items-center w-full px-3 py-2 rounded-xl text-gray-600 hover:text-primary-600 text-base font-medium"
            >
              我的主页
            </button>
            <div class="mt-2 space-y-1">
              <router-link
                to="/messages"
                class="block px-3 py-2 text-gray-600 hover:text-primary-600 text-base font-medium flex items-center justify-between"
                @click="showMobileMenu = false"
              >
                <span>私信</span>
                <span
                  v-if="unreadCount > 0"
                  class="bg-red-500 text-white text-xs rounded-full h-4 w-4 flex items-center justify-center"
                >
                  {{ unreadCount > 99 ? '99+' : unreadCount }}
                </span>
              </router-link>
            </div>
          </div>
          <div v-else class="mt-2 flex space-x-2">
            <router-link
              to="/login"
              class="flex-1 text-center text-gray-600 hover:text-primary-600 px-3 py-2 rounded-md text-base font-medium transition-colors duration-200"
              @click="showMobileMenu = false"
            >
              登录
            </router-link>
            <router-link
              to="/register"
              class="flex-1 btn-primary text-base text-center"
              @click="showMobileMenu = false"
            >
              注册
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()

const showUserMenu = ref(false)
const showMobileMenu = ref(false)
const showPublishMenu = ref(false)
const unreadCount = ref(0)

const navItems = [
  { name: '首页', path: '/' },
  { name: '组队大厅', path: '/team-hall' },
]

const isActive = (path: string) => {
  return route.path === path
}

const toggleUserMenu = (e?: Event) => {
  if (e) e.stopPropagation()
  showUserMenu.value = !showUserMenu.value
}

const toggleMobileMenu = () => {
  showMobileMenu.value = !showMobileMenu.value
}

const togglePublishMenu = () => {
  showPublishMenu.value = !showPublishMenu.value
}

const goToProfile = () => {
  router.push('/profile')
  showUserMenu.value = false
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
    showPublishMenu.value = false
  }
}

// ESC键关闭下拉框
const handleKeydown = (event: KeyboardEvent) => {
  if (event.key === 'Escape') {
    showUserMenu.value = false
    showPublishMenu.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  document.addEventListener('keydown', handleKeydown)
  // 这里应该获取未读消息数量
  unreadCount.value = 3 // 模拟数据
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
  document.removeEventListener('keydown', handleKeydown)
})
</script> 