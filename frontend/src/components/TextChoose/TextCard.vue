<template>
  <v-container class="pa-0" style="margin: 12px !important;">
    <v-hover v-slot="{ hover }" v-if="!hide">
      <v-card :width="cardWidth" :height="cardHeight" class="text-card px-1 pt-3 pb-1"
              style="display:flex; flex-direction:column; justify-content: space-between"
              :style="`background-color: ${hover ? '#4f4f4f' :'#fff'};
                                  color: ${hover ? '#fff' : '#000'}`"
              :elevation="hover ? 10 : 3" @click="go_type()" :ripple="false">
        <div style="background-color: #8b8b8b; color: white; position:absolute;
                    border-radius: 3px; padding: 2px 8px 2px 8px; font-size: 0.8rem; top: -14px;
                    align-self: flex-end; right: 10px; font-family: monospace">
          <b>Difficulty: {{ text.difficulty }}</b>
        </div>
        <div style="width: 100%; text-align: center;">
          <div style="font-size: 1.3rem; font-family: monospace; font-style: normal;
                            overflow-wrap: anywhere;">{{ text.title }}
          </div>
        </div>
        <div style="display: flex; flex-direction: column;">
          <div v-if="text.best_attempt"
            style="display: flex; justify-content: center; margin-bottom: 5px">
            <v-tooltip top>
              <template v-slot:activator="{on, attrs}">
                <div v-on="on" v-bind="attrs">
                  <Stars :score="text.best_attempt.score" size="1.3rem"></Stars>
                </div>
              </template>
              <div style="font-family: monospace; font-size: 0.85rem; font-weight: bold">
                <div style="display: flex;">
                  <div style="margin-right: 5px">Speed:</div>
                  <div>{{ text.best_attempt.speed }}cpm
                  </div>
                </div>
                <div style="display: flex;">
                  <div style="margin-right: 5px">Accuracy:</div>
                  <div>{{ Math.floor(text.best_attempt.accuracy) }}%</div>
                </div>
              </div>
            </v-tooltip>
          </div>
          <div style="display: flex">
            <template v-for="(lang, i) in text.codes">
              <!-- eslint-disable-next-line vue/valid-v-for -->
              <v-btn style="flex: 1 1 0; height: 30px; width: auto"
                     class="text-capitalize pa-0 ma-0"
                     elevation="0"
                     :color="lang_colors[lang]"
                     @click="go_type(lang)">{{ lang }}
              </v-btn>
              <!-- eslint-disable-next-line vue/require-v-for-key -->
              <div v-if="i !== text.codes.length - 1" style="width: 0; height: 0"
                   class="mr-1"></div>
            </template>
          </div>
        </div>

      </v-card>
    </v-hover>
    <v-card v-else flat :width="cardWidth" :height="cardHeight" style="opacity: 0"></v-card>
  </v-container>
</template>

<script>

import { langColors, changeLanguage } from '@/components/TextChoose/Languages';
import Stars from '@/components/TextChoose/Stars.vue';

export default {
  name: 'TextCard',
  components: { Stars },
  props: ['text', 'hide'],

  data: () => ({
    lang_colors: langColors,
    cardWidth: '250px',
    cardHeight: '230px',
  }),

  methods: {
    go_type(lang) {
      if (lang) {
        changeLanguage(lang);
      }
      this.$router.push(`/text/${this.text.id}`);
    },
  },
};
</script>

<style scoped>

.v-tooltip__content {
  padding: 3px 10px;
  margin-top: 4px;
  background-color: #8b8b8b !important;
}

.v-tooltip__content.menuable__content__active {
  opacity: 1 !important;
}

</style>
