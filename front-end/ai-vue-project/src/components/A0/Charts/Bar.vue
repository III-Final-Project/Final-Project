<template>
  <div></div>
</template>

<script>
import User from '../../../service/user';

export default {
  methods: {
    post() {
      const data = {};
      data.username = '';
      User.createUsers(data).then(() => {});
    },
  },
};
</script>

<style></style>
