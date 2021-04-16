<template>
  <v-progress-linear color="accent" :active="loading" :indeterminate="loading"
                     style="position: fixed; z-index: 5; top:0; left: 0; right: 0;">
  </v-progress-linear>
</template>

<script>
export default {
  name: 'PageLoader',
  props: ['loading'],
};
</script>
