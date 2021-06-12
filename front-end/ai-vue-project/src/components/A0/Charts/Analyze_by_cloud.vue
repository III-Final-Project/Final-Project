<template>
  <div class="hello">
    <div>
      <wordcloud
        :data="defaultWords"
        nameKey="name"
        valueKey="value"
        :color="myColors"
        :showTooltip="false"
        :wordClick="wordClickHandler"
      >
      </wordcloud>
    </div>
  </div>
</template>
<script>
import wordcloud from 'vue-wordcloud';

export default {
  name: 'app',
  components: {
    wordcloud,
  },
  props: ['myData'],
  data() {
    return {
      myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
      defaultWords: null,
      details: [],
    };
  },
  created() {
    this.setDatas();
    this.defaultWords = this.details;
  },
  methods: {
    wordClickHandler(name, value, vm) {
      // eslint-disable-next-line no-console
      console.log('wordClickHandler', name, value, vm);
    },
    setDatas() {
      let shirtValue = null;
      let tShirtValue = null;
      let pantsValue = null;
      let coatValue = null;
      let underDressValue = null;
      let dressValue = null;
      let hatValue = null;
      let redValue = null;
      let orangeValue = null;
      let yellowValue = null;
      let greenValue = null;
      let blueValue = null;
      let purpleValue = null;
      this.myData.forEach((element) => {
        const category = this.categoryClassified(
          element.customer_recommend_product,
        );
        const color = element.customer_recommend_color;
        if (category === '上衣') {
          shirtValue += 1;
        } else if (category === '襯衫') {
          tShirtValue += 1;
        } else if (category === '褲款') {
          pantsValue += 1;
        } else if (category === '外套、大衣') {
          coatValue += 1;
        } else if (category === '裙款') {
          underDressValue += 1;
        } else if (category === '洋裝') {
          dressValue += 1;
        } else {
          hatValue += 1;
        }
        if (color === 'red') {
          redValue += 1;
        } else if (color === 'orange') {
          orangeValue += 1;
        } else if (color === 'yellow') {
          yellowValue += 1;
        } else if (color === 'green') {
          greenValue += 1;
        } else if (color === 'blue') {
          blueValue += 1;
        } else {
          purpleValue += 1;
        }
      });
      this.details.push(
        { name: '上衣', value: shirtValue },
        { name: '襯衫', value: tShirtValue },
        { name: '褲款', value: pantsValue },
        { name: '外套、大衣', value: coatValue },
        { name: '裙款', value: underDressValue },
        { name: '洋裝', value: dressValue },
        { name: '帽款', value: hatValue },
        { name: '紅色', value: redValue },
        { name: '橙色', value: orangeValue },
        { name: '黃色', value: yellowValue },
        { name: '綠色', value: greenValue },
        { name: '藍色', value: blueValue },
        { name: '紫色', value: purpleValue },
      );
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
