<template>
  <div class="min-h-screen bg-gray-50 p-8">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-3xl font-bold text-gray-900 mb-8">错误处理测试页面</h1>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- 路由错误测试 -->
        <div class="bg-white p-6 rounded-lg shadow">
          <h2 class="text-xl font-semibold mb-4">路由错误测试</h2>
          <div class="space-y-3">
            <button
              @click="test404"
              class="w-full px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
            >
              测试404错误
            </button>
            <button
              @click="test403"
              class="w-full px-4 py-2 bg-orange-600 text-white rounded hover:bg-orange-700"
            >
              测试403错误
            </button>
            <button
              @click="test500"
              class="w-full px-4 py-2 bg-purple-600 text-white rounded hover:bg-purple-700"
            >
              测试500错误
            </button>
            <button
              @click="testNetwork"
              class="w-full px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
            >
              测试网络错误
            </button>
          </div>
        </div>
        
        <!-- API错误测试 -->
        <div class="bg-white p-6 rounded-lg shadow">
          <h2 class="text-xl font-semibold mb-4">API错误测试</h2>
          <div class="space-y-3">
            <button
              @click="testApiError"
              class="w-full px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
            >
              测试API错误
            </button>
            <button
              @click="testNetworkError"
              class="w-full px-4 py-2 bg-yellow-600 text-white rounded hover:bg-yellow-700"
            >
              测试网络连接错误
            </button>
          </div>
        </div>
        
        <!-- 组件错误测试 -->
        <div class="bg-white p-6 rounded-lg shadow">
          <h2 class="text-xl font-semibold mb-4">组件错误测试</h2>
          <div class="space-y-3">
            <button
              @click="testComponentError"
              class="w-full px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700"
            >
              测试组件渲染错误
            </button>
            <button
              @click="testPromiseRejection"
              class="w-full px-4 py-2 bg-pink-600 text-white rounded hover:bg-pink-700"
            >
              测试Promise拒绝
            </button>
          </div>
        </div>
        
        <!-- 返回首页 -->
        <div class="bg-white p-6 rounded-lg shadow">
          <h2 class="text-xl font-semibold mb-4">导航</h2>
          <button
            @click="goHome"
            class="w-full px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700"
          >
            返回首页
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { apiClient } from '@/api'

const router = useRouter()

// 测试404错误
const test404 = () => {
  router.push('/error/404')
}

// 测试403错误
const test403 = () => {
  router.push('/error/403')
}

// 测试500错误
const test500 = () => {
  router.push('/error/500')
}

// 测试网络错误
const testNetwork = () => {
  router.push('/error/network')
}

// 测试API错误
const testApiError = async () => {
  try {
    await apiClient.get('/non-existent-endpoint')
  } catch (error) {
    console.log('API错误测试完成')
  }
}

// 测试网络连接错误
const testNetworkError = async () => {
  try {
    // 尝试访问一个不存在的服务器
    await apiClient.get('http://localhost:9999/test')
  } catch (error) {
    console.log('网络错误测试完成')
  }
}

// 测试组件渲染错误
const testComponentError = () => {
  throw new Error('这是一个测试的组件渲染错误')
}

// 测试Promise拒绝
const testPromiseRejection = () => {
  Promise.reject(new Error('这是一个测试的Promise拒绝'))
}

// 返回首页
const goHome = () => {
  router.push('/')
}
</script> 