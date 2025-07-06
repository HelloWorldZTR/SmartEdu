<template>
  <ErrorBoundary>
    <div id="app" class="min-h-screen bg-gray-50">
      <router-view />
    </div>
  </ErrorBoundary>
</template>

<script setup lang="ts">
import ErrorBoundary from '@/components/ErrorBoundary.vue'
// 根组件，只负责渲染路由视图
</script> 