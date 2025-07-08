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
          <template v-if="isManager">
            <div class="card">
              <h3 class="text-lg font-semibold text-gray-900 mb-4">项目管理</h3>
              <div>
                <h4 class="text-md font-semibold text-gray-800 mb-2">队员列表</h4>
                <ul class="space-y-2">
                  <li v-for="member in acceptedMembers" :key="member.id">
                    <span class="text-sm text-gray-700">{{ member.applicant.username }}</span>
                    <span class="text-xs text-gray-400 ml-2">({{ member.jobTitle }})</span>
                  </li>
                </ul>
              </div>
              <button class="w-full py-2 mb-4 bg-red-600 text-white rounded hover:bg-red-700 transition" @click="endProject">
                结束项目
              </button>   
            </div>
          </template>
          <SimilarProjects/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, watch, computed } from 'vue'
import { useRoute } from 'vue-router'
import TopNavBar from '@/components/TopNavBar.vue'
import ProjectHeader from '@/components/ProjectHeader.vue'
import ProjectDescription from '@/components/ProjectDescription.vue'
import JobPostingsSection from '@/components/JobPostingsSection.vue'
import ApplySection from '@/components/ApplySection.vue'
import SimilarProjects from '@/components/SimilarProjects.vue'
import { useProjectStore } from '@/stores/project'
import { useUserStore } from '@/stores/user'

const route = useRoute()
const projectStore = useProjectStore()
const userStore = useUserStore()

const isManager = computed(() => {
  return (
    projectStore.currentProject &&
    userStore.currentUser &&
    projectStore.currentProject.creator.id === userStore.currentUser.id
  )
})

const acceptedMembers = computed(() => {
  if (!projectStore.currentProject) return [];
  const members = [];
  for (const job of projectStore.currentProject.jobs || []) {
    for (const application of job.applications || []) {
      if (application.status === 'accepted') {
        members.push({ ...application, jobTitle: job.title });
      }
    }
  }
  return members;
});

onMounted(async () => {
  const projectId = parseInt(route.params.id as string)
  if (projectId) {
    await projectStore.fetchProjectById(projectId)
  }
})

const endProject = () => {
  // TODO: 调用API结束项目
  alert('结束项目功能开发中')
}
</script> 