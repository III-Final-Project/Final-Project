<template>
  <div><v-chart class="chart" :option="option" /></div>
</template>

<script>
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { PieChart } from 'echarts/charts';
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  ToolboxComponent,
  DataZoomComponent,
  VisualMapComponent,
  TimelineComponent,
  CalendarComponent,
} from 'echarts/components';
import VChart, { THEME_KEY } from 'vue-echarts';

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  ToolboxComponent,
  DataZoomComponent,
  VisualMapComponent,
  TimelineComponent,
  CalendarComponent,
]);

export default {
  components: {
    VChart,
  },
  provide: {
    [THEME_KEY]: 'white',
  },
  data() {
    return {
      option: {
        title: {
          text: '2021-利潤分析圖',
          left: 'center',
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985',
            },
          },
        },
        legend: {
          padding: [30, 0, 0, 0],
          left: 'right',
          data: ['營業收入', '成本支出', '利潤'],
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true,
        },
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
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
          },
        ],
        yAxis: [
          {
            type: 'value',
          },
        ],
        series: [
          {
            name: '利潤',
            type: 'line',
            stack: '總量',
            areaStyle: {},
            emphasis: {
              focus: 'series',
            },
            data: [],
          },
          {
            name: '成本支出',
            type: 'line',
            stack: '總量',
            areaStyle: {},
            emphasis: {
              focus: 'series',
            },
            data: [320, 332, 301, 334, 390, 330, 320, 450, 500, 350, 450, 600],
          },
          {
            name: '營業收入',
            type: 'line',
            stack: '總量',
            label: {
              show: true,
              position: 'top',
            },
            areaStyle: {},
            emphasis: {
              focus: 'series',
            },
            data: [
              820,
              932,
              901,
              934,
              1290,
              1330,
              1320,
              1220,
              1502,
              1600,
              1302,
              967,
            ],
          },
        ],
      },
    };
  },
  created() {
    for (let i = 0; i < this.option.series[1].data.length; i += 1) {
      this.option.series[0].data.push(
        this.option.series[2].data[i] - this.option.series[1].data[i],
      );
    }
  },
};
</script>

<style scoped>
.chart {
  height: 400px;
  width: 500px;
  position: relative;
}
</style>
