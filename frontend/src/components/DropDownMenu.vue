<template>
  <v-card class="pa-0 ma-0" style="width: auto; display: inline-block">
    <v-menu
      rounded="lg"
      offset-y
      class="pa-0 ma-0"
    >
      <template v-slot:activator="{ attrs, on }">
        <div>
          <v-btn class="text-capitalize pa-0 ma-0 rounded-0 rounded-l" elevation="0"
                 :color="color" @click="on_click(text)">
            <div class="text-capitalize" :style="`min-width: ${minWidth}`">{{ text }}</div>
          </v-btn>
          <v-btn class="rounded-0 rounded-r pa-0 ma-0" elevation="0" style="min-width: 0;"
                 v-bind="attrs"
                 v-on="on"
                 :color="color">
            <v-icon>mdi-menu-down</v-icon>
          </v-btn>
        </div>
      </template>

      <v-list>
        <v-list-item
          v-for="item in items"
          :key="item"
          @click="on_change(item)"
        >
          <v-list-item-title v-text="item" class="text-capitalize"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

  </v-card>

</template>

<script>
export default {
  name: 'DropDownMenu',
  props: ['text', 'minWidth', 'color', 'items', 'on_change', 'on_click'],

  data: () => ({
    loading: true,
  }),

};
</script>

<style scoped>

</style>
