<template>
  <v-card class="big-card" rounded="lg" style="margin-left: 20px">
    <v-container>
      <v-tabs v-model="tab" fixed-tabs centered>
        <v-tab>Sign In</v-tab>
        <v-tab>Sign Up</v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab" fixed-height fill-height>
        <v-tab-item>
          <!--          <v-container class="px-6 py-10">-->
          <v-form class="px-6 py-8" ref="form" v-model="valid" lazy-validation autocomplete="off">
            <v-text-field class="form-field"
                          :rules="nameRules" label="Username" required
            ></v-text-field>
            <v-text-field class="form-field"
                          :rules="passwordRules" label="Password" type="password" required
            ></v-text-field>
            <a class="text-decoration-none font-weight-medium blue--text text--darken-3 text-body-2"
                  href="https://youtu.be/dQw4w9WgXcQ">Forgot password?</a>
            <v-container class="pa-0 pt-13">
              <v-btn :disabled="!valid" color="success" @click="validate" width="100%">
                Sign In
              </v-btn>
            </v-container>
          </v-form>
          <!--          </v-container>-->
        </v-tab-item>
        <v-tab-item>b</v-tab-item>
      </v-tabs-items>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      tab: null,
      valid: true,
      username: '',
      nameRules: [
        (v) => !!v || 'Name is required',
        (v) => /^[a-zA-Z0-9_.-]*$/.test(v) || 'Only Latin letters, digits, and symbols . - _ are allowed',
        (v) => (v && v.length <= 20) || 'Name must be less than 20 characters',
        (v) => (v && v.length >= 4) || 'Name must be more than 4 characters',
      ],
      password: '',
      passwordRules: [
        (v) => !!v || 'Password is required',
        // (v) => /^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/.test(v) || 'E-mail must be valid',
        (v) => (v && v.length <= 64) || 'Password must be less than 64 characters',
        (v) => (v && v.length >= 8) || 'Password must be more than 8 characters',
      ],
    };
  },
  methods: {
    validate() {
      this.$refs.form.validate();
    },
  },
};
</script>

<style scoped>

.big-card {
  min-width: 300px;
  min-height: 385px;
  width: 20vw;
  height: 40vh;
}

</style>
