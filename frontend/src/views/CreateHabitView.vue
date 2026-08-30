<template>
  <div>
    <h2>Мои привычки</h2>
    <button @click="logout">Выйти</button>

    <!-- Публичные привычки -->
    <router-link to="/habits/public" class="inline-block bg-green-100 text-green-800 font-semibold px-4 py-2 rounded-full border-2 border-green-500 shadow-md text-sm mb-4 hover:bg-green-200 transition">
      📢 Публичные привычки
    </router-link>

    <ul>
      <li v-for="habit in habits" :key="habit.id">
        {{ habit.action }} в {{ habit.time }} ({{ habit.place }})
        <div>
          <router-link :to="`/habits/edit/${habit.id}`">
            <button class="edit-btn">Редактировать</button>
          </router-link>
          <button @click="deleteHabit(habit.id)">Удалить</button>
        </div>
      </li>
    </ul>

    <!-- Создать привычку -->
    <router-link to="/habits/create" class="inline-block bg-emerald-600 text-white font-medium py-3 px-6 rounded-xl border-4 border-emerald-800 shadow-lg hover:bg-emerald-700 transition">
      + Создать привычку
    </router-link>
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
