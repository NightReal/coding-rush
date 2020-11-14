<template>
  <v-component>
  <v-app-bar app color="primary" dark>
    <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
    <v-toolbar-title>Coding Rush</v-toolbar-title>
  </v-app-bar>

  <v-navigation-drawer
    v-model="drawer"
    absolute
    temporary>

    <v-list nav dense>
      <v-list-item-group
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item href="/">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item href="/editor">
            <v-list-item-icon>
              <v-icon>mdi-keyboard</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Type</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-component>
</template>

<script>
export default {
  name: 'Header',

  data: () => ({
    drawer: false,
  }),
};
</script>

<style scoped>
#Title {
  font-size: 22px;
}
</style>
