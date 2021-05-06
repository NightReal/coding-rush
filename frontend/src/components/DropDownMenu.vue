<template>
  <v-tooltip top :disabled="!tooltipText">
    <template v-slot:activator="scope">
      <v-card class="pa-0 ma-0" style="width: auto">
        <v-menu
          offset-y
          class="pa-0 ma-0"
          transition="slide-y-transition"
        >
          <template v-slot:activator="{ attrs, on }">
            <div style="display: flex">
              <v-btn class="text-capitalize pa-0 ma-0 rounded-0 rounded-l" elevation="0"
                     :color="color" @click="on_click(text)" v-bind="scope.attrs" v-on="scope.on">
                <div class="text-capitalize" :style="`min-width: ${minWidth}; font-size: 0.95rem`">
                  {{ text }}
                </div>
              </v-btn>
              <v-btn class="rounded-0 rounded-r pa-0 ma-0" elevation="0" style="min-width: 0;"
                     v-bind="attrs"
                     v-on="on"
                     :color="color">
                <v-icon>mdi-menu-down</v-icon>
              </v-btn>
            </div>
          </template>

          <v-list class="pa-0 ma-0">
            <v-list-item
              v-for="item in items"
              :key="item"
              @click="on_change(item)"
            >
              <v-list-item-title v-text="item" style="font-size: 0.95rem"
                                 class="text-capitalize"></v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>

      </v-card>
    </template>
    <span style="font-size: 0.95rem">{{ tooltipText }}</span>
  </v-tooltip>
</template>

<script>

import '@/components/tooltip.css';

export default {
  name: 'DropDownMenu',
  props: ['text', 'minWidth', 'color', 'items', 'on_change', 'on_click', 'tooltipText'],

  data: () => ({
    loading: true,
  }),

};
</script>

<style scoped>

</style>
