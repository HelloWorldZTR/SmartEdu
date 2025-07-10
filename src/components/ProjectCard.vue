<template>
  <div class="card hover:shadow-md transition-shadow duration-200">
    <div class="flex justify-between items-start mb-3">
      <h3 class="text-lg font-semibold text-gray-900 line-clamp-2">
        {{ project.title }}
      </h3>
      <span class="text-xs px-2 py-1 rounded-full" :class="statusClass">
        {{ statusText }}
      </span>
    </div>
    
    <p class="text-sm text-gray-600 mb-4 line-clamp-2">
      {{ project.description }}
    </p>
    
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center space-x-2">
        <img
          :src="project.creator.avatar || '/default-avatar.png'"
          :alt="project.creator.username"
          class="w-6 h-6 rounded-full object-cover"
        />
        <span class="text-sm text-gray-700">{{ project.creator.username }}</span>
      </div>
      <span class="text-xs text-gray-500">{{ project.creator.school }}</span>
    </div>
    
    <div class="flex items-center justify-between">
      <div class="flex space-x-1">
        <span
          v-for="tag in getTagsSlice(project.tags)"
          :key="tag"
          class="tag"
        >
          {{ tag }}
        </span>
        <span v-if="getTagsCount(project.tags) > 3" class="text-xs text-gray-500">
          +{{ getTagsCount(project.tags) - 3 }}
        </span>
      </div>
      
      <router-link
        :to="`/team/${project.id}`"
        class="text-sm text-primary-600 hover:text-primary-700 font-medium"
      >
        查看详情 →
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
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

const getTagsSlice = (tags: any[]) => {
  return tags.slice(0, 3)
}

const getTagsCount = (tags: any[]) => {
  return tags.length
}
</script> 