<template>
  <div>
    <h2>Мои привычки</h2>
    <button @click="logout">Выйти</button>
    <ul>
      <li v-for="habit in habits" :key="habit.id">
        {{ habit.action }} в {{ habit.time }} ({{ habit.place }})
        <button @click="deleteHabit(habit.id)">Удалить</button>
      </li>
    </ul>
    <router-link to="/habits/create">Создать привычку</router-link>
  </div>
</template>

<script>
import api from '@/api'

export default {
  data() {
    return {
      habits: [],
    }
  },
  async mounted() {
    await this.loadHabits()
  },
  methods: {
    async loadHabits() {
      try {
        const response = await api.get('habits/')
        this.habits = response.data.results
      } catch (error) {
        if (error.response?.status === 401) {
          this.$router.push('/login')
        }
      }
    },
    async deleteHabit(id) {
      if (confirm('Удалить привычку?')) {
        await api.delete(`habits/${id}/`)
        await this.loadHabits()
      }
    },
    logout() {
      localStorage.removeItem('access_token')
      this.$router.push('/login')
    },
  },
}
</script>
