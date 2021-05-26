<template>
  <v-card v-if="show" flat outlined
          style="display: flex; align-items: center;"
          :style="`border-color: ${getBorderColor()}; background-color: ${getBgColor()}`">
    <v-container class="caption py-0 px-2">
      {{ formatMessage() }}
    </v-container>
  </v-card>
  <v-container v-else class="pa-0"></v-container>
</template>

<script>
export default {
  name: 'ErrorBox',
  props: ['message', 'show'],

  methods: {
    formatMessage() {
      return this.message && this.message[0] === '!'
        ? this.message.substring(1)
        : this.message;
    },
    getBorderColor() {
      return this.message && this.message[0] === '!'
        ? '#6fcc55'
        : '#cc5555';
    },
    getBgColor() {
      return this.message && this.message[0] === '!'
        ? '#e7ffe6'
        : '#ffe6e6';
    },
  },
};
</script>
