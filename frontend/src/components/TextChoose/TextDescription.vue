<template>
  <div>
    <page-loader :loading="loading"></page-loader>
    <div>text id: {{ textid }}</div>
    <div>language: {{ lang }}</div>
  </div>
</template>

<script>

import PageLoader from '@/components/PageLoader.vue';

export default {
  name: 'TextChoose',

  props: ['textid', 'lang'],

  components: { PageLoader },

  data: () => ({
    loading: true,
  }),

  mounted() {
  },

  methods: {
  },
};
</script>

