<template>
  <div style="height: 100%; width: 100%;
              display: flex; flex-direction: column; align-items: center">
    <div style="font-size: 1.3rem; color: #555555">Average Speed and Accuracy</div>
    <LineChart ref="chart" style="height: 100%; width: 100%"></LineChart>
  </div>
</template>

<script>
import { Line } from 'vue-chartjs';

export default {
  name: 'OnDifficulty',
  components: { LineChart: Line },
  props: ['cpm', 'acc', 'labels'],
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
          callbacks: {
            label(context) {
              let label = (context.datasetIndex === 0) ? 'Speed: ' : 'Accuracy: ';
              label += context.yLabel;
              label += (context.datasetIndex === 0) ? ' cpm' : '%';
              return label;
            },
            title(tooltipItems) {
              let label = 'Difficulty: ';
              label += tooltipItems[0].xLabel;
              return label;
            },
          },
          titleFontSize: 13,
          bodyFontSize: 13,
        },
        stacked: false,
        scales: {
          xAxes: [
            {
              scaleLabel: {
                display: true,
                labelString: 'Difficulty',
                fontSize: 14,
              },
            }],
          yAxes: [
            {
              display: true,
              type: 'linear',
              position: 'left',
              id: 'cpm',
              ticks: {
                suggestedMin: 0,
                suggestedMax: 400,
              },
              scaleLabel: {
                display: true,
                labelString: 'Speed - CPM',
                fontSize: 14,
              },
              gridLines: {
                display: false,
              },
            },
            {
              display: true,
              type: 'linear',
              position: 'right',
              id: 'acc',
              ticks: {
                suggestedMin: 0,
                suggestedMax: 100,
              },
              scaleLabel: {
                display: true,
                labelString: 'Accuracy %',
                fontSize: 14,
              },
            },
          ],
        },
      },
    };
  },
  methods: {
    updateData() {
      this.chartData.datasets[0].data = this.cpm;
      this.chartData.datasets[1].data = this.acc;
      this.$refs.chart.renderChart(this.chartData, this.options);
    },
  },
  mounted() {
    this.chartData = {
      labels: this.labels,
      datasets: [
        {
          label: 'Speed',
          borderColor: '#4dbf24',
          pointBackgroundColor: '#4dbf24',
          pointBorderColor: '#4dbf24',
          pointRadius: 2.5,
          borderWidth: 1,
          backgroundColor: 'transparent',
          yAxisID: 'cpm',
          data: [],
        },
        {
          label: 'Accuracy',
          borderColor: '#bf2424',
          pointBackgroundColor: '#bf2424',
          pointBorderColor: '#bf2424',
          pointRadius: 2.5,
          borderWidth: 1,
          backgroundColor: 'transparent',
          yAxisID: 'acc',
          data: [],
        }],
    };
    this.$refs.chart.renderChart(this.chartData, this.options);
  },
};
</script>

<style scoped>

</style>
