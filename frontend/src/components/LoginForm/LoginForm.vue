<template>
  <v-card class="big-card" rounded="lg" style="margin-left: 20px">
    <v-container>
      <v-tabs v-model="tab" fixed-tabs centered @change="$emit('tab-changed', tab)">
        <v-tab>Sign In</v-tab>
        <v-tab>Sign Up</v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab" fixed-height fill-height>
        <v-tab-item>
          <SignInForm/>
        </v-tab-item>
        <v-tab-item>
          <SignUpForm/>
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
  min-width: 300px;
  height: 384px;
  width: 20vw;
}

</style>
