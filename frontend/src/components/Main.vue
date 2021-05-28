<template>
  <v-container class="pa-0 ma-0">
    <v-sheet id="big-header" class="pa-0 ma-0" elevation="4" color="primary" dark>
      <a href="" id="header-title"><img alt="Coding Rush"
                                        src="@/assets/text-light-930x160.png"/></a>
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
        <div style="max-width: 10vw; min-width: 10vw; height: 0" v-if="!isAuthed()"></div>
        <v-container class="pa-0 ma-0 mt-8 mr-10" style="width: auto" v-if="!isAuthed()">
          <LoginForm class="pa-0 ma-0"/>
        </v-container>
      </v-container>
      <v-img id="header-logo" transition="scroll-x-transition"
             src="@/assets/logo-light-430x430.png"
             @click="scrollToContentStart()">
      </v-img>

      <div id="proceed-button" v-if="isAuthed()">
        <v-btn color="#ff8200" style="color: white; font-size: 1.8rem" width="200px"
               height="60px" class="text-capitalize" @click="$router.push('/lessons')">
          Proceed
        </v-btn>
      </div>

    </v-sheet>
    <v-container id="content" ref="content">
      <v-card class="card mb-3" rounded="lg" width="600px" elevation="6">
        <v-container class="px-10 pt-4 pb-5">
          <p class="card-title">Coding Rush is a</p>
          <p class="card-content">platform for learning to <span>type faster</span> designed for
                                  competitive programmers.</p>
        </v-container>
      </v-card>
      <p key="" class="card-content pt-4" style="width: 800px">
        You don't type snippets from books, lyrics from songs or
        famous quotes here. Instead, you can train your muscular memory to remember
        <span>competitive programming code</span>!
      </p>
      <PrettyDivider/>
      <v-container class="card pa-0 ma-0">
        <p class="card-title">What can you achieve here?</p>
        <p class="card-subtitle">Improve your skills</p>
        <v-container id="skills-list" class="pa-0 ma-0 mb-9 mt-3">
          <v-card class="list-card" elevation="3">
            <p class="list-item-title">Typing accuracy</p>
            <v-divider></v-divider>
            <p class="list-item-content">Make fewer typos and mistakes</p>
          </v-card>
          <v-card class="list-card" elevation="5" style="align-self: flex-start">
            <p class="list-item-title">Typing speed</p>
            <v-divider></v-divider>
            <p class="list-item-content">Type faster and faster:<br>letters, numbers, symbols</p>
          </v-card>
          <v-card class="list-card" elevation="3">
            <p class="list-item-title">Knowledge of algorithms</p>
            <v-divider></v-divider>
            <p class="list-item-content">Write simple code without stuttering</p>
          </v-card>
        </v-container>
        <p class="card-content" style="width: 600px">
          Learn <span>algorithms</span> and <span>data structures</span> that are often
          used in programming contests while training your <span>speed</span>
          and <span>accuracy</span>.
        </p>
      </v-container>
      <PrettyDivider/>
      <v-container class="card pa-0 ma-0">
        <p class="card-title">Who is it for?</p>
        <p class="card-subtitle" style="width: 600px">
          Our platform is designed for competitive programmers
          with different levels</p>
        <v-container id="for-list" class="pa-0 mb-9 mt-3">
          <v-card class="list-card" elevation="3">
            <p class="list-item-title">Beginners</p>
            <v-divider></v-divider>
            <p class="list-item-content">You have just started coding
                                         and know very few algorithms</p>
          </v-card>
          <v-card class="list-card" elevation="3">
            <p class="list-item-title">Advanced</p>
            <v-divider></v-divider>
            <p class="list-item-content">You know a lot of algorithms and data structures</p>
          </v-card>
        </v-container>
        <p class="card-content" style="width: 600px">
          <span>Everyone</span> can find <span>something new</span>
                                here regardless of their programming experience.
        </p>
      </v-container>
      <PrettyDivider/>
      <v-container class="pa-0 ma-0 card">
        <p class="card-title">What will you find here?</p>
        <p class="card-subtitle" style="width: 600px">
          Algorithms and data structures for competitive programming
        </p>
        <p class="card-content" style="width: 900px">
          Everyone will find some new (or difficult to code) for themselves — there are
          <span>more than 50 algorithms</span> of different levels from
          binary search to Link-Cut tree.
        </p>
        <p class="card-content mb-2" style="width: 900px">
          Here you will find algorithms of such topics as:
        </p>
        <ul class="card-content mt-0 ml-10" style="text-align: left">
          <li>Graphs</li>
          <li>Strings</li>
          <li>Geometry</li>
          <li>Maths</li>
          <li>Trees</li>
          <li>and much more</li>
        </ul>
        <p class="card-content mb-0">All algorithms are available in
          <span>C++</span>. Some algorithms are also available in <span>Python 3</span>.
        </p>

        <div v-if="isAuthed()">
          <v-btn color="#ff8200" style="color: white; font-size: 1.3rem; margin-top: 100px"
                 width="300px" height="40px" class="text-capitalize"
                 @click="$router.push('/lessons')">
            Proceed
          </v-btn>
        </div>
        <div v-else>
          <v-btn color="success" style="color: white; font-size: 1.2rem; margin-top: 100px"
                 width="300px" height="40px" class="text-capitalize"
                 @click="$router.push('/signin')">
            Sign in / Sign up
          </v-btn>
        </div>
      </v-container>
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
  methods: {
    scrollToContentStart() {
      const elementTop = this.$refs.content.getBoundingClientRect().top + window.scrollY;
      window.scrollTo({
        top: elementTop,
        behavior: 'smooth',
      });
    },
    isAuthed() {
      return this.$store.getters.isAuthenticated;
    },
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
  align-self: center;
  position: absolute;
}

#header-title img {
  max-width: 730px;
  min-width: 730px;
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
  cursor: default;
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
  cursor: pointer;
}

#proceed-button {
  margin-left: 60vw;
  margin-top: 650px;
  position: absolute;
}

#content {
  min-width: 100vw;
  max-width: 100vw;
  margin-top: 130px;
  padding-top: 70px;
  padding-bottom: 50px;
  padding-left: 30px;
  display: flex;
  align-items: center;
  flex-direction: column;
}

.v-divider {
  width: 50px;
}

.card {
  display: flex;
  align-items: center;
  flex-direction: column;
}

.card-title {
  font-size: 2.5rem;
  font-family: Roboto Slab, serif;
  font-weight: 600;
  margin-bottom: 0;
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

#skills-list {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  min-width: 1176px;
  max-width: 1176px;
  height: 210px;
}

#for-list {
  display: flex;
  justify-content: space-between;
  min-width: 780px;
  max-width: 780px;
}

.list-card {
  min-width: 384px;
  max-width: 384px;
  min-height: 180px;
  max-height: 180px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.list-item-title {
  font-size: 1.6rem;
  font-family: Roboto, sans-serif;
  font-style: italic;
  font-weight: 400;
  text-align: center;
}

.list-item-content {
  font-size: 1.28rem;
  font-family: Roboto Slab, serif;
  font-weight: 400;
  margin-top: 12px;
  margin-left: 40px;
  margin-right: 40px;
  text-align: center;
  color: #555555;
}

</style>
