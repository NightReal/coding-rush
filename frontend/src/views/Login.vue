<template>
  <div>
    <LoginForm/>
    <form class="login" @submit.prevent="login">
      <h1>Sign in</h1>
      <label>Username</label>
      <input required v-model="username" type="text" placeholder="Username"/>
      <label>Password</label>
      <input required v-model="password" type="password" placeholder="Password"/>
      <hr/>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue';

export default {
  name: 'Login.vue',
  components: { LoginForm },
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    login() {
      const { username } = this;
      const { password } = this;
      this.$store.dispatch('login', { username, password })
        .then(() => this.$router.push('/'))
        // eslint-disable-next-line no-console
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped>

</style>
