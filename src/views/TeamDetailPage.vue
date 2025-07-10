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
          <JobPostingsSection v-if="projectStore.currentProject" :project="projectStore.currentProject" @select-job="handleSelectJob" />
          
          <!-- 申请表单 -->
          <ApplySection v-if="projectStore.currentProject && !isManager" :project="projectStore.currentProject" :selected-job-id="selectedJobId" />
        </div>
        
        <!-- 侧边栏 -->
        <div class="lg:col-span-1 space-y-6">
          <!-- 项目成员预览 -->
          <div class="card">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">项目成员</h3>
            
            <!-- 已加入成员 -->
            <div class="mb-6">
              <h4 class="text-md font-semibold text-gray-800 mb-3">已加入 ({{ joinedMembers.length }})</h4>
              <div class="space-y-3">
                <div v-for="member in joinedMembers" :key="member.id" class="flex items-center justify-between p-3 bg-green-50 rounded-lg">
                  <div class="flex items-center space-x-3">
                    <div class="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center text-white text-sm font-medium">
                      {{ member.username.charAt(0).toUpperCase() }}
                    </div>
                    <div>
                      <div class="text-sm font-medium text-gray-900">{{ member.username }}</div>
                      <div class="text-xs text-gray-500">{{ member.jobTitle }}</div>
                    </div>
                  </div>
                  <button 
                    @click="sendMessage(member.id)"
                    class="text-xs bg-primary-500 text-white px-2 py-1 rounded hover:bg-primary-600 transition"
                  >
                    私信
                  </button>
                </div>
              </div>
            </div>

            <!-- 申请列表 -->
            <div v-if="isManager">
              <h4 class="text-md font-semibold text-gray-800 mb-3">待处理申请 ({{ pendingApplications.length }})</h4>
              <div class="space-y-3">
                <div 
                  v-for="application in pendingApplications" 
                  :key="application.id" 
                  :data-application-id="application.id"
                  class="p-3 bg-yellow-50 rounded-lg transition-all duration-300"
                >
                  <div class="flex items-center space-x-3 mb-2">
                    <div class="w-8 h-8 bg-yellow-500 rounded-full flex items-center justify-center text-white text-sm font-medium">
                      {{ application.applicant.username.charAt(0).toUpperCase() }}
                    </div>
                    <div>
                      <div class="text-sm font-medium text-gray-900">{{ application.applicant.username }}</div>
                      <div class="text-xs text-gray-500">{{ application.job.title }}</div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-600 mb-3">{{ application.note || '无申请说明' }}</div>
                  <div class="flex space-x-2">
                    <button 
                      @click="handleApplication(application.id, 'accept')"
                      :disabled="processingApplication === application.id"
                      class="flex-1 text-xs bg-green-500 text-white px-2 py-1 rounded hover:bg-green-600 transition disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                      {{ processingApplication === application.id ? '处理中...' : '同意' }}
                    </button>
                    <button 
                      @click="handleApplication(application.id, 'reject')"
                      :disabled="processingApplication === application.id"
                      class="flex-1 text-xs bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600 transition disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                      {{ processingApplication === application.id ? '处理中...' : '否决' }}
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- 项目管理操作 -->
            <div v-if="isManager" class="mt-6 pt-6 border-t border-gray-200">
              <h4 class="text-md font-semibold text-gray-800 mb-3">项目管理</h4>
              <button class="w-full py-2 bg-red-600 text-white rounded hover:bg-red-700 transition" @click="endProject">
                结束项目
              </button>
            </div>
          </div>

          <SimilarProjects/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, watch, computed, ref } from 'vue'
import { useRoute } from 'vue-router'
import TopNavBar from '@/components/TopNavBar.vue'
import ProjectHeader from '@/components/ProjectHeader.vue'
import ProjectDescription from '@/components/ProjectDescription.vue'
import JobPostingsSection from '@/components/JobPostingsSection.vue'
import ApplySection from '@/components/ApplySection.vue'
import SimilarProjects from '@/components/SimilarProjects.vue'
import { useProjectStore } from '@/stores/project'
import { useUserStore } from '@/stores/user'
import { useToast } from 'vue-toastification'
import { projectApi } from '@/api/project'
import { useRouter } from 'vue-router'

