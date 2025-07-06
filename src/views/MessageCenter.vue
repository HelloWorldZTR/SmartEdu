<template>
  <div class="min-h-screen bg-gray-50">
    <TopNavBar />
    
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 h-[calc(100vh-200px)]">
        <!-- 聊天列表 -->
        <div class="lg:col-span-1">
          <div class="card h-full">
            <div class="flex items-center justify-between mb-4">
              <h2 class="text-xl font-semibold text-gray-900">消息</h2>
              <button class="text-primary-600 hover:text-primary-700">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                </svg>
              </button>
            </div>
            
            <div class="space-y-2">
              <div
                v-for="conversation in conversations"
                :key="conversation.id"
                @click="selectConversation(conversation)"
                class="flex items-center space-x-3 p-3 rounded-lg cursor-pointer transition-colors duration-200"
                :class="selectedConversation?.id === conversation.id ? 'bg-primary-50 border border-primary-200' : 'hover:bg-gray-50'"
              >
                <img
                  :src="conversation.avatar || '/default-avatar.png'"
                  :alt="conversation.name"
                  class="w-10 h-10 rounded-full object-cover"
                />
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <h3 class="text-sm font-medium text-gray-900 truncate">{{ conversation.name }}</h3>
                    <span class="text-xs text-gray-500">{{ formatRelativeTime(conversation.lastMessageTime) }}</span>
                  </div>
                  <p class="text-xs text-gray-600 truncate">{{ conversation.lastMessage }}</p>
                </div>
                <div v-if="conversation.unreadCount > 0" class="bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
                  {{ conversation.unreadCount > 99 ? '99+' : conversation.unreadCount }}
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 聊天窗口 -->
        <div class="lg:col-span-2">
          <div class="card h-full flex flex-col">
            <div v-if="selectedConversation" class="flex-1 flex flex-col">
              <!-- 聊天头部 -->
              <div class="flex items-center space-x-3 p-4 border-b border-gray-200">
                <img
                  :src="selectedConversation.avatar || '/default-avatar.png'"
                  :alt="selectedConversation.name"
                  class="w-8 h-8 rounded-full object-cover"
                />
                <div>
                  <h3 class="text-sm font-medium text-gray-900">{{ selectedConversation.name }}</h3>
                  <p class="text-xs text-gray-500">在线</p>
                </div>
              </div>
              
              <!-- 消息列表 -->
              <div class="flex-1 overflow-y-auto p-4 space-y-4">
                <div
                  v-for="message in messages"
                  :key="message.id"
                  class="flex"
                  :class="message.isOwn ? 'justify-end' : 'justify-start'"
                >
                  <div
                    class="max-w-xs lg:max-w-md px-4 py-2 rounded-lg"
                    :class="message.isOwn ? 'bg-primary-600 text-white' : 'bg-gray-100 text-gray-900'"
                  >
                    <p class="text-sm">{{ message.content }}</p>
                    <p class="text-xs mt-1 opacity-70">{{ formatRelativeTime(message.sentAt) }}</p>
                  </div>
                </div>
              </div>
              
              <!-- 消息输入 -->
              <div class="p-4 border-t border-gray-200">
                <div class="flex space-x-2">
                  <input
                    v-model="newMessage"
                    type="text"
                    placeholder="输入消息..."
                    class="flex-1 input-field"
                    @keyup.enter="sendMessage"
                  />
                  <button
                    @click="sendMessage"
                    class="btn-primary"
                    :disabled="!newMessage.trim()"
                  >
                    发送
                  </button>
                </div>
              </div>
            </div>
            
            <!-- 未选择对话时的提示 -->
            <div v-else class="flex-1 flex items-center justify-center">
              <div class="text-center text-gray-500">
                <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                </svg>
                <h3 class="mt-2 text-sm font-medium text-gray-900">选择对话</h3>
                <p class="mt-1 text-sm text-gray-500">选择一个对话开始聊天</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import TopNavBar from '@/components/TopNavBar.vue'
import { formatRelativeTime } from '@/utils/date'

interface Conversation {
  id: number
  name: string
  avatar?: string
  lastMessage: string
  lastMessageTime: string
  unreadCount: number
}

interface Message {
  id: number
  content: string
  sentAt: string
  isOwn: boolean
}

const selectedConversation = ref<Conversation | null>(null)
const newMessage = ref('')

// 模拟对话数据
const conversations = ref<Conversation[]>([
  {
    id: 1,
    name: '张三',
    avatar: '/default-avatar.png',
    lastMessage: '你好，我对你的项目很感兴趣',
    lastMessageTime: '2024-01-15T10:30:00Z',
    unreadCount: 2
  },
  {
    id: 2,
    name: '李四',
    avatar: '/default-avatar.png',
    lastMessage: '项目进展如何？',
    lastMessageTime: '2024-01-15T09:15:00Z',
    unreadCount: 0
  }
])

// 模拟消息数据
const messages = ref<Message[]>([
  {
    id: 1,
    content: '你好，我对你的项目很感兴趣',
    sentAt: '2024-01-15T10:30:00Z',
    isOwn: false
  },
  {
    id: 2,
    content: '谢谢关注！请问你有什么问题吗？',
    sentAt: '2024-01-15T10:32:00Z',
    isOwn: true
  },
  {
    id: 3,
    content: '我想了解一下项目的具体技术栈',
    sentAt: '2024-01-15T10:35:00Z',
    isOwn: false
  }
])

const selectConversation = (conversation: Conversation) => {
  selectedConversation.value = conversation
  // 这里应该加载对应的消息记录
}

const sendMessage = () => {
  if (!newMessage.value.trim() || !selectedConversation.value) return
  
  const message: Message = {
    id: Date.now(),
    content: newMessage.value,
    sentAt: new Date().toISOString(),
    isOwn: true
  }
  
  messages.value.push(message)
  newMessage.value = ''
  
  // 这里应该发送消息到服务器
}
</script> 