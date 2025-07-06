<template>
  <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <div class="text-center">
        <h1 class="text-3xl font-bold text-gray-900">SmartEdu</h1>
        <h2 class="mt-6 text-2xl font-bold text-gray-900">创建新账户</h2>
        <p class="mt-2 text-sm text-gray-600">
          已有账户？
          <router-link
            to="/login"
            class="font-medium text-primary-600 hover:text-primary-500"
          >
            立即登录
          </router-link>
        </p>
      </div>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <!-- 用户名输入 -->
          <div>
            <label for="username" class="block text-sm font-medium text-gray-700">
              用户名
            </label>
            <div class="mt-1">
              <input
                id="username"
                v-model="form.username"
                type="text"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                placeholder="请输入用户名"
                :class="{ 'border-red-300 focus:ring-red-500 focus:border-red-500': errors.username }"
              />
            </div>
            <p v-if="errors.username" class="mt-2 text-sm text-red-600">
              {{ errors.username }}
            </p>
          </div>

          <!-- 邮箱输入 -->
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">
              邮箱地址
            </label>
            <div class="mt-1">
              <input
                id="email"
                v-model="form.email"
                type="email"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                placeholder="请输入邮箱地址"
                :class="{ 'border-red-300 focus:ring-red-500 focus:border-red-500': errors.email }"
              />
            </div>
            <p v-if="errors.email" class="mt-2 text-sm text-red-600">
              {{ errors.email }}
            </p>
          </div>

          <!-- 学校输入 -->
          <div>
            <label for="school" class="block text-sm font-medium text-gray-700">
              学校
            </label>
            <div class="mt-1">
              <input
                id="school"
                v-model="form.school"
                type="text"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                placeholder="请输入学校名称"
                :class="{ 'border-red-300 focus:ring-red-500 focus:border-red-500': errors.school }"
              />
            </div>
            <p v-if="errors.school" class="mt-2 text-sm text-red-600">
              {{ errors.school }}
            </p>
          </div>

          <!-- 院系输入 -->
          <div>
            <label for="department" class="block text-sm font-medium text-gray-700">
              院系
            </label>
            <div class="mt-1">
              <input
                id="department"
                v-model="form.department"
                type="text"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                placeholder="请输入院系名称"
                :class="{ 'border-red-300 focus:ring-red-500 focus:border-red-500': errors.department }"
              />
            </div>
            <p v-if="errors.department" class="mt-2 text-sm text-red-600">
              {{ errors.department }}
            </p>
          </div>

          <!-- 密码输入 -->
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700">
              密码
            </label>
            <div class="mt-1 relative">
              <input
                id="password"
                v-model="form.password"
                :type="showPassword ? 'text' : 'password'"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm pr-10"
                placeholder="请输入密码"
                :class="{ 'border-red-300 focus:ring-red-500 focus:border-red-500': errors.password }"
              />
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute inset-y-0 right-0 pr-3 flex items-center"
              >
                <svg v-if="showPassword" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.878 9.878L3 3m6.878 6.878L21 21" />
                </svg>
                <svg v-else class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
              </button>
            </div>
            <p v-if="errors.password" class="mt-2 text-sm text-red-600">
              {{ errors.password }}
            </p>
          </div>

          <!-- 确认密码输入 -->
          <div>
            <label for="confirmPassword" class="block text-sm font-medium text-gray-700">
              确认密码
            </label>
            <div class="mt-1 relative">
              <input
                id="confirmPassword"
                v-model="form.confirmPassword"
                :type="showConfirmPassword ? 'text' : 'password'"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm pr-10"
                placeholder="请再次输入密码"
                :class="{ 'border-red-300 focus:ring-red-500 focus:border-red-500': errors.confirmPassword }"
              />
              <button
                type="button"
                @click="showConfirmPassword = !showConfirmPassword"
                class="absolute inset-y-0 right-0 pr-3 flex items-center"
              >
                <svg v-if="showConfirmPassword" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.878 9.878L3 3m6.878 6.878L21 21" />
                </svg>
                <svg v-else class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
              </button>
            </div>
            <p v-if="errors.confirmPassword" class="mt-2 text-sm text-red-600">
              {{ errors.confirmPassword }}
            </p>
          </div>

          <!-- 同意条款 -->
          <div class="flex items-center">
            <input
              id="agree-terms"
              v-model="form.agreeTerms"
              type="checkbox"
              required
              class="h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded"
              :class="{ 'border-red-300': errors.agreeTerms }"
            />
            <label for="agree-terms" class="ml-2 block text-sm text-gray-900">
              我已阅读并同意
              <a href="#" class="text-primary-600 hover:text-primary-500">服务条款</a>
              和
              <a href="#" class="text-primary-600 hover:text-primary-500">隐私政策</a>
            </label>
          </div>
          <p v-if="errors.agreeTerms" class="text-sm text-red-600">
            {{ errors.agreeTerms }}
          </p>

          <!-- 提交按钮 -->
          <div>
            <button
              type="submit"
              :disabled="isSubmitting"
              class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="isSubmitting" class="absolute left-0 inset-y-0 flex items-center pl-3">
                <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
              </span>
              {{ isSubmitting ? '注册中...' : '注册' }}
            </button>
          </div>

          <!-- 错误信息 -->
          <div v-if="errorMessage" class="rounded-md bg-red-50 p-4">
            <div class="flex">
              <div class="flex-shrink-0">
                <svg class="h-5 w-5 text-red-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
                </svg>
              </div>
              <div class="ml-3">
                <h3 class="text-sm font-medium text-red-800">
                  {{ errorMessage }}
                </h3>
              </div>
            </div>
          </div>
        </form>

        <!-- 社交注册 -->
        <div class="mt-6">
          <div class="relative">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-gray-300" />
            </div>
            <div class="relative flex justify-center text-sm">
              <span class="px-2 bg-white text-gray-500">或者使用</span>
            </div>
          </div>

          <div class="mt-6 grid grid-cols-2 gap-3">
            <button
              type="button"
              class="w-full inline-flex justify-center py-2 px-4 border border-gray-300 rounded-md shadow-sm bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
            >
              <svg class="w-5 h-5" viewBox="0 0 24 24">
                <path fill="currentColor" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                <path fill="currentColor" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                <path fill="currentColor" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                <path fill="currentColor" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
              </svg>
              <span class="ml-2">Google</span>
            </button>

            <button
              type="button"
              class="w-full inline-flex justify-center py-2 px-4 border border-gray-300 rounded-md shadow-sm bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
              </svg>
              <span class="ml-2">GitHub</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()

