<template>
  <v-container>
    <v-form class="px-6 pt-4" ref="form" v-model="valid" lazy-validation autocomplete="off">
      <v-text-field class="form-field" v-model="username" ref="name"
                    :rules="nameRules" label="Username" required
      ></v-text-field>
      <v-text-field class="form-field" v-model="password" ref="password"
                    :rules="passwordRules" label="Password" type="password" required
      ></v-text-field>
      <a class="text-decoration-none font-weight-medium blue--text text--darken-3 text-body-2"
         href="https://youtu.be/dQw4w9WgXcQ">Forgot password?</a>
      <v-container class="pt-8">
        <v-btn color="success" @click="validate" width="100%"
               :loading="loading" :disabled="loading">
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
      loading: false,
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
      if (!this.$refs.form.validate()) {
        this.focusFirst(['name', 'password']);
        return;
      }
      this.loading = true;
      this.$store.dispatch('login', { username: this.username, password: this.password })
        .then(() => this.$router.push('/'))
        .catch((err) => console.log(err))
        .then(() => { this.loading = false; });
    },
    focusFirst(fields) {
      // eslint-disable-next-line guard-for-in,no-restricted-syntax
      for (const i in fields) {
        const element = this.$refs[fields[i]];
        if (!element.valid) {
          element.focus();
          break;
        }
      }
    },
  },
};
</script>

<style scoped>

</style>
