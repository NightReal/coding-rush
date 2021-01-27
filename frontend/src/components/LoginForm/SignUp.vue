<template>
  <v-container class="pb-0">
    <v-stepper v-model="formStep" class="elevation-0 mt-n2" non-linear>
      <v-stepper-items>
        <v-stepper-content step="1" class="pa-0">
          <v-form class="px-6 pt-6" ref="formRealName" v-model="validRealName" lazy-validation
                  autocomplete="off">
            <v-text-field class="form-field" v-model="firstName" ref="firstName"
                          :rules="firstNameRules" label="First Name" required
            ></v-text-field>
            <v-text-field class="form-field" v-model="lastName" ref="lastName"
                          :rules="lastNameRules" label="Last Name" required
            ></v-text-field>
            <v-container class="pt-16 pb-7">
              <v-btn color="primary" width="100%"
                     @click="validateRealName">
                Continue
              </v-btn>
            </v-container>
          </v-form>
        </v-stepper-content>

        <v-stepper-content step="2" class="pa-0">
          <v-form class="px-6 pt-6" ref="formName" v-model="validName" lazy-validation
                  autocomplete="off">
            <v-text-field class="form-field" v-model="username" ref="name"
                          :rules="nameRules" label="Username" required
            ></v-text-field>
            <v-text-field class="form-field" v-model="email" ref="email"
                          :rules="emailRules" label="Email" required
            ></v-text-field>
            <v-container class="pt-14">
              <v-btn color="primary" width="100%"
                     @click="validateName">
                Continue
              </v-btn>
              <v-btn text class="text--disabled caption" width="100%" height="20px"
                     @click="resetValidationName(); formStep = 1;">
                Back
              </v-btn>
            </v-container>
          </v-form>
        </v-stepper-content>

        <v-stepper-content step="2" class="pa-0">
          <v-form class="pa-0 px-6 pt-6" ref="formPassword" v-model="validPassword" lazy-validation
                  autocomplete="off"
                  style="display: flex; flex-direction: column;
                  justify-content: space-between">
            <v-text-field class="form-field" v-model="password" ref="password"
                          :rules="passwordRules" label="Password" type="password" required
            ></v-text-field>
            <v-text-field class="form-field" v-model="passwordConfirm" ref="passwordConfirm"
                          :rules="passwordConfirmRules" label="Confirm password" type="password"
                          required
            ></v-text-field>

            <p class="ma-0 pt-5 pb-1 text--disabled caption">
              By clicking «Sign Up», you accept
              <a class="text-decoration-none blue--text text--darken-3"
                 href="https://youtu.be/M5V_IXMewl4">Terms of Use</a>.</p>

            <v-container width="100%">
              <v-btn color="success" @click="validateForm" width="100%"
                     :loading="loading" :disabled="loading">
                Sign Up
              </v-btn>
              <v-btn text class="text--disabled caption" width="100%" height="20px"
                     @click="resetValidationPassword(); formStep = 2;">
                Back
              </v-btn>
            </v-container>
          </v-form>
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
      formStep: 1,
      loading: false,

      validRealName: true,
      firstName: '',
      lastName: '',
      firstNameRules: [
        (v) => !!v || 'First Name required',
      ],
      lastNameRules: [
        (v) => !!v || 'Last Name required',
      ],

      validName: true,
      username: '',
      nameRules: [
        (v) => !!v || 'Name is required',
        (v) => /^[a-zA-Z0-9_.-]*$/.test(v) || 'Only Latin letters, digits, and symbols . - _ are allowed',
        (v) => (v && v.length <= 20) || 'Name must be less than 20 characters',
        (v) => (v && v.length >= 4) || 'Name must be more than 4 characters',
      ],
      email: '',
      emailRules: [
        (v) => !!v || 'Email is required',
        (v) => /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(v)
          || 'Email must be valid',
        (v) => (v && v.length <= 320) || 'Email must be less than 320 characters',
      ],

      validPassword: true,
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

    };
  },
  methods: {
    validateRealName() {
      this.validRealName = this.$refs.formRealName.validate();
      if (!this.validRealName) {
        this.focusFirst(['firstName', 'lastName']);
      }
      this.formStep = this.validRealName ? 2 : 1;
      return this.validRealName;
    },
    validateName() {
      this.validName = this.$refs.formName.validate();
      if (!this.validName) {
        this.focusFirst(['name', 'email']);
      }
      this.formStep = this.validName ? 3 : 2;
      return this.validName;
    },
    validatePassword() {
      this.validPassword = this.$refs.formPassword.validate();
      if (!this.validPassword) {
        this.focusFirst(['password', 'passwordConfirm']);
      }
      return this.validPassword;
    },
    validateForm() {
      if (!this.validateRealName() || !this.validateName() || !this.validatePassword()) {
        return;
      }

      this.loading = true;
      // TODO: submit sign up form
      /* username - this.username
       * email - this.email
       * password - this.password */
      // this.$store.dispatch()
      //            .then(...)
      //            .catch(...)
      //            .then(() => { this.loading = false; });
      this.$store.dispatch('register',
        {
          username: this.username,
          password: this.password,
          password2: this.passwordConfirm,
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
        })
        .then(() => {
          this.$store.dispatch('login',
            {
              username: this.username,
              password: this.password,
            })
            .then(() => this.$router.push('/'))
            // eslint-disable-next-line no-console
            .catch((err) => console.log('Fail login after registration', err));
        })
        .catch((err) => {
          // eslint-disable-next-line no-console
          console.log('Fail', err);
        });
      // console.log('Submit registraciu tut, please');
      this.loading = false;
    },
    resetValidationName() {
      this.$refs.formName.resetValidation();
    },
    resetValidationPassword() {
      this.$refs.formPassword.resetValidation();
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
