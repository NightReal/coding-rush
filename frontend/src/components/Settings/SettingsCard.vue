<template>
  <v-card class="px-7 pt-4 pb-5 ma-5" style="width: 315px; min-height: 310px;
                                                   display: flex; flex-direction: column">
    <div style="font-weight: 500; font-size: 1.3rem">{{ title }}</div>
    <div style="color: #444444; font-size: 0.9rem">{{ caption }}</div>
    <div>
      <slot></slot>
    </div>
    <div style="flex-grow: 100"></div>
    <ErrorBox class="pa-0 ma-0 mt-1" :message="errorBox" :show="!!errorBox"
              style="min-height: 24px; max-height: 24px"></ErrorBox>
    <div style="display: flex" class="mt-2">
      <v-btn style="flex: 1 1 0;" color="#ff8200" class="mr-2" text
             @click="$emit('cancel')">
        Cancel
      </v-btn>
      <v-btn style="flex: 1 1 0; color: white" color="#ff8200"
             @click="$emit('update')">
        Update
      </v-btn>
    </div>
  </v-card>
</template>

<script>

import ErrorBox from '@/components/ErrorBox.vue';

export default {
  name: 'SettingsCard',
  components: { ErrorBox },
  props: ['title', 'caption', 'errorBox'],
};
</script>

<style scoped>

</style>
