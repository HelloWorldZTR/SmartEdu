<template>
  <div class="card">
    <h2 class="text-xl font-semibold text-gray-900 mb-4">招募岗位</h2>
    <div class="space-y-4">
      <div
        v-for="job in project.jobs"
        :key="job.id"
        class="border border-gray-200 rounded-lg p-4 hover:border-primary-300 transition-colors duration-200"
      >
        <div class="flex items-start justify-between mb-3">
          <div>
            <h3 class="text-lg font-medium text-gray-900">{{ job.title }}</h3>
            <p class="text-sm text-gray-600 mt-1">{{ job.description }}</p>
          </div>
          <div class="text-right">
            <span class="text-sm text-gray-500">招{{ job.headcount }}人</span>
            <div v-if="getSalaryInfo(job)" class="text-sm font-medium text-green-600 mt-1">
              {{ getSalaryInfo(job) }}
            </div>
          </div>
        </div>
        
        <div class="flex flex-wrap gap-2 mb-3">
          <span
            v-for="skill in getSkills(job)"
            :key="skill"
            class="tag"
          >
            {{ skill }}
          </span>
        </div>
        
        <div class="flex items-center justify-between">
          <span class="text-xs text-gray-500">
            已有{{ getApplicationsCount(job) }}人申请
          </span>
          <button
            @click="selectJob(job)"
            class="btn-primary text-sm"
          >
            申请岗位
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Project, Job } from '@/types'

interface Props {
  project: Project
}

defineProps<Props>()

const selectJob = (job: Job) => {
  // 处理岗位选择逻辑
  console.log('Selected job:', job)
}

// 获取薪资信息的辅助函数
const getSalaryInfo = (job: Job) => {
  if (job.salary) {
    return `${job.salary.min}-${job.salary.max}元`
  }
  if (job.salary_min !== undefined && job.salary_max !== undefined) {
    return `${job.salary_min}-${job.salary_max}元`
  }
  return null
}

// 获取技能列表的辅助函数
const getSkills = (job: Job) => {
  return job.requiredSkills || job.required_skills || []
}

// 获取申请人数的辅助函数
const getApplicationsCount = (job: Job) => {
  return job.applications?.length || 0
}
</script> 