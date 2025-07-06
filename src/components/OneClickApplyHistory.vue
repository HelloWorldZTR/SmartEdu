<template>
  <div class="card">
    <h2 class="text-xl font-semibold text-gray-900 mb-4">申请历史</h2>
    <div class="space-y-3">
      <div
        v-for="application in applications"
        :key="application.id"
        class="border border-gray-200 rounded-lg p-4"
      >
        <div class="flex items-start justify-between">
          <div>
            <h3 class="text-sm font-medium text-gray-900">{{ application.projectTitle }}</h3>
            <p class="text-xs text-gray-600 mt-1">{{ application.jobTitle }}</p>
            <p class="text-xs text-gray-500 mt-2">申请时间: {{ application.appliedAt }}</p>
          </div>
          <span class="text-xs px-2 py-1 rounded-full" :class="getStatusClass(application.status)">
            {{ getStatusText(application.status) }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const applications = ref([
  {
    id: 1,
    projectTitle: '智能校园导航系统',
    jobTitle: '前端开发工程师',
    status: 'pending',
    appliedAt: '2024-01-15 10:30'
  }
])

const getStatusClass = (status: string) => {
  switch (status) {
    case 'pending':
      return 'bg-yellow-100 text-yellow-800'
    case 'accepted':
      return 'bg-green-100 text-green-800'
    case 'rejected':
      return 'bg-red-100 text-red-800'
    default:
      return 'bg-gray-100 text-gray-800'
  }
}

const getStatusText = (status: string) => {
  switch (status) {
    case 'pending':
      return '待处理'
    case 'accepted':
      return '已通过'
    case 'rejected':
      return '已拒绝'
    default:
      return '未知'
  }
}
</script> 