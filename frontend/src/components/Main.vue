<template>
  <v-container class="pa-0 ma-0">
    <v-sheet class="pa-0 ma-0" id="big-header" elevation="4" color="primary" dark>
      <v-img id="header-title" transition="" alt="Coding Rush"
             src="@/assets/text-930x160.png"></v-img>
      <v-container id="header-content" class="pa-0 ma-0">
        <v-container class="pa-0 ma-0 mb-16 ml-16" style="display: flex; flex-direction: column;
         width:auto; font-family: monospace;">
          <v-container class="pa-0 ma-0" style="font-size: 3rem; text-align: left;">
            {{ 'Competitive' }} <br>
            {{ '\xa0\xa0\xa0coding' }} <br>
            {{ '\xa0\xa0\xa0\xa0\xa0\xa0practice' }}
          </v-container>
          <v-container class="pa-0 ma-0 pt-5" style="font-size: 1.3rem; width:auto;
        text-align: center; font-style: italic"
          >
            Improve your coding skills
          </v-container>
        </v-container>
        <v-container class="pa-0 ma-0 mt-10 mr-10 ml-n10" style="width: auto">
          <LoginForm style="margin-left: 100px"/>
        </v-container>
      </v-container>
      <v-img id="header-logo" transition="scroll-x-transition"
             src="@/assets/logo-430x430.png"></v-img>
    </v-sheet>
    <v-container style="height: 1100px; margin-top: 180px; padding-left: 30px">
      <br>dummy
    </v-container>
  </v-container>
</template>

<script>

import LoginForm from '@/components/LoginForm/LoginForm.vue';

export default {
  name: 'Main',
  components: {
    LoginForm,
  },
  data() {
    return {
      isActive: false,
      show: true,
    };
  },
  methods: {
    kek() {
      console.log('kek');
    },
  },
};
</script>
<style scoped>

#big-header {
  height: 750px;
  min-width: 100vw;
  display: flex;
  flex-direction: column;
  /*justify-content: center;*/
}

#header-content {
  align-self: center;
  flex-grow: 100;
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: space-evenly;
}

#header-logo {
  max-width: 430px;
  min-width: 430px;
  margin-left: 150px;
  margin-top: 492px;
  position: absolute;
}
#header-title{
  max-width: 730px;
  min-width: 730px;
  align-self: center;
  margin-right: 100px;
  position: absolute;
}

</style>
