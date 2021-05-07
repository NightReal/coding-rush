<template>
  <v-container>
    <v-row justify="space-between">
      <v-col cols="2" style="white-space: nowrap">
        {{ textName }}
      </v-col>
      <v-col cols="2">
        <v-btn min-width="90px" color="primary" dark @click="switchTyping()">
          {{ typing ? "Stop" : "Start" }}
        </v-btn>
      </v-col>
    </v-row>
    <v-row justify="space-between">
      <v-container
        style="width: 50%"
        :class="editorClass">
        <textarea ref="editor"></textarea>
      </v-container>
      <v-container style="width: 50%">
        <textarea ref="target"></textarea>
      </v-container>
    </v-row>
    <p>
      {{ cpm + " CPM" }}
    </p>
    <p>
      {{ acc * 100 + "%" }}
    </p>
  </v-container>
</template>

<script>
import CodeMirror from 'codemirror';
import 'codemirror/lib/codemirror.css';
import 'codemirror/theme/monokai.css';
import 'codemirror/mode/clike/clike';
import 'codemirror/addon/scroll/scrollpastend';

export default {
  name: 'Editor',
  props: ['textNameProp', 'targetTextProp'],
  data() {
    return {
      targetText: this.targetTextProp,
      textName: this.textNameProp,
      typing: false,
      startTime: 0,
      cpm: 0,
      mark: null,
      editorClass: '',
      cursorDefault: null,
      isBad: null,
      acc: 1,
    };
  },
  methods: {
    switchTyping() {
      console.log(this.typing);
      if (!this.typing) {
        this.editor.setValue('');
        this.editor.focus();
        this.startTime = new Date();
        this.isBad = new Array(0);
      } else {
        this.typing = false;
      }
    },
    onChange() {
      const lcp = this.getLCP(this.editor.getValue(), this.target.getValue());
      this.updateCPM(lcp);
      for (let i = lcp; i < this.editor.getValue().length; i += 1) {
        this.isBadSum += 1 - this.isBad[i];
        this.isBad[i] = 1;
      }
      this.updateAcc();
      this.updateMark();
      if (this.editor.getValue() === this.target.getValue()) {
        this.typing = false;
      }
      this.scrollIntoMiddle();
    },
    beforeChange() {
      console.log('bruh');
      if (!this.typing) {
        this.typing = true;
        this.startTime = new Date();
        this.isBad = new Array(0);
        this.editor.setValue('');
      }
    },
    scrollIntoMiddle() {
      const cursorPos = this.editor.cursorCoords(false, 'local');
      const defPos = this.editor.cursorCoords({ line: 0, ch: 0 }, 'local');
      const winInfo = this.editor.getScrollInfo();
      const top = (cursorPos.top - defPos.top) - winInfo.clientHeight / 2;
      this.editor.scrollTo(null, top);
      this.target.scrollTo(null, top);
    },
    getLCP(s1, s2) {
      let ans = 0;
      while (ans < s1.length && ans < s2.length && s1[ans] === s2[ans]) {
        ans += 1;
      }
      return ans;
    },
    getLineCh(n) {
      let curLine = 0;
      let curPos = 0;
      const code = this.editor.getValue();
      for (let i = 0; i < n; i += 1) {
        if (code[i] === '\n') {
          curLine += 1;
          curPos = 0;
        } else {
          curPos += 1;
        }
      }
      return { line: curLine, ch: curPos };
    },
    updateMark() {
      if (this.mark !== null) {
        this.mark.clear();
      }
      const length = this.getLCP(this.editor.getValue(), this.target.getValue());
      this.mark = this.editor.markText(this.getLineCh(length),
        this.getLineCh(this.editor.getValue().length),
        { className: 'redbg' });
      if (this.editor.getValue() === this.target.getValue()) {
        this.editorClass = 'greenbg';
      } else {
        this.editorClass = '';
      }
    },
    updateCPM(lcp) {
      const curTime = new Date();
      if ((curTime - this.startTime) > 0.0001) {
        this.cpm = (lcp * 1000 * 60) / (curTime - this.startTime);
      }
    },
    updateAcc() {
      const len = Math.max(this.editor.getValue().length, this.isBad.length);
      let cntBad = 0;
      for (let i = 0; i < this.isBad.length; i += 1) {
        if (this.isBad[i] === 1) {
          cntBad += 1;
        }
      }
      this.acc = (len - cntBad) / len;
    },
  },
  mounted() {
    const cmOptions = {
      mode: 'text/x-c++src',
      theme: 'monokai',
      tabSize: 4,
      indentWithTabs: true, // change to false in case we switch to spaces again
      smartIndent: true,
      indentUnit: 4,
      scrollPastEnd: true,
      // lineNumbers: true,
    };
    this.editor = CodeMirror.fromTextArea(this.$refs.editor, cmOptions);
    this.editor.on('beforeChange', this.beforeChange);
    this.editor.on('change', this.onChange);
    cmOptions.readOnly = true;
    this.target = CodeMirror.fromTextArea(this.$refs.target, cmOptions);
    this.target.setValue(this.targetText);
  },
};
</script>

<style>

.redbg {
  background-color: #a01f1f;
}

.greenbg .CodeMirror, .greenbg .CodeMirror-gutter {
  background-color: #005a00 !important;
}

.CodeMirror {
  height: 65vh;
}

.CodeMirror-vscrollbar {
  display: block !important;
}

</style>
