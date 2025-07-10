<template>
  <div class="card">
    <h2 class="text-xl font-semibold text-gray-900 mb-4">我的申请信息</h2>
    <div class="mb-2"><span class="font-medium">岗位：</span>{{ application.job.title }}</div>
    <div class="mb-2"><span class="font-medium">说明：</span>{{ application.note || '无' }}</div>
    <div class="mb-2"><span class="font-medium">状态：</span>{{ statusText[application.status] }}</div>
    <div class="mb-2"><span class="font-medium">申请时间：</span>{{ application.createdAt || application.created_at }}</div>
  </div>
</template>

<script setup lang="ts">
import type { Application } from '@/types'
const props = defineProps<{ application: Application }>()
const statusText = {
  pending: '待处理',
  accepted: '已接受',
  rejected: '已拒绝'
}
</script> 