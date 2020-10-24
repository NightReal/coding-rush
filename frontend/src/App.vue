<template>
  <div id="app"
       style="display: flex; flex-direction: column; height: 100%; justify-content: space-between;">
    <!-- <img src="./assets/logo.png"> -->
    <Header/>
    <Editor :text="text"></Editor>
    <Footer style="flex-shrink: 0;"></Footer>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import Editor from './components/Editor.vue';

export default {
  name: 'App',
  components: {
    Header,
    Footer,
    Editor,
  },
  data() {
    return {
      text: 'Hello, world!',
    };
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  margin: 0;
}
</style>
