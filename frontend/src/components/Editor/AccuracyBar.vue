<template>
  <div style="display: inline-flex; flex-direction: column; text-align: center">
    <VueSvgGauge
      :start-angle="-100"
      :end-angle="100"
      :value="acc * 100"
      :separator-step="25"
      :min="0"
      :max="100"
      :scale-interval="0"
      :transition-duration="animationTime"
      :inner-radius="50"
      :gauge-color="[{ offset: 0, color: '#aa0000'},
                     { offset: 50, color: '#ff992e'},
                     { offset: 100, color: '#ffe600'}]"
      easing="Cubic.Out"
      :style="`max-width: ${maxWidth}`"
    >
      <div class="inner-text" style="margin-top: 80px; display: flex;
                                             justify-content: center; font-size: 1.3rem">
        {{ Math.round(acc * 100) }}%
      </div>
    </VueSvgGauge>
    <slot v-if="$slots.default"/>
    <div v-else style="font-weight: 600; margin-top: -10px"
         :style="`font-size: ${fontSize}`">Accuracy
    </div>
  </div>
</template>
<script>

import { VueSvgGauge } from 'vue-svg-gauge';

export default {
  name: 'AccuracyBar',
  props: ['acc', 'maxWidth', 'fontSize', 'animationTime'],
  components: { VueSvgGauge },
};
</script>

<style scoped>

</style>
