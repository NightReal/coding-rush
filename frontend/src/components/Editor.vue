<template>
  <v-container>
    <v-row justify="space-between">
      <v-col cols="2" style="white-space: nowrap">
        {{ textName }}
      </v-col>
      <v-col cols="2">
        <v-tooltip top>
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="primary" dark v-bind="attrs" v-on="on" @click="switchTyping()">
            {{ typing ? 'Stop' : 'Start' }}
          </v-btn>
        </template>
        <span>
          <div v-if="!typing">Click or press Ctrl+Enter<br>
          to start typing<br>(or just begin typing)</div>
          <div v-else>Click or press Ctrl+Enter<br>to stop typing</div>
        </span>
      </v-tooltip>
      </v-col>
    </v-row>
    <v-textarea readonly id="target" outlined rounded v-model="textb"/>
    <v-textarea id="editor" outlined rounded v-model="code"
         @input="compareCode()"></v-textarea>
    <p>
      {{ getWPM() + ' WPM' }}
    </p>
  </v-container>
</template>

<script>
export default {
  name: 'Editor',
  props: ['textNameProp', 'textProp'],
  data() {
    return {
      textb: this.textProp,
      textName: this.textNameProp,
      typing: false,
      code: '',
      typingTimer: undefined,
    };
  },
  methods: {
    compareCode() {
      if (!this.typing && this.code !== '') {
        this.typing = true;
        this.typingTimer = new Date();
      }
      if (this.code === this.textb) {
        this.typing = false;
        clearInterval(this.typingTimer);
      }
    },
    switchTyping() {
      this.typing = !this.typing;
      this.code = '';
    },
    getWPM() {
      return Math.round((this.code.length * 1000 * 60) / (new Date() - this.typingTimer), 2);
    },
  },
};
</script>

<style scoped>
</style>
