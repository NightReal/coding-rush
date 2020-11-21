<template>
  <v-container>
    just some text
    <br/>
    Your username:
    {{ $store.state.user.username }}
  </v-container>
</template>

<script>

export default {
  name: 'Main',
  beforeMount() {
    this.$store.dispatch('getUser');
  },
};
</script>

<style scoped>
</style>
