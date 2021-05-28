<template>
  <div>
    <v-dialog v-model="signOutDialog" max-width="300px">
      <v-card>
        <v-card-title class="headline">Signing out</v-card-title>
        <v-card-text class="pb-0">
          Do you really want to sign out from your account? All attempts and statistics
          will be saved.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="#ff8000" text @click="signOutDialog = false">
            No
          </v-btn>
          <v-btn color="#ff8000" text @click="signOutDialog = false; signout()">
            Yes
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <div class="mb-12">
      <v-app-bar app dense color="primary" dark class="ma-0 pa-0"
                 :elevate-on-scroll="isAboutPage()">
        <div style="display: flex; justify-content: flex-start;
                    padding: 0; margin: 0; width: 100%; height: 100%">
          <div style="display: flex; align-items: center; margin-right: 16px"
                       @click="$router.push('/about')">
            <img style="margin: 0 13px 0 15px"
                 src="@/assets/logo-light-35x35.png" alt=""/>
            <div style="font-size: 1.3rem; font-weight: 500; letter-spacing: 0.05rem;
                        white-space: nowrap;">
              Coding Rush
            </div>
          </div>
          <div v-if="isAuthed()" style="display: flex; align-items: center; width: 100%">
            <div style="width: 2.5vw"></div>
            <div style="display: flex; align-items: center; height: 100%;
                        justify-content: space-between; width: 100%">
              <div style="display: flex; align-items: center; height: 100%">
                <v-btn @click="goto('/lessons')" text class="header-btn">Lessons</v-btn>
                <v-btn @click="goto('/')" text class="header-btn">Profile</v-btn>
              </div>
              <div style="display: flex; align-items: center; height: 100%">
                <v-btn @click="goto('/about')" text class="header-btn">About</v-btn>
                <v-btn @click="goto('/settings')" text class="header-btn">Settings</v-btn>
                <v-btn @click="signOutDialog = true" text class="header-btn">Sign out</v-btn>
              </div>
            </div>
            <div style="width: 5vw"></div>
          </div>
          <div v-else style="display: flex; align-items: center; width: 100%">
            <div style="width: 2.5vw"></div>
            <div style="display: flex; align-items: center; height: 100%;
                        justify-content: space-between; width: 100%">
              <div style="display: flex; align-items: center; height: 100%">
                <v-btn @click="goto('/about')" text class="header-btn">About</v-btn>
              </div>
              <div style="display: flex; align-items: center; height: 100%">
                <v-btn @click="goto('/signin')" text class="header-btn">Sign in</v-btn>
                <v-btn @click="goto('/signup')" text class="header-btn">Sign up</v-btn>
              </div>
            </div>
            <div style="width: 5vw"></div>
          </div>
        </div>
      </v-app-bar>
    </div>
  </div>
</template>

<script>

import store from '@/store/index';

export default {
  name: 'HeaderUnauth',
  components: {},
  data() {
    return {
      signOutDialog: false,
    };
  },
  methods: {
    goto(item) {
      this.$router.push(item).catch((e) => e);
    },
    isAboutPage() {
      return this.$route.name === 'About';
    },
    isAuthed() {
      return store.getters.isAuthenticated;
    },
    signout() {
      this.$store.dispatch('logout')
        .then(() => this.goto('/'))
        // eslint-disable-next-line no-console
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style>

.v-toolbar__content {
  padding: 0 !important;
}

.header-btn {
  height: 100% !important;
  display: flex !important;
  align-items: center !important;
  background-color: #2b2b2b !important;
  border-radius: 0 !important;
  padding: 0 16px !important;
  font-size: 1.05rem !important;
  font-family: monospace !important;
  text-transform: none !important;
  letter-spacing: inherit !important;
}

.header-btn:hover {
  background-color: #555 !important;
  /*background-color: rgba(255, 153, 46, 0.6) !important;*/
}

.header-btn:before {
  background-color: inherit !important;
}

</style>
