<template>
  <div style="display: flex; flex-direction: column; align-items: center">
    <SpeedBar :cpm="cpm" max-width="200px" :animation-time="3000"
              :max-cpm="9999" style="color: #555">
      <div style="font-size: 1.2rem; color: #333">Average Speed</div>
    </SpeedBar>
    <AccuracyBar :acc="acc / 100" max-width="200px"
                 :animation-time="3000" class="mt-3" style="color: #555">
      <div style="font-size: 1.2rem; color: #333">Average Accuracy</div>
    </AccuracyBar>
  </div>
</template>

<script>

import SpeedBar from '@/components/Editor/SpeedBar.vue';
import AccuracyBar from '@/components/Editor/AccuracyBar.vue';

export default {
  name: 'AverageCpmAcc',
  props: ['cpm', 'acc'],
  components: { SpeedBar, AccuracyBar },
};
</script>

<style scoped>

</style>
