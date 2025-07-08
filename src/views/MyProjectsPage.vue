<template>
  <div class="min-h-screen bg-gray-50">
    <TopNavBar />
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <!-- 主内容区 -->
        <div class="lg:col-span-3 space-y-6">
          <!-- 标签页导航 -->
          <div class="border-b border-gray-200 mb-4">
            <nav class="-mb-px flex space-x-8">
              <button
                v-for="tab in tabs"
                :key="tab.key"
                @click="activeTab = tab.key"
                :class="[
                  'py-2 px-1 border-b-2 font-medium text-sm',
                  activeTab === tab.key
                    ? 'border-primary-500 text-primary-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                ]"
              >
                {{ tab.label }}
                <span
                  v-if="tab.count !== undefined"
                  :class="[
                    'ml-2 px-2 py-0.5 text-xs rounded-full',
                    activeTab === tab.key
                      ? 'bg-primary-100 text-primary-800'
                      : 'bg-gray-100 text-gray-600'
                  ]"
                >
                  {{ tab.count }}
                </span>
              </button>
            </nav>
          </div>

          <!-- 筛选器 -->
          <div class="mb-4 flex flex-wrap gap-4 items-center">
            <CustomSelect
              v-model="filters.status"
              :options="statusOptions"
              class="w-40"
            />
            <button
              @click="loadData"
              class="px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500"
              :disabled="loading"
            >
              <span v-if="loading" class="inline-block animate-spin mr-2">⟳</span>
              刷新
            </button>
          </div>

          <!-- 加载状态 -->
          <div v-if="loading" class="flex justify-center items-center py-12">
            <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
          </div>

          <!-- 我创建的项目 -->
          <div v-else-if="activeTab === 'created'">
            <div v-if="createdProjects.length === 0" class="text-center py-12">
              <div class="text-gray-400 mb-4">
                <svg class="mx-auto h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
              <h3 class="text-lg font-medium text-gray-900 mb-2">还没有创建的项目</h3>
              <p class="text-gray-500 mb-4">开始创建您的第一个项目吧！</p>
              <router-link
                to="/launch-team"
                class="inline-flex items-center px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700"
              >
                创建项目
              </router-link>
            </div>
            <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <ProjectCard
                v-for="project in createdProjects"
                :key="project.id"
                :project="project"
              />
            </div>
          </div>

          <!-- 我参与的项目 -->
          <div v-else-if="activeTab === 'participated'">
            <div v-if="participatedProjects.length === 0" class="text-center py-12">
              <div class="text-gray-400 mb-4">
                <svg class="mx-auto h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </div>
              <h3 class="text-lg font-medium text-gray-900 mb-2">还没有参与的项目</h3>
              <p class="text-gray-500 mb-4">去发现一些有趣的项目并申请加入吧！</p>
              <router-link
                to="/"
                class="inline-flex items-center px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700"
              >
                浏览项目
              </router-link>
            </div>
            <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <ProjectCard
                v-for="project in participatedProjects"
                :key="project.id"
                :project="project"
              />
            </div>
          </div>

          <!-- 我的申请记录 -->
          <div v-else-if="activeTab === 'applications'">
            <div v-if="applications.length === 0" class="text-center py-12">
              <div class="text-gray-400 mb-4">
                <svg class="mx-auto h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                </svg>
              </div>
              <h3 class="text-lg font-medium text-gray-900 mb-2">还没有申请记录</h3>
              <p class="text-gray-500 mb-4">开始申请您感兴趣的项目岗位吧！</p>
              <router-link
                to="/"
                class="inline-flex items-center px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700"
              >
                浏览项目
              </router-link>
            </div>
            <div v-else class="space-y-4">
              <div
                v-for="application in applications"
                :key="application.id"
                class="bg-white border border-gray-200 rounded-lg p-6 hover:shadow-md transition-shadow"
              >
                <div class="flex justify-between items-start mb-4">
                  <div>
                    <h3 class="text-lg font-semibold text-gray-900">
                      {{ application.job.title }}
                    </h3>
                    <p class="text-sm text-gray-600">
                      项目：{{ application.job.project?.title || '未知项目' }}
                    </p>
                  </div>
                  <span
                    class="text-xs px-2 py-1 rounded-full"
                    :class="getApplicationStatusClass(application.status)"
                  >
                    {{ getApplicationStatusText(application.status) }}
                  </span>
                </div>
                <div class="flex items-center justify-between text-sm text-gray-600 mb-3">
                  <span>申请时间：{{ formatDate(application.appliedAt) }}</span>
                  <span v-if="application.note" class="text-gray-500">
                    备注：{{ application.note }}
                  </span>
                </div>
                <div class="flex justify-end space-x-2">
                  <router-link
                    :to="`/team/${application.job.project?.id}`"
                    class="text-sm text-primary-600 hover:text-primary-700 font-medium"
                  >
                    查看项目详情 →
                  </router-link>
                </div>
              </div>
            </div>
          </div>

          <!-- 分页 -->
          <div v-if="totalPages > 1" class="mt-8 flex justify-center">
            <nav class="flex space-x-2">
              <button
                @click="changePage(currentPage - 1)"
                :disabled="currentPage === 1"
                class="px-3 py-2 text-sm border border-gray-300 rounded-md hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                上一页
              </button>
              <span class="px-3 py-2 text-sm text-gray-700">
                第 {{ currentPage }} 页，共 {{ totalPages }} 页
              </span>
              <button
                @click="changePage(currentPage + 1)"
                :disabled="currentPage === totalPages"
                class="px-3 py-2 text-sm border border-gray-300 rounded-md hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                下一页
              </button>
            </nav>
          </div>
        </div>
        <!-- 侧边栏 -->
        <div class="lg:col-span-1 space-y-6">
          <Sidebar :tags="tags" :announcements="announcements" :topics="topics" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted, watch } from 'vue'
