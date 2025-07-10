<template>
  <div class="card hover:shadow-md transition-shadow duration-200">
    <div class="flex justify-between items-start mb-3">
      <h3 class="text-lg font-semibold text-gray-900 line-clamp-2 flex-1 mr-4">
        {{ share.title }}
      </h3>
      <span class="text-xs text-gray-500 whitespace-nowrap">{{ formatRelativeTime(share.publishedAt) }}</span>
    </div>
    
    <p class="text-sm text-gray-600 mb-4 line-clamp-2">
      {{ share.content }}
    </p>
    
    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-2">
        <img
          :src="share.author.avatar || '/default-avatar.png'"
          :alt="share.author.username"
          class="w-6 h-6 rounded-full object-cover"
        />
        <span class="text-sm text-gray-700">{{ share.author.username }}</span>
        <span class="text-xs text-gray-500">·</span>
        <span class="text-xs text-gray-500">{{ share.author.school }}</span>
      </div>
      
      <div class="flex items-center space-x-2">
        <div class="flex space-x-1">
          <span
            v-for="tech in (share.techStack || []).slice(0, 2)"
            :key="tech"
            class="tag text-xs"
          >
            {{ tech }}
          </span>
          <span v-if="(share.techStack || []).length > 2" class="text-xs text-gray-500">
            +{{ (share.techStack || []).length - 2 }}
          </span>
        </div>
        
        <span class="text-xs px-2 py-1 rounded-full bg-primary-100 text-primary-800">
          {{ share.category.name }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { formatRelativeTime } from '@/utils/date'
import type { Share } from '@/types'

interface Props {
  share: Share
}

defineProps<Props>()
</script> 