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
  name: 'Pie',
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
          text: 'Customer Analysis',
          left: 'center',
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)',
        },
        legend: {
          orient: 'vertical',
          left: 'left',
          data: ['Clothes', 'Pants', 'Shoes', 'Underwear', 'Hats'],
        },
        series: [
          {
            name: 'Customer Sources',
            type: 'pie',
            radius: '70%',
            center: ['50%', '60%'],
            data: [
              { value: 335, name: 'Clothes' },
              { value: 310, name: 'Pants' },
              { value: 234, name: 'Shoes' },
              { value: 135, name: 'Underwear' },
              { value: 1548, name: 'Hats' },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
              },
            },
          },
        ],
      },
    };
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
