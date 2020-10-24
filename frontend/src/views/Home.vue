<template>
  <!-- <img src="./assets/logo.png"> -->
  <div class="editor">
    <Editor :text="text"></Editor>
  </div>
</template>

<script>
import Editor from '@/components/Editor.vue';

export default {
  name: 'Home',
  components: {
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
