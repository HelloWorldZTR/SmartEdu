<template>
  <div class="card">
    <h3 class="text-lg font-semibold text-gray-900 mb-4">相似项目</h3>
    <div class="space-y-3">
      <div
        v-for="project in similarProjects"
        :key="project.id"
        class="p-3 border border-gray-200 rounded-lg hover:border-primary-300 transition-colors duration-200 cursor-pointer"
        @click="goToProject(project.id)"
      >
        <h4 class="text-sm font-medium text-gray-900 line-clamp-1">{{ project.title }}</h4>
        <p class="text-xs text-gray-600 mt-1 line-clamp-2">{{ project.description }}</p>
        <div class="flex items-center justify-between mt-2">
          <span class="text-xs text-gray-500">{{ project.creator.username }}</span>
          <span class="text-xs text-primary-600">查看详情</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import type { Project } from '@/types'

const router = useRouter()

// 模拟相似项目数据
const similarProjects = ref<Project[]>([
  {
    id: 2,
    title: '智能图书馆管理系统',
    description: '基于Vue3和Python的图书馆管理系统',
    creator: {
      id: 2,
      username: '李四',
      email: 'lisi@example.com',
      school: '北京大学',
      department: '软件工程',
      level: 4,
      points: 800,
      skills: ['Vue.js', 'Python'],
      interests: ['Web开发'],
      createdAt: '2024-01-01'
    },
    targetAudience: 'school',
    tags: ['Vue.js', 'Python', '管理系统'],
    jobs: [],
    status: 'recruiting',
    createdAt: '2024-01-10',
    updatedAt: '2024-01-10'
  },
  {
    id: 3,
    title: '校园二手交易平台',
    description: '学生二手物品交易平台',
    creator: {
      id: 3,
      username: '王五',
      email: 'wangwu@example.com',
      school: '复旦大学',
      department: '计算机科学',
      level: 3,
      points: 600,
      skills: ['React', 'Node.js'],
      interests: ['全栈开发'],
      createdAt: '2024-01-01'
    },
    targetAudience: 'school',
    tags: ['React', 'Node.js', '交易平台'],
    jobs: [],
    status: 'recruiting',
    createdAt: '2024-01-05',
    updatedAt: '2024-01-05'
  }
])

const goToProject = (projectId: number) => {
  router.push(`/team/${projectId}`)
}
</script> 