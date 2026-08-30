<template>
  <div>
    <h2>Вход</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Логин" required />
      <input v-model="password" type="password" placeholder="Пароль" required />
      <button type="submit">Войти</button>
    </form>
    <p>Нет аккаунта? <router-link to="/register">Зарегистрироваться</router-link></p>
  </div>
</template>

<script>
import api from '@/api'

export default {
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    async login() {
      try {
        const response = await api.post('/auth/token/', {
          username: this.username,
          password: this.password,
        })
        localStorage.setItem('access_token', response.data.access)
        localStorage.setItem('refresh_token', response.data.refresh)
        this.$router.push('/habits')
      } catch (error) {
        alert('Неверный логин или пароль')
      }
    },
  },
}
</script>