<template>
  <div class="min-h-screen bg-gray-50">
    <TopNavBar />
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <!-- 主要内容区域 -->
        <div class="lg:col-span-3 space-y-6">
          <!-- 轮播图 -->
          <CarouselBanner :banners="banners" />
          
          <!-- 分类标签 -->
          <CategoryTabs 
            :active-tab="activeTab"
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
            <div v-if="['AI', 'CS', 'EE'].includes(activeTab)" class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <ShareCard
                v-for="share in shares"
                :key="share.id"
                :share="share"
              />
            </div>
          </div>
        </div>
        
        <!-- 侧边栏 -->
        <div class="lg:col-span-1 space-y-6">
          <Sidebar />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import TopNavBar from '@/components/TopNavBar.vue'
import CarouselBanner from '@/components/CarouselBanner.vue'
import CategoryTabs from '@/components/CategoryTabs.vue'
import CompetitionCard from '@/components/CompetitionCard.vue'
import ProjectCard from '@/components/ProjectCard.vue'
import ShareCard from '@/components/ShareCard.vue'
import Sidebar from '@/components/Sidebar.vue'
import type { Competition, Project, Share } from '@/types'

const activeTab = ref('competitions')

// 模拟数据
const banners = ref([
  {
    id: 1,
    title: '蓝桥杯程序设计大赛',
    image: '/banners/lanqiao.jpg',
    link: '/competition/1'
  },
  {
    id: 2,
    title: '互联网+创新创业大赛',
    image: '/banners/internet-plus.jpg',
    link: '/competition/2'
  }
])

const competitions = ref<Competition[]>([
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
])

const projects = ref<Project[]>([
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
])

const shares = ref<Share[]>([
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
  }
])

const handleTabChange = (tab: string) => {
  activeTab.value = tab
}

onMounted(() => {
  // 这里应该从API获取数据
  console.log('HomePage mounted')
})
</script> 