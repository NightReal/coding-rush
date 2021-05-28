<template>
  <div style="height: 100%; width: 100%;
              display: flex; flex-direction: column; align-items: center">
    <div style="font-size: 1.3rem; color: #555555">Average Score</div>
    <VerticalBar ref="chart" style="height: 100%; width: 100%"></VerticalBar>
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs';

export default {
  name: 'OnDifficulty',
  components: { VerticalBar: Bar },
  props: ['data', 'labels'],
  data() {
    return {
      chartData: null,
      options: {
        maintainAspectRatio: false,
        scaleShowValues: true,
        legend: {
          display: true,
          labels: {
            fontSize: 14,
          },
        },
        animation: {
          onComplete: () => {
            this.$emit('ready');
          },
        },
        responsive: true,
        interaction: {
          mode: 'index',
          intersect: false,
        },
        tooltips: {
          mode: 'index',
          titleFontSize: 13,
          bodyFontSize: 13,
        },
        stacked: false,
        scales: {
          xAxes: [
            {
              ticks: {
                fontSize: 14,
              },
            }],
          yAxes: [
            {
              display: true,
              type: 'linear',
              position: 'left',
              id: 'score',
              ticks: {
                suggestedMin: 0,
                suggestedMax: 130,
              },
            },
          ],
        },
      },
    };
  },
  methods: {
    updateData() {
      this.chartData.datasets[0].data = this.data;
      this.chartData.labels = this.labels;
      this.$refs.chart.renderChart(this.chartData, this.options);
    },
  },
  mounted() {
    this.chartData = {
      labels: [],
      datasets: [
        {
          label: 'Score',
          borderColor: '#246fbf',
          borderWidth: 1,
          backgroundColor: '#b8d7fc',
          data: [],
          id: 'score',
        }],
    };
    this.$refs.chart.renderChart(this.chartData, this.options);
  },
};
</script>

<style scoped>

</style>
