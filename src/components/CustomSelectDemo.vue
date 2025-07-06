<template>
  <div class="max-w-4xl mx-auto p-6 space-y-8">
    <div class="text-center">
      <h1 class="text-3xl font-bold text-gray-900 mb-4">自定义选择器演示</h1>
      <p class="text-gray-600">展示自定义下拉选择器的效果和交互体验</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <!-- 基本用法 -->
      <div class="card">
        <h2 class="text-xl font-semibold text-gray-900 mb-4">基本用法</h2>
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">选择水果</label>
            <CustomSelect
              v-model="selectedFruit"
              :options="fruitOptions"
              placeholder="请选择水果"
            />
            <p class="mt-2 text-sm text-gray-500">选中值: {{ selectedFruit }}</p>
          </div>
        </div>
      </div>

      <!-- 带默认值 -->
      <div class="card">
        <h2 class="text-xl font-semibold text-gray-900 mb-4">带默认值</h2>
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">选择颜色</label>
            <CustomSelect
              v-model="selectedColor"
              :options="colorOptions"
              placeholder="请选择颜色"
            />
            <p class="mt-2 text-sm text-gray-500">选中值: {{ selectedColor }}</p>
          </div>
        </div>
      </div>

      <!-- 必填字段 -->
      <div class="card">
        <h2 class="text-xl font-semibold text-gray-900 mb-4">必填字段</h2>
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">选择城市 *</label>
            <CustomSelect
              v-model="selectedCity"
              :options="cityOptions"
              placeholder="请选择城市"
              required
            />
            <p class="mt-2 text-sm text-gray-500">选中值: {{ selectedCity }}</p>
          </div>
        </div>
      </div>

      <!-- 动态选项 -->
      <div class="card">
        <h2 class="text-xl font-semibold text-gray-900 mb-4">动态选项</h2>
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">选择技术</label>
            <CustomSelect
              v-model="selectedTech"
              :options="techOptions"
              placeholder="请选择技术栈"
            />
            <p class="mt-2 text-sm text-gray-500">选中值: {{ selectedTech }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 功能说明 -->
    <div class="card">
      <h2 class="text-xl font-semibold text-gray-900 mb-4">功能特性</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="space-y-3">
          <h3 class="font-medium text-gray-900">交互功能</h3>
          <ul class="space-y-2 text-sm text-gray-600">
            <li>• 点击展开/收起下拉选项</li>
            <li>• 点击外部区域自动关闭</li>
            <li>• 按 ESC 键关闭下拉框</li>
            <li>• 选中项高亮显示</li>
            <li>• 平滑的动画过渡效果</li>
          </ul>
        </div>
        <div class="space-y-3">
          <h3 class="font-medium text-gray-900">样式特性</h3>
          <ul class="space-y-2 text-sm text-gray-600">
            <li>• 与现有 input-field 样式一致</li>
            <li>• 响应式设计，适配移动端</li>
            <li>• 悬停和焦点状态效果</li>
            <li>• 自定义下拉箭头图标</li>
            <li>• 阴影和边框效果</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import CustomSelect from './CustomSelect.vue'

const selectedFruit = ref('')
const selectedColor = ref('red')
const selectedCity = ref('')
const selectedTech = ref('')

const fruitOptions = [
  { value: 'apple', label: '苹果' },
  { value: 'banana', label: '香蕉' },
  { value: 'orange', label: '橙子' },
  { value: 'grape', label: '葡萄' },
  { value: 'watermelon', label: '西瓜' }
]

const colorOptions = [
  { value: 'red', label: '红色' },
  { value: 'blue', label: '蓝色' },
  { value: 'green', label: '绿色' },
  { value: 'yellow', label: '黄色' },
  { value: 'purple', label: '紫色' }
]

const cityOptions = [
  { value: 'beijing', label: '北京' },
  { value: 'shanghai', label: '上海' },
  { value: 'guangzhou', label: '广州' },
  { value: 'shenzhen', label: '深圳' },
  { value: 'hangzhou', label: '杭州' }
]

const techOptions = [
  { value: 'vue', label: 'Vue.js' },
  { value: 'react', label: 'React' },
  { value: 'angular', label: 'Angular' },
  { value: 'typescript', label: 'TypeScript' },
  { value: 'python', label: 'Python' },
  { value: 'java', label: 'Java' }
]
</script> 