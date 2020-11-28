<template>
  <v-container>
    <v-form class="px-6 pt-4" ref="form" v-model="valid" lazy-validation autocomplete="off">
      <v-text-field class="form-field" v-model="username"
                    :rules="nameRules" label="Username" required
      ></v-text-field>
      <v-text-field class="form-field" v-model="password"
                    :rules="passwordRules" label="Password" type="password" required
      ></v-text-field>
      <a class="text-decoration-none font-weight-medium blue--text text--darken-3 text-body-2"
         href="https://youtu.be/dQw4w9WgXcQ">Forgot password?</a>
      <v-container class="pt-10">
        <v-btn :disabled="!valid" color="success" @click="validate" width="100%">
          Sign In
        </v-btn>
      </v-container>
    </v-form>
  </v-container>
</template>

<script>
export default {
  name: 'SignInForm',
  data() {
    return {
      valid: true,
      username: '',
      nameRules: [
        (v) => !!v || 'Name is required',
      ],
      password: '',
      passwordRules: [
        (v) => !!v || 'Password is required',
      ],
    };
  },
  methods: {
    validate() {
      if (!this.$refs.form.validate()) { return; }

      this.$store.dispatch('login', { username: this.username, password: this.password })
        .then(() => this.$router.push('/'))
        // eslint-disable-next-line no-console
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped>

</style>
