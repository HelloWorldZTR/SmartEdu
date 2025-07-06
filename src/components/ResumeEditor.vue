<template>
  <div class="card">
    <h2 class="text-xl font-semibold text-gray-900 mb-4">编辑简历</h2>
    <div class="space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">技能标签</label>
        <div class="flex flex-wrap gap-2">
          <button
            v-for="skill in availableSkills"
            :key="skill"
            @click="toggleSkill(skill)"
            class="tag cursor-pointer transition-colors duration-200"
            :class="resume.skills.includes(skill) ? 'bg-primary-600 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
          >
            {{ skill }}
          </button>
        </div>
      </div>
      
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">自我评价</label>
        <textarea
          v-model="resume.selfEvaluation"
          rows="4"
          class="input-field"
          placeholder="请描述你的技能、经验和职业目标..."
        ></textarea>
      </div>
      
      <div class="flex justify-end">
        <button @click="saveResume" class="btn-primary">
          保存简历
        </button>
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

defineEmits<{
  save: [resume: Resume]
}>()

const availableSkills = [
  'Vue.js', 'React', 'TypeScript', 'Python', 'Java', 'C++',
  '机器学习', '深度学习', 'Node.js', 'MySQL', 'MongoDB'
]

const toggleSkill = (skill: string) => {
  // 处理技能切换逻辑
  console.log('Toggle skill:', skill)
}

const saveResume = () => {
  // 处理保存逻辑
  console.log('Save resume')
}
</script> 