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
        <SpeedBar :cpm="cpm" max-width="170px" font-size="1.1rem" :max-cpm="999"></SpeedBar>
        <AccuracyBar :acc="acc" max-width="170px" font-size="1.1rem" class="ml-5"></AccuracyBar>
      </div>
      <div style="flex: 1 1 0; display: flex; justify-content: center; align-items: center;">
        <v-btn :color="typing ? '#ce0000' : '#4dc751'" min-width="124px" min-height="45px"
               class="mr-5"
               @click="switchTyping()">
          <div v-if="!typing" class="text-capitalize" style="font-size: 1.1rem">
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
                      :on_change="changeLang" font-size="1.1rem"></DropDownMenu>
      </div>
    </div>
    <div style="display: flex; justify-content: center">
      <div :style="`min-width: ${editorWidth}px; max-width: ${editorWidth}px`">
        <EditorArea v-if="editorAreaReady" ref="editor"
                    :target-text="texts[language].code" :is-typing="typing" :lang="language"
                    @setTyping="setTyping"
                    @setCPM="cpm = $event" @setACC="acc = $event"></EditorArea>
      </div>
    </div>
    <div style="display: flex; justify-content: space-between; margin: 0 7vw">

      <v-btn class="text-capitalize" color="#ff8200" style="color: white; font-size: 0.95rem"
             @click="$router.push(`/lesson/${textid}`)">
        <v-icon class="ml-n2 mr-1">mdi-chevron-left</v-icon>
        Back to lesson
      </v-btn>
      <v-card style="display: inline-block">
        <v-btn v-long-press="500" class="rounded-0 rounded-l" elevation="0"
               @long-press-start="startChangingEditorWidth(-10)"
               @long-press-stop="stopChangingEditorWidth()"
               @mousedown="changeEditorWidth(-10)"
               color="#ff8200" style="color: white">
          <span style="font-size: 1.3rem">−</span>
        </v-btn>
        <v-btn v-long-press="500" class="rounded-0 rounded-r" elevation="0"
               @long-press-start="startChangingEditorWidth(+10)"
               @long-press-stop="stopChangingEditorWidth()"
               @mousedown="changeEditorWidth(+10)"
               color="#ff8200" style="color: white">
          <span style="font-size: 1.3rem">+</span>
        </v-btn>
      </v-card>
    </div>
    <v-dialog v-model="finished" max-width="900"
              transition="slide-y-transition" persistent>
      <AttemptResult :cpm="cpm" :acc="acc" :duration="duration" :score="score"
                     :committed="committed" :lesson_id="textid"
                     :next_lesson="next_lesson" :reset="resetPage"></AttemptResult>
    </v-dialog>
  </div>
</template>

<script>
import EditorArea from '@/components/Editor/EditorArea.vue';
import { langColors } from '@/components/TextChoose/Languages';
import DropDownMenu from '@/components/DropDownMenu.vue';
import LongPress from 'vue-directive-long-press';
import AttemptResult from '@/components/Editor/AttemptResult.vue';
import SpeedBar from '@/components/Editor/SpeedBar.vue';
import AccuracyBar from '@/components/Editor/AccuracyBar.vue';
import { formatTime } from '@/components/Editor/formatTime';
import APIHelper from '@/api/apihelper';

export default {
  name: 'EditorView',
  components: {
    AccuracyBar,
    SpeedBar,
    AttemptResult,
    DropDownMenu,
    EditorArea,
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
    'next_lesson',
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
      finished: false,
      score: null,
      committed: false,
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
    finished() {
      if (!this.finished) {
        setTimeout(this.continueReset, 200);
      }
    },
  },
  methods: {
    onReady() {
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
      return formatTime(this.duration);
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
    setTyping(t) {
      this.typing = t;
      if (t) this.duration = 0;
      else if (this.$refs.editor.finished) this.finishAttempt();
    },
    finishAttempt() {
      this.updateDuration();
      const speed = Math.round(this.$refs.editor.cpm);
      const accuracy = this.$refs.editor.acc * 100;
      APIHelper.put('lessons/commitAttempt', {
        speed,
        accuracy,
        duration: this.duration,
        code: this.texts[this.language].id,
      })
        .then((e) => {
          this.score = e.data.score;
          this.cpm = e.data.speed;
          this.acc = e.data.accuracy / 100;
          this.duration = e.data.duration;
          this.committed = true;
        })
        .catch((err) => console.log(err));
      this.finished = true;
    },
    resetPage() {
      this.finished = false;
      this.typing = false;
      this.committed = false;
    },
    continueReset() {
      this.score = null;
      this.cpm = 0;
      this.acc = 0;
      this.duration = 0;
      const { editor } = this.$refs;
      editor.init();
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
