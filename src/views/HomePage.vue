<template>
  <div class="min-h-screen bg-gray-50">
    <TopNavBar />
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      <!-- 调试信息 -->
      <div v-if="isLoading" class="mb-4 p-4 bg-blue-50 border border-blue-200 rounded-lg">
        <p class="text-blue-700">正在加载数据...</p>
      </div>
      
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <!-- 主要内容区域 -->
        <div class="lg:col-span-3 space-y-6">
          <!-- 轮播图 -->
          <CarouselBanner :banners="banners" />
          
          <!-- 分类标签 -->
          <CategoryTabs 
            :active-tab="activeTab"
            :categories="categories"
            @tab-change="handleTabChange"
          />
          
          <!-- 内容列表 -->
          <div class="space-y-4">
            <!-- 比赛列表 -->
            <div v-if="activeTab === 'competitions'" class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <CompetitionCard
                v-for="competition in competitions"
                :key="competition.id"
                :competition="competition"
              />
            </div>
            
            <!-- 项目列表 -->
            <div v-if="activeTab === 'projects'" class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <ProjectCard
                v-for="project in projects"
                :key="project.id"
                :project="project"
              />
            </div>
            
            <!-- 分享列表 -->
            <div v-if="currentCategoryType === 'shares'" class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <ShareCard
                v-for="share in filteredShares"
                :key="share.id"
                :share="share"
              />
            </div>
          </div>
        </div>
        
        <!-- 侧边栏 -->
        <div class="lg:col-span-1 space-y-6">
          <Sidebar 
            :hot-tags="hotTags"
            :announcements="announcements"
            :hot-topics="homeStats?.hotTopics || []"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import TopNavBar from '@/components/TopNavBar.vue'
import CarouselBanner from '@/components/CarouselBanner.vue'
import CategoryTabs from '@/components/CategoryTabs.vue'
import CompetitionCard from '@/components/CompetitionCard.vue'
import ProjectCard from '@/components/ProjectCard.vue'
import ShareCard from '@/components/ShareCard.vue'
import Sidebar from '@/components/Sidebar.vue'
import { categoryApi } from '@/api/category'
import { homeApi } from '@/api/home'
import type { Competition, Project, Share, Category } from '@/types'
import type { Banner, Announcement } from '@/api/home'

const activeTab = ref('competitions')
const categories = ref<Category[]>([])
const isLoading = ref(false)

// 数据状态
const banners = ref<Banner[]>([])
const competitions = ref<Competition[]>([])
const projects = ref<Project[]>([])
const shares = ref<Share[]>([])
const announcements = ref<Announcement[]>([])
const hotTags = ref<string[]>([])
const homeStats = ref<any>(null)

const handleTabChange = (tab: string) => {
  activeTab.value = tab
}

// 获取当前分类类型
const currentCategoryType = computed(() => {
  const currentCategory = categories.value.find(cat => cat.id === activeTab.value)
  return currentCategory?.type || 'competitions'
})

// 根据当前选中的标签过滤分享内容
const filteredShares = computed(() => {
  const currentCategory = categories.value.find(cat => cat.id === activeTab.value)
  if (currentCategory && currentCategory.type === 'shares') {
    return shares.value.filter(share => share.category === activeTab.value)
  }
  return []
})

// 获取分类数据
const fetchCategories = async () => {
  try {
    const response = await categoryApi.getActiveCategories()
    categories.value = response.data.sort((a, b) => a.order - b.order)
    
    // 如果没有分类数据，设置默认分类
    if (categories.value.length === 0) {
      categories.value = [
        { id: 'competitions', name: '比赛', type: 'competitions', order: 1, isActive: true },
        { id: 'projects', name: '项目', type: 'projects', order: 2, isActive: true },
        { id: 'AI', name: 'AI', type: 'shares', order: 3, isActive: true },
        { id: 'CS', name: 'CS', type: 'shares', order: 4, isActive: true },
        { id: 'EE', name: 'EE', type: 'shares', order: 5, isActive: true }
      ]
    }
    
    // 设置默认选中的标签
    if (categories.value.length > 0) {
      activeTab.value = categories.value[0].id
    }
  } catch (error) {
    console.error('Failed to fetch categories:', error)
    // 设置默认分类作为后备
    categories.value = [
      { id: 'competitions', name: '比赛', type: 'competitions', order: 1, isActive: true },
      { id: 'projects', name: '项目', type: 'projects', order: 2, isActive: true },
      { id: 'AI', name: 'AI', type: 'shares', order: 3, isActive: true },
      { id: 'CS', name: 'CS', type: 'shares', order: 4, isActive: true },
      { id: 'EE', name: 'EE', type: 'shares', order: 5, isActive: true }
    ]
    // 确保设置默认选中的标签
    activeTab.value = 'competitions'
  }
}

// 获取轮播图数据
const fetchBanners = async () => {
  try {
    const response = await homeApi.getBanners()
    banners.value = response.data.filter(banner => banner.isActive).sort((a, b) => a.order - b.order)
  } catch (error) {
    console.error('Failed to fetch banners:', error)
    // 设置默认轮播图作为后备
    banners.value = [
      {
        id: 1,
        title: '蓝桥杯程序设计大赛',
        image: '/banners/lanqiao.jpg',
        link: '/competition/1',
        order: 1,
        isActive: true
      },
      {
        id: 2,
        title: '互联网+创新创业大赛',
        image: '/banners/internet-plus.jpg',
        link: '/competition/2',
        order: 2,
        isActive: true
      }
    ]
  }
}

