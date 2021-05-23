<template>
  <div style="height: 100%; width: 100%;
              display: flex; flex-direction: column; align-items: center">
    <div style="font-size: 1.3rem; color: #555555">User Activity</div>
    <div :id="chartId" class="activity-chart" style="width: 100%" :ref="chartId"></div>
  </div>
</template>

<script>

import Highcharts from 'highcharts';
import heatmap from 'highcharts/modules/heatmap';

heatmap(Highcharts);

export default {
  name: 'Activity',
  props: ['chartId'],
  data() {
    return {
      chart: undefined,
      chartWidth: undefined,
      options: undefined,
      emptyData: undefined,
      chartData: undefined,
    };
  },
  mounted() {
    this.createEmptyData();
    const data = this.chartData ? this.chartData : this.emptyData;
    this.options = {
      chart: {
        type: 'heatmap',
        renderTo: this.chartId,
        marginTop: 0,
        marginBottom: 0,
        plotBorderWidth: 0,
        height: '13.2%',
      },

      credits: false,
      title: false,

      xAxis: {
        gridLineWidth: 0,
        lineWidth: 0,
        categories: Array(53).fill(''),
      },
      yAxis: {
        gridLineWidth: 0,
        lineWidth: 0,
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        title: null,
        reversed: true,
      },
      colorAxis: {
        min: 1,
        max: 21,
        type: 'logarithmic',
        stops: [
          [0, '#fff0e1'],
          [0.15, '#ffdcbb'],
          [0.5, '#ff8200'],
          [1, '#e04600'],
        ],
      },

      legend: false,

      tooltip: {
        borderWidth: 0,
        formatter() {
          const dt = this.point.date;
          const day = dt.getDate().toString().padStart(2, '0');
          const mon = (dt.getMonth() + 1).toString().padStart(2, '0');
          const year = dt.getFullYear().toString();
          const val = this.point.value - 1;
          const sval = val === 0 ? 'no' : val.toString();
          const code = val === 1 ? 'code' : 'codes';
          return `${day}.${mon}.${year}<br><b>${sval}</b> typed ${code}</b>`;
        },
      },

      series: [
        {
          name: 'User activity',
          borderWidth: 2,
          borderColor: '#ffffff',
          data,
        }],
    };
    this.chart = new Highcharts.Chart(this.options);
    this.resizeEvent();
  },
  watch: {
    chart() {
      this.$emit('ready');
    },
  },
  created() {
    window.addEventListener('resize', this.resizeEvent);
  },
  destroyed() {
    window.removeEventListener('resize', this.resizeEvent);
  },
  methods: {
    createEmptyData() {
      this.emptyData = [];
      let x = 52;
      const d = new Date();
      let y = (d.getDay() + 6) % 7;
      while (x >= 0) {
        this.emptyData.push({
          x, y, value: 1, date: new Date(d.getTime()),
        });
        d.setDate(d.getDate() - 1);
        y -= 1;
        if (y < 0) {
          y = 6;
          x -= 1;
        }
      }
    },
    resizeEvent() {
      const newWidth = this.$refs[this.chartId].clientWidth;
      if (this.chartWidth === undefined || (this.chartWidth >= 666) !== (newWidth >= 666)) {
        this.chart.series[0].update({ borderWidth: newWidth >= 666 ? 2 : 1 });
      }
      this.chartWidth = newWidth;
    },
    updateData(newData) {
      this.chartData = newData;
      const data = this.chartData ? this.chartData : this.emptyData;
      this.chart.series[0].setData(data);
    },
  },

};

</script>
<style>

.activity-chart {
  overflow: visible !important;
}

</style>
