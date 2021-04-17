<template>
  <v-container class="pa-0 mt-8">
    <TextChoose/>
  </v-container>
</template>

<script>
import TextChoose from '@/components/TextChoose/TextChoose.vue';

export default {
  name: 'TextChooseView',
  components: {
    TextChoose,
  },
};
</script>
