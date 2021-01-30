<template>
  <v-container>
    <v-row justify="space-between">
      <v-col cols="2" style="white-space: nowrap">
        {{ textName }}
      </v-col>
      <v-col cols="2">
        <v-btn min-width="90px" color="primary" dark @click="switchTyping()">
          {{ typing ? 'Stop' : 'Start' }}
        </v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-textarea id="editor" outlined rounded v-model="code" ref="editor"
                  @input="compareCode()"></v-textarea>
      <v-textarea :readonly="typing" id="target" outlined rounded v-model="textb"/>
    </v-row>
    <p>
      {{ getCPM() + ' CPM' }}
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
      typingTimer: 0,
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
      if (this.typing) {
        this.$refs.editor.focus();
        this.typingTimer = new Date();
      }
      this.code = '';
    },
    getCPM() {
      return Math.round((this.code.length * 1000 * 60) / (new Date() - this.typingTimer), 2);
    },
  },
};
</script>

<style scoped>

</style>