// 获取比赛数据
const fetchCompetitions = async () => {
  try {
    const response = await homeApi.getCompetitions({ limit: 10 })
    competitions.value = response.data
  } catch (error) {
    console.error('Failed to fetch competitions:', error)
    // 设置默认比赛数据作为后备
    competitions.value = [
      {
        id: 1,
        title: '蓝桥杯程序设计大赛',
        organizer: '蓝桥杯组委会',
        deadline: '2024-03-15',
        tags: ['算法', '编程'],
        description: '全国性的程序设计竞赛'
      },
      {
        id: 2,
        title: '互联网+创新创业大赛',
        organizer: '教育部',
        deadline: '2024-04-20',
        tags: ['创业', '创新'],
        description: '大学生创新创业竞赛'
      }
    ]
  }
}

// 获取项目数据
const fetchProjects = async () => {
  try {
    const response = await homeApi.getProjects({ limit: 10, status: 'recruiting' })
    projects.value = response.data
  } catch (error) {
    console.error('Failed to fetch projects:', error)
    // 设置默认项目数据作为后备
    projects.value = [
      {
        id: 1,
        title: '智能校园导航系统',
        description: '基于AI的校园导航应用',
        creator: {
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
        targetAudience: 'school',
        tags: ['AI', '导航'],
        jobs: [],
        status: 'recruiting',
        createdAt: '2024-01-15',
        updatedAt: '2024-01-15'
      }
    ]
  }
}

// 获取分享数据
const fetchShares = async () => {
  try {
    const response = await homeApi.getShares({ limit: 20 })
    shares.value = response.data
  } catch (error) {
    console.error('Failed to fetch shares:', error)
    // 设置默认分享数据作为后备
    shares.value = [
      {
        id: 1,
        title: 'Vue3 + TypeScript 最佳实践',
        author: {
          id: 1,
          username: '李四',
          email: 'lisi@example.com',
          school: '北京大学',
          department: '软件工程',
          level: 4,
          points: 800,
          skills: ['Vue.js', 'TypeScript'],
          interests: ['前端开发'],
          createdAt: '2024-01-01'
        },
        content: '分享Vue3和TypeScript的使用经验...',
        techStack: ['Vue3', 'TypeScript', 'Vite'],
        category: 'CS',
        publishedAt: '2024-01-10'
      },
      {
        id: 2,
        title: '机器学习入门指南',
        author: {
          id: 2,
          username: '王五',
          email: 'wangwu@example.com',
          school: '复旦大学',
          department: '人工智能',
          level: 6,
          points: 1500,
          skills: ['Python', 'TensorFlow'],
          interests: ['机器学习'],
          createdAt: '2024-01-01'
        },
        content: '从零开始学习机器学习的基础知识...',
        techStack: ['Python', 'TensorFlow', 'Scikit-learn'],
        category: 'AI',
        publishedAt: '2024-01-12'
      }
    ]
  }
}

// 获取公告数据
const fetchAnnouncements = async () => {
  try {
    const response = await homeApi.getAnnouncements({ limit: 5 })
    announcements.value = response.data
  } catch (error) {
    console.error('Failed to fetch announcements:', error)
    // 设置默认公告数据作为后备
    announcements.value = [
      {
        id: 1,
        title: '平台功能更新通知',
        content: '新增了更多功能，欢迎体验！',
        type: 'system',
        isImportant: true,
        createdAt: '2024-01-15'
      }
    ]
  }
}

// 获取热门标签
const fetchHotTags = async () => {
  try {
    const response = await homeApi.getHotTags()
    hotTags.value = response.data
  } catch (error) {
    console.error('Failed to fetch hot tags:', error)
    // 设置默认热门标签作为后备
    hotTags.value = ['#蓝桥杯', '#互联网+', '#数模竞赛', '#AI', '#Vue.js']
  }
}

// 获取首页统计数据
const fetchHomeStats = async () => {
  try {
    const response = await homeApi.getHomeStats()
    homeStats.value = response.data
  } catch (error) {
    console.error('Failed to fetch home stats:', error)
    // 设置默认统计数据作为后备
    homeStats.value = {
      totalUsers: 1000,
      totalProjects: 50,
      totalCompetitions: 10
    }
  }
}

// 获取所有首页数据
const fetchAllData = async () => {
  isLoading.value = true
  try {
    // 使用 Promise.allSettled 确保所有请求都能完成，即使部分失败
    const results = await Promise.allSettled([
      fetchCategories(),
      fetchBanners(),
      fetchCompetitions(),
      fetchProjects(),
      fetchShares(),
      fetchAnnouncements(),
      fetchHotTags(),
      fetchHomeStats()
    ])
    
    // 检查哪些请求失败了
    results.forEach((result, index) => {
      if (result.status === 'rejected') {
        const apiNames = ['categories', 'banners', 'competitions', 'projects', 'shares', 'announcements', 'hotTags', 'homeStats']
        console.error(`Failed to fetch ${apiNames[index]}:`, result.reason)
      }
    })
  } catch (error) {
    console.error('Failed to fetch home data:', error)
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchAllData()
  console.log('HomePage mounted')
})
</script> 