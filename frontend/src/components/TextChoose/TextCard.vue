<template>
  <v-container class="pa-0 ma-4">
    <v-hover v-slot="{ hover }" v-if="!hide"
             style="display:flex; flex-direction:column; justify-content: space-between">
      <v-card width="220px" height="220px" class="text-card px-1 pt-3 pb-1"
              :style="`background-color: ${hover ? 'rgba(255, 255, 255, 0.85)' :
                                                   'rgba(255, 255, 255, 1)'}`"
              :elevation="hover ? 7 : 3">
        <div style="width: 100%; display: flex; flex-direction: column; align-items: center;
                  font-size: 1.3rem; text-align: center; justify-content: space-between;
                  font-family: monospace; font-style: normal; overflow-wrap: anywhere;">
          {{ text.title }}
        </div>
        <div style="display: flex">
          <template v-for="(lang, i) in text.codes">
            <!-- eslint-disable-next-line vue/valid-v-for -->
            <v-btn style="flex: 1 1 0; height: 30px; width: auto" class="text-capitalize pa-0 ma-0"
                   elevation="0"
                   :color="lang_colors[lang]"
                   @click="go_type(lang)">{{ lang }}
            </v-btn>
            <!-- eslint-disable-next-line vue/require-v-for-key -->
            <div v-if="i !== text.codes.length - 1" style="width: 0; height: 0" class="mr-1"></div>
          </template>
        </div>
      </v-card>
    </v-hover>
    <v-card v-else flat width="220px" height="220px" style="opacity: 0"></v-card>
  </v-container>
</template>

<script>
export default {
  name: 'TextCard',
  props: ['text', 'hide'],

  data: () => ({
    // eslint-disable-next-line quote-props
    lang_colors: { 'python': 'yellow', 'c++': '#68d2ff', 'java': '#ff7575' },
  }),

  methods: {
    go_type(lang) {
      this.$router.push({ path: `/text/${this.text.id}`, params: { language: lang } });
    },
  },
};
</script>

<style scoped>

</style>
