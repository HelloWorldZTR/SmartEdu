<template>
  <div class="card hover:shadow-md transition-shadow duration-200">
    <div class="flex justify-between items-start mb-3">
      <h3 class="text-lg font-semibold text-gray-900 line-clamp-2">
        {{ project.title }}
      </h3>
      <button
        @click="$emit('favorite', project.id)"
        class="text-gray-400 hover:text-red-500 transition-colors duration-200"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
        </svg>
      </button>
    </div>
    
    <p class="text-sm text-gray-600 mb-4 line-clamp-2">
      {{ project.description }}
    </p>
    
    <!-- 招募岗位 -->
    <div class="mb-4">
      <h4 class="text-sm font-medium text-gray-700 mb-2">招募岗位</h4>
      <div class="space-y-2">
        <div
          v-for="job in getJobsSlice(project.jobs || [])"
          :key="job.id"
          class="flex items-center justify-between p-2 bg-gray-50 rounded-lg"
        >
          <div>
            <span class="text-sm font-medium text-gray-900">{{ job.title }}</span>
            <span class="text-xs text-gray-500 ml-2">招{{ job.headcount }}人</span>
          </div>
          <div v-if="getSalaryInfo(job)" class="text-xs text-green-600 font-medium">
            {{ getSalaryInfo(job) }}
          </div>
        </div>
        <div v-if="getJobsCount(project.jobs || []) > 3" class="text-xs text-gray-500 text-center">
          还有{{ getJobsCount(project.jobs || []) - 3 }}个岗位
        </div>
      </div>
    </div>
    
    <!-- 项目信息 -->
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
    
    <!-- 标签和操作 -->
    <div class="flex items-center justify-between">
      <div class="flex space-x-1">
        <span
          v-for="tag in getTagsSlice(project.tags || [])"
          :key="tag"
          class="tag"
        >
          {{ tag }}
        </span>
        <span v-if="getTagsCount(project.tags || []) > 3" class="text-xs text-gray-500">
          +{{ getTagsCount(project.tags || []) - 3 }}
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
import type { Project } from '@/types'

interface Props {
  project: Project
}

defineProps<Props>()

defineEmits<{
  favorite: [projectId: number]
}>()

const getSalaryInfo = (job: any) => {
  if (job.salary) {
    return `${job.salary.min}-${job.salary.max}元`
  }
  if (job.salary_min !== undefined && job.salary_max !== undefined) {
    return `${job.salary_min}-${job.salary_max}元`
  }
  return null
}

const getJobsSlice = (jobs: any[]) => {
  return (jobs || []).slice(0, 3)
}

const getJobsCount = (jobs: any[]) => {
  return (jobs || []).length
}

const getTagsSlice = (tags: any[]) => {
  return (tags || []).slice(0, 3)
}

const getTagsCount = (tags: any[]) => {
  return (tags || []).length
}
</script> 