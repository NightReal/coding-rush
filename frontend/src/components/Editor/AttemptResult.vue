<template>
  <v-card class="pt-10 pb-5 px-16"
          style="display: flex; flex-direction: column; align-items: center">
    <div style="display: flex; justify-content: center">
      <SpeedBar :cpm="cpm" max-width="250px" font-size="1.4rem" :animation-time="3000"
                :max-cpm="9999" class="mr-10"></SpeedBar>
      <AccuracyBar :acc="acc" max-width="250px" font-size="1.4rem"
                   :animation-time="3000"></AccuracyBar>
    </div>

    <div style="display: flex; flex-direction: column; align-items: center">
      <v-card color="#2b2b2b" min-width="160px" min-height="60px" class="mt-5"
              style="display: flex; justify-content: center; align-items: center">
        <div style="font-family: monospace; font-size: 1.45rem; font-weight: 600;
                        color: #ffffff; letter-spacing: 0.05rem; word-spacing: -0.5rem;
                        white-space: nowrap;">
          {{ formatTime() }}
        </div>
      </v-card>
      <div style="font-weight: 600; margin-top: 10px; font-size: 1.4rem">Duration</div>
    </div>
    <v-divider class="mt-7 mb-5" style="min-width: 50%"></v-divider>
    <Stars class="mb-3" :score="score" size="1.8rem"></Stars>
    <div class="mb-7"
         style="font-size: 1.2rem; display: flex; flex-direction: column; align-items: center;">
      <div style="font-size: 1.4rem; font-weight: 500">
        <span v-if="score < 15">Bad</span>
        <span v-else-if="score < 35">So-so</span>
        <span v-else-if="score < 50">Normal</span>
        <span v-else-if="score < 75">Good!</span>
        <span v-else-if="score < 90">Great!</span>
        <span v-else-if="score <= 100">Excellent!</span>
        <span v-else>Wow!</span>
      </div>
      <div class="ma-2" style="text-align: center">
        You finished this lesson<!--
        --><span v-if="committed"> with score {{ score }} out of 100</span>
        <span v-if="score > 100"><br>Are you genius?</span>
      </div>
      <div v-if="acc < 0.5 || cpm < 150">
        <span style="font-weight: 500">Advice: </span>
        <span v-if="acc < 0.5 && (cpm >= 150 || acc / 0.8 < cpm / 300)">
          Try typing more accurately.
        </span>
        <span v-if="cpm < 150 && (acc >= 0.5 || cpm / 300 < acc / 0.8)">
          Try typing faster.
        </span>
      </div>
      <div v-if="score < 90 && (acc >= 0.95 || cpm >= 400)">
        <span style="font-weight: 500">Note: </span>
        <span v-if="acc >= 0.95 && cpm >= 400">Good speed and accuracy!</span>
        <span v-else-if="acc >= 0.95">Good accuracy!</span>
        <span v-else-if="cpm >= 400">Good speed!</span>
      </div>
    </div>
    <div style="display: flex; justify-content: space-between; width: 100%">
      <div>
        <v-btn class="mx-1 text-capitalize dbutton" color="#ff8200" style="color: white"
               @click="$router.push(`/lesson/${lesson_id}`)">
          <v-icon class="ml-n2 mr-1">mdi-format-list-bulleted</v-icon>
          Attempts
        </v-btn>
        <v-btn class="mx-1 text-capitalize dbutton" color="#ff8200" style="color: white"
               @click="$router.push('/lessons')">
          <v-icon class="ml-n2 mr-1 ">mdi-view-grid-outline</v-icon>
          Lessons
        </v-btn>
      </div>
      <div>
        <v-btn class="mx-1 text-capitalize dbutton" color="#ff8200" style="color: white"
               @click="$router.go(0)">
          <v-icon class="ml-n2 mr-1">mdi-cached</v-icon>
          Try again
        </v-btn>
        <v-btn class="mx-1 text-capitalize dbutton" color="#ff8200" style="color: white"
               @click="$router.push(`/lesson/${next_lesson}`)" :disabled="!next_lesson">
          <v-icon class="ml-n2 mr-1">mdi-chevron-right</v-icon>
          Next lesson
        </v-btn>
      </div>
    </div>
  </v-card>
</template>

<script>

import SpeedBar from '@/components/Editor/SpeedBar.vue';
import AccuracyBar from '@/components/Editor/AccuracyBar.vue';
import { formatTime } from '@/components/Editor/formatTime';
import Stars from '@/components/TextChoose/Stars.vue';

export default {
  name: 'AttemptResult',
  components: { Stars, AccuracyBar, SpeedBar },
  props: ['cpm', 'acc', 'duration', 'score', 'committed', 'lesson_id', 'next_lesson'],
  methods: {
    formatTime() {
      return formatTime(this.duration);
    },
  },
};
</script>

<style>

.dbutton span {
  font-size: 1rem;
  /*color: #00c197;*/
}

</style>
