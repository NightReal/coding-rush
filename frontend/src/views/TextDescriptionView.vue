<template>
  <v-container class="pa-0 mt-8">
    <TextDescription :textid="$route.params.textid"
                     :default_lang="$store.getters.lastUsedLanguage"/>
  </v-container>
</template>

<script>
import TextDescription from '@/components/TextChoose/TextDescription.vue';

export default {
  name: 'TextDescriptionView',
  components: {
    TextDescription,
  },
};
</script>
