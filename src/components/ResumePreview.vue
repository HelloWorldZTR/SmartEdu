<template>
  <div class="card">
    <h2 class="text-xl font-semibold text-gray-900 mb-4">简历预览</h2>
    <div class="space-y-4">
      <div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">基本信息</h3>
        <p class="text-sm text-gray-600">{{ resume.user.username }}</p>
        <p class="text-sm text-gray-600">{{ resume.user.school }} · {{ resume.user.department }}</p>
      </div>
      
      <div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">技能</h3>
        <div class="flex flex-wrap gap-2">
          <span
            v-for="skill in resume.skills"
            :key="skill"
            class="tag"
          >
            {{ skill }}
          </span>
        </div>
      </div>
      
      <div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">自我评价</h3>
        <p class="text-sm text-gray-600">{{ resume.selfEvaluation }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Resume } from '@/types'

interface Props {
  resume: Resume
}

defineProps<Props>()
</script> 