<template>
  <v-container class="pt-2 pb-0 px-2">
    <v-stepper v-model="formStep" class="elevation-0" non-linear>
      <v-stepper-items>
        <v-stepper-content step="1" class="pa-0">
          <v-form class="px-6 pt-6" ref="formRealName" v-model="validRealName" lazy-validation
                  autocomplete="off">
            <v-text-field class="form-field" v-model="firstName" ref="firstName"
                          :rules="firstNameRules" label="First name" required
            ></v-text-field>
            <v-text-field class="form-field" v-model="lastName" ref="lastName"
                          :rules="lastNameRules" label="Last name" required
            ></v-text-field>
            <v-container class="pt-12 pb-5">
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
                          :rules="nameRules" :error-messages="nameErrorMessage"
                          label="Username" required
            ></v-text-field>
            <v-text-field class="form-field" v-model="email" ref="email"
                          :rules="emailRules" :error-messages="emailErrorMessage"
                          label="Email" required
            ></v-text-field>
            <v-container class="pt-12 pb-0">
              <v-btn color="primary" width="100%"
                     @click="validateName" :loading="continueLoading" :disabled="continueLoading">
                Continue
              </v-btn>
              <v-btn text class="text--disabled caption" width="100%" height="20px"
                     @click="resetValidationName(); formStep = 1;">
                Back
              </v-btn>
            </v-container>
          </v-form>
        </v-stepper-content>

        <v-stepper-content step="3" class="pa-0">
          <ErrorBox class="pa-0 ma-0 mb-1" :message="errorMessage" :show="!!errorMessage"
                    style="min-height: 24px; max-height: 24px"></ErrorBox>
          <v-form class="pa-0 px-6" ref="formPassword" v-model="validPassword" lazy-validation
                  autocomplete="off"
                  style="display: flex; flex-direction: column;
                  justify-content: space-between">
            <v-text-field class="form-field" v-model="password" ref="password"
                          :rules="passwordRules" label="Password" type="password" required
                          autocomplete="new-password"
            ></v-text-field>
            <v-text-field class="form-field" v-model="passwordConfirm" ref="passwordConfirm"
                          :rules="passwordConfirmRules" label="Confirm password" type="password"
                          required
            ></v-text-field>
            <div hidden>
              <v-text-field name="username" :value="username" autocomplete="username">
              </v-text-field>
            </div>

            <p class="ma-0 pt-3 pb-0 text--disabled caption">
              By clicking «Sign Up», you accept
              <a class="text-decoration-none blue--text text--darken-3"
                 href="https://youtu.be/M5V_IXMewl4">Terms of Use</a>.</p>

            <v-container width="100%" class="pb-0">
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
import APIHelper from '@/api/apihelper';
import ErrorBox from '@/components/ErrorBox.vue';

export default {
  name: 'SignUpForm',
  components: { ErrorBox },
  data() {
    return {
      formStep: 1,
      loading: false,
      continueLoading: false,
      errorMessage: '',

      validRealName: true,
      firstName: '',
      lastName: '',
      firstNameRules: [
        (v) => !!v || 'First name required',
        (v) => /^[a-zA-Z0-9 _.-]*$/.test(v)
          || 'Only Latin letters, digits and symbols . - _ are allowed',
        (v) => v.replace(/[^a-zA-Z]/g, '').length >= 3
          || 'First name must contain at least 3 letters',
        (v) => (v && v.length <= 40) || 'First name must be less than 40 characters',
      ],
      lastNameRules: [
        (v) => !!v || 'Last name required',
        (v) => /^[a-zA-Z0-9 _.-]*$/.test(v)
          || 'Only Latin letters, digits and symbols . - _ are allowed',
        (v) => v.replace(/[^a-zA-Z]/g, '').length >= 3
          || 'Last name must contain at least 3 letters',
        (v) => (v && v.length <= 40) || 'Last name must be less than 40 characters',
      ],

      validName: true,
      username: '',
      nameErrorMessage: [],
      nameRules: [
        () => {
          this.nameErrorMessage = [];
          return true;
        },
        (v) => !!v || 'Name is required',
        (v) => /^[a-zA-Z0-9_.-]*$/.test(v)
          || 'Only Latin letters, digits and symbols . - _ are allowed',
        (v) => (v && v.length <= 20) || 'Username must be less than 20 characters',
        (v) => (v && v.length >= 4) || 'Username must be more than 4 characters',
      ],
      email: '',
      emailErrorMessage: [],
      emailRules: [
        () => {
          this.emailErrorMessage = [];
          return true;
        },
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
    validateRealName(move = true) {
      this.validRealName = this.$refs.formRealName.validate();
      if (!this.validRealName) {
        this.focusFirst(['firstName', 'lastName']);
      }
      if (move) {
        this.formStep = this.validRealName ? 2 : 1;
      }
      return this.validRealName;
    },
    checkNameUnique(name) {
      return APIHelper.get(`/account/usernameExists/${name}`)
        .then((res) => !res.data.username)
        .catch(() => false);
    },
    checkEmailUnique(email) {
      return APIHelper.get(`/account/emailExists/${email}`)
        .then((res) => !res.data.email)
        .catch(() => false);
    },
    async validateUnique() {
      if (this.$refs.name.valid) {
        if (!await this.checkNameUnique(this.username)) {
          this.$refs.name.valid = false;
          this.validName = false;
          this.$data.nameErrorMessage = ['This username is already taken'];
        }
      }
      if (this.$refs.email.valid) {
        if (!await this.checkEmailUnique(this.email)) {
          this.$refs.email.valid = false;
          this.validName = false;
          this.$data.emailErrorMessage = ['This email is already taken'];
        }
      }
      return this.validName;
    },
    async validateName(move = true) {
      if (move) {
        this.continueLoading = true;
      }
      this.validName = this.$refs.formName.validate();
      if (move) {
        await this.validateUnique();
      }
      if (!this.validName) {
        this.focusFirst(['name', 'email']);
      }
      if (move) {
        this.continueLoading = false;
        this.formStep = this.validName ? 3 : 2;
      }
      return this.validName;
    },
    validatePassword() {
      this.validPassword = this.$refs.formPassword.validate();
      if (!this.validPassword) {
        this.focusFirst(['password', 'passwordConfirm']);
      }
      return this.validPassword;
    },
    showSthWrong(err) {
      const { data } = err.response;
      if (data.password) {
        [this.errorMessage] = data.password;
      } else if (data.username) {
        [this.errorMessage] = data.username;
      } else if (data.email) {
        [this.errorMessage] = data.email;
      } else {
        this.errorMessage = 'Something went wrong.';
        console.log(err);
        console.log(err.response);
      }
    },
    async validateForm() {
      this.errorMessage = '';
      this.loading = true;

      if (!this.validateRealName(false)
        || !await this.validateName(false)
        || !this.validatePassword()) {
        this.loading = false;
        return;
      }

      this.$store.dispatch('register',
        {
          username: this.username,
          password: this.password,
          password_confirm: this.passwordConfirm,
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
            .then(() => {
              if (this.$route.path !== '/') this.$router.push('/');
              else this.$router.go(0);
            })
            .catch((err) => this.showSthWrong(err));
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          this.showSthWrong(err);
        });
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
