<template>
  <div v-if="texts && texts.length > 0"
       :style="`min-width: ${inRow === 4 ? 1250 : 750}px`" class="mb-16">
    <h1>{{ topic }}</h1>
    <div style="display: flex; justify-content: center">
      <v-container style="display: inline-block; width: auto; border-radius: 10px;"
                   :class="`pa-4 ma-0 bg-${color}`">
        <v-container v-for="row in Math.ceil(texts.length / inRow)" v-bind:key="row"
                     style="display: flex; flex-direction: row; justify-content: center;"
                     class="pa-0 ma-0">
          <TextCard v-for="col in inRow"
                    v-bind:key="col" style="width: auto" class="pa-0 ma-0"
                    :text="(row - 1) * inRow + col - 1 < texts.length ?
                       texts[(row - 1) * inRow + col - 1] : null"
                    :hide="(row - 1) * inRow + col - 1 >= texts.length">
          </TextCard>
        </v-container>
      </v-container>
    </div>
  </div>
</template>

<script>
import TextCard from '@/components/TextChoose/TextCard.vue';

export default {
  name: 'Topic',
  props: ['texts', 'color', 'topic'],
  components: { TextCard },

  data: () => ({
    inRow: 4,
  }),

  created() {
    window.addEventListener('resize', this.resizeHandler);
  },
  destroyed() {
    window.removeEventListener('resize', this.resizeHandler);
  },
  mounted() {
    this.resizeHandler();
  },
  methods: {
    resizeHandler() {
      this.inRow = window.innerWidth < 1250 ? 2 : 4;
    },
  },
};
</script>

<style scoped>

.bg-red {
  background-color: rgba(255, 30, 0, 0.05);
}

.bg-orange {
  background-color: rgba(255, 153, 46, 0.1);
}

.bg-green {
  background-color: rgba(50, 255, 0, 0.05);
}

.bg-yellow {
  background-color: rgba(255, 255, 0, 0.1);
}

.bg-cyan {
  background-color: rgba(0, 255, 255, 0.05);
}

.bg-magenta {
  background-color: rgba(255, 0, 255, 0.04);
}

</style>
