<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
@font-face {
  font-family: 'Roboto-Regular';
  src: url('~@/assets/font/Roboto-Regular.ttf');
}

@font-face {
  font-family: 'Roboto-Medium';
  src: url('~@/assets/font/Roboto-Medium.ttf');
}

@font-face {
  font-family: 'NotoSansCJKtc-Regular';
  src: url('~@/assets/font/NotoSansCJKtc-Regular.otf');
}

/* 消除瀏覽器預設css */
body {
  margin: 0;
  font-family: 'NotoSansCJKtc-Regular,Roboto-Regular';
}

a,
input,
button {
  outline: none !important;
  text-decoration: none !important;
}

ul {
  margin: 0;
  padding: 0;
}

li {
  list-style-type: none;
}

p,
td {
  color: rgb(95, 94, 94);
}

label {
  margin: 0;
}
</style>
