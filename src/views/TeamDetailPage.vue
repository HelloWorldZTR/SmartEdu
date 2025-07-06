<template>
  <div class="min-h-screen bg-gray-50">
    <TopNavBar />
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <!-- 主要内容 -->
        <div class="lg:col-span-3 space-y-6">
          <!-- 项目头部 -->
          <ProjectHeader v-if="projectStore.currentProject" :project="projectStore.currentProject" />
          
          <!-- 项目描述 -->
          <ProjectDescription v-if="projectStore.currentProject" :project="projectStore.currentProject" />
          
          <!-- 岗位列表 -->
          <JobPostingsSection v-if="projectStore.currentProject" :project="projectStore.currentProject" />
          
          <!-- 申请表单 -->
          <ApplySection v-if="projectStore.currentProject" :project="projectStore.currentProject" />
        </div>
        
        <!-- 侧边栏 -->
        <div class="lg:col-span-1 space-y-6">
          <SimilarProjects />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import TopNavBar from '@/components/TopNavBar.vue'
import ProjectHeader from '@/components/ProjectHeader.vue'
import ProjectDescription from '@/components/ProjectDescription.vue'
import JobPostingsSection from '@/components/JobPostingsSection.vue'
import ApplySection from '@/components/ApplySection.vue'
import SimilarProjects from '@/components/SimilarProjects.vue'
import { useProjectStore } from '@/stores/project'

const route = useRoute()
const projectStore = useProjectStore()

onMounted(async () => {
  const projectId = parseInt(route.params.id as string)
  if (projectId) {
    await projectStore.fetchProjectById(projectId)
  }
})
</script> 