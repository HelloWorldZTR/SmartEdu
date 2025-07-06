<template>
  <div class="relative">
    <!-- 触发器 -->
    <div
      @click="toggleDropdown"
      class="input-field cursor-pointer flex items-center justify-between"
      :class="{ 'ring-2 ring-primary-500': isOpen }"
    >
      <span class="text-gray-700" :class="{ 'text-gray-400': !modelValue }">
        {{ displayValue || placeholder }}
      </span>
      <svg
        class="w-4 h-4 text-gray-400 transition-transform duration-200"
        :class="{ 'rotate-180': isOpen }"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </div>

    <!-- 下拉选项 -->
    <Transition
      enter-active-class="transition ease-out duration-200"
      enter-from-class="opacity-0 scale-95"
      enter-to-class="opacity-100 scale-100"
      leave-active-class="transition ease-in duration-150"
      leave-from-class="opacity-100 scale-100"
      leave-to-class="opacity-0 scale-95"
    >
      <div
        v-if="isOpen"
        class="absolute z-50 w-full mt-1 bg-white border border-gray-200 rounded-lg shadow-lg max-h-60 overflow-auto"
      >
        <div
          v-for="option in options"
          :key="option.value"
          @click="selectOption(option)"
          class="px-4 py-3 cursor-pointer hover:bg-gray-50 transition-colors duration-150"
          :class="{ 'bg-primary-50 text-primary-700': modelValue === option.value }"
        >
          {{ option.label }}
        </div>
      </div>
    </Transition>

    <!-- 遮罩层 -->
    <div
      v-if="isOpen"
      @click="closeDropdown"
      class="fixed inset-0 z-40"
    ></div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'

interface Option {
  value: string | number
  label: string
}

interface Props {
  modelValue: string | number
  options: Option[]
  placeholder?: string
  required?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  placeholder: '请选择...',
  required: false
})

const emit = defineEmits<{
  'update:modelValue': [value: string | number]
}>()

const isOpen = ref(false)

const displayValue = computed(() => {
  const selectedOption = props.options.find(option => option.value === props.modelValue)
  return selectedOption?.label
})

const toggleDropdown = () => {
  isOpen.value = !isOpen.value
}

const closeDropdown = () => {
  isOpen.value = false
}

const selectOption = (option: Option) => {
  emit('update:modelValue', option.value)
  closeDropdown()
}

// 点击外部关闭下拉框
const handleClickOutside = (event: Event) => {
  const target = event.target as HTMLElement
  if (!target.closest('.relative')) {
    closeDropdown()
  }
}

// ESC键关闭下拉框
const handleKeydown = (event: KeyboardEvent) => {
  if (event.key === 'Escape') {
    closeDropdown()
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  document.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
  document.removeEventListener('keydown', handleKeydown)
})
</script> 