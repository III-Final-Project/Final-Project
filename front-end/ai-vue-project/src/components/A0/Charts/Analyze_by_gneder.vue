<template>
  <div>
    <v-chart class="chart" :option="option" />
  </div>
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
  props: ['myData'],
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
            // max: 15,
            interval: 5,
            axisLabel: {
              formatter: '{value} ',
            },
          },
        ],
        series: [
          {
            name: '男性',
            type: 'bar',
            data: new Array(12),
          },
          {
            name: '女性',
            type: 'bar',
            data: new Array(12),
            color: 'pink',
          },
          {
            name: '平均總人數',
            type: 'line',
            data: new Array(12),
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
      // 建立12x1的array Array(0)表示空陣列
      const maleArrayByMonth = Array.from(Array(12), () => new Array(0));
      const femaleArrayByMonth = Array.from(Array(12), () => new Array(0));
      this.myData.forEach((element) => {
        const customerMonth = element.customer_time.substring(5, 7);
        if (element.customer_sex === 'male') {
          maleArrayByMonth[parseInt(customerMonth, 10) - 1].push(element);
        } else {
          femaleArrayByMonth[parseInt(customerMonth, 10) - 1].push(element);
        }
      });
      // data array
      for (let i = 0; i < 12; i += 1) {
        this.option.series[0].data[i] = maleArrayByMonth[i].length;
        this.option.series[1].data[i] = femaleArrayByMonth[i].length;
        this.option.series[2].data[i] =
          (maleArrayByMonth[i].length + femaleArrayByMonth[i].length) / 2;
      }
    },
  },
};
</script>

<style scoped>
.chart {
  height: 600px;
  width: 800px;
  position: relative;
  margin: 0 auto;
}
</style>
