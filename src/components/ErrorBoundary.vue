<template>
  <div v-if="hasError" class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
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
          应用发生错误
        </h1>
        
        <!-- 错误描述 -->
        <p class="text-lg text-gray-600 mb-8 max-w-md mx-auto">
          抱歉，应用遇到了一个意外错误。请尝试刷新页面或联系技术支持。
        </p>
        
        <!-- 错误详情（开发环境） -->
        <div v-if="isDevelopment" class="mb-8 p-4 bg-gray-100 rounded-lg text-left">
          <p class="text-sm font-medium text-gray-700 mb-2">错误详情：</p>
          <pre class="text-xs text-gray-600 overflow-auto">{{ errorDetails }}</pre>
        </div>
        
        <!-- 操作按钮 -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <button
            @click="reload"
            class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            刷新页面
          </button>
          
          <button
            @click="goHome"
            class="inline-flex items-center px-6 py-3 border border-gray-300 text-base font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            返回首页
          </button>
        </div>
        
        <!-- 联系信息 -->
        <div class="mt-8 text-sm text-gray-500">
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
  
  <slot v-else />
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

interface Props {
  error?: Error
}

const props = withDefaults(defineProps<Props>(), {
  error: undefined
})

const router = useRouter()
const hasError = ref(false)
const errorDetails = ref('')

// 检查是否为开发环境
const isDevelopment = computed(() => process.env.NODE_ENV === 'development')

// 设置错误
const setError = (error: Error) => {
  hasError.value = true
  errorDetails.value = error.stack || error.message
  console.error('ErrorBoundary caught error:', error)
}

// 清除错误
const clearError = () => {
  hasError.value = false
  errorDetails.value = ''
}

// 如果有传入的错误，立即显示
if (props.error) {
  setError(props.error)
}

// 暴露方法给父组件
defineExpose({
  setError,
  clearError
})

// 导航方法
const goHome = () => {
  router.push('/')
}

const reload = () => {
  window.location.reload()
}

// 全局错误处理
const handleGlobalError = (event: ErrorEvent) => {
  setError(event.error || new Error(event.message))
}

// 全局未处理的Promise拒绝
const handleUnhandledRejection = (event: PromiseRejectionEvent) => {
  setError(new Error(event.reason?.message || 'Unhandled Promise Rejection'))
}

// 在组件挂载时添加全局错误监听器
const addGlobalErrorListeners = () => {
  window.addEventListener('error', handleGlobalError)
  window.addEventListener('unhandledrejection', handleUnhandledRejection)
}

// 在组件卸载时移除全局错误监听器
const removeGlobalErrorListeners = () => {
  window.removeEventListener('error', handleGlobalError)
  window.removeEventListener('unhandledrejection', handleUnhandledRejection)
}

// 生命周期钩子
import { onMounted, onUnmounted } from 'vue'

onMounted(() => {
  addGlobalErrorListeners()
})

onUnmounted(() => {
  removeGlobalErrorListeners()
})
</script> 