const router = useRouter()
const route = useRoute()
const projectStore = useProjectStore()
const userStore = useUserStore()
const toast = useToast()

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

const selectedJobId = ref('')

// Dummy data for project members
const joinedMembers = ref([
  {
    id: 1,
    username: '张三',
    jobTitle: '前端开发'
  },
  {
    id: 2,
    username: '李四',
    jobTitle: '后端开发'
  },
  {
    id: 3,
    username: '王五',
    jobTitle: 'UI设计师'
  }
])

const pendingApplications = ref([
  {
    id: 1,
    applicant: {
      id: 4,
      username: '赵六'
    },
    job: {
      id: 1,
      title: '前端开发'
    },
    note: '我有3年前端开发经验，熟悉Vue.js和React'
  },
  {
    id: 2,
    applicant: {
      id: 5,
      username: '钱七'
    },
    job: {
      id: 2,
      title: '后端开发'
    },
    note: '熟悉Django和Python，有项目经验'
  }
])

const processingApplication = ref<number | null>(null)

const sendMessage = (userId: number) => {
  window.open(`/messages?userId=${userId}`, '_blank')
}

const handleApplication = async (applicationId: number, action: 'accept' | 'reject') => {
  processingApplication.value = applicationId
  try {
    if (action === 'accept') {
      // TODO: 调用API处理申请
      // const response = await projectApi.handleApplication(projectId, applicationId, action)
      
      // 模拟API调用延迟
      await new Promise(resolve => setTimeout(resolve, 1000))
      
      // 模拟成功响应
      const application = pendingApplications.value.find(app => app.id === applicationId)
      if (application) {
        // 将申请移动到已加入成员
        const newMember = {
          id: application.applicant.id,
          username: application.applicant.username,
          jobTitle: application.job.title
        }
        joinedMembers.value.push(newMember)
        
        // 从待处理申请中移除
        pendingApplications.value = pendingApplications.value.filter(app => app.id !== applicationId)
        
        toast.success('申请已同意，成员已加入项目')
      }
    } else if (action === 'reject') {
      // TODO: 调用API处理申请
      // const response = await projectApi.handleApplication(projectId, applicationId, action)
      
      // 模拟API调用延迟
      await new Promise(resolve => setTimeout(resolve, 1000))
      
      // 模拟成功响应
      const application = pendingApplications.value.find(app => app.id === applicationId)
      if (application) {
        // 显示删除动画
        const applicationElement = document.querySelector(`[data-application-id="${applicationId}"]`)
        if (applicationElement) {
          applicationElement.classList.add('animate-slide-out')
          setTimeout(() => {
            pendingApplications.value = pendingApplications.value.filter(app => app.id !== applicationId)
            toast.info('申请已拒绝')
          }, 300)
        } else {
          // 如果找不到元素，直接移除
          pendingApplications.value = pendingApplications.value.filter(app => app.id !== applicationId)
          toast.info('申请已拒绝')
        }
      }
    }
  } catch (error) {
    console.error('处理申请失败:', error)
    toast.error('操作失败，请稍后重试')
  } finally {
    processingApplication.value = null
  }
}

const handleSelectJob = (jobId: string|number) => {
  // 滚动到申请表单
  setTimeout(() => {
    const form = document.getElementById('apply-section-form')
    if (form) {
      form.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }, 100)
}

const fetchProjectMembers = async (projectId: number) => {
  const res = await projectApi.getProjectMembers(projectId)
  return res
}

onMounted(async () => {
  const projectId = parseInt(route.params.id as string)
  if (projectId) {
    await projectStore.fetchProjectById(projectId)
    const memberApplications = await fetchProjectMembers(projectId)
    let tempAccepted = []
    let tempPending = []
    for (const member of memberApplications) {
      if (member.status === 'accepted') {
        tempAccepted.push({
          id: member.applicant_id,
          username: member.applicant_name,
          jobTitle: member.job_title,
        })
      } else {
        tempPending.push({
          id: member.id,
          applicant: {
            id: member.applicant_id,
            username: member.applicant_name,
          },
          job: {
            id: member.job_id,
            title: member.job_title,
          },
          note: member.note,
        })
      }
    }
    joinedMembers.value = tempAccepted
    pendingApplications.value = tempPending
  }
})

const endProject = () => {
  // TODO: 调用API结束项目
  alert('结束项目功能开发中')
}
</script> 