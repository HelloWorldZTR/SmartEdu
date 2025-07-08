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
          <CarouselBanner 
            :banners="banners" 
            :current-index="currentBannerIndex"
            :is-autoplay="isAutoplay"
            @banner-click="handleBannerClick"
            @banner-change="handleBannerChange"
            @toggle-autoplay="toggleAutoplay"
          />
          
          <!-- 分类标签 -->
          <CategoryTabs 
            :active-tab="activeTab"
            :categories="categories"
            @tab-change="handleTabChange"
          />
          
          <!-- 内容列表 -->
          <div class="space-y-6">
            <!-- 比赛列表 -->
            <div v-if="currentCategoryType === 'competitions'" class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <CompetitionCard
                v-for="competition in competitions"
                :key="competition.id"
                :competition="competition"
              />
            </div>
            
            <!-- 项目列表 -->
            <div v-if="currentCategoryType === 'projects'" class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <ProjectCard
                v-for="project in projects"
                :key="project.id"
                :project="project"
              />
            </div>
            
            <!-- 分享新闻流 - 始终显示 -->
            <div class="space-y-4">
              <h3 class="text-xl font-semibold text-gray-900 border-b border-gray-200 pb-2">
                最新分享
              </h3>
              <div class="space-y-4">
                <ShareCard
                  v-for="share in shares"
                  :key="share.id"
                  :share="share"
                />
              </div>
            </div>
          </div>
        </div>
        
        <!-- 侧边栏 -->
        <div class="lg:col-span-1 space-y-6">
          <Sidebar 
            :tags="tags"
            :announcements="announcements"
            :hot-topics="hotTopics"
            @category-change="handleCategoryChange"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
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
import { useRouter } from 'vue-router'

const activeTab = ref('competitions')
const categories = ref<Category[]>([])
const isLoading = ref(false)

// Banner动态更新相关状态
const currentBannerIndex = ref(0)
const isAutoplay = ref(true)
const autoplayInterval = ref<number | null>(null)
const AUTOPLAY_DURATION = 5000 // 5秒自动切换

// 数据状态
const banners = ref<Banner[]>([])
const competitions = ref<Competition[]>([])
const projects = ref<Project[]>([])
const shares = ref<Share[]>([])
const announcements = ref<Announcement[]>([])
const tags = ref<string[]>([])
const hotTopics = ref<Array<{
  id: number
  title: string
  tag: string
  count: number
}>>([])
const homeStats = ref<any>(null)

const handleTabChange = (tab: string) => {
  activeTab.value = tab
}

// Banner相关方法
const handleBannerClick = (banner: Banner) => {
  console.log('Banner clicked:', banner.title)
  // 可以在这里添加点击统计或其他逻辑
  if (banner.link) {
    window.open(banner.link, '_blank')
  }
}

const handleBannerChange = (index: number) => {
  currentBannerIndex.value = index
  // 重置自动播放计时器
  resetAutoplayTimer()
}

const toggleAutoplay = () => {
  isAutoplay.value = !isAutoplay.value
  if (isAutoplay.value) {
    startAutoplay()
  } else {
    stopAutoplay()
  }
}

const startAutoplay = () => {
  if (banners.value.length <= 1) return
  
  stopAutoplay() // 先清除之前的定时器
  
  autoplayInterval.value = window.setInterval(() => {
    currentBannerIndex.value = (currentBannerIndex.value + 1) % banners.value.length
  }, AUTOPLAY_DURATION)
}

const stopAutoplay = () => {
  if (autoplayInterval.value) {
    clearInterval(autoplayInterval.value)
    autoplayInterval.value = null
  }
}

const resetAutoplayTimer = () => {
  if (isAutoplay.value) {
    stopAutoplay()
    startAutoplay()
  }
}

// 监听banners变化，重新启动自动播放
watch(banners, (newBanners) => {
  if (newBanners.length > 0) {
    currentBannerIndex.value = 0
    if (isAutoplay.value) {
      startAutoplay()
    }
  }
}, { immediate: true })

// 获取当前分类类型
const currentCategoryType = computed(() => {
  const currentCategory = categories.value.find(cat => cat.id === activeTab.value)
  return currentCategory?.type || 'competitions'
})

// 获取分类数据
const fetchCategories = async () => {
  try {
    const response = await categoryApi.getActiveCategories()
    
    // 确保response是数组
    if (Array.isArray(response)) {
      categories.value = response
    } else if (response && typeof response === 'object' && 'results' in response && Array.isArray((response as any).results)) {
      // 如果response是分页响应格式
      categories.value = (response as any).results
    } else {
      // 如果response不是数组，设置为空数组
      console.warn('Categories response is not an array:', response)
      categories.value = []
    }
    
    for (const category of categories.value) {
      category.id = String(category.id) //Fix this stupid bug
    }

    // 设置默认选中的标签
    if (categories.value.length > 0) {
      activeTab.value = String(categories.value[0].id)
    }
  } catch (error) {
    console.error('Failed to fetch categories:', error)
    // 设置默认分类作为后备
    categories.value = [
      { id: 'competitions', name: '比赛', type: 'competitions', order: 1, isActive: true },
      { id: 'projects', name: '项目', type: 'projects', order: 2, isActive: true }
    ]
    // 确保设置默认选中的标签
    activeTab.value = 'competitions'
  }
}

