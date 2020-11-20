<template>
  <v-container>
    just some text
    <br/>
    {{ username }}
  </v-container>
</template>

<script>
import store from '../store/index';

export default {
  name: 'Main',
  data() {
    return {
      username: store.state.user,
    };
  },
};
</script>

<style scoped>
</style>
