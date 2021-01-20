<template>
  <v-footer id="footer">
    <v-col class="pa-0 ma-0 text-center">
      BIG FOOTER<br>idk<br>some information<br>more information<br>mb contacts<br>about?<br>
      terms of use<br>something more<br>good luck!<br><br>
      {{ new Date().getFullYear() }} — <strong>Coding Rush</strong>
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
  height: 280px;
  align-items: center;
  font-size: 0.93rem;
}

</style>
