<template>
  <div class="min-h-screen bg-gray-50">
    <TopNavBar />
    
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="mb-8">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">发布分享</h1>
        <p class="text-gray-600">分享你的技术经验和学习心得</p>
      </div>

      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <!-- 标题 -->
          <div>
            <label for="title" class="block text-sm font-medium text-gray-700 mb-2">
              分享标题 <span class="text-red-500">*</span>
            </label>
            <input
              id="title"
              v-model="form.title"
              type="text"
              required
              class="input-field"
              placeholder="请输入分享标题"
              maxlength="200"
            />
            <p class="mt-1 text-sm text-gray-500">{{ form.title.length }}/200</p>
          </div>

          <!-- 分类 -->
          <div>
            <label for="category" class="block text-sm font-medium text-gray-700 mb-2">
              分类 <span class="text-red-500">*</span>
            </label>
            <CustomSelect
              v-model="form.category"
              :options="categoryOptions"
              placeholder="请选择分类"
              required
            />
          </div>

          <!-- 内容 -->
          <div>
            <label for="content" class="block text-sm font-medium text-gray-700 mb-2">
              分享内容 <span class="text-red-500">*</span>
            </label>
            <textarea
              id="content"
              v-model="form.content"
              required
              rows="8"
              class="input-field resize-none"
              placeholder="请详细描述你的技术分享内容..."
              maxlength="5000"
            ></textarea>
            <p class="mt-1 text-sm text-gray-500">{{ form.content.length }}/5000</p>
          </div>

          <!-- 技术栈 -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              技术栈
            </label>
            <div class="space-y-3">
              <!-- 已选技术栈 -->
              <div v-if="form.techStack.length > 0" class="flex flex-wrap gap-2">
                <span
                  v-for="tech in form.techStack"
                  :key="tech"
                  class="tag flex items-center"
                >
                  {{ tech }}
                  <button
                    type="button"
                    @click="removeTech(tech)"
                    class="ml-1 text-primary-600 hover:text-primary-800"
                  >
                    ×
                  </button>
                </span>
              </div>
              
              <!-- 添加技术栈 -->
              <div class="flex gap-2">
                <input
                  v-model="newTech"
                  type="text"
                  class="input-field flex-1"
                  placeholder="输入技术名称"
                  @keyup.enter="addTech()"
                />
                <button
                  type="button"
                  @click="addTech()"
                  class="btn-secondary"
                  :disabled="!newTech.trim()"
                >
                  添加
                </button>
              </div>
              
              <!-- 常用技术栈 -->
              <div class="flex flex-wrap gap-2">
                <button
                  v-for="tech in commonTechs"
                  :key="tech"
                  type="button"
                  @click="addTech(tech)"
                  class="text-sm px-3 py-1 border border-gray-300 rounded-full text-gray-600 hover:bg-gray-50"
                  :class="{ 'bg-primary-100 text-primary-700 border-primary-300': form.techStack.includes(tech) }"
                >
                  {{ tech }}
                </button>
              </div>
            </div>
          </div>

          <!-- 提交按钮 -->
          <div class="flex justify-end space-x-4 pt-6 border-t border-gray-200">
            <button
              type="button"
              @click="router.back()"
              class="btn-secondary"
            >
              取消
            </button>
            <button
              type="submit"
              :disabled="isSubmitting"
              class="btn-primary"
            >
              <span v-if="isSubmitting" class="flex items-center">
                <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                发布中...
              </span>
              <span v-else>发布分享</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import TopNavBar from '@/components/TopNavBar.vue'
import CustomSelect from '@/components/CustomSelect.vue'
import { shareApi } from '@/api/share'
import { categoryApi } from '@/api/category'
import type { Category } from '@/types'

const router = useRouter()
const isSubmitting = ref(false)
const newTech = ref('')
const categories = ref<Category[]>([])

const form = reactive({
  title: '',
  content: '',
  category: '',
  techStack: [] as string[]
})

const commonTechs = [
  'Vue.js', 'React', 'TypeScript', 'JavaScript', 'Python', 'Java', 'C++',
  'Node.js', 'Express', 'Django', 'Flask', 'MySQL', 'MongoDB', 'Redis',
  'Docker', 'Kubernetes', 'Git', 'Linux', 'AWS', 'Azure', 'GCP'
]

// 分类选项
const categoryOptions = computed(() => {
  return categories.value.map(category => ({
    value: category.id,
    label: category.name
  }))
})

// 获取分类列表
const fetchCategories = async () => {
  try {
    const response = await categoryApi.getCategoriesByType('shares')
    console.log(response)
    // 处理分页格式的响应
    if (response && typeof response === 'object' && 'results' in response) {
      categories.value = (response as any).results
    } else if (Array.isArray(response)) {
      categories.value = response
    } else {
      categories.value = []
    }
  } catch (error) {
    console.error('Failed to fetch categories:', error)
    categories.value = []
  }
}

const addTech = (tech?: string) => {
  const techToAdd = tech || newTech.value.trim()
  if (techToAdd && !form.techStack.includes(techToAdd)) {
    form.techStack.push(techToAdd)
    newTech.value = ''
  }
}

const removeTech = (tech: string) => {
  const index = form.techStack.indexOf(tech)
  if (index > -1) {
    form.techStack.splice(index, 1)
  }
}

const handleSubmit = async () => {
  if (!form.title.trim() || !form.content.trim() || !form.category) {
    alert('请填写必填字段')
    return
  }

  isSubmitting.value = true
  try {
    await shareApi.createShare({
      title: form.title.trim(),
      content: form.content.trim(),
      category: form.category,
      techStack: form.techStack
    })
    
    // 发布成功后跳转到首页
    router.push('/')
  } catch (error) {
    console.error('发布分享失败:', error)
    alert('发布失败，请重试')
  } finally {
    isSubmitting.value = false
  }
}

onMounted(() => {
  fetchCategories()
})
</script> 