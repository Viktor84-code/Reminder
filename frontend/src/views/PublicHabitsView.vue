<template>
  <div>
    <h2>Публичные привычки</h2>
    <ul>
      <li v-for="habit in habits" :key="habit.id">
        {{ habit.action }} в {{ habit.time }} ({{ habit.place }})
        <span class="author">Автор: {{ habit.user }}</span>
      </li>
    </ul>
    <router-link to="/habits">Назад к моим привычкам</router-link>
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
    try {
      const response = await api.get('habits/public/')
      this.habits = response.data.results
    } catch (error) {
      console.error('Ошибка загрузки публичных привычек', error)
    }
  },
}
</script>

<style scoped>
span.author {
  font-size: 12px;
  color: #718096;
  margin-left: 10px;
}
</style>
