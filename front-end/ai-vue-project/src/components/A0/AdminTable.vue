<!-- 
 Page : AdminTable.vue
 Author : Michael
 Time: 2021-04-21
 Desc: build table for admin.
 -->
<template>
  <div class="outer">
    <div class="content">
      <table id="data-table">
        <thead>
          <tr>
            <th title="Field #1">客戶編號</th>
            <th title="Field #2">客戶名稱</th>
            <th title="Field #3">客戶身份</th>
            <th title="Field #4">客戶心情</th>
            <th title="Field #5">客戶曾購買</th>
            <th title="Field #6">購買時間</th>
            <th title="Field #7">欲推薦商品</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>Michael</td>
            <td>VVIP</td>
            <td>Happy</td>
            <td>Angelus B</td>
            <td>2021-04-22</td>
            <td>UA shoes</td>
          </tr>
          <tr>
            <td>2</td>
            <td>Jyun</td>
            <td>VVIP</td>
            <td>Sad</td>
            <td>Nike</td>
            <td>2021-04-25</td>
            <td>LV bag</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminTable',
};
</script>

<style scoped>
table {
  width: 50vw;
  border-collapse: collapse;
}

thead {
  text-transform: uppercase;
  border-bottom: 1px solid #0e0e0e;
}

thead th {
  padding: 5px;
  text-align: center;
}

td {
  text-align: center;
  padding: 5px;
  border-bottom: 1px solid #d6d6d6;
}

tr:hover td {
  background: #e6e6e6;
}

.outer {
  display: flex;
  align-items: center;
  justify-content: center;
}

.content {
  margin: 40px auto;
}
</style>
