<template>
  <div class="min-h-screen bg-gray-50">
    <TopNavBar />
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      <div class="mb-6">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">组队大厅</h1>
        <p class="text-gray-600">浏览当前公开招募信息，找到合适的项目加入</p>
      </div>

      <!-- 筛选栏 -->
      <FilterBar 
        :filters="filters"
        :tags="allTags"
        @filter-change="handleFilterChange"
        @clear-filters="clearFilters"
      />

      <!-- 项目列表 -->
      <div class="mt-6">
        <div v-if="projectStore.isLoading" class="flex justify-center py-12">
          <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
        </div>
        
        <div v-else-if="projectStore.filteredProjects.length === 0" class="text-center py-12">
          <div class="text-gray-500">
            <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <h3 class="mt-2 text-sm font-medium text-gray-900">暂无项目</h3>
            <p class="mt-1 text-sm text-gray-500">没有找到符合条件的项目</p>
          </div>
        </div>
        
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <TeamCard
            v-for="project in projectStore.filteredProjects"
            :key="project.id"
            :project="project"
            @favorite="handleFavorite"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { categoryApi } from '@/api/category'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import TopNavBar from '@/components/TopNavBar.vue'
import FilterBar from '@/components/FilterBar.vue'
import TeamCard from '@/components/TeamCard.vue'
import { useProjectStore } from '@/stores/project'
import { homeApi } from '@/api/home'

const projectStore = useProjectStore()

const filters = {
  jobType: '',
  skills: [] as string[],
  salaryRange: '',
  targetAudience: '',
  category: '' // 新增分类字段
}

const handleFilterChange = (newFilters: any) => {
  projectStore.setFilters(newFilters)
}

const clearFilters = () => {
  projectStore.clearFilters()
}

const handleFavorite = (projectId: number) => {
  // 处理收藏逻辑
  console.log('Favorite project:', projectId)
}

const route = useRoute()

const allTags = ref<string[]>([])

const loadAllTags = async () => {
  try {
    const response = await homeApi.getTags()
    let tagData = []
    if (Array.isArray(response)) {
      tagData = response
    } else if (response && typeof response === 'object' && 'results' in response && Array.isArray((response as any).results)) {
      tagData = (response as any).results
    } else {
      console.warn('Tags response format is unexpected:', response)
      tagData = []
    }
    allTags.value = tagData.map((tag: any) => tag.name);
  } catch (e) {
    console.error('Failed to load all tags:', e)
    allTags.value = []
  }
}

onMounted(() => {
  loadAllTags()
  // 如果有category参数，自动筛选
  if (route.query.category) {
    projectStore.setFilters({ ...filters, category: route.query.category as string })
  } else {
    projectStore.fetchProjects()
  }
})
</script> 