<template>
  <v-card v-if="show" flat outlined style="border-color: #cc5555; background-color: #ffe6e6;
                                           display: flex; align-items: center;">
    <v-container class="caption py-0 px-2">
      {{ message }}
    </v-container>
  </v-card>
  <v-container v-else class="pa-0"></v-container>
</template>

<script>
export default {
  name: 'ErrorBox',
  props: ['message', 'show'],
};
</script>
