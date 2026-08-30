<template>
  <div>
    <h2>Мои привычки</h2>
    <button @click="logout">Выйти</button>

    <div style="background-color: #d1fae5; color: #065f46; font-weight: 600; padding: 8px 16px; border-radius: 9999px; display: inline-block; font-size: 14px; margin-bottom: 16px; margin-top: 8px; cursor: pointer;" @click="$router.push('/habits/public')">
      📢 Публичные привычки
    </div>

    <ul>
      <li v-for="habit in habits" :key="habit.id">
        {{ habit.action }} в {{ habit.time }} ({{ habit.place }})
        <div>
          <router-link :to="`/habits/edit/${habit.id}`">
            <button>Редактировать</button>
          </router-link>
          <button @click="deleteHabit(habit.id)">Удалить</button>
        </div>
      </li>
    </ul>

    <button style="width: 100%; border: 2px solid #059669; color: #059669; background-color: transparent; font-weight: 500; padding: 12px 24px; border-radius: 12px; cursor: pointer; font-size: 16px; text-align: center; display: block; box-sizing: border-box;" @click="$router.push('/habits/create')">
      + Создать привычку
    </button>
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
        this.habits = response.data.results || []
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