<template>
  <v-container class="pa-0 ma-0">
    <v-sheet id="big-header" class="pa-0 ma-0" elevation="4" color="primary" dark>
      <img id="header-title" alt="Coding Rush" src="@/assets/text-light-930x160.png"/>
      <v-container id="header-content" class="pa-0 ma-0">
        <v-container id="header-texts" class="pa-0 ma-0 mb-16 ml-16 mr-n16">
          <v-container id="header-text-big" class="pa-0 ma-0">
            {{ 'Competitive' }} <br>
            {{ '\xa0\xa0\xa0coding' }} <br>
            {{ '\xa0\xa0\xa0\xa0\xa0\xa0practice' }}
          </v-container>
          <v-container id="header-text-caption" class="pa-0 ma-0 pt-5">
            Improve your coding skills
          </v-container>
        </v-container>
        <v-container class="pa-0 ma-0 mt-8 mr-10 ml-n10" style="width: auto">
          <LoginForm style="margin-left: 100px"/>
        </v-container>
      </v-container>
      <v-img id="header-logo" transition="scroll-x-transition"
             src="@/assets/logo-light-430x430.png"></v-img>
    </v-sheet>
    <v-container style="min-width: 100vw; margin-top: 180px; padding-left: 30px;
    display: flex; align-items: center; flex-direction: column; padding-bottom: 200px;">
      <v-card class="card" rounded="lg" width="600px" elevation="6">
        <v-container class="px-10 pt-4 pb-5">
          <p class="card-title">Coding Rush is a</p>
          <p class="card-content">platform for learning to <span>type faster</span> for
                                  competitive programmers.</p>
        </v-container>
      </v-card>
      <p class="card-content pt-4" style="font-size: 1.4rem; color: #555555">
        You won't be typing snippets from books, lyrics from songs or
        famous quotes here.<br>But you can typing
        <span>competitive programming code</span>!
      </p>
      <PrettyDivider/>
      <v-card class="card" flat>
        <p class="card-title">For whom?</p>
        <p class="card-content"> ???? For competitive programmers who wants to increase their coding
                                 skills. ???? </p>
        <p class="card-content"></p>
      </v-card>
      <PrettyDivider/>
      <v-card class="card" flat>
        <p class="card-title">For what?</p>
        <v-container class="pa-0 card-content" style="text-align: left; display: flex;
            flex-direction: column; align-items: center;">
          <v-container class="pa-0 pb-3" style="width: auto">
            Increase your skills:
            <ul style="margin-left: 50px">
              <li>typing speed</li>
              <li>typing accuracy</li>
              <li>???</li>
            </ul>
          </v-container>
          <p style="text-align: center">Learn basic <span>algorithms</span>
                                        and <span>data structures</span>, which are often
                                        needed at olympiads and contests.</p>
        </v-container>
      </v-card>
    </v-container>
  </v-container>
</template>

<script>

import LoginForm from '@/components/LoginForm/LoginForm.vue';
import PrettyDivider from '@/components/PrettyDivider.vue';

export default {
  name: 'Main',
  components: {
    LoginForm,
    PrettyDivider,
  },
  data() {
    return {
      isActive: false,
      show: true,
    };
  },
};
</script>
<style scoped>

@import url('https://fonts.googleapis.com/css?family=Roboto+Slab:400,600');

#big-header {
  height: 750px;
  min-width: 100vw;
  display: flex;
  flex-direction: column;
}

#header-title {
  max-width: 730px;
  min-width: 730px;
  align-self: center;
  margin-right: 100px;
  position: absolute;
}

#header-content {
  align-self: center;
  flex-grow: 100;
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: space-evenly;
}

#header-texts {
  display: flex;
  flex-direction: column;
  width: auto;
}

#header-text-big {
  font-size: 3rem;
  text-align: left;
  font-family: monospace;
  font-style: normal;
}

#header-text-caption {
  font-size: 1.3rem;
  text-align: center;
  font-family: monospace;
  font-style: italic;
}

#header-logo {
  max-width: 430px;
  min-width: 430px;
  margin-left: 7.8vw;
  margin-top: 492px;
  position: absolute;
}

.card {
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 600px;
}

.card-title {
  font-size: 2.5rem;
  font-family: Roboto Slab, serif;
  font-weight: 600;
  margin-top: 10px;
  text-align: center;
}

.card-content {
  font-size: 1.5rem;
  font-family: Roboto Slab, serif;
  font-weight: 200;
  margin-top: 10px;
  text-align: center;
  color: #444444;
}

span {
  background-color: #FFFFDA;
  color: #404040;
}

</style>
