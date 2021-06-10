<template>
  <div><v-chart class="chart" :option="option" /></div>
</template>

<script>
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { BarChart, LineChart } from 'echarts/charts';
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
} from 'echarts/components';
import VChart from 'vue-echarts';

use([
  CanvasRenderer,
  BarChart,
  LineChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
]);

export default {
  components: {
    VChart,
  },
  data() {
    return {
      option: {
        title: {
          text: '2021-人數總計(By Gender)',
          left: 'center',
          textStyle: {
            color: '#708069',
          },
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            crossStyle: {
              color: '#999',
            },
          },
        },
        legend: {
          orient: 'vertical',
          left: 'right',
          top: '15%',
          data: ['男性', '女性', '平均總人數'],
        },
        xAxis: [
          {
            type: 'category',
            data: [
              '1月',
              '2月',
              '3月',
              '4月',
              '5月',
              '6月',
              '7月',
              '8月',
              '9月',
              '10月',
              '11月',
              '12月',
            ],
            axisPointer: {
              type: 'shadow',
            },
          },
        ],
        yAxis: [
          {
            type: 'value',
            name: '總人數',
            min: 0,
            max: 500,
            interval: 100,
            axisLabel: {
              formatter: '{value} ',
            },
          },
        ],
        series: [
          {
            name: '男性',
            type: 'bar',
            data: [],
          },
          {
            name: '女性',
            type: 'bar',
            data: [],
            color: 'pink',
          },
          {
            name: '平均總人數',
            type: 'line',
            data: [],
            color: 'gray',
          },
        ],
      },
    };
  },
  created() {
    this.dataSeries();
  },
  methods: {
    dataSeries() {
      // male array
      this.option.series[0].data = [
        100,
        150,
        120,
        160,
        170,
        230,
        300,
        400,
        367,
        160,
        230,
        320,
      ];
      // female array
      this.option.series[1].data = [
        100,
        100,
        175,
        205,
        120,
        169,
        230,
        340,
        236,
        270,
        180,
        250,
      ];
      // average
      for (let i = 0; i < 12; i += 1) {
        this.option.series[2].data.push(
          (this.option.series[0].data[i] + this.option.series[0].data[2]) / 2,
        );
      }
    },
  },
};
</script>

<style scoped>
.chart {
  height: 400px;
  width: 500px;
  position: relative;
  margin: 0 auto;
}
</style>
