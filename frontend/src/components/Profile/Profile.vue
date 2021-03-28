<template>
  <div>
    <v-container id="bar-container" style="display: flex; justify-content: center;
                                            max-width: 1277px">

      <div id="left-bar" style="display: flex;
                                          width: 100%; word-wrap: break-word;">
        <div id="pictureContainer">
          <img class="elevation-5 rounded-circle" :src="picture"
               @error="$event.target.src = defaultPicture"
               style="width: 100%;"/>
        </div>
        <div>
          <div class="font-weight-bold" style="font-size: 1.625rem">
            {{ firstName }} {{ lastName }}
          </div>
          <div class="font-weight-regular" style="color: #666; font-size: 1.3rem">
            {{ username }}
          </div>
        </div>
      </div>

      <div id="center-bar" style="display: flex; flex-direction: column;
                                          align-items: center; width: 100%">
        <v-card flat style="width: 77%" :loading="activityLoading">
          <template slot="progress">
            <v-progress-linear color="accent" indeterminate></v-progress-linear>
          </template>
          <Activity class="mt-3" chart-id="activityChart" ref="activity"></Activity>
        </v-card>
      </div>
    </v-container>

  </div>
</template>

<script>

import Activity from '@/components/Profile/Activity.vue';
import defaultAvatar from '@/assets/default-avatar-268x268.png';

export default {
  name: 'Profile',
  components: { Activity },
  props: ['username'],
  data() {
    return {
      firstName: 'First',
      lastName: 'Lastname',
      picture: defaultAvatar,
      defaultPicture: defaultAvatar,
      activityLoading: true,
    };
  },
  methods: {
    process_stats() {
      const data = (() => {
        const arr = [];
        let x = 52;
        const d = new Date();
        let y = (d.getDay() + 6) % 7;
        while (x >= 0) {
          let value = Math.floor((Math.random() ** 8) * 10);
          value = Math.max(value, 0);
          arr.push({
            x, y, value: value + 1, date: new Date(d.getTime()),
          });
          y -= 1;
          d.setDate(d.getDate() - 1);
          if (y < 0) {
            y = 6;
            x -= 1;
          }
        }
        return arr;
      })();

      this.$refs.activity.updateData(data);
      this.activityLoading = false;
    },
  },
  mounted() {
    // load info
    setTimeout(this.process_stats, 1000);
  },
};

</script>
<style>

@media all and (min-width: 770px) {
  #left-bar {
    flex: 2 0 0;
    flex-direction: column;
  }

  #center-bar {
    flex: 7 0 0;
  }

  #bar-container {
    flex-direction: row;
  }

  #pictureContainer {
    margin-bottom: 20px;
  }
}

@media all and (max-width: 769px) {
  #left-bar, #center-bar {
    flex: 1 100%;
  }

  #pictureContainer {
    width: 20%;
    margin-right: 40px
  }

  #left-bar {
    align-items: center;
    justify-content: center;
    margin-bottom: 30px;
    flex-direction: row;
  }

  #bar-container {
    flex-direction: column;
  }
}

</style>
