<template>
  <div>
    <h2>Регистрация</h2>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Логин" required />
      <input v-model="password" type="password" placeholder="Пароль" required />
      <input v-model="email" type="email" placeholder="Email" required />
      <button type="submit">Зарегистрироваться</button>
    </form>
    <p>Уже есть аккаунт? <router-link to="/login">Войти</router-link></p>
  </div>
</template>

<script>
import api from '@/api'

export default {
  data() {
    return {
      username: '',
      password: '',
      email: '',
    }
  },
  methods: {
    async register() {
      try {
        await api.post('auth/register/', {
          username: this.username,
          password: this.password,
          email: this.email,
        })
        alert('Регистрация успешна! Теперь войдите.')
        this.$router.push('/login')
      } catch (error) {
        alert('Ошибка регистрации')
      }
    },
  },
}
</script>
