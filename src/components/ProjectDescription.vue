<template>
  <div class="card">
    <h2 class="text-xl font-semibold text-gray-900 mb-4">项目介绍</h2>
    <div class="prose max-w-none">
      <p class="text-gray-700 leading-relaxed">{{ project.description }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Project } from '@/types'

interface Props {
  project: Project
}

defineProps<Props>()
</script> 