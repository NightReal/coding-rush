<template>
  <!-- <img src="./assets/logo.png"> -->
  <v-container>
    <Editor :textProp="text" :textNameProp="textName"></Editor>
  </v-container>
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
      textName: 'First step - Hello, world!',
    };
  },
};
</script>

<style>
</style>
