<template>
  <div class="card">
    <h2 class="text-xl font-semibold text-gray-900 mb-4">申请加入</h2>
    <form id="apply-section-form" @submit.prevent="handleSubmit" class="space-y-4">
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
import { ref, computed, watch } from 'vue'
import type { Project } from '@/types'
import CustomSelect from '@/components/CustomSelect.vue'
import { projectApi } from '@/api/project'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'

interface Props {
  project: Project
  selectedJobId?: string
}

const props = defineProps<Props>()

const selectedJobId = ref(props.selectedJobId ?? '')

watch(() => props.selectedJobId, (val) => {
  if (val !== undefined) selectedJobId.value = val
})

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

// watch(() => props.selectedJobId, (val) => {
//   if (val) selectedJobId.value = val
// })

const router = useRouter()
const toast = useToast()

const handleSubmit = async () => {
  if (!selectedJobId.value || !selectedResumeId.value) {
    return
  }
  
  isSubmitting.value = true
  try {
    await projectApi.applyToJob(
      props.project.id,
      Number(selectedJobId.value),
      {
        resumeId: Number(selectedResumeId.value),
        note: note.value
      }
    )
    toast.success('申请成功，3秒后自动跳转到“我的项目”！')
    setTimeout(() => {
      router.push('/my-projects')
    }, 3000)
  } catch (error) {
    console.error('Application failed:', error)
    toast.error('申请失败，请稍后重试')
  } finally {
    isSubmitting.value = false
  }
}
</script> 