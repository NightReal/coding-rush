<template>
  <div>
    <v-hover v-slot="{ hover }">
      <v-card width="200px" height="200px" style="padding: 15px" class="text-card"
              :elevation="hover ? 5 : 2" @click="$router.push(`/text/${text.id}`)">
        <div style="width: 100%; display: flex; flex-direction: column; align-items: center;
                  font-size: 1.3rem; text-align: center; justify-content: space-between;
                  font-family: monospace; font-style: normal; overflow-wrap: anywhere;">
          {{ text.title }}
        </div>
      </v-card>
    </v-hover>
  </div>
</template>

<script>
export default {
  name: 'TextCard',
  props: ['text'],
};
</script>

<style scoped>

</style>
