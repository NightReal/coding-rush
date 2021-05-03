<template>
  <!-- <img src="./assets/logo.png"> -->
  <v-container>
    <Editor :targetTextProp="text" :textNameProp="textName"></Editor>
  </v-container>
</template>

<script>
import Editor from '@/components/Editor.vue';

export default {
  name: 'EditorView',
  components: {
    Editor,
  },
  data() {
    return {
      text: '#include <bits/stdc++.h>\nusing namespace std;\n\n\nint main() {\n\tios_base::sync_with_stdio(0);\n\tcin.tie(0);\n\tcout.tie(0);\n\tint n;\n\tcin >> n;\n\treturn 0;\n}\n#include <bits/stdc++.h>\nusing namespace std;\n\n\nint main() {\n\tios_base::sync_with_stdio(0);\n\tcin.tie(0);\n\tcout.tie(0);\n\tint n;\n\tcin >> n;\n\treturn 0;\n}',
      textName: 'First step - Hello, world!',
    };
  },
};
</script>
