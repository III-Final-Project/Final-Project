<template>
  <div>
    <Header />
    <div class="content">content</div>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/F0/Header';
import Footer from '@/components/F0/Footer';

export default {
  name: 'AIF000',
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      data: [
        { id: 1, username: 'Jyun' },
        { id: 2, username: 'Michael' },
      ],
    };
  },
};
</script>

<style scoped>
.content {
  width: 200px;
  height: 1000px;
}
</style>
