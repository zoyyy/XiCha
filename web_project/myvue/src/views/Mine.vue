<template>
  <div class="mine">
    <div class="mine_img">
      <img src="../assets/mine.jpg"/>
   </div>
    <div class="mine1">
      <el-card class="mine_card">
        <div class="minecard_head">

          </div>
        <hr noshade="true" style="height:1px;background-color:#FAFAFA;border: none">
        <div class="minecard_body">
           </div>
      </el-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "Mine"
}
</script>

<style scoped>
*{
  margin: 0;
  padding: 0;
}
html{
  margin: 0;
  padding: 0;
  height: 100%;
}
body{
  margin: 0px;
  padding: 0;
  height: 100%;
}
.mine1{
  position: absolute;
  margin-top:-40px;
  left: 17px;
  z-index:0
}
.mine_card{
  width: 340px;
  height: 200px;
}


</style>
