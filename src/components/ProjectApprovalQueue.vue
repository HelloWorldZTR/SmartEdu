<template>
  <div class="card">
    <h3 class="text-lg font-semibold text-gray-900 mb-4">项目审核队列</h3>
    <div class="space-y-3">
      <div
        v-for="project in pendingProjects"
        :key="project.id"
        class="border border-gray-200 rounded-lg p-4"
      >
        <div class="flex items-start justify-between">
          <div>
            <h4 class="text-sm font-medium text-gray-900">{{ project.title }}</h4>
            <p class="text-xs text-gray-600 mt-1">{{ project.description }}</p>
            <p class="text-xs text-gray-500 mt-2">提交时间: {{ project.submittedAt }}</p>
          </div>
          <div class="flex space-x-2">
            <button class="text-xs px-2 py-1 bg-green-100 text-green-800 rounded">
              通过
            </button>
            <button class="text-xs px-2 py-1 bg-red-100 text-red-800 rounded">
              拒绝
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const pendingProjects = ref([
  {
    id: 1,
    title: '智能校园导航系统',
    description: '基于AI的校园导航应用',
    submittedAt: '2024-01-15 09:30'
  }
])
</script> 