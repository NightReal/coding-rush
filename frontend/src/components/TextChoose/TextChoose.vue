<template>
  <div>
    <page-loader :loading="loading"></page-loader>
    <v-container style="display: flex; flex-direction: column; align-items: center">
      <div class="mb-10" style="display: flex; flex-direction: column; align-items: center">
        <div style="font-size: 2.5rem; font-weight: 600" class="mb-3">Lessons</div>
        <div style="color: #444444; font-size: 1.2rem; max-width: 500px; text-align: center;">
          Choose topic, lesson and programming language to learn algorithm and practice it.
        </div>
      </div>
      <Topic v-for="(texts, topic, i) in texts" v-bind:key="topic"
             :texts="texts" :color="colors[i % colors.length]"
             :topic="topic"></Topic>
    </v-container>
  </div>
</template>

<script>

import APIHelper from '@/api/apihelper';
import PageLoader from '@/components/PageLoader.vue';
import Topic from '@/components/TextChoose/Topic.vue';

export default {
  name: 'TextChoose',

  components: { Topic, PageLoader },

  data: () => ({
    loading: true,
    texts: [],
    colors: [
      'chartreuse',
      'yellow',
      'orange',
      'red',
      'crimson',
      'magenta',
      'blue',
      'cyan',
      'green'],
  }),

  mounted() {
    APIHelper.get('/lessons')
      .then((res) => {
        this.parse_data(res.data);
        this.loading = false;
      });
  },
  methods: {
    parse_data(data) {
      const dt = {};
      for (let i = 0; i < data.length; i += 1) {
        const el = data[i];
        if (el.topic in dt) {
          dt[el.topic].push(el);
        } else {
          dt[el.topic] = [el];
        }
      }
      this.texts = dt;
    },
  },
};
</script>

<style scoped>

</style>
