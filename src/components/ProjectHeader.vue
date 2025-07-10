<template>
  <div class="card">
    <div class="flex items-start justify-between mb-4">
      <div class="flex-1">
        <h1 class="text-2xl font-bold text-gray-900 mb-2">{{ project.title }}</h1>
        <div class="flex items-center space-x-4 text-sm text-gray-600">
          <span>发起人: {{ project.creator.username }}</span>
          <span>{{ project.creator.school }}</span>
          <span>{{ formatDate(project.createdAt) }}</span>
        </div>
      </div>
      <span class="text-xs px-3 py-1 rounded-full" :class="statusClass">
        {{ statusText }}
      </span>
    </div>
    
    <div class="flex flex-wrap gap-2">
      <span
        v-for="tag in project.tags"
        :key="tag"
        class="tag"
      >
        {{ tag }}
      </span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { formatDate } from '@/utils/date'
import type { Project } from '@/types'

interface Props {
  project: Project
}

const props = defineProps<Props>()

const statusClass = computed(() => {
  switch (props.project.status) {
    case 'recruiting':
      return 'bg-green-100 text-green-800'
    case 'in_progress':
      return 'bg-primary-100 text-primary-800'
    case 'completed':
      return 'bg-gray-100 text-gray-800'
    default:
      return 'bg-gray-100 text-gray-800'
  }
})

const statusText = computed(() => {
  switch (props.project.status) {
    case 'recruiting':
      return '招募中'
    case 'in_progress':
      return '进行中'
    case 'completed':
      return '已完成'
    default:
      return '未知'
  }
})
</script> 