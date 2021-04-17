<template>
  <div>
    <page-loader :loading="loading"></page-loader>
    <v-container style="display: flex; flex-direction: column; align-items: center">
      <Topic v-for="i in colors.length" v-bind:key="i"
             :texts="texts" :color="colors[i - 1]"></Topic>
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
    texts: null,
    colors: ['red', 'green', 'orange', 'cyan', 'magenta', 'yellow'],
  }),

  mounted() {
    APIHelper.get('/snippets')
      .then((res) => {
        this.parse_data(res.data);
        this.loading = false;
      });
  },
  methods: {
    parse_data(data) {
      this.texts = data;
    },
  },
};
</script>

<style scoped>

</style>
