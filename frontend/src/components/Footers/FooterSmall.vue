<template>
  <v-footer id="footer">
    <v-col class="pa-0 ma-0 text-center">
      © {{ new Date().getFullYear() }} <span class="font-weight-medium">Coding Rush</span>
    </v-col>
  </v-footer>
</template>

<script>
export default {
  name: 'Footer',
};
</script>

<style scoped>

#footer {
  height: 45px;
  align-items: center;
  font-size: 0.93rem;
}

</style>
