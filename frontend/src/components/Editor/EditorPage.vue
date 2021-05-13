<template>
  <div style="margin: 10px 7vw 50px 7vw; min-width: 800px" v-if="ready">
    <div style="display: flex; justify-content: space-between">
      <div style="white-space: nowrap; flex: 1 1 0; display: flex; align-items: center;
                  justify-content: space-between">
        <div v-if="topic || title" style="font-size: 1.6rem; margin-left: 20px; font-weight: 500">
          {{ topic }}<span style="word-spacing: 1rem" v-if="topic && title"> — </span>{{ title }}
        </div>
      </div>
      <div style="flex: 1 1 0; display: flex; justify-content: center; align-items: center"
           class="mx-4">
        <div style="display: flex; flex-direction: column; text-align: center">
          <VueSvgGauge
            :start-angle="-100"
            :end-angle="100"
            :value="cpm"
            :separator-step="100"
            :min="0"
            :max="500"
            :scale-interval="0"
            :inner-radius="50"
            :gauge-color="[{ offset: 0, color: '#0056b1'},
                           { offset: 50, color: '#00a8a4'},
                           { offset: 100, color: '#00cb51'}]"
            easing="Cubic.Out"
            style="max-width: 170px"
          >
            <div class="inner-text" style="margin-top: 80px; display: flex;
                                             justify-content: center; font-size: 1.3rem">
              {{ Math.min(999, Math.round(cpm)) }} cpm
            </div>
          </VueSvgGauge>
          <div style="font-weight: 600; font-size: 1.1rem; margin-top: -10px">Speed</div>
        </div>
        <div class="ml-5" style="display: flex; flex-direction: column; text-align: center">
          <VueSvgGauge
            :start-angle="-100"
            :end-angle="100"
            :value="acc * 100"
            :separator-step="25"
            :min="0"
            :max="100"
            :scale-interval="0"
            :inner-radius="50"
            :gauge-color="[{ offset: 0, color: '#aa0000'},
                           { offset: 50, color: '#ff992e'},
                           { offset: 100, color: '#ffe600'}]"
            easing="Cubic.Out"
            style="max-width: 170px"
          >
            <div class="inner-text" style="margin-top: 80px; display: flex;
                                             justify-content: center; font-size: 1.3rem">
              {{ Math.round(acc * 100) }}%
            </div>
          </VueSvgGauge>
          <div style="font-weight: 600; font-size: 1.1rem; margin-top: -10px">Accuracy</div>
        </div>
      </div>
      <div style="flex: 1 1 0; display: flex; justify-content: center; align-items: center;">
        <v-btn :color="typing ? '#ce0000' : '#00e000'" min-width="124px" min-height="45px"
               class="mr-5"
               @click="switchTyping()">
          <div v-if="!typing" class="text-capitalize" style="color: #000000; font-size: 1.1rem">
            Start
          </div>
          <div v-else
               style="font-family: monospace; font-size: 1.2rem; font-weight: 600; color: #ffffff;
               letter-spacing: 0.05rem; word-spacing: -0.5rem; white-space: nowrap;">
            {{ formatTime() }}
          </div>
        </v-btn>
        <DropDownMenu :text="language" :disabled="typing"
                      min-width="100px" min-height="45px" :color="lang_colors[language]"
                      :items="Object.keys(texts)"
                      :on_change="changeLang" font-size="1.1rem"
                      :tooltip-text="`${this.typing ? 'Stop' : 'Start'} typing!`"></DropDownMenu>
      </div>
    </div>
    <div style="display: flex; justify-content: center">
      <div :style="`min-width: ${editorWidth}px; max-width: ${editorWidth}px`">
        <EditorArea v-if="editorAreaReady" ref="editor"
                    :target-text="texts[language]" :is-typing="typing"
                    @setTyping="typing = $event; duration = 0"
                    @setCPM="cpm = $event" @setACC="acc = $event"></EditorArea>
      </div>
    </div>
    <div style="display: flex; justify-content: flex-end; margin: 0 7vw">
      <v-card style="display: inline-block">
        <v-btn v-long-press="500" class="rounded-0 rounded-l" elevation="0"
               @long-press-start="startChangingEditorWidth(-10)"
               @long-press-stop="stopChangingEditorWidth()"
               @mousedown="changeEditorWidth(-10)"
               color="accent">
          <span style="font-size: 1.3rem">−</span>
        </v-btn>
        <v-btn v-long-press="500" class="rounded-0 rounded-r" elevation="0"
               @long-press-start="startChangingEditorWidth(+10)"
               @long-press-stop="stopChangingEditorWidth()"
               @mousedown="changeEditorWidth(+10)"
               color="accent">
          <span style="font-size: 1.3rem">+</span>
        </v-btn>
      </v-card>
    </div>
  </div>
</template>

<script>
import EditorArea from '@/components/Editor/EditorArea.vue';
import { langColors } from '@/components/TextChoose/Languages';
import DropDownMenu from '@/components/DropDownMenu.vue';
import { VueSvgGauge } from 'vue-svg-gauge';
import LongPress from 'vue-directive-long-press';

export default {
  name: 'EditorView',
  components: {
    DropDownMenu,
    EditorArea,
    VueSvgGauge,
  },
  directives: {
    'long-press': LongPress,
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
      duration: 0,
      timer: null,
      editorWidth: this.$store.getters.lastEditorWidth || 1300,
      intervalWidthEditor: null,
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
    typing() {
      if (this.typing) {
        this.timer = setInterval(this.updateDuration, 1000);
      } else {
        clearInterval(this.timer);
      }
    },
  },
  methods: {
    onReady() {
      this.code = this.texts[this.language];
      this.editorAreaReady = true;
    },
    switchTyping() {
      this.duration = 0;
      this.$refs.editor.switchTyping();
    },
    changeLang(lang) {
      if (this.typing) {
        this.switchTyping();
      }
      this.$emit('setLang', lang);
    },
    formatTime() {
      const s = this.duration % 60;
      const m = Math.floor(this.duration / 60) % 60;
      const h = Math.floor(this.duration / 3600);
      const ss = ('0' + s).slice(-2); // eslint-disable-line prefer-template
      const mm = ('0' + m).slice(-2); // eslint-disable-line prefer-template
      if (h === 0) {
        return mm + ' : ' + ss; // eslint-disable-line prefer-template
      }
      return (h <= 9 ? '0' : '') + h + ' : ' + mm + ' : ' + ss; // eslint-disable-line prefer-template
    },
    saveEditorWidth() {
      // eslint-disable-next-line no-restricted-globals
      this.$store.commit('updateLastEditorWidth', this.editorWidth);
    },
    updateDuration() {
      const curTime = new Date();
      const seconds = (curTime - this.$refs.editor.startTime) / 1000;
      this.duration = Math.floor(seconds);
    },
    changeEditorWidth(delta) {
      this.editorWidth += delta;
      this.editorWidth = Math.max(600, this.editorWidth);
      this.editorWidth = Math.min(window.innerWidth * 0.95, this.editorWidth);
      if (!this.intervalWidthEditor) this.saveEditorWidth();
    },
    startChangingEditorWidth(delta) {
      this.intervalWidthEditor = setInterval(() => { this.changeEditorWidth(delta); }, 20);
    },
    stopChangingEditorWidth() {
      clearInterval(this.intervalWidthEditor);
      this.intervalWidthEditor = null;
      this.saveEditorWidth();
    },
  },
};
</script>

<style scoped>

.inner-text {
  height: 100%;
  width: 100%;
}

</style>
