<template>
  <div>
    <h2>Редактировать привычку</h2>
    <form @submit.prevent="updateHabit">
      <input v-model="habit.place" placeholder="Место" required />
      <input v-model="habit.time" type="time" required />
      <input v-model="habit.action" placeholder="Действие" required />
      <label>
        <input v-model="habit.is_pleasant" type="checkbox" />
        Приятная привычка
      </label>
      <input v-model="habit.periodicity" type="number" placeholder="Периодичность (дней)" min="1" max="7" />
      <input v-model="habit.duration" type="number" placeholder="Длительность (сек)" required />
      <button type="submit">Сохранить</button>
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
        place: '',
        time: '',
        action: '',
        is_pleasant: false,
        periodicity: 1,
        duration: 60,
        is_public: false,
      },
    }
  },
  async mounted() {
    const id = this.$route.params.id
    const response = await api.get(`habits/${id}/`)
    this.habit = response.data
  },
  methods: {
    async updateHabit() {
      const id = this.$route.params.id
      await api.put(`habits/${id}/`, this.habit)
      this.$router.push('/habits')
    },
  },
}
</script>
