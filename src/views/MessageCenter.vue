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
            
            <div v-if="loading" class="flex justify-center py-8">
              <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
            </div>
            
            <div v-else class="space-y-2">
              <div
                v-for="conversation in conversations"
                :key="conversation.id"
                @click="selectConversation(conversation)"
                class="flex items-center space-x-3 p-3 rounded-lg cursor-pointer transition-colors duration-200"
                :class="selectedConversation?.id === conversation.id ? 'bg-primary-50 border border-primary-200' : 'hover:bg-gray-50'"
              >
                <img
                  :src="getOtherParticipant(conversation)?.avatar || '/default-avatar.png'"
                  :alt="getOtherParticipant(conversation)?.username"
                  class="w-10 h-10 rounded-full object-cover"
                />
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <h3 class="text-sm font-medium text-gray-900 truncate">{{ getOtherParticipant(conversation)?.username }}</h3>
                    <span class="text-xs text-gray-500">{{ formatRelativeTime(conversation.updated_at) }}</span>
                  </div>
                  <p class="text-xs text-gray-600 truncate">{{ conversation.last_message || '暂无消息' }}</p>
                </div>
                <div v-if="conversation.unread_count && conversation.unread_count > 0" class="bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
                  {{ conversation.unread_count > 99 ? '99+' : conversation.unread_count }}
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
                  :src="getOtherParticipant(selectedConversation)?.avatar || '/default-avatar.png'"
                  :alt="getOtherParticipant(selectedConversation)?.username"
                  class="w-8 h-8 rounded-full object-cover"
                />
                <div>
                  <h3 class="text-sm font-medium text-gray-900">{{ getOtherParticipant(selectedConversation)?.username }}</h3>
                  <p class="text-xs text-gray-500">在线</p>
                </div>
              </div>
              
              <!-- 消息列表 -->
              <div class="flex-1 overflow-y-auto p-4 space-y-4">
                <div v-if="messagesLoading" class="flex justify-center py-4">
                  <div class="animate-spin rounded-full h-6 w-6 border-b-2 border-primary-600"></div>
                </div>
                <div
                  v-for="message in messages"
                  :key="message.id"
                  class="flex"
                  :class="message.sender && message.sender.id === currentUser?.id ? 'justify-end' : 'justify-start'"
                >
                  <div
                    class="max-w-xs lg:max-w-md px-4 py-2 rounded-lg"
                    :class="message.sender && message.sender.id === currentUser?.id ? 'bg-primary-600 text-white' : 'bg-gray-100 text-gray-900'"
                  >
                    <p class="text-sm">{{ message.content }}</p>
                    <p class="text-xs mt-1 opacity-70">{{ formatRelativeTime(message.created_at) }}</p>
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
                    :disabled="sending"
                  />
                  <button
                    @click="sendMessage"
                    class="btn-primary"
                    :disabled="!newMessage.trim() || sending"
                  >
                    {{ sending ? '发送中...' : '发送' }}
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
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import TopNavBar from '@/components/TopNavBar.vue'
import { formatRelativeTime } from '@/utils/date'
import { chatApi } from '@/api/chat'
import { useUserStore } from '@/stores/user'
import { useToast } from 'vue-toastification'
import type { Conversation, ChatMessage } from '@/types'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()
const toast = useToast()

const currentUser = computed(() => userStore.currentUser)
const selectedConversation = ref<Conversation | null>(null)
const newMessage = ref('')
const loading = ref(false)
const messagesLoading = ref(false)
const sending = ref(false)

const conversations = ref<Conversation[]>([])
const messages = ref<ChatMessage[]>([])

// 确保conversations初始化为空数组
console.log('初始化conversations:', conversations.value)
console.log('conversations类型:', typeof conversations.value)
console.log('conversations是否为数组:', Array.isArray(conversations.value))

// 获取对话中的其他参与者
const getOtherParticipant = (conversation: Conversation) => {
  if (!currentUser.value || !conversation || !conversation.participants) return null
  return conversation.participants.find(p => p.id !== currentUser.value?.id)
}

// 加载对话列表
const loadConversations = async () => {
  loading.value = true
  try {
    const response = await chatApi.getConversations()
    console.log('loadConversations响应:', response)
    console.log('response类型:', typeof response)
    console.log('response是否为数组:', Array.isArray(response))
    
    // 处理分页响应
    if (response && response.results) {
      conversations.value = response.results
    } else if (Array.isArray(response)) {
      conversations.value = response
    } else {
      conversations.value = []
    }
    
    console.log('设置后的conversations.value:', conversations.value)
    console.log('conversations.value是否为数组:', Array.isArray(conversations.value))
  } catch (error) {
    console.error('加载对话列表失败:', error)
    toast.error('加载对话列表失败')
    conversations.value = []
  } finally {
    loading.value = false
  }
}

