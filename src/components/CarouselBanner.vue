<template>
  <div class="relative overflow-hidden rounded-lg shadow-lg">
    <div class="relative h-64 md:h-80">
      <div
        v-for="(banner, index) in banners"
        :key="banner.id"
        class="absolute inset-0 transition-opacity duration-500"
        :class="{ 'opacity-100': currentIndex === index, 'opacity-0': currentIndex !== index }"
      >
        <img
          :src="banner.image"
          :alt="banner.title"
          class="w-full h-full object-cover"
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
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

interface Banner {
  id: number
  title: string
  image: string
  description?: string
  link?: string
}

interface Props {
  banners: Banner[]
  autoplay?: boolean
  interval?: number
}

const props = withDefaults(defineProps<Props>(), {
  autoplay: true,
  interval: 5000
})

const currentIndex = ref(0)
let autoplayTimer: number | null = null

const next = () => {
  currentIndex.value = (currentIndex.value + 1) % props.banners.length
}

const previous = () => {
  currentIndex.value = currentIndex.value === 0 
    ? props.banners.length - 1 
    : currentIndex.value - 1
}

const setCurrentIndex = (index: number) => {
  currentIndex.value = index
}

const startAutoplay = () => {
  if (props.autoplay && props.banners.length > 1) {
    autoplayTimer = window.setInterval(() => {
      next()
    }, props.interval)
  }
}

const stopAutoplay = () => {
  if (autoplayTimer) {
    clearInterval(autoplayTimer)
    autoplayTimer = null
  }
}

onMounted(() => {
  startAutoplay()
})

onUnmounted(() => {
  stopAutoplay()
})
</script> 