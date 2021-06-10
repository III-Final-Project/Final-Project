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
  props: ['myData'],
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
            data: [],
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
            data: [],
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
            data: [],
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
            data: [],
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
            data: [],
          },
        ],
      },
    };
  },
  mounted() {
    this.setDatas();
  },
  methods: {
    setDatas() {
      const dataArray = Array.from(Array(5), () => new Array(0));
      // 先分年齡層
      this.myData.forEach((element) => {
        if (element.customer_age < 20) {
          dataArray[0].push(element);
        } else if (element.customer_age < 30) {
          dataArray[1].push(element);
        } else if (element.customer_age < 40) {
          dataArray[2].push(element);
        } else if (element.customer_age < 50) {
          dataArray[3].push(element);
        } else {
          dataArray[4].push(element);
        }
      });
      // 接著分季節(Q1,Q2,Q3,Q4)
      const under20 = [[], [], [], []];
      const under30 = [[], [], [], []];
      const under40 = [[], [], [], []];
      const under50 = [[], [], [], []];
      const under60 = [[], [], [], []];
      for (let i = 0; i < dataArray.length; i += 1) {
        // eslint-disable-next-line no-loop-func
        dataArray[0].forEach((element) => {
          const customerMonth = parseInt(
            element.customer_time.substring(5, 7),
            10,
          );
          if (customerMonth < 4) {
            under20[0].push(element);
          } else if (customerMonth < 7) {
            under20[1].push(element);
          } else if (customerMonth < 10) {
            under20[2].push(element);
          } else {
            under20[3].push(element);
          }
        });
        dataArray[1].forEach((element) => {
          const customerMonth = parseInt(
            element.customer_time.substring(5, 7),
            10,
          );
          if (customerMonth < 4) {
            under30[0].push(element);
          } else if (customerMonth < 7) {
            under30[1].push(element);
          } else if (customerMonth < 10) {
            under30[2].push(element);
          } else {
            under30[3].push(element);
          }
        });
        dataArray[2].forEach((element) => {
          const customerMonth = parseInt(
            element.customer_time.substring(5, 7),
            10,
          );
          if (customerMonth < 4) {
            under40[0].push(element);
          } else if (customerMonth < 7) {
            under40[1].push(element);
          } else if (customerMonth < 10) {
            under40[2].push(element);
          } else {
            under40[3].push(element);
          }
        });
        dataArray[3].forEach((element) => {
          const customerMonth = parseInt(
            element.customer_time.substring(5, 7),
            10,
          );
          if (customerMonth < 4) {
            under50[0].push(element);
          } else if (customerMonth < 7) {
            under50[1].push(element);
          } else if (customerMonth < 10) {
            under50[2].push(element);
          } else {
            under50[3].push(element);
          }
        });
        dataArray[4].forEach((element) => {
          const customerMonth = parseInt(
            element.customer_time.substring(5, 7),
            10,
          );
          if (customerMonth < 4) {
            under60[0].push(element);
          } else if (customerMonth < 7) {
            under60[1].push(element);
          } else if (customerMonth < 10) {
            under60[2].push(element);
          } else {
            under60[3].push(element);
          }
        });
        for (let x = 0; x < 4; x += 1) {
          this.option.series[0].data.push(under20[x].length);
          this.option.series[1].data.push(under30[x].length);
          this.option.series[2].data.push(under40[x].length);
          this.option.series[3].data.push(under50[x].length);
          this.option.series[4].data.push(under60[x].length);
        }
      }
    },
  },
};
</script>

<style scoped>
.chart {
  height: 450px;
  width: 550px;
  position: relative;
  margin: 0 auto;
}
</style>