// 表单数据
const form = reactive({
  username: '',
  email: '',
  school: '',
  department: '',
  password: '',
  confirmPassword: '',
  agreeTerms: false
})

// 状态
const isSubmitting = ref(false)
const showPassword = ref(false)
const showConfirmPassword = ref(false)
const errorMessage = ref('')
const errors = reactive({
  username: '',
  email: '',
  school: '',
  department: '',
  password: '',
  confirmPassword: '',
  agreeTerms: ''
})

// 表单验证
const validateForm = () => {
  errors.username = ''
  errors.email = ''
  errors.school = ''
  errors.department = ''
  errors.password = ''
  errors.confirmPassword = ''
  errors.agreeTerms = ''
  
  if (!form.username) {
    errors.username = '请输入用户名'
    return false
  }
  
  if (form.username.length < 2) {
    errors.username = '用户名长度至少2位'
    return false
  }
  
  if (!form.email) {
    errors.email = '请输入邮箱地址'
    return false
  }
  
  if (!form.email.includes('@')) {
    errors.email = '请输入有效的邮箱地址'
    return false
  }
  
  if (!form.school) {
    errors.school = '请输入学校名称'
    return false
  }
  
  if (!form.department) {
    errors.department = '请输入院系名称'
    return false
  }
  
  if (!form.password) {
    errors.password = '请输入密码'
    return false
  }
  
  if (form.password.length < 6) {
    errors.password = '密码长度至少6位'
    return false
  }
  
  if (!form.confirmPassword) {
    errors.confirmPassword = '请确认密码'
    return false
  }
  
  if (form.password !== form.confirmPassword) {
    errors.confirmPassword = '两次输入的密码不一致'
    return false
  }
  
  if (!form.agreeTerms) {
    errors.agreeTerms = '请同意服务条款和隐私政策'
    return false
  }
  
  return true
}

// 提交表单
const handleSubmit = async () => {
  if (!validateForm()) {
    return
  }
  
  isSubmitting.value = true
  errorMessage.value = ''
  
  try {
    await userStore.register({
      username: form.username,
      email: form.email,
      password: form.password,
      school: form.school,
      department: form.department
    })
    
    // 注册成功，跳转到登录页
    router.push('/login')
  } catch (error: any) {
    console.error('Registration failed:', error)
    
    // 处理不同的错误类型
    if (error.response?.status === 400) {
      const errorData = error.response.data
      if (errorData.email) {
        errors.email = errorData.email[0]
      }
      if (errorData.username) {
        errors.username = errorData.username[0]
      }
      if (errorData.password) {
        errors.password = errorData.password[0]
      }
      if (errorData.school) {
        errors.school = errorData.school[0]
      }
      if (errorData.department) {
        errors.department = errorData.department[0]
      }
    } else if (error.response?.status === 409) {
      errorMessage.value = '邮箱或用户名已存在'
    } else if (error.code === 'ECONNREFUSED' || error.code === 'ERR_NETWORK') {
      errorMessage.value = '网络连接失败，请检查网络设置'
    } else {
      errorMessage.value = '注册失败，请稍后重试'
    }
  } finally {
    isSubmitting.value = false
  }
}
</script> 