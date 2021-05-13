<template>
  <div>
    <page-loader :loading="loading"></page-loader>
    <EditorPage :texts="codes" :topic="topic" :title="title"
                :ready="editorReady" :language="lang" :textid="id"
                @setLang="setLang"></EditorPage>
  </div>
</template>

<script>
import EditorPage from '@/components/Editor/EditorPage.vue';
import APIHelper from '@/api/apihelper';
import { changeLanguage } from '@/components/TextChoose/Languages';
import PageLoader from '@/components/PageLoader.vue';

export default {
  name: 'EditorView',
  components: {
    EditorPage,
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
      editorReady: false,
      id: parseInt(this.textid, 10),
    };
  },
  mounted() {
    if (this.texts === undefined) {
      this.loading = true;
      APIHelper.get(`/lessons/${this.id}`)
        .then((e) => {
          this.codes = {};
          // eslint-disable-next-line no-restricted-syntax
          for (const code of e.data.codes) {
            this.codes[code.language] = { code: code.code, id: code.id };
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
      this.editorReady = true;
    },
    fixLanguage() {
      if (this.codes[this.lang] === undefined) {
        // eslint-disable-next-line prefer-destructuring
        this.lang = Object.keys(this.codes)[0];
        changeLanguage(this.lang);
      }
    },
    setLang(lang) {
      this.lang = lang;
      changeLanguage(this.lang);
    },
  },
};
</script>