// 加载消息记录
const loadMessages = async (conversationId: number) => {
  messagesLoading.value = true
  try {
    const response = await chatApi.getConversationMessages(conversationId)
    console.log('loadMessages响应:', response)
    
    // 处理分页响应或直接数组
    let messageList: ChatMessage[] = []
    if (response && response.results) {
      messageList = response.results
    } else if (Array.isArray(response)) {
      messageList = response
    }
    
    // 验证消息数据的完整性
    messageList = messageList.filter((message: ChatMessage) => {
      if (!message || !message.sender) {
        console.warn('跳过无效消息:', message)
        return false
      }
      return true
    })
    
    messages.value = messageList
    console.log('设置后的messages.value:', messages.value)
  } catch (error) {
    console.error('加载消息记录失败:', error)
    toast.error('加载消息记录失败')
    messages.value = []
  } finally {
    messagesLoading.value = false
  }
}

// 选择对话
const selectConversation = async (conversation: Conversation) => {
  selectedConversation.value = conversation
  await loadMessages(conversation.id)
}

// 发送消息
const sendMessage = async () => {
  if (!newMessage.value.trim() || !selectedConversation.value || sending.value) return
  
  const messageContent = newMessage.value
  newMessage.value = ''
  sending.value = true
  
  try {
    const response = await chatApi.sendMessage({
      conversation: selectedConversation.value.id,
      content: messageContent,
      message_type: 'text'
    })
    
    // 验证响应数据
    if (!response) {
      console.error('发送消息响应为空:', response)
      toast.error('发送消息失败：响应为空')
      newMessage.value = messageContent
      return
    }
    
    // 验证消息数据完整性
    if (!response.id || !response.sender) {
      console.error('消息数据不完整:', response)
      toast.error('发送消息失败：消息数据不完整')
      newMessage.value = messageContent
      return
    }
    
    // 添加新消息到列表
    messages.value.push(response)
    
    // 更新对话列表中的最后消息
    const conversation = conversations.value.find(c => c.id === selectedConversation.value?.id)
    if (conversation) {
      conversation.last_message = messageContent
      conversation.updated_at = new Date().toISOString()
    }
  } catch (error) {
    console.error('发送消息失败:', error)
    toast.error('发送消息失败')
    // 恢复消息内容
    newMessage.value = messageContent
  } finally {
    sending.value = false
  }
}

// 处理URL参数中的userId
const handleUserIdFromUrl = async () => {
  const userId = route.query.userId
  if (userId && typeof userId === 'string') {
    console.log('处理URL参数userId:', userId)
    console.log('当前conversations.value:', conversations.value)
    console.log('conversations.value类型:', typeof conversations.value)
    console.log('conversations.value是否为数组:', Array.isArray(conversations.value))
    
    // 验证userId格式
    const userIdNum = parseInt(userId)
    if (isNaN(userIdNum) || userIdNum <= 0) {
      console.error('无效的userId:', userId)
      toast.error('无效的用户ID')
      return
    }
    
    try {
      const response = await chatApi.getOrCreateConversation(userIdNum)
      console.log('完整API响应:', response)
      console.log('response类型:', typeof response)
      
      // 后端直接返回对话对象，不是ApiResponse包装
      const conversation = response
      
      // 检查conversation是否存在
      if (!conversation) {
        console.error('API返回的conversation为空')
        console.error('完整响应内容:', JSON.stringify(response, null, 2))
        toast.error('创建对话失败：服务器返回空数据')
        return
      }
      
      console.log('解析后的conversation:', conversation)
      console.log('participants:', conversation.participants)
      
      // 验证participants字段
      if (!conversation.participants || !Array.isArray(conversation.participants)) {
        console.error('conversation.participants格式错误:', conversation.participants)
        toast.error('对话数据格式错误')
        return
      }
      
      // 确保conversations.value是数组
      if (!Array.isArray(conversations.value)) {
        console.error('conversations.value不是数组:', conversations.value)
        conversations.value = []
      }
      
      // 如果对话不在列表中，添加到列表
      if (!conversations.value.find(c => c.id === conversation.id)) {
        conversations.value.unshift(conversation)
      }
      
      // 选择这个对话
      await selectConversation(conversation)
      
      // 清除URL参数
      router.replace({ query: {} })
    } catch (error: any) {
      console.error('创建对话失败:', error)
      
      // 根据错误类型显示不同的提示
      if (error.response?.status === 404) {
        toast.error('用户不存在')
      } else if (error.response?.status === 400) {
        toast.error(error.response.data?.error || '请求参数错误')
      } else {
        toast.error('创建对话失败，请稍后重试')
      }
    }
  }
}

onMounted(async () => {
  await loadConversations()
  await handleUserIdFromUrl()
})
</script> 