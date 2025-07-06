<template>
  <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <div class="text-center">
        <!-- 错误图标 -->
        <div class="mx-auto flex items-center justify-center h-24 w-24 rounded-full bg-red-100 mb-6">
          <svg class="h-12 w-12 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z" />
          </svg>
        </div>
        
        <!-- 错误标题 -->
        <h1 class="text-4xl font-bold text-gray-900 mb-4">
          {{ errorTitle }}
        </h1>
        
        <!-- 错误描述 -->
        <p class="text-lg text-gray-600 mb-8 max-w-md mx-auto">
          {{ errorDescription }}
        </p>
        
        <!-- 错误代码 -->
        <div v-if="errorCode" class="mb-8">
          <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800">
            错误代码: {{ errorCode }}
          </span>
        </div>
        
        <!-- 操作按钮 -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <button
            @click="goHome"
            class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            返回首页
          </button>
          
          <button
            @click="goBack"
            class="inline-flex items-center px-6 py-3 border border-gray-300 text-base font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            返回上页
          </button>
          
          <button
            v-if="errorType === 'server'"
            @click="retry"
            class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-blue-600 bg-blue-100 hover:bg-blue-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            重试
          </button>
        </div>
        
        <!-- 额外信息 -->
        <div v-if="errorType === 'server'" class="mt-8 text-sm text-gray-500">
          <p>如果问题持续存在，请联系技术支持</p>
          <p class="mt-2">
            <a href="mailto:support@smartedu.com" class="text-blue-600 hover:text-blue-500">
              support@smartedu.com
            </a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

// 从路由参数获取错误信息
const errorType = computed(() => route.params.type as string || '404')
const errorCode = computed(() => route.params.code as string || '')

// 根据错误类型设置显示内容
const errorTitle = computed(() => {
  switch (errorType.value) {
    case '404':
      return '页面未找到'
    case '403':
      return '访问被拒绝'
    case '500':
      return '服务器错误'
    case 'server':
      return '服务暂时不可用'
    case 'network':
      return '网络连接错误'
    default:
      return '发生错误'
  }
})

const errorDescription = computed(() => {
  switch (errorType.value) {
    case '404':
      return '抱歉，您访问的页面不存在或已被移除。请检查网址是否正确，或返回首页继续浏览。'
    case '403':
      return '抱歉，您没有权限访问此页面。请确认您已登录并具有相应权限。'
    case '500':
      return '服务器内部发生错误，我们正在努力修复。请稍后再试。'
    case 'server':
      return '服务器暂时无法响应，可能是由于维护或网络问题。请稍后再试。'
    case 'network':
      return '网络连接出现问题，请检查您的网络连接后重试。'
    default:
      return '发生了一个意外错误，请稍后再试。'
  }
})

// 导航方法
const goHome = () => {
  router.push('/')
}

const goBack = () => {
  if (window.history.length > 1) {
    router.back()
  } else {
    router.push('/')
  }
}

const retry = () => {
  // 重新加载当前页面
  window.location.reload()
}
</script> 