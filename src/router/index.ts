import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/HomePage.vue'),
    meta: { title: '首页' }
  },
  {
    path: '/team-hall',
    name: 'TeamHall',
    component: () => import('@/views/TeamHallPage.vue'),
    meta: { title: '组队大厅' }
  },
  {
    path: '/team/:id',
    name: 'TeamDetail',
    component: () => import('@/views/TeamDetailPage.vue'),
    meta: { title: '项目详情' }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('@/views/ProfilePage.vue'),
    meta: { title: '个人主页' }
  },
  {
    path: '/launch-team',
    name: 'LaunchTeam',
    component: () => import('@/views/LaunchTeamPage.vue'),
    meta: { title: '发起组队' }
  },
  {
    path: '/messages',
    name: 'Messages',
    component: () => import('@/views/MessageCenter.vue'),
    meta: { title: '消息中心' }
  },
  {
    path: '/resume',
    name: 'Resume',
    component: () => import('@/views/MyResumePage.vue'),
    meta: { title: '我的简历' }
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('@/views/AdminDashboard.vue'),
    meta: { title: '管理后台', requiresAdmin: true }
  },
  {
    path: '/test-error',
    name: 'TestError',
    component: () => import('@/views/TestErrorPage.vue'),
    meta: { title: '错误测试' }
  },
  // 错误页面路由
  {
    path: '/error/:type',
    name: 'Error',
    component: () => import('@/views/ErrorPage.vue'),
    meta: { title: '错误页面' }
  },
  // 404 捕获路由 - 必须放在最后
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/ErrorPage.vue'),
    meta: { title: '页面未找到' },
    beforeEnter: (to) => {
      // 重定向到404错误页面
      return { name: 'Error', params: { type: '404' } }
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
  // 设置页面标题
  document.title = `${to.meta.title} - SmartEdu`
  
  // 检查管理员权限
  if (to.meta.requiresAdmin) {
    // 这里应该检查用户是否有管理员权限
    // 暂时跳过权限检查
  }
  
  next()
})

export default router 