<template>
  <div class="card hover:shadow-md transition-shadow duration-200">
    <div class="flex justify-between items-start mb-4">
      <h3 class="text-lg font-semibold text-gray-900 line-clamp-2">
        {{ competition.title }}
      </h3>
      <span class="text-xs text-gray-500">{{ formatDate(competition.deadline) }}</span>
    </div>
    
    <p class="text-sm text-gray-600 mb-3 line-clamp-2">
      {{ competition.description }}
    </p>
    
    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-2">
        <span class="text-sm text-gray-500">举办方:</span>
        <span class="text-sm font-medium text-gray-700">{{ competition.organizer }}</span>
      </div>
      
      <div class="flex space-x-1">
        <span
          v-for="tag in competition.tags.slice(0, 2)"
          :key="tag"
          class="tag"
        >
          {{ tag }}
        </span>
        <span v-if="competition.tags.length > 2" class="text-xs text-gray-500">
          +{{ competition.tags.length - 2 }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { formatDate } from '@/utils/date'
import type { Competition } from '@/types'

interface Props {
  competition: Competition
}

defineProps<Props>()
</script> 