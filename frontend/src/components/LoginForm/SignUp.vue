<template>
  <v-container>
    <!--
    <v-form class="px-6" ref="form" v-model="valid" lazy-validation autocomplete="off">
      <v-text-field class="form-field" v-model="username"
                    :rules="nameRules" label="Username" required
      ></v-text-field>
      <v-text-field class="form-field" v-model="email"
                    :rules="emailRules" label="Email" required
      ></v-text-field>
      <v-text-field class="form-field" v-model="password"
                    :rules="passwordRules" label="Password" type="password" required
      ></v-text-field>
      <v-text-field class="form-field" v-model="passwordConfirm"
                    :rules="passwordConfirmRules" label="Confirm password" type="password" required
      ></v-text-field>
      <v-container class="pa-0 pt-4">
        <v-btn :disabled="!valid" color="success" @click="validate" width="100%">
          Sign Up
        </v-btn>
      </v-container>
    </v-form>-->

    <v-stepper v-model="e1" class="elevation-0 mt-n2" non-linear>
      <v-stepper-header style="height: 48px" class="elevation-0">
        <v-stepper-step step="1" editable style="height: 24px"></v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step step="2" editable style="height: 24px;"></v-stepper-step>
      </v-stepper-header>
      <v-stepper-items>
        <v-stepper-content step="1">
          <v-card class="mb-12" color="grey lighten-2" height="200px">
          </v-card>
          <v-btn color="primary" @click="e1 = 2" width="100%">
            Continue
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="2">
          <v-card class="mb-12" color="grey lighten-1" height="200px">
          </v-card>
          <v-container class="pa-0 ma-0" width="100%">
            <v-btn :disabled="!valid" color="success" @click="validate" width="100%">
              Sign Up
            </v-btn>
          </v-container>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </v-container>
</template>

<script>
export default {
  name: 'SignUpForm',
  data() {
    return {
      e1: 1,
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
        (v) => (v && v.length <= 64) || 'Password must be less than 64 characters',
        (v) => (v && v.length >= 8) || 'Password must be more than 8 characters',
      ],
      passwordConfirm: '',
      passwordConfirmRules: [
        (v) => !!v || 'Password confirmation is required',
        (v) => (v === this.password) || 'Passwords didn\'t match',
      ],
      email: '',
      emailRules: [
        (v) => !!v || 'Email is required',
        (v) => /^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/.test(v) || 'Email must be valid',
        (v) => (v && v.length <= 320) || 'Email must be less than 320 characters',
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

</style>
