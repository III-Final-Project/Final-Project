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
        color: [
          '#03A89E',
          '#00BBFF',
          '#FF8888',
          '#FFBB66',
          '#9999FF',
          '#BBFF66',
          '#FFFF00',
        ],
        title: {
          text: '2021-推薦商品比例圖(By product)',
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
          data: ['上衣', '襯衫', '外套、大衣', '褲款', '裙款', '洋裝', '帽款'],
        },
        series: [
          {
            name: '商品種類',
            type: 'pie',
            radius: '70%',
            center: ['50%', '60%'],
            data: [
              { value: null, name: '上衣' },
              { value: null, name: '襯衫' },
              { value: null, name: '外套、大衣' },
              { value: null, name: '褲款' },
              { value: null, name: '裙款' },
              { value: null, name: '洋裝' },
              { value: null, name: '帽款' },
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
  created() {
    this.setDatas();
  },
  methods: {
    setDatas() {
      const categoryArray = Array.from(Array(7), () => new Array(0));
      this.myData.forEach((element) => {
        const category = this.categoryClassified(
          element.customer_recommend_product,
        );
        if (category === '上衣') {
          categoryArray[0].push(element);
        } else if (category === '襯衫') {
          categoryArray[1].push(element);
        } else if (category === '外套、大衣') {
          categoryArray[2].push(element);
        } else if (category === '褲款') {
          categoryArray[3].push(element);
        } else if (category === '裙款') {
          categoryArray[4].push(element);
        } else if (category === '洋裝') {
          categoryArray[5].push(element);
        } else {
          categoryArray[6].push(element);
        }
      });
      for (let i = 0; i < 7; i += 1) {
        this.option.series[0].data[i].value = categoryArray[i].length;
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
