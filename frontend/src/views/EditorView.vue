<template>
  <div>
    <page-loader :loading="loading"></page-loader>
    <Editor v-if="editorReady"
            :targetTextProp="code" :topic-name="topic" :title-name="title"></Editor>
  </div>
</template>

<script>
import Editor from '@/components/Editor.vue';
import APIHelper from '@/api/apihelper';
import { changeLanguage } from '@/components/TextChoose/Languages';
import PageLoader from '@/components/PageLoader.vue';

export default {
  name: 'EditorView',
  components: {
    Editor,
    PageLoader,
  },
  props: [
    'textid',
    'texts',
    'language',
    'topicName',
    'titleName',
  ],
  data() {
    return {
      loading: false,
      topic: this.topicName,
      title: this.titleName,
      codes: null,
      lang: this.language ? this.language : this.$store.getters.lastUsedLanguage,
      code: null,
      editorReady: false,
    };
  },
  mounted() {
    if (this.texts === undefined) {
      this.loading = true;
      APIHelper.get(`/lessons/${this.textid}`)
        .then((e) => {
          this.codes = {};
          // eslint-disable-next-line no-restricted-syntax
          for (const code of e.data.codes) {
            this.codes[code.language] = code.code;
          }
          this.topic = e.data.topic;
          this.title = e.data.title;
          this.loading = false;
          this.prepareEditor();
        })
        .catch(() => {
          this.$router.push('/404');
        });
    } else {
      this.codes = JSON.parse(JSON.stringify(this.texts));
      this.prepareEditor();
    }
  },
  methods: {
    prepareEditor() {
      this.fixLanguage();
      this.code = this.codes[this.lang];
      this.editorReady = true;
    },
    fixLanguage() {
      if (this.codes[this.lang] === undefined) {
        // eslint-disable-next-line prefer-destructuring
        this.lang = Object.keys(this.codes)[0];
        changeLanguage(this.lang);
      }
    },
  },
};
</script>
