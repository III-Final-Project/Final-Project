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
/* 消除瀏覽器預設css */
body {
  margin: 0;
}

a,
input,
button {
  outline: none;
  text-decoration: none;
}

ul {
  margin: 0;
  padding: 0;
}

li {
  list-style-type: none;
}
</style>
