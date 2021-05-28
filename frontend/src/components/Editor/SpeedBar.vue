<template>
  <div style="display: inline-flex; flex-direction: column; text-align: center">
    <VueSvgGauge
      :start-angle="-100"
      :end-angle="100"
      :value="cpm"
      :separator-step="100"
      :min="0"
      :max="500"
      :scale-interval="0"
      :transition-duration="animationTime"
      :inner-radius="50"
      :gauge-color="[{ offset: 0, color: '#0056b1'},
                     { offset: 50, color: '#00a8a4'},
                     { offset: 100, color: '#00cb51'}]"
      easing="Cubic.Out"
      :style="`max-width: ${maxWidth}`"
    >
      <div class="inner-text" style="margin-top: 80px; display: flex;
                                             justify-content: center; font-size: 1.3rem">
        {{ Math.min(maxCpm, Math.round(cpm)) }} cpm
      </div>
    </VueSvgGauge>
    <slot v-if="$slots.default"/>
    <div v-else style="font-weight: 600; margin-top: -10px"
         :style="`font-size: ${fontSize}`">Speed
    </div>
  </div>
</template>
<script>

import { VueSvgGauge } from 'vue-svg-gauge';

export default {
  name: 'SpeedBar',
  props: ['cpm', 'maxWidth', 'fontSize', 'animationTime', 'maxCpm'],
  components: { VueSvgGauge },
};
</script>

<style scoped>

</style>
