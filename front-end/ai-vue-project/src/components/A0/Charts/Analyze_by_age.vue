<template>
  <div class="chart"><v-chart :option="option" /></div>
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
          text: '2021-人數總計(By Age)',
          left: 'center',
          textStyle: {
            color: '#708069',
          },
        },
        tooltip: {
          //   trigger: 'axis',
          axisPointer: {
            type: 'line',
          },
        },
        legend: {
          top: '8%',
          left: '10%',
          data: ['10-20', '20-30', '30-40', '40-50', '50-60'],
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true,
        },
        xAxis: {
          name: '總人數',
          nameLocation: 'middle',
          nameTextStyle: { padding: [7, 0, 0, 0] },
          type: 'value',
        },
        yAxis: {
          type: 'category',
          data: ['Q1', 'Q2', 'Q3', 'Q4'],
        },
        series: [
          {
            name: '10-20',
            type: 'bar',
            stack: 'total',
            label: {
              show: true,
            },
            emphasis: {
              focus: 'series',
            },
            data: [320, 302, 301, 334],
          },
          {
            name: '20-30',
            type: 'bar',
            stack: 'total',
            label: {
              show: true,
            },
            emphasis: {
              focus: 'series',
            },
            data: [100, 350, 101, 145],
          },
          {
            name: '30-40',
            type: 'bar',
            stack: 'total',
            label: {
              show: true,
            },
            emphasis: {
              focus: 'series',
            },
            data: [220, 182, 191, 234],
          },
          {
            name: '40-50',
            type: 'bar',
            stack: 'total',
            label: {
              show: true,
            },
            emphasis: {
              focus: 'series',
            },
            data: [150, 212, 201, 154],
          },
          {
            name: '50-60',
            type: 'bar',
            stack: 'total',
            label: {
              show: true,
            },
            emphasis: {
              focus: 'series',
            },
            data: [820, 832, 901, 934],
          },
        ],
      },
    };
  },
};
</script>

<style scoped>
.chart {
  height: 450px;
  width: 550px;
  position: relative;
}
</style>
