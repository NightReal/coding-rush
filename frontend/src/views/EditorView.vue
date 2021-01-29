<template>
  <!-- <img src="./assets/logo.png"> -->
  <v-container>
    <Editor :textProp="text" :textNameProp="textName"></Editor>
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
      text: '#include <bits/stdc++.h>\nusing namespace std;\n\n\nint main() {\n    ios_base::sync_with_stdio(0);\n    cin.tie(0);\n    cout.tie(0);\n    int n;\n    cin >> n;\n    return 0;\n}\n',
      textName: 'First step - Hello, world!',
    };
  },
};
</script>

