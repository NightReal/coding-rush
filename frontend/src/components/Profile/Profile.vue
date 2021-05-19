<template>
  <div>
    <page-loader :loading="loading"></page-loader>
    <v-container id="bar-container" style="display: flex; justify-content: center;
                                            max-width: 1277px">

      <div id="left-bar" style="display: flex; width: 100%; word-wrap: break-word;
                                flex-direction: column;">
        <div id="left-bar-info" style="display: flex; width: 100%;">
          <div id="pictureContainer">
            <img class="elevation-5" :src="picture ? picture : defaultPicture"
                 @error="$event.target.src = this.defaultPicture"
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
        <div class="mt-8">
          <v-icon class="mr-1">mdi-laptop</v-icon>
          {{ numberOfCompletedCodes === 0 ? 'no' : numberOfCompletedCodes }} completed
          code{{ numberOfCompletedCodes === 1 ? '' : 's' }}
        </div>
        <v-btn class="mt-11 text-capitalize" style="font-size: 1rem !important; font-weight: 400"
               v-if="$store.getters.isAuthenticated && $store.state.user.username !== undefined &&
                     this.user.toLowerCase() === $store.state.user.username.toLowerCase()"
               @click="$router.push('/settings')">
          Settings
        </v-btn>
      </div>

      <div id="center-bar" class="px-16" style="display: flex; flex-direction: column;
                                  align-items: center; width: 100%">
        <div style="width: 90%; min-width: 350px">
          <Activity class="mt-3" chart-id="activityChart" ref="activity"></Activity>
        </div>
      </div>
    </v-container>

  </div>
</template>

<script>

import APIHelper from '@/api/apihelper';
import Activity from '@/components/Profile/Activity.vue';
import PageLoader from '@/components/PageLoader.vue';
import defaultAvatar from '@/assets/default-avatar-268x268.png';

export default {
  name: 'Profile',
  components: { Activity, PageLoader },
  props: ['user'],
  data() {
    return {
      firstName: '',
      lastName: '',
      username: '',
      picture: defaultAvatar,
      defaultPicture: defaultAvatar,
      loading: true,
      numberOfCompletedCodes: 0,
    };
  },
  methods: {
    // eslint-disable-next-line no-unused-vars
    process_stats(rawData) {
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
    },
  },

  mounted() {
    APIHelper.get(`/account/profile/${this.user}`)
      .then((res) => {
        this.firstName = res.data.first_name;
        this.lastName = res.data.last_name;
        this.username = res.data.username;
        this.picture = res.data.avatar;
        if (this.username !== this.user) {
          this.$router.push(`/profile/${this.username}`);
        }
        if (this.$store.getters.isAuthenticated && !this.$store.getters.user.username) {
          this.$store.dispatch('getUser');
        }
        this.process_stats();
        this.loading = false;
      })
      .catch((e) => {
        if (e.response && e.response.status === 404) {
          this.$router.push('/404');
        } else {
          this.$router.go(0);
        }
      });
  },
};

</script>
<style>

@media all and (min-width: 770px) {
  #left-bar-info {
    flex-direction: column;
  }

  #left-bar {
    flex: 2 0 0;
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

  #left-bar {
    align-items: center;
  }

  #pictureContainer {
    width: 20%;
    min-width: 100px;
    margin-right: 40px
  }

  #left-bar-info {
    align-items: center;
    justify-content: center;
    margin-bottom: 30px;
    flex-direction: row;
  }

  #bar-container {
    flex-direction: column;
  }
}

text {
  font-size: 0.8rem !important;;
}

</style>
