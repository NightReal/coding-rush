<template>
  <v-container class="pa-0 ma-0">
    <v-sheet class="pa-0 ma-0" id="big-header" elevation="4" color="primary" dark>
      <div id="header-content">
        <div style="font-size: 3rem">OwO</div>
      </div>
      <v-img id="header-logo" transition="scroll-x-transition"
             src="@/assets/logo-430x430.png"></v-img>
    </v-sheet>
    <v-container style="height: 1100px; margin-top: 180px; padding-left: 30px">
      <br>dummy
    </v-container>
  </v-container>
</template>

<script>

export default {
  name: 'Main',
  data() {
    return {
      isActive: false,
      show: true,
    };
  },
  methods: {
    kek() {
      console.log('kek');
    },
  },
};
</script>
<style scoped>

#big-header {
  height: 700px;
  min-width: 100vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#header-content {
  align-self: center;
  flex-grow: 100;
  display: flex;
  align-items: center;
}

#header-logo {
  max-width: 430px;
  margin-left: 150px;
  margin-bottom: -170px;
  justify-self: flex-end;
}

</style>
