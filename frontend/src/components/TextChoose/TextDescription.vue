<template>
  <div>
    <page-loader :loading="loading"></page-loader>
    <div>text id: {{ textid }}</div>
    <div>language: {{ lang }}</div>
    <div>{{ codes }}</div>
    <DropDownMenu v-if="codes"
                  :text="lang" min-width="100px" :color="lang_colors[lang]"
                  :items="Object.keys(codes)"
                  :on_change="changeLang"
                  :on_click="go_type"></DropDownMenu>
  </div>
</template>

<script>

import PageLoader from '@/components/PageLoader.vue';
import APIHelper from '@/api/apihelper';
import langColors from '@/components/TextChoose/LangColors';
import DropDownMenu from '@/components/DropDownMenu.vue';

export default {
  name: 'TextChoose',

  props: ['textid', 'default_lang'],

  components: { DropDownMenu, PageLoader },

  data: () => ({
    lang: null,
    loading: true,
    codes: null,
    description: null,
    topic: null,
    title: null,
    difficulty: null,
    lang_colors: langColors,
  }),

  mounted() {
    this.lang = this.default_lang;
    APIHelper.get(`/lessons/${this.textid}`)
      .then((e) => {
        this.description = e.data.description;
        this.topic = e.data.topic;
        this.title = e.data.title;
        this.difficulty = e.data.difficulty;
        this.codes = {};
        // eslint-disable-next-line no-restricted-syntax
        for (const code of e.data.codes) {
          this.codes[code.language] = code.code;
        }
        this.loading = false;
      })
      .catch(() => {
        this.$router.push('/404');
      });
  },

  methods: {
    changeLang(lang) {
      this.$store.commit('updateLastUsedLanguage', lang);
      this.lang = lang;
    },
    go_type(lang) {
      console.log('type', lang);
    },
  },
};
</script>
