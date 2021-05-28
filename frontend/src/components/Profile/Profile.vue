<template>
  <div>
    <page-loader :loading="loadingUser || loadingAttempts"></page-loader>
    <v-container v-if="!loadingUser && !loadingAttempts" id="bar-container" class="mb-8"
                 style="display: flex; justify-content: center; max-width: 1277px">

      <div id="left-bar" style="display: flex; width: 100%; word-wrap: break-word;
                                flex-direction: column;">
        <div id="left-bar-info" style="display: flex; width: 100%;">
          <div id="pictureContainer">
            <img class="elevation-5" :src="picture ? picture : defaultPicture"
                 @error="picture = null"
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
        <v-btn style="font-size: 1.1rem !important; font-weight: 500;
                      color: white" color="#ff8200" class="mt-11 text-capitalize"
               v-if="$store.getters.isAuthenticated && $store.state.user.username !== undefined &&
                     this.user.toLowerCase() === $store.state.user.username.toLowerCase()"
               @click="$router.push('/settings')">
          Settings
        </v-btn>
        <AverageCpmAcc :cpm="averageCpm" :acc="averageAcc" class="mt-7"></AverageCpmAcc>
      </div>

      <div id="center-bar" class="pl-7" style="display: flex; flex-direction: column;
                                  align-items: center; width: 100%">
        <div id="activity-container">
          <Activity class="mt-3" chart-id="activityChart" ref="activity"
                    @ready="activity.ready = true"></Activity>
        </div>
        <PrettyDivider class="mt-10 mb-8" style="max-width: 60px"></PrettyDivider>
        <div id="stats-on-difficulty-container">
          <OnDifficulty :cpm="onDifficulty.cpm" :acc="onDifficulty.acc"
                        :labels="onDifficulty.labels"
                        ref="onDifficulty" @ready="onDifficulty.ready = true"></OnDifficulty>
        </div>
        <PrettyDivider class="mt-16 mb-8" style="max-width: 60px"></PrettyDivider>
        <div id="score-on-topic-container">
          <ScoreOnTopic :data="scoreOnTopic.data" :labels="scoreOnTopic.labels" ref="scoreOnTopic"
                        @ready="scoreOnTopic.ready = true"></ScoreOnTopic>
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
import OnDifficulty from '@/components/Profile/OnDifficulty.vue';
import AverageCpmAcc from '@/components/Profile/AverageCpmAcc.vue';
import ScoreOnTopic from '@/components/Profile/ScoreOnTopic.vue';
import PrettyDivider from '@/components/PrettyDivider.vue';

