import { apiClient } from './index'
import type { Conversation, ChatMessage, Notification, PaginatedResponse } from '@/types'

export const chatApi = {
  // 获取对话列表
  getConversations: () => apiClient.get<PaginatedResponse<Conversation>>('/messages/conversations'),

  // 获取对话详情（消息记录）
  getConversationMessages: (conversationId: number) => 
    apiClient.get<PaginatedResponse<ChatMessage>>(`/messages/conversations/${conversationId}`),

  // 发送消息
  sendMessage: (data: {
    conversation: number
    content: string
    message_type?: 'text' | 'image' | 'file'
  }) => apiClient.postRaw<ChatMessage>('/messages/send', data),

  // 创建或获取与指定用户的对话
  getOrCreateConversation: (userId: number) => 
    apiClient.postRaw<Conversation>('/messages/conversations', { participant_id: userId }),

  // 获取通知列表
  getNotifications: () => apiClient.get<Notification[]>('/notifications'),

  // 标记通知为已读
  markNotificationAsRead: (notificationId: number) => 
    apiClient.patch(`/notifications/${notificationId}/read`),
} 