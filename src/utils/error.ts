import { useRouter } from 'vue-router'

export interface ErrorInfo {
  type: '404' | '403' | '500' | 'server' | 'network'
  code?: string
  message?: string
}

/**
 * 跳转到错误页面
 * @param errorInfo 错误信息
 */
export function navigateToError(errorInfo: ErrorInfo) {
  const router = useRouter()
  router.push({
    name: 'Error',
    params: {
      type: errorInfo.type,
      code: errorInfo.code || ''
    }
  })
}

/**
 * 处理API错误
 * @param error 错误对象
 */
export function handleApiError(error: any) {
  console.error('API Error:', error)
  
  let errorType: ErrorInfo['type'] = 'server'
  let errorCode = ''
  
  if (error.response) {
    // 服务器响应了错误状态码
    const status = error.response.status
    errorCode = status.toString()
    
    switch (status) {
      case 404:
        errorType = '404'
        break
      case 403:
        errorType = '403'
        break
      case 500:
        errorType = '500'
        break
      default:
        errorType = 'server'
    }
  } else if (error.request) {
    // 请求已发出但没有收到响应
    errorType = 'network'
    errorCode = 'NETWORK_ERROR'
  } else {
    // 其他错误
    errorType = 'server'
    errorCode = 'UNKNOWN_ERROR'
  }
  
  return { type: errorType, code: errorCode }
}

/**
 * 检查是否为网络错误
 * @param error 错误对象
 */
export function isNetworkError(error: any): boolean {
  return !error.response && error.request
}

/**
 * 检查是否为服务器错误
 * @param error 错误对象
 */
export function isServerError(error: any): boolean {
  return error.response && error.response.status >= 500
}

/**
 * 检查是否为客户端错误
 * @param error 错误对象
 */
export function isClientError(error: any): boolean {
  return error.response && error.response.status >= 400 && error.response.status < 500
} 