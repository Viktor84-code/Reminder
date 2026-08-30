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
        const payload = {
          username: this.username.trim(),
          password: this.password.trim(),
          email: this.email.trim(),
          telegram_chat_id: this.telegram_chat_id.trim(),
        }
        const response = await api.post('/auth/register/', payload)
        alert('Регистрация успешна! Войдите в систему.')
        this.$router.push('/login')
      } catch (error) {
        if (error.response) {
          alert('Ошибка: ' + JSON.stringify(error.response.data))
        } else {
          alert('Ошибка соединения')
        }
      }
    },
  },
}
</script>
