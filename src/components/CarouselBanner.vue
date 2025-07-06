<template>
  <div class="relative overflow-hidden rounded-lg shadow-lg">
    <div class="relative h-64 md:h-80">
      <div
        v-for="(banner, index) in banners"
        :key="banner.id"
        class="absolute inset-0 transition-opacity duration-500 cursor-pointer"
        :class="{ 'opacity-100': currentIndex === index, 'opacity-0': currentIndex !== index }"
        @click="handleBannerClick(banner)"
      >
        <img
          :src="banner.image"
          :alt="banner.title"
          class="w-full h-full object-cover"
          @error="handleImageError"
          @load="handleImageLoad"
          @abort="handleImageAbort"
        />
        <div class="absolute inset-0 bg-black bg-opacity-40"></div>
        <div class="absolute bottom-0 left-0 right-0 p-6 text-white">
          <h3 class="text-xl md:text-2xl font-bold mb-2">{{ banner.title }}</h3>
          <p class="text-sm md:text-base opacity-90">{{ banner.description }}</p>
        </div>
      </div>
    </div>
    
    <!-- 指示器 -->
    <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-2">
      <button
        v-for="(banner, index) in banners"
        :key="banner.id"
        @click="setCurrentIndex(index)"
        class="w-3 h-3 rounded-full transition-colors duration-200"
        :class="currentIndex === index ? 'bg-white' : 'bg-white bg-opacity-50'"
      ></button>
    </div>
    
    <!-- 左右箭头 -->
    <button
      @click="previous"
      class="absolute left-4 top-1/2 transform -translate-y-1/2 w-10 h-10 bg-black bg-opacity-30 hover:bg-opacity-50 text-white rounded-full flex items-center justify-center transition-all duration-200"
    >
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
      </svg>
    </button>
    
    <button
      @click="next"
      class="absolute right-4 top-1/2 transform -translate-y-1/2 w-10 h-10 bg-black bg-opacity-30 hover:bg-opacity-50 text-white rounded-full flex items-center justify-center transition-all duration-200"
    >
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
      </svg>
    </button>
    
    <!-- 自动播放控制按钮 -->
    <button
      v-if="banners.length > 1"
      @click="toggleAutoplay"
      class="absolute top-4 right-4 w-8 h-8 bg-black bg-opacity-30 hover:bg-opacity-50 text-white rounded-full flex items-center justify-center transition-all duration-200"
      :title="isAutoplay ? '暂停自动播放' : '开始自动播放'"
    >
      <svg v-if="isAutoplay" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 9v6m4-6v6" />
      </svg>
      <svg v-else class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue'
import type { Banner } from '@/api/home'

interface Props {
  banners: Banner[]
  currentIndex?: number
  isAutoplay?: boolean
}

interface Emits {
  (e: 'banner-click', banner: Banner): void
  (e: 'banner-change', index: number): void
  (e: 'toggle-autoplay'): void
}

const props = withDefaults(defineProps<Props>(), {
  currentIndex: 0,
  isAutoplay: true
})

const emit = defineEmits<Emits>()

// 内部状态，用于处理外部传入的currentIndex
const currentIndex = computed({
  get: () => props.currentIndex,
  set: (value: number) => {
    emit('banner-change', value)
  }
})

const handleBannerClick = (banner: Banner) => {
  emit('banner-click', banner)
}

const next = () => {
  if (props.banners.length > 1) {
    const newIndex = (currentIndex.value + 1) % props.banners.length
    currentIndex.value = newIndex
  }
}

const previous = () => {
  if (props.banners.length > 1) {
    const newIndex = currentIndex.value === 0 
      ? props.banners.length - 1 
      : currentIndex.value - 1
    currentIndex.value = newIndex
  }
}

const setCurrentIndex = (index: number) => {
  currentIndex.value = index
}

const toggleAutoplay = () => {
  emit('toggle-autoplay')
}

const handleImageError = (event: Event) => {
  const img = event.target as HTMLImageElement
  console.error('Image failed to load:', img.src)
  // 可以设置一个默认图片
  img.src = '/placeholder-banner.jpg'
}

const handleImageLoad = (event: Event) => {
  // 图片加载成功，无需特殊处理
}

const handleImageAbort = (event: Event) => {
  const img = event.target as HTMLImageElement
  console.warn('Image aborted loading:', img.src)
}
</script> 