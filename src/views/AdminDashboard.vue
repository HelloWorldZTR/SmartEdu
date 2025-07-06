<template>
  <div class="min-h-screen bg-gray-50">
    <TopNavBar />
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      <div class="mb-6">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">管理后台</h1>
        <p class="text-gray-600">平台运行状况与内容管理</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <!-- 统计面板 -->
        <div class="lg:col-span-1 space-y-6">
          <UserStatsPanel />
        </div>
        
        <!-- 主要内容 -->
        <div class="lg:col-span-3 space-y-6">
          <ReportedContentList />
          <ProjectApprovalQueue />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import TopNavBar from '@/components/TopNavBar.vue'
import UserStatsPanel from '@/components/UserStatsPanel.vue'
import ReportedContentList from '@/components/ReportedContentList.vue'
import ProjectApprovalQueue from '@/components/ProjectApprovalQueue.vue'
</script> 