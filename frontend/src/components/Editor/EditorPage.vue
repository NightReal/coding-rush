<template>
  <div style="margin: 50px 7vw; min-width: 800px">
    <div style="display: flex; justify-content: space-between">
      <div style="white-space: nowrap">
        <div v-if="topic || title" style="font-size: 1.5rem; margin-left: 20px; font-weight: 500">
          {{ topic }}<span style="word-spacing: 1rem" v-if="topic && title"> — </span>{{ title }}
        </div>
      </div>
      <div>
        <div>Speed: {{ Math.round(cpm) }} cpm</div>
        <div>Accuracy: {{ Math.round(acc * 100) }}%</div>
      </div>
      <div>
        <DropDownMenu v-if="ready" :text="!typing ? language : 'Typing...'"
                      min-width="100px" :color="lang_colors[language]"
                      :items="Object.keys(texts)"
                      :on_change="changeLang"
                      :on_click="switchTyping"
                      :tooltip-text="`${this.typing ? 'Stop' : 'Start'} typing!`"></DropDownMenu>
      </div>
    </div>
    <EditorArea v-if="editorAreaReady" ref="editor"
                :target-text="texts[language]" :is-typing="typing"
                @setTyping="typing = $event"
                @setCPM="cpm = $event" @setACC="acc = $event"></EditorArea>
  </div>
</template>

<script>
import EditorArea from '@/components/Editor/EditorArea.vue';
import { langColors } from '@/components/TextChoose/Languages';
import DropDownMenu from '@/components/DropDownMenu.vue';

export default {
  name: 'EditorView',
  components: {
    DropDownMenu,
    EditorArea,
  },
  props: [
    'textid',
    'texts',
    'language',
    'topic',
    'title',
    'ready',
  ],
  data() {
    return {
      typing: false,
      editorAreaReady: false,
      cpm: 0,
      acc: 0,
      lang_colors: langColors,
    };
  },
  mounted() {
    if (this.ready) {
      this.onReady();
    }
  },
  watch: {
    ready() {
      if (this.ready) {
        this.onReady();
      }
    },
  },
  methods: {
    onReady() {
      this.code = this.texts[this.language];
      this.editorAreaReady = true;
    },
    switchTyping() {
      this.$refs.editor.switchTyping();
    },
    changeLang(lang) {
      if (this.typing) {
        this.switchTyping();
      }
      this.$emit('setLang', lang);
    },
  },
};
</script>
