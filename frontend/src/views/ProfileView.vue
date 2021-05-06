<template>
  <div>
    <Profile :user="$route.params.username"/>
  </div>
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
