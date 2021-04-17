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
    this.$store.dispatch('getUser')
      .catch(() => {
        this.$router.push('/login');
      });
  },
};
</script>

<style scoped>
</style>
