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
  props: ['myData'],
  data() {
    return {
      option: {
        title: {
          left: 'center',
          text: '2021-推薦商品分析圖(By color)',
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow',
          },
        },
        legend: {
          padding: [35, 0, 0, 0],
          data: ['紅色', '橙色', '黃色', '綠色', '藍色', '紫色'],
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
          data: ['上衣', '襯衫', '外套、大衣', '褲款', '裙款', '洋裝', '帽款'],
        },
        series: [
          {
            name: '紅色',
            type: 'bar',
            color: '#FF8888',
            data: [],
          },
          {
            name: '橙色',
            type: 'bar',
            color: '#FFBB66',
            data: [],
          },
          {
            name: '黃色',
            type: 'bar',
            color: '#EEEE00',
            data: [],
          },
          {
            name: '綠色',
            type: 'bar',
            color: '#03A89E',
            data: [],
          },
          {
            name: '藍色',
            type: 'bar',
            color: '#5599FF',
            data: [],
          },
          {
            name: '紫色',
            type: 'bar',
            color: '#9999FF',
            data: [],
          },
        ],
      },
    };
  },
  created() {
    this.setDatas();
  },
  methods: {
    setDatas() {
      const colorArray = Array.from(Array(6), () => new Array(0));
      this.myData.forEach((element) => {
        if (element.customer_recommend_color === 'red') {
          colorArray[0].push(element);
        } else if (element.customer_recommend_color === 'orange') {
          colorArray[1].push(element);
        } else if (element.customer_recommend_color === 'yellow') {
          colorArray[2].push(element);
        } else if (element.customer_recommend_color === 'green') {
          colorArray[3].push(element);
        } else if (
          element.customer_recommend_color === 'blue' ||
          element.customer_recommend_color === 'indigo'
        ) {
          colorArray[4].push(element);
        } else {
          colorArray[5].push(element);
        }
      });
      const redArray = Array.from(Array(7), () => new Array(0));
      colorArray[0].forEach((element) => {
        const category = this.categoryClassified(
          element.customer_recommend_product,
        );
        if (category === '上衣') {
          redArray[0].push(element);
        } else if (category === '襯衫') {
          redArray[1].push(element);
        } else if (category === '褲款') {
          redArray[2].push(element);
        } else if (category === '外套、大衣') {
          redArray[3].push(element);
        } else if (category === '裙款') {
          redArray[4].push(element);
        } else if (category === '洋裝') {
          redArray[5].push(element);
        } else {
          redArray[6].push(element);
        }
      });
      const orangeArray = Array.from(Array(7), () => new Array(0));
      colorArray[1].forEach((element) => {
        const category = this.categoryClassified(
          element.customer_recommend_product,
        );
        if (category === '上衣') {
          orangeArray[0].push(element);
        } else if (category === '襯衫') {
          orangeArray[1].push(element);
        } else if (category === '褲款') {
          orangeArray[2].push(element);
        } else if (category === '外套、大衣') {
          orangeArray[3].push(element);
        } else if (category === '裙款') {
          orangeArray[4].push(element);
        } else if (category === '洋裝') {
          orangeArray[5].push(element);
        } else {
          orangeArray[6].push(element);
        }
      });
      const yellowArray = Array.from(Array(7), () => new Array(0));
      colorArray[2].forEach((element) => {
        const category = this.categoryClassified(
          element.customer_recommend_product,
        );
        if (category === '上衣') {
          yellowArray[0].push(element);
        } else if (category === '襯衫') {
          yellowArray[1].push(element);
        } else if (category === '褲款') {
          yellowArray[2].push(element);
        } else if (category === '外套、大衣') {
          yellowArray[3].push(element);
        } else if (category === '裙款') {
          yellowArray[4].push(element);
        } else if (category === '洋裝') {
          yellowArray[5].push(element);
        } else {
          yellowArray[6].push(element);
        }
      });
      const greenArray = Array.from(Array(7), () => new Array(0));
      colorArray[3].forEach((element) => {
        const category = this.categoryClassified(
          element.customer_recommend_product,
        );
        if (category === '上衣') {
          greenArray[0].push(element);
        } else if (category === '襯衫') {
          greenArray[1].push(element);
        } else if (category === '褲款') {
          greenArray[2].push(element);
        } else if (category === '外套、大衣') {
          greenArray[3].push(element);
        } else if (category === '裙款') {
          greenArray[4].push(element);
        } else if (category === '洋裝') {
          greenArray[5].push(element);
        } else {
          greenArray[6].push(element);
        }
      });
      const blueArray = Array.from(Array(7), () => new Array(0));
      colorArray[4].forEach((element) => {
        const category = this.categoryClassified(
          element.customer_recommend_product,
        );
        if (category === '上衣') {
          blueArray[0].push(element);
        } else if (category === '襯衫') {
          blueArray[1].push(element);
        } else if (category === '褲款') {
          blueArray[2].push(element);
        } else if (category === '外套、大衣') {
          blueArray[3].push(element);
        } else if (category === '裙款') {
          blueArray[4].push(element);
        } else if (category === '洋裝') {
          blueArray[5].push(element);
        } else {
          blueArray[6].push(element);
        }
      });
      const purpleArray = Array.from(Array(7), () => new Array(0));
      colorArray[5].forEach((element) => {
        const category = this.categoryClassified(
          element.customer_recommend_product,
        );
        if (category === '上衣') {
          purpleArray[0].push(element);
        } else if (category === '襯衫') {
          purpleArray[1].push(element);
        } else if (category === '褲款') {
          purpleArray[2].push(element);
        } else if (category === '外套、大衣') {
          purpleArray[3].push(element);
        } else if (category === '裙款') {
          purpleArray[4].push(element);
        } else if (category === '洋裝') {
          purpleArray[5].push(element);
        } else {
          purpleArray[6].push(element);
        }
      });
      for (let x = 0; x < redArray.length; x += 1) {
        this.option.series[0].data.push(redArray[x].length);
        this.option.series[1].data.push(orangeArray[x].length);
        this.option.series[2].data.push(yellowArray[x].length);
        this.option.series[3].data.push(greenArray[x].length);
        this.option.series[4].data.push(blueArray[x].length);
        this.option.series[5].data.push(purpleArray[x].length);
      }
    },
    categoryClassified(styleData) {
      let output = '';
      if (
        styleData === '女學生 上衣' ||
        styleData === '青少年 條紋上衣' ||
        styleData === '男款 條紋上衣' ||
        styleData === '男 卡通 上衣' ||
        styleData === 'JERSCY 新色素T' ||
        styleData === '男版 uniqlo 素T'
      ) {
        output = '上衣';
      } else if (
        styleData === 'caco 女 格紋襯衫' ||
        styleData === 'mouggan 襯衫' ||
        styleData === 'mobo 白 襯衫' ||
        styleData === '男款 襯衫' ||
        styleData === 'meier q 襯衫'
      ) {
        output = '襯衫';
      } else if (
        styleData === 'mouggan 風衣外套 大衣' ||
        styleData === 'Adidas 女款外套' ||
        styleData === 'uniqlo 防曬外套' ||
        styleData === '男款 Adidas 運動外套' ||
        styleData === 'Calvin Klein slim fit  jacket'
      ) {
        output = '外套、大衣';
      } else if (
        styleData === 'uniqlo 褲裙' ||
        styleData === 'jendes 牛仔褲' ||
        styleData === '牛仔短褲' ||
        styleData === '學生 運動褲' ||
        styleData === '男生 休閒短褲' ||
        styleData === 'mouggan 連身褲' ||
        styleData === '牛仔褲'
      ) {
        output = '褲款';
      } else if (
        styleData === '短裙' ||
        styleData === '長裙' ||
        styleData === '皮革短裙' ||
        styleData === 'mouggan 長裙'
      ) {
        output = '裙款';
      } else if (
        styleData === '女學生 洋裝' ||
        styleData === 'mouggan 丹寧洋裝' ||
        styleData === '碎花洋裝' ||
        styleData === 'jendes 洋裝' ||
        styleData === 'brand dress'
      ) {
        output = '洋裝';
      } else if (styleData === '漁夫帽') {
        output = '帽款';
      }
      return output;
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
