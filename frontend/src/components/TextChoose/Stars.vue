<template>
  <v-rating
    color="warning"
    empty-icon="mdi-star-outline"
    full-icon="mdi-star"
    half-icon="mdi-star-half-full"
    half-increments
    size="1.7rem"
    length="5"
    readonly
    :value="score / 20"
    dense
  ></v-rating>
</template>

<script>
export default {
  name: 'Stars',
  props: ['score'],
};
</script>

<style scoped>

</style>