export default {
  name: 'Profile',
  components: {
    OnDifficulty, Activity, PageLoader, AverageCpmAcc, ScoreOnTopic, PrettyDivider,
  },
  props: ['user'],
  data() {
    return {
      firstName: '',
      lastName: '',
      username: '',
      picture: defaultAvatar,
      defaultPicture: defaultAvatar,
      loadingUser: false,
      loadingAttempts: false,
      numberOfCompletedCodes: 0,
      activity: { data: undefined, ready: false, loaded: false },
      attempts: [],
      best_attempts: [],
      onDifficulty: {
        ready: false,
        loaded: false,
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        cpm: undefined,
        acc: undefined,
      },
      scoreOnTopic: {
        ready: false,
        loaded: false,
        labels: undefined,
        data: undefined,
      },
      averageCpm: 0,
      averageAcc: 0,
    };
  },
  methods: {
    getDay(date) {
      const d = new Date(date);
      let minutes = d.getTime() / 1000 / 60;
      minutes -= d.getTimezoneOffset();
      const dd = Math.floor(minutes / 60 / 24);
      return dd;
    },
    process_best_attempts() {
      const { attempts } = this;
      attempts.sort(
        (a, b) => {
          const scoreA = a.score;
          const scoreB = b.score;
          if (scoreA !== scoreB) {
            return scoreB - scoreA;
          }
          const timeA = new Date(a.date).getTime();
          const timeB = new Date(b.date).getTime();
          return timeA - timeB;
        },
      );
      // eslint-disable-next-line camelcase
      const best_attempts = {};
      // eslint-disable-next-line no-restricted-syntax
      for (const at of attempts) {
        const { id } = at.lesson;
        if (best_attempts[id] === undefined) {
          best_attempts[id] = at;
        }
      }
      this.best_attempts = Object.values(best_attempts);
    },
    process_activity_data() {
      // const attempts = JSON.parse(JSON.stringify(this.attempts));
      this.attempts.sort(
        (a, b) => {
          const timeA = new Date(a.date).getTime();
          const timeB = new Date(b.date).getTime();
          return timeA - timeB;
        },
      );
      const activityData = [];
      let p = this.attempts.length - 1;
      let x = 52;
      const d = new Date();
      let y = (d.getDay() + 6) % 7;
      while (x >= 0) {
        let value = 0;
        const curDay = this.getDay(d);
        while (p >= 0 && this.getDay(this.attempts[p].date) === curDay) {
          p -= 1;
          value += 1;
        }
        activityData.push({
          x, y, value: value + 1, date: new Date(d.getTime()),
        });
        y -= 1;
        d.setDate(d.getDate() - 1);
        if (y < 0) {
          y = 6;
          x -= 1;
        }
      }
      this.activity.data = activityData;
    },
    process_numbers() {
      this.numberOfCompletedCodes = this.best_attempts.length;
      let sumCpm = 0;
      let sumAcc = 0;
      // eslint-disable-next-line no-restricted-syntax
      for (const at of this.best_attempts) {
        sumCpm += at.speed;
        sumAcc += at.accuracy;
      }
      this.averageCpm = Math.round(sumCpm / this.numberOfCompletedCodes);
      this.averageAcc = Math.round(sumAcc / this.numberOfCompletedCodes);
    },
    process_statsOnDiff() {
      const cntDiff = new Array(10).fill(0);
      const cpm = new Array(10).fill(0);
      const acc = new Array(10).fill(0);
      // eslint-disable-next-line no-restricted-syntax
      for (const at of this.best_attempts) {
        const dif = at.lesson.difficulty - 1;
        cntDiff[dif] += 1;
        cpm[dif] += at.speed;
        acc[dif] += at.accuracy;
      }
      for (let i = 0; i < 10; i += 1) {
        if (cntDiff[i] === 0) {
          cpm[i] = 0;
          acc[i] = 0;
        } else {
          cpm[i] = Math.round(cpm[i] / cntDiff[i]);
          acc[i] = Math.round(acc[i] / cntDiff[i]);
        }
      }
      this.onDifficulty.cpm = cpm;
      this.onDifficulty.acc = acc;
    },
    process_scoreOnTopic() {
      const scores = {};
      const counts = {};
      // eslint-disable-next-line no-restricted-syntax
      for (const at of this.best_attempts) {
        const { topic } = at.lesson;
        if (!(topic in scores)) {
          scores[topic] = 0;
          counts[topic] = 0;
        }
        scores[topic] += at.score;
        counts[topic] += 1;
      }
      this.scoreOnTopic.labels = Object.keys(scores);
      const score = [];
      // eslint-disable-next-line no-restricted-syntax
      for (const top of this.scoreOnTopic.labels) {
        const sc = scores[top] / counts[top];
        score.push(Math.round(sc));
      }
      this.scoreOnTopic.data = score;
    },
    process_stats() {
      this.process_best_attempts();
      this.process_activity_data();
      this.process_numbers();
      this.process_statsOnDiff();
      this.process_scoreOnTopic();
    },
    loadUser() {
      if (this.$store.getters.isAuthenticated && this.$store.getters.user.username
        && this.user.toLowerCase() === this.$store.getters.user.username.toLowerCase()) {
        const { user } = this.$store.getters;
        this.firstName = user.first_name;
        this.lastName = user.last_name;
        this.username = user.username;
        this.picture = user.avatar;
        if (this.username !== this.user) {
          this.$router.push(`/profile/${this.username}`);
        }
      } else {
        this.loadingUser = true;
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
            this.loadingUser = false;
          })
          .catch((e) => {
            console.log(e);
            if (e.response && e.response.status === 404) {
              this.$router.push('/404');
            } else {
              this.$router.go(0);
            }
          });
      }
    },
    loadAttempts() {
      this.loadingAttempts = true;
      APIHelper.get(`/lessons/attempts/${this.user}`)
        .then((e) => {
          this.attempts = e.data.attempts;
          this.loadingAttempts = false;
          this.process_stats();
        })
        .catch((e) => {
          console.log(e);
          if (e.response && e.response.status === 404) {
            this.$router.push('/404');
          } else {
            this.$router.go(-1);
          }
        });
    },
  },
  watch: {
    activity: {
      deep: true,
      handler() {
        if (this.activity.data && this.activity.ready && !this.activity.loaded) {
          this.activity.loaded = true;
          this.$refs.activity.updateData(this.activity.data);
        }
      },
    },
    onDifficulty: {
      deep: true,
      handler() {
        if (this.onDifficulty.cpm && this.onDifficulty.acc
          && this.onDifficulty.ready && !this.onDifficulty.loaded) {
          this.onDifficulty.loaded = true;
          this.$refs.onDifficulty.updateData();
        }
      },
    },
    scoreOnTopic: {
      deep: true,
      handler() {
        if (this.scoreOnTopic.data && this.scoreOnTopic.labels
          && this.scoreOnTopic.ready && !this.scoreOnTopic.loaded) {
          this.scoreOnTopic.loaded = true;
          this.$refs.scoreOnTopic.updateData();
        }
      },
    },
  },
  mounted() {
    this.loadUser();
    this.loadAttempts();
  },
};

</script>
<style>

@media all and (min-width: 890px) {
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

  #activity-container {
    width: 700px;
  }

  #stats-on-difficulty-container {
    width: 700px;
    height: 300px;
  }

  #score-on-topic-container {
    width: 650px;
    height: 300px;
  }
}

@media all and (max-width: 889px) {
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

  #activity-container {
    width: 500px;
  }

  #stats-on-difficulty-container {
    width: 500px;
    height: 300px;
  }

  #score-on-topic-container {
    width: 500px;
    height: 300px;
  }
}

text {
  font-size: 0.8rem !important;;
}

</style>
