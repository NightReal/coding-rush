<template>
  <v-container class="pa-0 ma-4">
    <v-hover v-slot="{ hover }" v-if="!hide">
      <v-card width="220px" height="220px" style="padding: 15px" class="text-card"
              :elevation="hover ? 5 : 2" @click="$router.push(`/text/${text.id}`)">
        <div style="width: 100%; display: flex; flex-direction: column; align-items: center;
                  font-size: 1.3rem; text-align: center; justify-content: space-between;
                  font-family: monospace; font-style: normal; overflow-wrap: anywhere;">
          {{ text.title }}
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
};
</script>

<style scoped>

</style>
