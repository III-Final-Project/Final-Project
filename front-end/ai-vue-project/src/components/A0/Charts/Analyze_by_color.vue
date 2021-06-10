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
          left: 'center',
          text: '推薦商品分析圖(By color)',
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow',
          },
        },
        legend: {
          padding: [35, 0, 0, 0],
          data: ['藍色', '綠色', '粉色', '黃色', '淡紫色'],
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true,
        },
        xAxis: {
          name: '數量',
          nameLocation: 'middle',
          nameGap: '15',
          type: 'value',
          boundaryGap: [0, 0.01],
        },
        yAxis: {
          name: '商品種類',
          type: 'category',
          data: ['衣服', '褲子', '內衣褲', '鞋子', '帽子'],
        },
        series: [
          {
            name: '藍色',
            type: 'bar',
            color: '#87ceeb',
            data: [200, 100, 50, 35, 150],
          },
          {
            name: '綠色',
            type: 'bar',
            color: '#66cdaa',
            data: [240, 160, 230, 60, 140],
          },
          {
            name: '粉色',
            type: 'bar',
            color: '#ffe4e1',
            data: [179, 240, 130, 90, 140],
          },
          {
            name: '黃色',
            type: 'bar',
            color: '#f0e68c',
            data: [100, 120, 90, 165, 130],
          },
          {
            name: '淡紫色',
            type: 'bar',
            color: '#e6e6fa',
            data: [160, 180, 210, 145, 132],
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
  margin: 0 auto;
}
</style>
