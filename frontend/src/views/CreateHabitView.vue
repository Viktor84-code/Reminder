<template>
  <div>
    <h2>Мои привычки</h2>
    <button @click="logout">Выйти</button>

    <!-- Публичные привычки -->
    <router-link to="/habits/public" class="public-btn">
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
    <router-link to="/habits/create" class="create-btn">
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

<style scoped>
.public-btn {
  display: inline-block;
  background-color: #d1fae5;
  color: #065f46;
  font-weight: 600;
  padding: 8px 16px;
  border-radius: 9999px;
  border: 2px solid #34d399;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  font-size: 14px;
  margin-bottom: 16px;
  transition: 0.2s;
}

.public-btn:hover {
  background-color: #a7f3d0;
}

.create-btn {
  display: inline-block;
  background-color: #059669;
  color: white;
  font-weight: 500;
  padding: 12px 24px;
  border-radius: 12px;
  border: 4px solid #065f46;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
  transition: 0.2s;
}

.create-btn:hover {
  background-color: #047857;
}
</style>