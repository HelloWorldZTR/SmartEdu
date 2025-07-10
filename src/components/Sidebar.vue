<template>
  <div class="space-y-6">
    <!-- 搜索栏 -->
    <div class="card">
      <div class="relative">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="搜索项目、比赛、分享..."
          class="input-field pr-10"
          @keyup.enter="handleSearch"
        />
        <button
          @click="handleSearch"
          class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-gray-600"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </button>
      </div>
    </div>

    <!-- 标签筛选 -->
    <div class="card">
      <h3 class="text-lg font-semibold text-gray-900 mb-4">热门标签</h3>
      <div class="flex flex-wrap gap-2">
        <button
          v-for="tag in tagList"
          :key="tag"
          @click="toggleTag(tag)"
          class="tag cursor-pointer transition-colors duration-200"
          :class="selectedTags.includes(tag) ? 'bg-primary-600 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
        >
          {{ tag }}
        </button>
      </div>
    </div>

    <!-- 通知栏 -->
    <div class="card">
      <h3 class="text-lg font-semibold text-gray-900 mb-4">系统公告</h3>
      <div class="space-y-3">
        <div
          v-for="notification in notifications"
          :key="notification.id"
          class="p-3 bg-primary-50 rounded-lg border border-primary-200"
        >
          <h4 class="text-sm font-medium text-primary-900 mb-1">
            {{ notification.title }}
          </h4>
          <p class="text-xs text-primary-700 line-clamp-2">
            {{ notification.content }}
          </p>
          <span class="text-xs text-primary-500 mt-2 block">
            {{ formatRelativeTime(notification.created_at || notification.createdAt || new Date()) }}
          </span>
        </div>
      </div>
    </div>

    <!-- 热门话题 -->
    <div class="card">
      <h3 class="text-lg font-semibold text-gray-900 mb-4">热门话题</h3>
      <div class="space-y-3">
        <div
          v-for="topic in topicList"
          :key="topic.id"
          class="flex items-center justify-between p-2 hover:bg-gray-50 rounded-lg cursor-pointer transition-colors duration-200"
        >
          <div class="flex-1">
            <h4 class="text-sm font-medium text-gray-900">{{ topic.title }}</h4>
            <p class="text-xs text-gray-500">{{ topic.count }} 人参与</p>
          </div>
          <span class="text-xs text-gray-400">#{{ topic.tag }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { formatRelativeTime } from '@/utils/date'
import type { Announcement } from '@/api/home'

interface Props {
  tags?: string[]
  announcements?: Announcement[]
  topics?: Array<{
    id: number
    title: string
    tag: string
    count: number
  }>
}

const props = withDefaults(defineProps<Props>(), {
  tags: () => ['#蓝桥杯', '#互联网+', '#数模竞赛', '#AI', '#Vue.js'],
  announcements: () => [],
  topics: () => []
})

const router = useRouter()

const searchQuery = ref('')
const selectedTags = ref<string[]>([])

// 使用computed来确保响应式更新
const tagList = computed(() => props.tags)
const notifications = computed(() => props.announcements)
const topicList = computed(() => props.topics)

const handleSearch = () => {
  if (searchQuery.value.trim()) {
    router.push({
      path: '/search',
      query: { q: searchQuery.value }
    })
  }
}

const toggleTag = (tag: string) => {
  const index = selectedTags.value.indexOf(tag)
  if (index > -1) {
    selectedTags.value.splice(index, 1)
  } else {
    selectedTags.value.push(tag)
  }
}
</script> 