// 获取轮播图数据
const fetchBanners = async () => {
  try {
    const response = await homeApi.getBanners()
    // 直接使用response，因为它已经是分页响应格式
    const bannerData = response?.results || []
    banners.value = bannerData.filter((banner: any) => banner.isActive || banner.is_active).sort((a: any, b: any) => (a.order || 0) - (b.order || 0))
  } catch (error) {
    console.error('Failed to fetch banners:', error)
  }
}

// 获取比赛数据
const fetchCompetitions = async () => {
  try {
    const response = await homeApi.getCompetitions({ limit: 10 })
    
    // 确保response格式正确
    let competitionData = []
    if (Array.isArray(response)) {
      competitionData = response
    } else if (response && typeof response === 'object' && 'results' in response && Array.isArray((response as any).results)) {
      competitionData = (response as any).results
    } else {
      console.warn('Competitions response format is unexpected:', response)
      competitionData = []
    }
    competitions.value = competitionData
  } catch (error) {
    console.error('Failed to fetch competitions:', error)
  }
}

// 获取项目数据
const fetchProjects = async () => {
  try {
    const response = await homeApi.getProjects({ limit: 10, status: 'recruiting' })
    
    // 确保response格式正确
    let projectData = []
    if (Array.isArray(response) ) {
      projectData = response
    } else if (response && typeof response === 'object' && 'results' in response && Array.isArray((response as any).results)) {
      projectData = (response as any).results
    } else {
      console.warn('Projects response format is unexpected:', response)
      projectData = []
    }
    
    projects.value = projectData
  } catch (error) {
    console.error('Failed to fetch projects:', error)
  }
}

// 获取分享数据
const fetchShares = async () => {
  try {
    const response = await homeApi.getShares({ limit: 20 })
    
    // 确保response格式正确
    let shareData = []
    if (Array.isArray(response)) {
      shareData = response
    } else if (response && typeof response === 'object' && 'results' in response && Array.isArray((response as any).results)) {
      shareData = (response as any).results
    } else {
      console.warn('Shares response format is unexpected:', response)
      shareData = []
    }
    
    shares.value = shareData

    // console.log(shares.value)
  } catch (error) {
    console.error('Failed to fetch shares:', error)
  }
}

// 获取公告数据
const fetchAnnouncements = async () => {
  try {
    const response = await homeApi.getAnnouncements({ limit: 5 })
    
    // 确保response格式正确
    let announcementData = []
    if (Array.isArray(response)) {
      announcementData = response
    } else if (response && typeof response === 'object' && 'results' in response && Array.isArray((response as any).results)) {
      announcementData = (response as any).results
    } else {
      console.warn('Announcements response format is unexpected:', response)
      announcementData = []
    }
    
    announcements.value = announcementData
  } catch (error) {
    console.error('Failed to fetch announcements:', error)
  }
}

// 获取热门标签
const fetchTags = async () => {
  try {
      const response = await homeApi.getTags()
    
    // 确保response格式正确
    let tagData = []
    if (Array.isArray(response)) {
      tagData = response
    } else if (response && typeof response === 'object' && 'results' in response && Array.isArray((response as any).results)) {
      tagData = (response as any).results
    } else {
      console.warn('Hot tags response format is unexpected:', response)
      tagData = []
    }
    
    tags.value = tagData.map((tag: any) => "#" + tag.name);
  } catch (error) {
    console.error('Failed to fetch hot tags:', error)
  }
}

// 获取热门话题
const fetchHotTopics = async () => {
  try {
    const response = await homeApi.getTopics()
    
    // 确保response格式正确
    let topicData = []
    if (Array.isArray(response)) {
      topicData = response
    } else if (response && typeof response === 'object' && 'results' in response && Array.isArray((response as any).results)) {
      topicData = (response as any).results
    } else {
      console.warn('Hot topics response format is unexpected:', response)
      topicData = []
    }
    
    hotTopics.value = topicData
  } catch (error) {
    console.error('Failed to fetch hot topics:', error)
  }
}

// 获取首页统计数据
// const fetchHomeStats = async () => {
//   try {
//     const response = await homeApi.getHomeStats()
//     homeStats.value = response
//   } catch (error) {
//     console.error('Failed to fetch home stats:', error)
//     // 设置默认统计数据作为后备
//     homeStats.value = {
//       totalUsers: 1000,
//       totalProjects: 50,
//       totalCompetitions: 10
//     }
//   }
// }

// 获取所有首页数据
const fetchAllData = async () => {
  isLoading.value = true
  try {
    // 使用 Promise.allSettled 确保所有请求都能完成，即使部分失败
    const results = await Promise.allSettled([
      fetchBanners(),
      fetchCompetitions(),
      fetchProjects(),
      fetchShares(),
      fetchCategories(),
      fetchAnnouncements(),
      fetchTags(),
      fetchHotTopics(), // 新增热门话题
      // fetchHomeStats()
    ])
    
    // 检查哪些请求失败了
    results.forEach((result, index) => {
      if (result.status === 'rejected') {
        const apiNames = ['categories', 'banners', 'competitions', 'projects', 'shares', 'announcements', 'tags', 'hotTopics', 'homeStats']
        console.error(`Failed to fetch ${apiNames[index]}:`, result.reason)
      }
    })
  } catch (error) {
    console.error('Failed to fetch home data:', error)
  } finally {
    isLoading.value = false
  }
}

const router = useRouter()

// 处理Sidebar分类点击
const handleCategoryChange = (category: string) => {
  router.push({
    path: '/team-hall',
    query: { category }
  })
}

onMounted(() => {
  fetchAllData()
  console.log('HomePage mounted')
})

onUnmounted(() => {
  // 清理定时器
  stopAutoplay()
})
</script> 