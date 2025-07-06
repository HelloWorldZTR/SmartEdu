<template>
  <div class="min-h-screen bg-gray-50">
    <TopNavBar />
    
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      <div class="mb-6">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">我的简历</h1>
        <p class="text-gray-600">管理你的简历信息，提升求职成功率</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- 简历编辑器 -->
        <div class="lg:col-span-2 space-y-6">
          <ResumeEditor :resume="resume" @save="saveResume" />
        </div>
        
        <!-- 简历预览 -->
        <div class="lg:col-span-1">
          <ResumePreview :resume="resume" />
        </div>
      </div>
      
      <!-- 申请历史 -->
      <div class="mt-8">
        <OneClickApplyHistory />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import TopNavBar from '@/components/TopNavBar.vue'
import ResumeEditor from '@/components/ResumeEditor.vue'
import ResumePreview from '@/components/ResumePreview.vue'
import OneClickApplyHistory from '@/components/OneClickApplyHistory.vue'
import type { Resume } from '@/types'

const resume = ref<Resume>({
  id: 1,
  user: {
    id: 1,
    username: '张三',
    email: 'zhangsan@example.com',
    school: '清华大学',
    department: '计算机系',
    level: 5,
    points: 1200,
    skills: ['Vue.js', 'Python'],
    interests: ['AI', 'Web开发'],
    createdAt: '2024-01-01'
  },
  education: [
    {
      school: '清华大学',
      major: '计算机科学与技术',
      degree: '本科',
      startDate: '2020-09-01',
      endDate: '2024-07-01',
      gpa: 3.8
    }
  ],
  skills: ['Vue.js', 'React', 'TypeScript', 'Python', '机器学习'],
  projects: [
    {
      name: '智能校园导航系统',
      role: '前端开发',
      description: '基于Vue3的校园导航应用',
      startDate: '2023-09-01',
      endDate: '2024-01-01',
      result: '获得校级一等奖',
      link: 'https://github.com/example/project'
    }
  ],
  selfEvaluation: '热爱编程，擅长前端开发，有良好的团队协作能力',
  updatedAt: '2024-01-15'
})

const saveResume = async (updatedResume: Resume) => {
  try {
    // 这里应该调用API保存简历
    console.log('Saving resume:', updatedResume)
    resume.value = updatedResume
  } catch (error) {
    console.error('Save resume failed:', error)
  }
}

onMounted(() => {
  // 这里应该从API获取简历数据
  console.log('MyResumePage mounted')
})
</script> 