import TopNavBar from '@/components/TopNavBar.vue'
import Sidebar from '@/components/Sidebar.vue'
import { projectApi } from '@/api/project'
import ProjectCard from '@/components/ProjectCard.vue'
import type { Project, Application } from '@/types'
import CustomSelect from '@/components/CustomSelect.vue'
import { homeApi } from '@/api/home'

// 响应式数据
const activeTab = ref('created')
const loading = ref(false)
const currentPage = ref(1)
const pageSize = ref(12)

const createdProjects = ref<Project[]>([])
const participatedProjects = ref<Project[]>([])
const applications = ref<Application[]>([])

const totalCount = ref(0)
const totalPages = computed(() => Math.ceil(totalCount.value / pageSize.value))

const filters = reactive({
  status: ''
})

const tags = ref<string[]>([])
const announcements = ref<any[]>([])
const topics = ref<any[]>([])

// 状态选项
const statusOptions = [
  { value: '', label: '全部状态' },
  { value: 'recruiting', label: '招募中' },
  { value: 'in_progress', label: '进行中' },
  { value: 'completed', label: '已完成' },
]

// 标签页配置
const tabs = computed(() => [
  {
    key: 'created',
    label: '我创建的项目',
    count: createdProjects.value.length
  },
  {
    key: 'participated',
    label: '我参与的项目',
    count: participatedProjects.value.length
  },
  {
    key: 'applications',
    label: '我的申请',
    count: applications.value.length
  }
])

// 加载数据
const loadData = async () => {
  loading.value = true
  try {
    const params = {
      page: currentPage.value,
      pageSize: pageSize.value,
      ...(filters.status && { status: filters.status })
    }

    if (activeTab.value === 'created') {
      const response = await projectApi.getMyCreatedProjects(params)
      createdProjects.value = response.results
      totalCount.value = response.count
    } else if (activeTab.value === 'participated') {
      const response = await projectApi.getMyParticipatedProjects(params)
      participatedProjects.value = response.results
      totalCount.value = response.count
    } else if (activeTab.value === 'applications') {
      const response = await projectApi.getMyApplications(params)
      applications.value = response.results
      totalCount.value = response.count
    }
  } catch (error) {
    console.error('加载数据失败:', error)
  } finally {
    loading.value = false
  }
}

// 切换页面
const changePage = (page: number) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page
    loadData()
  }
}

// 申请状态样式
const getApplicationStatusClass = (status: string) => {
  switch (status) {
    case 'pending':
      return 'bg-yellow-100 text-yellow-800'
    case 'accepted':
      return 'bg-green-100 text-green-800'
    case 'rejected':
      return 'bg-red-100 text-red-800'
    default:
      return 'bg-gray-100 text-gray-800'
  }
}

// 申请状态文本
const getApplicationStatusText = (status: string) => {
  switch (status) {
    case 'pending':
      return '待处理'
    case 'accepted':
      return '已通过'
    case 'rejected':
      return '已拒绝'
    default:
      return '未知'
  }
}

// 格式化日期
const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('zh-CN')
}

// 加载Sidebar数据
const loadSidebarData = async () => {
  try {
    // 获取标签
    const tagsResponse = await homeApi.getTags()
    let tagData = []
    if (Array.isArray(tagsResponse)) {
      tagData = tagsResponse
    } else if (tagsResponse && typeof tagsResponse === 'object' && 'results' in tagsResponse && Array.isArray((tagsResponse as any).results)) {
      tagData = (tagsResponse as any).results
    } else {
      console.warn('Tags response format is unexpected:', tagsResponse)
      tagData = []
    }
    tags.value = tagData.map((tag: any) => `#${tag.name}`)

    // 获取公告
    const annResponse = await homeApi.getAnnouncements({ limit: 5 })
    let announcementData = []
    if (Array.isArray(annResponse)) {
      announcementData = annResponse
    } else if (annResponse && typeof annResponse === 'object' && 'results' in annResponse && Array.isArray((annResponse as any).results)) {
      announcementData = (annResponse as any).results
    } else {
      console.warn('Announcements response format is unexpected:', annResponse)
      announcementData = []
    }
    announcements.value = announcementData

    // 获取话题
    const topicsResponse = await homeApi.getTopics()
    let topicData = []
    if (Array.isArray(topicsResponse)) {
      topicData = topicsResponse
    } else if (topicsResponse && typeof topicsResponse === 'object' && 'results' in topicsResponse && Array.isArray((topicsResponse as any).results)) {
      topicData = (topicsResponse as any).results
    } else {
      console.warn('Topics response format is unexpected:', topicsResponse)
      topicData = []
    }
    topics.value = topicData
  } catch (error) {
    console.error('Failed to fetch sidebar data:', error)
  }
}

// 监听标签页切换
watch(activeTab, () => {
  currentPage.value = 1
  loadData()
})

// 监听筛选器变化
watch(filters, () => {
  currentPage.value = 1
  loadData()
}, { deep: true })

// 组件挂载时加载数据
onMounted(() => {
  loadData()
  loadSidebarData()
})
</script>

<style scoped>
.card {
  @apply bg-white border border-gray-200 rounded-lg p-6;
}

.tag {
  @apply px-2 py-1 text-xs bg-gray-100 text-gray-700 rounded-full;
}
</style> 