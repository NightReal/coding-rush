<template>
  <v-container class="pt-2 px-2">
    <ErrorBox class="pa-0 ma-0 mb-1" :message="errorMessage" :show="!!errorMessage"
              style="min-height: 24px; max-height: 24px"></ErrorBox>
    <v-form class="pa-0 px-6" ref="form" v-model="valid" lazy-validation autocomplete="off">
      <v-text-field class="form-field" v-model="username" ref="name"
                    :rules="nameRules" label="Username" required
                    autocomplete="username"
      ></v-text-field>
      <v-text-field class="form-field" v-model="password" ref="password"
                    :rules="passwordRules" label="Password" type="password" required
                    autocomplete="current-password"
      ></v-text-field>
      <a class="text-decoration-none font-weight-medium blue--text text--darken-3 text-body-2"
         href="https://youtu.be/dQw4w9WgXcQ">Forgot password?</a>
      <v-container class="pt-6">
        <v-btn color="success" @click="validate" width="100%"
               :loading="loading" :disabled="loading">
          Sign In
        </v-btn>
      </v-container>
    </v-form>
  </v-container>
</template>

<script>
import ErrorBox from '@/components/ErrorBox.vue';

export default {
  name: 'SignInForm',
  components: { ErrorBox },
  data() {
    return {
      loading: false,
      valid: true,
      errorMessage: '',

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
    showSmthWrong(err) {
      if (err.response && err.response.status === 401) {
        this.errorMessage = 'Incorrect username or password.';
      } else {
        this.errorMessage = 'Something went wrong.';
        console.log(err);
        console.log(err.response);
      }
    },
    validate() {
      this.errorMessage = '';
      if (!this.$refs.form.validate()) {
        this.focusFirst(['name', 'password']);
        return;
      }
      this.loading = true;
      this.$store.dispatch('login', { username: this.username, password: this.password })
        .then(() => (this.$route.path !== '/' ? this.$router.push('/') : {}))
        .catch((err) => this.showSmthWrong(err))
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
