<template>
  <v-card class="big-card" rounded="lg" style="margin-left: 20px" light>
    <v-container>
      <v-tabs v-model="tab" fixed-tabs centered @change="$emit('tab-changed', tab)">
        <v-tab>Sign In</v-tab>
        <v-tab>Sign Up</v-tab>
      </v-tabs>

      <!-- <v-tabs-items v-model="tab" fixed-height fill-height> -->
      <v-tabs-items v-model="tab" fill-height>
        <v-tab-item>
          <SignInForm ref="signin"/>
        </v-tab-item>
        <v-tab-item>
          <SignUpForm ref="signup"/>
        </v-tab-item>
      </v-tabs-items>
    </v-container>
  </v-card>
</template>

<script>
import SignUpForm from './SignUp.vue';
import SignInForm from './SignIn.vue';

export default {
  name: 'LoginForm',
  components: { SignInForm, SignUpForm },
  methods: {
    continueAuth() {
      if (this.tab === 0) {
        this.$refs.signin.validate();
        return;
      }
      const step = this.$refs.signup.$data.formStep;
      if (step === 1) {
        this.$refs.signup.validateRealName();
      } else if (step === 2) {
        this.$refs.signup.validateName();
      } else {
        this.$refs.signup.validateForm();
      }
    },
    onkeyup(e) {
      if (e.key === 'Enter') {
        this.continueAuth();
      }
    },
  },
  created() {
    window.addEventListener('keyup', this.onkeyup);
  },
  beforeDestroy() {
    window.removeEventListener('keyup', this.onkeyup);
  },
  data() {
    return {
      tab: 0,
    };
  },
  props: ['parentTab'],
  watch: {
    parentTab(to) {
      this.tab = to;
    },
  },
};
</script>

<style scoped>

.big-card {
  height: 360px;
  width: 370px;
  max-width: 370px;
  min-width: 370px;
}

</style>
