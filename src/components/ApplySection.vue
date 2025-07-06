<template>
  <div class="card">
    <h2 class="text-xl font-semibold text-gray-900 mb-4">申请加入</h2>
    <form @submit.prevent="handleSubmit" class="space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">选择岗位</label>
        <CustomSelect
          v-model="selectedJobId"
          :options="jobOptions"
          placeholder="请选择岗位"
          required
        />
      </div>
      
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">选择简历</label>
        <CustomSelect
          v-model="selectedResumeId"
          :options="resumeOptions"
          placeholder="请选择简历"
          required
        />
      </div>
      
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">申请说明</label>
        <textarea
          v-model="note"
          rows="4"
          class="input-field"
          placeholder="请简要说明你为什么想加入这个项目..."
        ></textarea>
      </div>
      
      <div class="flex justify-end">
        <button
          type="submit"
          class="btn-primary"
          :disabled="isSubmitting"
        >
          {{ isSubmitting ? '提交中...' : '提交申请' }}
        </button>
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import type { Project } from '@/types'
import CustomSelect from '@/components/CustomSelect.vue'

interface Props {
  project: Project
}

const props = defineProps<Props>()

const selectedJobId = ref('')
const selectedResumeId = ref('')
const note = ref('')
const isSubmitting = ref(false)

const jobOptions = computed(() => 
  props.project.jobs.map(job => ({
    value: job.id,
    label: `${job.title} (招${job.headcount}人)`
  }))
)

const resumeOptions = computed(() => [
  { value: '1', label: '我的简历' }
])

const handleSubmit = async () => {
  if (!selectedJobId.value || !selectedResumeId.value) {
    return
  }
  
  isSubmitting.value = true
  try {
    // 这里应该调用API提交申请
    console.log('Submitting application:', {
      jobId: selectedJobId.value,
      resumeId: selectedResumeId.value,
      note: note.value
    })
  } catch (error) {
    console.error('Application failed:', error)
  } finally {
    isSubmitting.value = false
  }
}
</script> 