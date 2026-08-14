import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import HabitsView from '@/views/HabitsView.vue'
import CreateHabitView from '@/views/CreateHabitView.vue'

const routes = [
  { path: '/', redirect: '/habits' },
  { path: '/login', component: LoginView },
  { path: '/register', component: RegisterView },
  { path: '/habits', component: HabitsView, meta: { requiresAuth: true } },
  { path: '/habits/create', component: CreateHabitView, meta: { requiresAuth: true } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('access_token')
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
