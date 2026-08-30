<template>
  <div>
    <h2>Регистрация</h2>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Логин" required />
      <input v-model="password" type="password" placeholder="Пароль" required />
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="telegram_chat_id" placeholder="Telegram Chat ID" required />
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
      telegram_chat_id: '',
    }
  },
  methods: {
    async register() {
      try {
        await api.post('auth/register/', {
          username: this.username,
          password: this.password,
          email: this.email,
          telegram_chat_id: this.telegram_chat_id,
        })
        alert('Регистрация успешна! Войдите в систему.')
        this.$router.push('/login')
      } catch (error) {
        alert('Ошибка регистрации')
      }
    },
  },
}
</script>
