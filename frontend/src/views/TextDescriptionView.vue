<template>
  <div>
    <TextDescription :textid="$route.params.textid"
                     :default_lang="$store.getters.lastUsedLanguage"/>
  </div>
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
