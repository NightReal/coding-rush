<template>
  <v-container>
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-toolbar-title>Coding Rush</v-toolbar-title>

    </v-app-bar>

    <v-navigation-drawer class="active" dark
                         v-model="drawer"
                         absolute
                         temporary
                         color="#2b2b2b">

      <v-list nav dense flat>
        <v-list-item-group mandatory>
          <template v-for="(item, i) in items">
            <v-divider class="mb-1" v-if="item === ''" :key="i"></v-divider>
            <v-list-item v-else
                         @click="item.text !== 'Close' ? goto(item.path) : drawer = false"
                         v-bind:class="isActive(item.path)"
                         :key="i">
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>
              <v-list-item-title>{{ item.text }}</v-list-item-title>
            </v-list-item>
          </template>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-container>

</template>

<script>

export default {
  name: 'Header',

  data() {
    return {
      drawer: false,
      items: [
        {
          text: 'Close',
          icon: 'mdi-close',
        },
        '',
        {
          text: 'Home',
          path: '/',
          icon: 'mdi-home',
        },
        {
          text: 'Typing',
          path: '/editor',
          icon: 'mdi-keyboard',
        },
      ],
    };
  },
  methods: {
    isActive(path) {
      return path === this.$router.currentRoute.path ? 'active' : false;
    },
    goto(route) {
      this.$router.push(route).catch((e) => e);
    },
  },
};
</script>

<style scoped>
#Title {
  font-size: 22px;
}

.active {
  background-color: #d07205;
}

</style>
