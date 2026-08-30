<template>
  <div>
    <h2>Создать привычку</h2>
    <form @submit.prevent="createHabit">
      <input v-model="habit.action" placeholder="Действие" required />
      <input v-model="habit.time" type="time" required />
      <input v-model="habit.place" placeholder="Место" required />
      <button type="submit">Создать</button>
    </form>
    <router-link to="/habits">Назад</router-link>
  </div>
</template>

<script>
import api from '@/api'

export default {
  data() {
    return {
      habit: {
        action: '',
        time: '',
        place: '',
      },
    }
  },
  methods: {
    async createHabit() {
      try {
        await api.post('habits/', this.habit)
        this.$router.push('/habits')
      } catch (error) {
        alert('Ошибка при создании привычки')
      }
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