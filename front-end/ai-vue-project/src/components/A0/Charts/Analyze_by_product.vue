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
        color: ['#03A89E', '#00BBFF', '#FF8888', '#FFBB66', '#9999FF'],
        title: {
          text: '2021-商品售出比例圖(By product)',
          left: 'center',
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)',
        },
        legend: {
          // orient: 'vertical',
          padding: [50, 0, 0, 0],
          left: 'center',
          data: ['衣服', '褲子', '鞋子', '內衣褲', '帽子'],
        },
        series: [
          {
            name: '商品種類',
            type: 'pie',
            radius: '70%',
            center: ['50%', '60%'],
            data: [
              { value: 500, name: '衣服' },
              { value: 310, name: '褲子' },
              { value: 234, name: '鞋子' },
              { value: 135, name: '內衣褲' },
              { value: 350, name: '帽子' },
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
  width: 600px;
  position: relative;
}
</style>
