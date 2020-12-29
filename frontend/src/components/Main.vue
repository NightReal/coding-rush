<template>
  <v-container class="pa-0 ma-0">
    <v-sheet id="big-header" class="pa-0 ma-0" elevation="4" color="primary" dark>
      <img id="header-title" alt="Coding Rush" src="@/assets/text-light-930x160.png"/>
      <v-container id="header-content" class="pa-0 ma-0">
        <v-container id="header-texts" class="pa-0 ma-0 mb-16 ml-16">
          <v-container id="header-text-big" class="pa-0 ma-0">
            {{ 'Competitive' }} <br>
            {{ '\xa0\xa0\xa0coding' }} <br>
            {{ '\xa0\xa0\xa0\xa0\xa0\xa0practice' }}
          </v-container>
          <v-container id="header-text-caption" class="pa-0 ma-0 pt-5">
            Improve your coding skills
          </v-container>
        </v-container>
        <div style="max-width: 10vw; min-width: 10vw; height: 0"></div>
        <v-container class="pa-0 ma-0 mt-8 mr-10" style="width: auto">
          <LoginForm class="pa-0 ma-0"/>
        </v-container>
      </v-container>
      <v-img id="header-logo" transition="scroll-x-transition"
             src="@/assets/logo-light-430x430.png"></v-img>
    </v-sheet>
    <v-container style="min-width: 100vw; margin-top: 160px; padding-left: 30px;
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
        <p class="card-title">Who is it for?</p>
        <p class="card-content"> ???? For competitive programmers who wants to increase their coding
                                 skills. ???? </p>
        <p class="card-content"></p>
      </v-card>
      <PrettyDivider/>
      <v-card class="card" flat>
        <p class="card-title">What is it for?</p>
        <v-container class="pa-0 card-content" style="text-align: left; display: flex;
            flex-direction: column; align-items: center;">
          <p class="card-subtitle">Increase your skills</p>
          <v-container class="pa-0 mb-7"
                       style="display: flex; justify-content: space-between; min-width: 980px;
                              margin-left: -200px; height: 165px; align-items: flex-end">
            <v-card class="list-card-3" elevation="3">
              <p class="list-item-title">Typing accuracy</p>
              <v-divider style="width: 50px"></v-divider>
              <p class="list-item-content">Make fewer typos and mistakes</p>
            </v-card>
            <v-card class="list-card-3" elevation="5" style="align-self: flex-start">
              <p class="list-item-title">Typing speed</p>
              <v-divider style="width: 50px"></v-divider>
              <p class="list-item-content">Type faster and faster<br>Letters, numbers, symbols</p>
            </v-card>
            <v-card class="list-card-3" elevation="3">
              <p class="list-item-title">Knowledge of algorithms</p>
              <v-divider style="width: 50px"></v-divider>
              <p class="list-item-content">Write basic code without hesitation</p>
            </v-card>
          </v-container>
          <p style="text-align: center">Learn basic <span>algorithms</span> and <span>data
                                        structures</span> that are often needed in contests while
                                        training <span>speed</span> and <span>accuracy</span>.</p>
        </v-container>
      </v-card>
      <PrettyDivider/>
      <v-card class="card" flat>
        <p class="card-title">What kind of code?</p>
        <p class="card-content">Ещё раз сказать что код для спортивного программирования.<br>
                                Привести примеры а-ля "от Z-функции до Линката".<br>
                                Сказать какие есть темы (Графы, Строки, Геома, что там ещё бывает)
                                                                                      <br>
                                Весь код для написания доступен на C++, но некоторые алгоритмы также
                                доступны на Python 3, и что там ещё я хз.
        </p>
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

@import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;600&family=Roboto:ital@1&display=swap');

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
  justify-content: center;
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

.card-subtitle {
  font-size: 1.85rem;
  font-family: Roboto Slab, serif;
  font-weight: 400;
  margin-top: 10px;
  text-align: center;
  color: #222222;
}

.card-content {
  font-size: 1.5rem;
  font-family: Roboto Slab, serif;
  font-weight: 400;
  margin-top: 10px;
  text-align: center;
  color: #444444;
}

span {
  background-color: #FFFFDA;
  color: #404040;
}

.list-card-3 {
  min-width: 320px;
  max-width: 320px;
  min-height: 150px;
  max-height: 150px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.list-item-title {
  font-size: 1.5rem;
  font-family: Roboto, sans-serif;
  font-style: italic;
  font-weight: 400;
  margin-top: 6px;
  text-align: center;
}

.list-item-content {
  font-size: 1.15rem;
  font-family: Roboto Slab, serif;
  font-weight: 400;
  margin-top: 12px;
  margin-left: 22px;
  margin-right: 22px;
  text-align: center;
  color: #555555;
}

</style>
