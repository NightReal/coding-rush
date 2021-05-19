<template>
  <div style="display: flex; flex-direction: column; align-items: center">
    <div style="display: flex; align-items: center; flex-direction: row; width: 60vw" class="mt-5">
      <h1 class="mr-10">{{ name }}</h1>
      <v-divider></v-divider>
    </div>
    <div style="width: 52vw; display: flex; flex-direction: row; flex-wrap: wrap;
                    align-items: center; justify-content: flex-start" class="slot">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SettingsSection',
  props: ['name'],
};
</script>

<style scoped>

</style>
