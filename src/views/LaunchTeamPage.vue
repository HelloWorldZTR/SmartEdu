<template>
  <div class="min-h-screen bg-gray-50">
    <TopNavBar />
    
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      <div class="mb-6">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">发起组队</h1>
        <p class="text-gray-600">创建一个新的项目，招募志同道合的伙伴</p>
      </div>

      <form @submit.prevent="handleSubmit" class="space-y-6">
        <!-- 基本信息 -->
        <div class="card">
          <h2 class="text-xl font-semibold text-gray-900 mb-4">基本信息</h2>
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">项目名称</label>
              <input
                v-model="form.title"
                type="text"
                class="input-field"
                placeholder="请输入项目名称"
                required
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">项目描述</label>
              <textarea
                v-model="form.description"
                rows="4"
                class="input-field"
                placeholder="请详细描述项目内容、目标和技术栈"
                required
              ></textarea>
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">面向人群</label>
              <CustomSelect
                v-model="form.targetAudience"
                :options="targetAudienceOptions"
                placeholder="请选择面向人群"
                required
              />
            </div>
          </div>
        </div>

        <!-- 岗位设置 -->
        <div class="card">
          <h2 class="text-xl font-semibold text-gray-900 mb-4">岗位设置</h2>
          <div class="space-y-4">
            <div
              v-for="(job, index) in form.jobs"
              :key="index"
              class="border border-gray-200 rounded-lg p-4"
            >
              <div class="flex items-center justify-between mb-4">
                <h3 class="text-lg font-medium text-gray-900">岗位 {{ index + 1 }}</h3>
                <button
                  type="button"
                  @click="removeJob(index)"
                  class="text-red-500 hover:text-red-700"
                >
                  删除
                </button>
              </div>
              
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">岗位名称</label>
                  <input
                    v-model="job.title"
                    type="text"
                    class="input-field"
                    placeholder="如：前端开发工程师"
                    required
                  />
                </div>
                
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">需求人数</label>
                  <input
                    v-model="job.headcount"
                    type="number"
                    min="1"
                    class="input-field"
                    required
                  />
                </div>
              </div>
              
              <div class="mt-4">
                <label class="block text-sm font-medium text-gray-700 mb-2">岗位描述</label>
                <textarea
                  v-model="job.description"
                  rows="3"
                  class="input-field"
                  placeholder="请描述岗位职责和要求"
                  required
                ></textarea>
              </div>
              
              <div class="mt-4">
                <label class="block text-sm font-medium text-gray-700 mb-2">技能要求</label>
                <div class="flex flex-wrap gap-2">
                  <button
                    v-for="skill in availableSkills"
                    :key="skill"
                    type="button"
                    @click="toggleJobSkill(index, skill)"
                    class="tag cursor-pointer transition-colors duration-200"
                    :class="job.requiredSkills.includes(skill) ? 'bg-primary-600 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
                  >
                    {{ skill }}
                  </button>
                </div>
              </div>
              
              <div class="mt-4 grid grid-cols-1 md:grid-cols-3 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">最低薪酬</label>
                  <input
                    v-model="job.salary.min"
                    type="number"
                    class="input-field"
                    placeholder="0"
                  />
                </div>
                
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">最高薪酬</label>
                  <input
                    v-model="job.salary.max"
                    type="number"
                    class="input-field"
                    placeholder="0"
                  />
                </div>
                
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">货币单位</label>
                  <CustomSelect
                    v-model="job.salary.currency"
                    :options="currencyOptions"
                    placeholder="请选择货币单位"
                  />
                </div>
              </div>
            </div>
            
            <button
              type="button"
              @click="addJob"
              class="w-full py-3 border-2 border-dashed border-gray-300 rounded-lg text-gray-600 hover:border-primary-500 hover:text-primary-600 transition-colors duration-200"
            >
              + 添加岗位
            </button>
          </div>
        </div>

        <!-- 标签设置 -->
        <div class="card">
          <h2 class="text-xl font-semibold text-gray-900 mb-4">项目标签</h2>
          <div class="flex flex-wrap gap-2">
            <button
              v-for="tag in availableTags"
              :key="tag"
              type="button"
              @click="toggleTag(tag)"
              class="tag cursor-pointer transition-colors duration-200"
              :class="form.tags.includes(tag) ? 'bg-primary-600 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
            >
              {{ tag }}
            </button>
          </div>
        </div>

        <!-- 提交按钮 -->
        <div class="flex justify-end space-x-4">
          <button
            type="button"
            @click="resetForm"
            class="btn-secondary"
          >
            重置
          </button>
          <button
            type="submit"
            class="btn-primary"
            :disabled="isSubmitting"
          >
            {{ isSubmitting ? '发布中...' : '发布项目' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import TopNavBar from '@/components/TopNavBar.vue'
import CustomSelect from '@/components/CustomSelect.vue'
import { useProjectStore } from '@/stores/project'

const router = useRouter()
const projectStore = useProjectStore()

const isSubmitting = ref(false)

const form = reactive({
  title: '',
  description: '',
  targetAudience: 'school' as 'school' | 'department' | 'national',
  tags: [] as string[],
  jobs: [
    {
      title: '',
      description: '',
      requiredSkills: [] as string[],
      headcount: 1,
      salary: {
        min: 0,
        max: 0,
        currency: 'CNY'
      }
    }
  ]
})

const availableSkills = [
  'Vue.js', 'React', 'TypeScript', 'Python', 'Java', 'C++',
  '机器学习', '深度学习', 'Node.js', 'MySQL', 'MongoDB'
]

const availableTags = [
  'AI', 'Vue.js', 'React', 'Python', 'Java', '机器学习',
  'Web开发', '移动开发', '数据库', '云计算', '区块链'
]

const targetAudienceOptions = [
  { value: 'school', label: '本校' },
  { value: 'department', label: '本院系' },
  { value: 'national', label: '全国' }
]

const currencyOptions = [
  { value: 'CNY', label: '人民币' },
  { value: 'USD', label: '美元' }
]

const addJob = () => {
  form.jobs.push({
    title: '',
    description: '',
    requiredSkills: [],
    headcount: 1,
    salary: {
      min: 0,
      max: 0,
      currency: 'CNY'
    }
  })
}

const removeJob = (index: number) => {
  if (form.jobs.length > 1) {
    form.jobs.splice(index, 1)
  }
}

const toggleJobSkill = (jobIndex: number, skill: string) => {
  const job = form.jobs[jobIndex]
  const index = job.requiredSkills.indexOf(skill)
  if (index > -1) {
    job.requiredSkills.splice(index, 1)
  } else {
    job.requiredSkills.push(skill)
  }
}

const toggleTag = (tag: string) => {
  const index = form.tags.indexOf(tag)
  if (index > -1) {
    form.tags.splice(index, 1)
  } else {
    form.tags.push(tag)
  }
}

const resetForm = () => {
  form.title = ''
  form.description = ''
  form.targetAudience = 'school'
  form.tags = []
  form.jobs = [
    {
      title: '',
      description: '',
      requiredSkills: [],
      headcount: 1,
      salary: {
        min: 0,
        max: 0,
        currency: 'CNY'
      }
    }
  ]
}

const handleSubmit = async () => {
  isSubmitting.value = true
  try {
    await projectStore.createProject(form)
    router.push('/team-hall')
  } catch (error) {
    console.error('Create project failed:', error)
  } finally {
    isSubmitting.value = false
  }
}
</script> 