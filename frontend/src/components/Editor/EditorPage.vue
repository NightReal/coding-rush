<template>
  <div style="margin: 10px 7vw 50px 7vw; min-width: 800px">
    <div style="display: flex; justify-content: space-between" v-if="ready">
      <div style="white-space: nowrap; flex: 1 1 0; display: flex; align-items: center">
        <div v-if="topic || title" style="font-size: 1.6rem; margin-left: 20px; font-weight: 500">
          {{ topic }}<span style="word-spacing: 1rem" v-if="topic && title"> — </span>{{ title }}
        </div>
      </div>
      <div style="flex: 1 1 0; display: flex; justify-content: center" class="mx-4">
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
            <div class="inner-text" style="margin-top: 80px; display: flex; justify-content: center;
            font-size: 1.3rem">
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
            <div class="inner-text" style="margin-top: 80px; display: flex; justify-content: center;
            font-size: 1.3rem">
              {{ Math.round(acc * 100) }}%
            </div>
          </VueSvgGauge>
          <div style="font-weight: 600; font-size: 1.1rem; margin-top: -10px">Accuracy</div>
        </div>
      </div>
      <div style="flex: 1 1 0; display: flex; justify-content: center; align-items: center">
        <v-btn :color="typing ? '#ce0000' : '#00e000'" min-width="124px" class="mr-5"
               @click="switchTyping()">
          <div class="text-capitalize" :style="`color: ${typing ? '#ffffff' : '#000000'}`"
               style="font-size: 1rem">
            {{ typing ? 'Stop' : 'Start' }}
          </div>
        </v-btn>
        <DropDownMenu :text="language" :disabled="typing"
                      min-width="100px" :color="lang_colors[language]"
                      :items="Object.keys(texts)"
                      :on_change="changeLang"
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
import { VueSvgGauge } from 'vue-svg-gauge';

export default {
  name: 'EditorView',
  components: {
    DropDownMenu,
    EditorArea,
    // eslint-disable-next-line
    VueSvgGauge,
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

<style scoped>

.inner-text {
  height: 100%;
  width: 100%;
}

</style>
