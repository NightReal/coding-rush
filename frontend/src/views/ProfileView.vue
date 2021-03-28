<template>
  <v-container class="pa-0 mt-8">
    <Profile :username="$route.params.username"/>
  </v-container>
</template>

<script>
import Profile from '@/components/Profile/Profile.vue';

export default {
  name: 'ProfileView',
  components: {
    Profile,
  },
};
</script>
