<template>
  <div style="display: flex; flex-direction: column; align-items: center">
    <h2 class="pa-4" style="color: #444; letter-spacing: 0.02rem">Attempts</h2>
    <v-card style="display: flex; flex-direction: column; align-items: center;"
            elevation="3" rounded="lg" class="pt-4 pb-2">
      <div style="display: flex; align-items: center; width: 60vw; min-width: 470px;
                  padding: 0 2vw 8px 2vw">
        <div class="attempt-title" :style="`flex-grow: ${1 + showStars}`">Date</div>
        <div class="attempt-title" style="flex-grow: 2" v-if="showStars">Stars</div>
        <div class="attempt-title">Score</div>
        <div class="attempt-title">Speed</div>
        <div class="attempt-title">Accuracy</div>
        <div class="attempt-title">Duration</div>
      </div>
      <div v-for="i in sorted_attempts.length" :key="i" class="py-4 ma-0 list-item">
        <Attempt :attempt="sorted_attempts[i - 1]" :show-stars="showStars"></Attempt>
      </div>
    </v-card>
  </div>
</template>

<script>
import Attempt from '@/components/TextChoose/Attempt.vue';

export default {
  name: 'AttemptsList',
  props: ['attempts'],
  // eslint-disable-next-line vue/no-unused-components
  components: { Attempt },

  data: () => ({
    selectedItem: null,
    sorted_attempts: [],
    showStars: true,
  }),
  created() {
    window.addEventListener('resize', this.resizeHandler);
  },
  destroyed() {
    window.removeEventListener('resize', this.resizeHandler);
  },
  mounted() {
    this.updateSortedAttempts();
    this.resizeHandler();
  },
  watch: {
    attempts() {
      this.updateSortedAttempts();
    },
  },
  methods: {
    updateSortedAttempts() {
      this.sorted_attempts = JSON.parse(JSON.stringify(this.attempts)); // deep copy
      this.sorted_attempts.sort(
        (a, b) => {
          const timeA = new Date(a.date).getTime();
          const timeB = new Date(b.date).getTime();
          return timeB - timeA;
        },
      );
    },
    resizeHandler() {
      this.showStars = window.innerWidth >= 1200;
    },
  },
};
</script>

<style scoped>

.list-item {
  border-radius: 0 !important;
}

.list-item:hover {
  background-color: #f0f0f0;
}

.attempt-title {
  padding-top: 2px;
  color: #555;
  font-size: 1.2rem;
  font-weight: 600;
  flex: 1 1 0;
  display: flex;
  justify-content: center;
  text-align: center;
  margin: 0 5px
}

</style>
