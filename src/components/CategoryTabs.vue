<template>
  <div class="bg-white rounded-lg shadow-sm border border-gray-200">
    <div class="border-b border-gray-200">
      <nav class="flex space-x-8 px-6" aria-label="Tabs">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          @click="$emit('tab-change', tab.id)"
          class="py-4 px-1 border-b-2 font-medium text-sm transition-colors duration-200"
          :class="activeTab === tab.id 
            ? 'border-primary-500 text-primary-600' 
            : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'"
        >
          {{ tab.name }}
        </button>
      </nav>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Tab {
  id: string
  name: string
}

interface Props {
  activeTab: string
}

defineProps<Props>()

defineEmits<{
  'tab-change': [tabId: string]
}>()

const tabs: Tab[] = [
  { id: 'competitions', name: '比赛' },
  { id: 'projects', name: '项目' },
  { id: 'AI', name: 'AI' },
  { id: 'CS', name: 'CS' },
  { id: 'EE', name: 'EE' }
]
</script> 