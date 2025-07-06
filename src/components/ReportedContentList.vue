<template>
  <div class="card">
    <h3 class="text-lg font-semibold text-gray-900 mb-4">举报内容</h3>
    <div class="space-y-3">
      <div
        v-for="report in reports"
        :key="report.id"
        class="border border-gray-200 rounded-lg p-4"
      >
        <div class="flex items-start justify-between">
          <div>
            <h4 class="text-sm font-medium text-gray-900">{{ report.title }}</h4>
            <p class="text-xs text-gray-600 mt-1">{{ report.content }}</p>
            <p class="text-xs text-gray-500 mt-2">举报时间: {{ report.reportedAt }}</p>
          </div>
          <div class="flex space-x-2">
            <button class="text-xs px-2 py-1 bg-red-100 text-red-800 rounded">
              处理
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const reports = ref([
  {
    id: 1,
    title: '不当内容举报',
    content: '用户举报某项目包含不当内容',
    reportedAt: '2024-01-15 10:30'
  }
])
</script> 