<template>
  <div class="min-h-screen bg-gray-50">
    <TopNavBar />
    
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- 个人信息 -->
        <div class="lg:col-span-1">
          <div class="card text-center">
            <img
              :src="userStore.currentUser?.avatar || '/default-avatar.png'"
              :alt="userStore.currentUser?.username"
              class="w-24 h-24 rounded-full mx-auto mb-4 object-cover"
            />
            <h1 class="text-xl font-bold text-gray-900 mb-2">
              {{ userStore.currentUser?.username }}
            </h1>
            <p class="text-gray-600 mb-4">
              {{ userStore.currentUser?.school }} · {{ userStore.currentUser?.department }}
            </p>
            <p class="text-sm text-gray-500 mb-4">
              {{ userStore.currentUser?.bio || '这个人很懒，还没有写简介' }}
            </p>
            
            <!-- 等级和积分 -->
            <div class="bg-gray-50 rounded-lg p-4 mb-4">
              <div class="flex justify-between items-center">
                <div>
                  <span class="text-sm text-gray-600">等级</span>
                  <div class="text-lg font-bold text-primary-600">Lv.{{ userStore.userLevel }}</div>
                </div>
                <div>
                  <span class="text-sm text-gray-600">积分</span>
                  <div class="text-lg font-bold text-green-600">{{ userStore.userPoints }}</div>
                </div>
              </div>
            </div>
            
            <button class="btn-primary w-full">
              编辑资料
            </button>
          </div>
        </div>
        
        <!-- 详细内容 -->
        <div class="lg:col-span-2 space-y-6">
          <!-- 技能与兴趣方向 -->
          <div class="card">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">技能与兴趣方向</h2>
            <div class="flex flex-wrap gap-2 mb-4">
              <span
                v-for="skill in userStore.currentUser?.skills || []"
                :key="skill"
                class="tag bg-green-100 text-green-800"
              >
                {{ skill }}
              </span>
            </div>
            <div>
              <h3 class="text-sm font-medium text-gray-700 mb-2">兴趣方向</h3>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="interest in userStore.currentUser?.interests || []"
                  :key="interest"
                  class="tag bg-blue-100 text-blue-800"
                >
                  {{ interest }}
                </span>
              </div>
            </div>
            <div class="mt-8">
              <h3 class="text-sm font-medium text-gray-700 mb-2">能力雷达图</h3>
              <VueECharts :option="radarOption" style="width: 100%; max-width: 400px; height: 320px; margin: 0 auto;" />
            </div>
          </div>
          
          <!-- 项目经历 -->
          <div class="card">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">项目经历</h2>
            <div class="space-y-4">
              <div
                v-for="project in userProjects"
                :key="project.id"
                class="border border-gray-200 rounded-lg p-4"
              >
                <div class="flex items-start justify-between">
                  <div>
                    <h3 class="text-lg font-medium text-gray-900">{{ project.title }}</h3>
                    <p class="text-sm text-gray-600 mt-1">{{ project.description }}</p>
                    <div class="flex items-center space-x-4 mt-2 text-xs text-gray-500">
                      <span>{{ project.creator.username }}</span>
                      <span>{{ formatDate(project.createdAt) }}</span>
                    </div>
                  </div>
                  <span class="text-xs px-2 py-1 rounded-full" :class="getStatusClass(project.status)">
                    {{ getStatusText(project.status) }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import TopNavBar from '@/components/TopNavBar.vue'
import { useUserStore } from '@/stores/user'
import { formatDate } from '@/utils/date'
import type { Project } from '@/types'
import VueECharts from 'vue-echarts'
import * as echarts from 'echarts/core'
import { RadarChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'

echarts.use([RadarChart, TitleComponent, TooltipComponent, LegendComponent, CanvasRenderer])

const userStore = useUserStore()

// 模拟用户项目数据
const userProjects = ref<Project[]>([
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

const abilityData = ref([
  80, // 专业能力
  70, // 问题解决能力
  65, // 沟通能力
  75, // 执行能力
  85, // 学习能力
  60  // 领导能力
])

const radarOption = computed(() => ({
  title: {
    text: '能力雷达图',
    left: 'center',
    top: 0,
    textStyle: { fontSize: 16 }
  },
  tooltip: {},
  radar: {
    indicator: [
      { name: '专业能力', max: 100 },
      { name: '问题解决能力', max: 100 },
      { name: '沟通能力', max: 100 },
      { name: '执行能力', max: 100 },
      { name: '学习能力', max: 100 },
      { name: '领导能力', max: 100 }
    ],
    radius: 80
  },
  series: [
    {
      name: '能力评估',
      type: 'radar',
      data: [
        {
          value: abilityData.value,
          name: '我的能力',
          areaStyle: { color: 'rgba(59,130,246,0.2)' },
          lineStyle: { color: '#3b82f6' },
          symbol: 'circle',
          symbolSize: 6,
          itemStyle: { color: '#3b82f6' }
        }
      ]
    }
  ]
}))

const getStatusClass = (status: string) => {
  switch (status) {
    case 'recruiting':
      return 'bg-green-100 text-green-800'
    case 'in_progress':
      return 'bg-blue-100 text-blue-800'
    case 'completed':
      return 'bg-gray-100 text-gray-800'
    default:
      return 'bg-gray-100 text-gray-800'
  }
}

const getStatusText = (status: string) => {
  switch (status) {
    case 'recruiting':
      return '招募中'
    case 'in_progress':
      return '进行中'
    case 'completed':
      return '已完成'
    default:
      return '未知'
  }
}

onMounted(() => {
  // 这里应该获取用户数据
  console.log('ProfilePage mounted')
})
</script> 