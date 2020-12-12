<template>
  <v-navigation-drawer class="active" dark
                       v-model="drawer"
                       absolute
                       temporary
                       color="#2b2b2b"
                       @input="$emit('drawer-switched', drawer)">

    <v-list nav dense flat>
      <v-list-item-group mandatory>
        <template v-for="(item, i) in items">
          <v-divider class="mb-1" v-if="item === ''" :key="i"></v-divider>
          <v-list-item v-else
                       @click="item.function(item)"
                       v-bind:class="isActive(item)"
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
</template>

<script>
export default {
  name: 'HeaderNavigationBar',
  data() {
    return {
      drawer: false,
    };
  },
  props: ['parentDrawer', 'items'],
  methods: {
    isActive(item) {
      return item.activating && item.path === this.$router.currentRoute.fullPath
        ? 'active' : false;
    },
  },
  watch: {
    parentDrawer(to) {
      this.drawer = to;
    },
  },
};
</script>
<style scoped>

.active {
  background-color: #d07205;
}

</style>
