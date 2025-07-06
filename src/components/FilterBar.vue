<template>
  <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- 岗位类型 -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">岗位类型</label>
        <CustomSelect
          v-model="localFilters.jobType"
          :options="jobTypeOptions"
          placeholder="全部岗位"
          @update:modelValue="handleFilterChange"
        />
      </div>

      <!-- 技能标签 -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">技能要求</label>
        <div class="flex flex-wrap gap-2">
          <button
            v-for="skill in availableSkills"
            :key="skill"
            @click="toggleSkill(skill)"
            class="tag cursor-pointer transition-colors duration-200"
            :class="localFilters.skills.includes(skill) ? 'bg-primary-600 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
          >
            {{ skill }}
          </button>
        </div>
      </div>

      <!-- 薪酬区间 -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">薪酬区间</label>
        <CustomSelect
          v-model="localFilters.salaryRange"
          :options="salaryRangeOptions"
          placeholder="不限"
          @update:modelValue="handleFilterChange"
        />
      </div>

      <!-- 面向人群 -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">面向人群</label>
        <CustomSelect
          v-model="localFilters.targetAudience"
          :options="targetAudienceOptions"
          placeholder="全部"
          @update:modelValue="handleFilterChange"
        />
      </div>
    </div>

    <!-- 操作按钮 -->
    <div class="flex justify-between items-center mt-6 pt-4 border-t border-gray-200">
      <div class="text-sm text-gray-500">
        找到 {{ totalCount }} 个项目
      </div>
      <div class="flex space-x-2">
        <button
          @click="clearFilters"
          class="btn-secondary text-sm"
        >
          清除筛选
        </button>
        <button
          @click="applyFilters"
          class="btn-primary text-sm"
        >
          应用筛选
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, watch } from 'vue'
import CustomSelect from '@/components/CustomSelect.vue'

interface Filters {
  jobType: string
  skills: string[]
  salaryRange: string
  targetAudience: string
}

interface Props {
  filters: Filters
}

interface Emits {
  (e: 'filter-change', filters: Filters): void
  (e: 'clear-filters'): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

const localFilters = reactive<Filters>({
  jobType: '',
  skills: [],
  salaryRange: '',
  targetAudience: ''
})

const totalCount = ref(0)

const availableSkills = [
  'Vue.js', 'React', 'TypeScript', 'Python', 'Java', 'C++',
  '机器学习', '深度学习', 'Node.js', 'MySQL', 'MongoDB'
]

const jobTypeOptions = [
  { value: '', label: '全部岗位' },
  { value: 'frontend', label: '前端开发' },
  { value: 'backend', label: '后端开发' },
  { value: 'fullstack', label: '全栈开发' },
  { value: 'ai', label: 'AI/机器学习' },
  { value: 'design', label: 'UI/UX设计' },
  { value: 'product', label: '产品经理' }
]

const salaryRangeOptions = [
  { value: '', label: '不限' },
  { value: '0-2000', label: '2000元以下' },
  { value: '2000-5000', label: '2000-5000元' },
  { value: '5000-10000', label: '5000-10000元' },
  { value: '10000+', label: '10000元以上' }
]

const targetAudienceOptions = [
  { value: '', label: '全部' },
  { value: 'school', label: '本校' },
  { value: 'department', label: '本院系' },
  { value: 'national', label: '全国' }
]

// 同步props到本地状态
watch(() => props.filters, (newFilters) => {
  Object.assign(localFilters, newFilters)
}, { immediate: true, deep: true })

const toggleSkill = (skill: string) => {
  const index = localFilters.skills.indexOf(skill)
  if (index > -1) {
    localFilters.skills.splice(index, 1)
  } else {
    localFilters.skills.push(skill)
  }
  handleFilterChange()
}

const handleFilterChange = () => {
  emit('filter-change', { ...localFilters })
}

const clearFilters = () => {
  localFilters.jobType = ''
  localFilters.skills = []
  localFilters.salaryRange = ''
  localFilters.targetAudience = ''
  emit('clear-filters')
}

const applyFilters = () => {
  emit('filter-change', { ...localFilters })
}
</script> 