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
  methods: {
    wordClickHandler(name, value, vm) {
      // eslint-disable-next-line no-console
      console.log('wordClickHandler', name, value, vm);
    },
  },
  data() {
    return {
      myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
      defaultWords: null,
    };
  },
  created() {
    const details = [
      { name: 'Anglus B', value: 55 },
      { name: 'Nike', value: 15 },
      { name: 'Coach', value: 36 },
      { name: 'Adidas', value: 37 },
      { name: 'Prada', value: 40 },
      { name: 'Polo', value: 24 },
      { name: 'Armani', value: 16 },
      { name: 'Burberry', value: 46 },
      { name: 'CELINE', value: 57 },
      { name: 'BOSS', value: 36 },
      { name: 'Jimmy CHOO', value: 15 },
      { name: 'Kate spade', value: 42 },
      { name: 'Michael Kors', value: 46 },
      { name: 'Tommy', value: 26 },
      { name: 'CHARLES & KEITH', value: 21 },
      { name: 'HangTen', value: 36 },
      { name: 'H20', value: 10 },
      { name: 'HConnet', value: 45 },
    ];
    this.defaultWords = details;
  },
};
</script>
