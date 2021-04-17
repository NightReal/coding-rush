<template>
  <div>
    <page-loader :loading="loading"></page-loader>
    <v-container style="max-width: 1277px">
        <v-container v-for="text in texts" :key="text.id">
          <TextCard :text="text"></TextCard>
        </v-container>
    </v-container>
  </div>
</template>

<script>

import APIHelper from '@/api/apihelper';
import PageLoader from '@/components/PageLoader.vue';
import TextCard from '@/components/TextChoose/TextCard.vue';

export default {
  name: 'TextChoose',

  components: { PageLoader, TextCard },

  data: () => ({
    loading: true,
    texts: null,
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
