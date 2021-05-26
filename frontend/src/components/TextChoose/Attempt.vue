<template>
  <div style="display: flex; align-items: center; width: 60vw; min-width: 470px; padding: 0 2vw">
    <div class="attempt-text" :style="`flex-grow: ${1 + showStars}`">
      {{ date }}
    </div>
    <div class="attempt-text" style="flex-grow: 2" v-if="showStars">
      <Stars :score="score" :size="starSize"></Stars>
    </div>
    <div class="attempt-text">
      {{ score }}
    </div>
    <div class="attempt-text">
      {{ speed }} cpm
    </div>
    <div class="attempt-text">
      {{ accuracy }}%
    </div>
    <div class="attempt-text">
      {{ duration }}
    </div>
  </div>
</template>

<script>

import '@/components/tooltip.css';
import Stars from '@/components/TextChoose/Stars.vue';

function time0(date) {
  const res = new Date(date);
  res.setHours(0);
  res.setMinutes(0);
  res.setSeconds(0);
  res.setMilliseconds(0);
  return res;
}

function whenDate(datetime) {
  const date = time0(datetime);
  const today = time0(new Date(Date.now()));
  const yesterday = time0(new Date(Date.now()));
  yesterday.setDate(yesterday.getDate() - 1);
  if (date.getTime() === today.getTime()) return 'today';
  if (date.getTime() === yesterday.getTime()) return 'yesterday';
  if (date.getFullYear() === today.getFullYear()) return 'this year';
  return 'long ago';
}

function formatDate(date) {
  const when = whenDate(date);
  const HH = ('0' + date.getHours()).slice(-2); // eslint-disable-line prefer-template
  const MM = ('0' + date.getMinutes()).slice(-2); // eslint-disable-line prefer-template
  const HHMM = HH + ':' + MM; // eslint-disable-line prefer-template
  const MONTH = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December',
  ][date.getMonth()];
  const DATE = MONTH + ' ' + date.getDate(); // eslint-disable-line prefer-template
  const YEAR = date.getFullYear();
  switch (when) {
    case 'today':
      return HHMM;
    case 'yesterday':
      return `Yesterday, ${HHMM}`;
    case 'this year':
      return `${DATE}, ${HHMM}`;
    default:
      return `${DATE}, ${YEAR}, ${HHMM}`;
  }
}

function formatDuration(time) {
  const s = time % 60;
  const m = Math.floor(time / 60) % 60;
  const h = Math.floor(time / 3600) % 60;
  const SS = ('0' + s % 60).slice(-2); // eslint-disable-line prefer-template, no-mixed-operators
  const MM = ('0' + m % 60).slice(-2); // eslint-disable-line prefer-template, no-mixed-operators
  const HH = ('0' + h % 60).slice(-2); // eslint-disable-line prefer-template, no-mixed-operators
  let res = MM + ':' + SS; // eslint-disable-line prefer-template
  if (h > 0) res = HH + ':' + res; // eslint-disable-line prefer-template
  return res;
}

export default {
  name: 'Attempt',
  components: { Stars },
  props: ['attempt', 'showStars'],

  data: () => ({
    date: null,
    speed: null,
    accuracy: null,
    duration: null,
    score: null,
    starSize: null,
  }),

  created() {
    window.addEventListener('resize', this.resizeHandler);
  },
  destroyed() {
    window.removeEventListener('resize', this.resizeHandler);
  },

  mounted() {
    const date = new Date(this.attempt.date);
    this.date = formatDate(date);
    this.speed = this.attempt.speed;
    this.accuracy = Math.floor(this.attempt.accuracy);
    this.duration = formatDuration(this.attempt.duration);
    this.score = this.attempt.score;
    this.resizeHandler();
  },
  methods: {
    resizeHandler() {
      this.starSize = window.innerWidth < 1350 ? '1.4rem' : '1.7rem';
    },
  },
};
</script>

<style scoped>

.v-tooltip__content {
  font-size: 1rem;
}

.attempt-text {
  padding-top: 2px;
  color: #555;
  font-size: 1.2rem;
  flex: 1 1 0;
  display: flex;
  justify-content: center;
  text-align: center;
  margin: 0 5px
}

</style>
