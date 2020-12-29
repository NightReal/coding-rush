<template>
  <v-footer absolute>
      <v-col class="text-center" cols="200">
        © {{ new Date().getFullYear() }} <span class="font-weight-medium">Coding Rush</span>
      </v-col>
    </v-footer>
</template>

<script>
export default {
  name: 'Footer',
};
</script>
