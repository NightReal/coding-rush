<template>
  <div>
    <page-loader :loading="loading"></page-loader>
    <div style="display: flex; flex-direction: column; align-items: center">
      <v-card style="display: flex; justify-content: center; width: 60vw; height: 20vh;
                     min-width: 470px; align-items: center" rounded="lg" elevation="3">
        <a href="" style="height: 18vh">
          <img style="height: 18vh" src=""/>
        </a>
      </v-card>
      <div style="display: flex; flex-direction: column; width: 50vw; margin-top: 30px;
                  min-width: 420px;">
        <div style="display: flex; justify-content: space-between; align-items: center;
                    margin-bottom: 30px">
          <h1 class="mr-3" v-if="topic || title">
            {{ topic }}<span style="word-spacing: 1rem" v-if="topic && title"> — </span>{{ title }}
          </h1>
          <DropDownMenu v-if="!loading"
                        :text="lang" min-width="100px" :color="lang_colors[lang]"
                        :items="Object.keys(codes)"
                        :on_change="changeLang"
                        :on_click="go_type" tooltip-text="Start typing!"></DropDownMenu>
        </div>
        <v-runtime-template :template="description"></v-runtime-template>
      </div>
      <AttemptsList v-if="attempts !== null" :attempts="attempts" class="mb-16"></AttemptsList>
    </div>
  </div>
</template>

<script>

import PageLoader from '@/components/PageLoader.vue';
import APIHelper from '@/api/apihelper';
import { langColors, changeLanguage } from '@/components/TextChoose/Languages';
import DropDownMenu from '@/components/DropDownMenu.vue';
import AttemptsList from '@/components/TextChoose/AttemptsList.vue';
import VRuntimeTemplate from 'v-runtime-template';
import * as vuetifyComponents from 'vuetify/lib';

export default {
  name: 'TextDescription',

  props: ['textid', 'default_lang'],

  components: {
    AttemptsList,
    DropDownMenu,
    PageLoader,
    VRuntimeTemplate,
    ...vuetifyComponents,
  },

  data: () => ({
    lang: null,
    loading: true,
    codes: null,
    description: null,
    topic: null,
    title: null,
    difficulty: null,
    attempts: null,
    next_lesson: null,
    lang_colors: langColors,
  }),

  mounted() {
    this.lang = this.default_lang ? this.default_lang : this.$store.getters.lastUsedLanguage;
    APIHelper.get(`/lessons/${this.textid}`)
      .then((e) => {
        this.description = e.data.description;
        this.topic = e.data.topic;
        this.title = e.data.title;
        this.difficulty = e.data.difficulty;
        this.attempts = e.data.attempts;
        this.next_lesson = e.data.next_lesson;
        this.codes = {};
        // eslint-disable-next-line no-restricted-syntax
        for (const code of e.data.codes) {
          this.codes[code.language] = { code: code.code, id: code.id };
        }
        if (this.codes[this.lang] === undefined) {
          if (e.data.codes.length !== 0) {
            this.lang = e.data.codes[0].language;
            changeLanguage(this.lang);
          }
        }
        this.loading = false;
      })
      .catch(() => {
        this.$router.push('/404');
      });
  },

  methods: {
    changeLang(lang) {
      changeLanguage(lang);
      this.lang = lang;
    },
    go_type(lang) {
      this.$router.push({
        name: 'Editor',
        params: {
          texts: this.codes,
          language: lang,
          topicName: this.topic,
          titleName: this.title,
          nextLesson: this.next_lesson,
        },
      });
    },
  },
};
</script>
