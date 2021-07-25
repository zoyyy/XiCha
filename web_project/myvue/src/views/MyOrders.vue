<template>
<!--  <h1>这是“订单“页面</h1>-->
  <div class="myorders-head">
   <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="当前订单" name="first">当前订单</el-tab-pane>
    <el-tab-pane label="历史订单" name="second">历史订单</el-tab-pane>
   </el-tabs>
  </div>
</template>

<script>

export default {
  name: "MyOrders",
  data() {
    return {
      activeName: 'second'
    };
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    }
  }
};
</script>

<style scoped>

</style>
