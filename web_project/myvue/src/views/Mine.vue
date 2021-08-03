<template>
  <div class="mine">
    <div class="mine_img">
      <img src="../assets/mine/me-focus.png" style="width: 375px"/>
   </div>
    <div class="mine1">
      <el-card class="mine_card">
        <div class="minecard_head">
          <div class="minecard-head-content">未登录</div>
          <div class="minecard-head-img">
<!--            <img class="minecard-head-icon" src="../assets/mine/me_icon_head.png"/>-->
            <img class="minecard-head-icon" @click="goTo('/info')"src="../assets/mine/a.jpg"/>
          </div>
        </div>
        <hr noshade="true" style="height:1px;background-color:#FAFAFA;border: none">
        <div class="minecard_body">
          <span class="mine-item">
            <span >
              <img class="mine-item-icon" src="../assets/mine/me_icon_points.png"/>
            </span>
            <span class="mine-item-num">0</span>
            <span>积分商城</span>
          </span>
          <span class="mine-item">
            <span >
              <img class="mine-item-icon" src="../assets/mine/me_icon_quan.png"/>
            </span>
            <span class="mine-item-num">0</span>
            <span>喜茶券</span>
          </span>
          <span class="mine-item">
            <span >
              <img class="mine-item-icon" src="../assets/mine/me_icon_wallet.png"/>
            </span>
            <span class="mine-item-num">0</span>
            <span>钱包</span>
          </span>
          <span class="mine-item">
            <span >
              <img class="mine-item-icon" src="../assets/mine/me_icon_gift_card.png"/>
            </span>
            <span class="mine-item-num">0</span>
            <span>阿喜有礼</span>
          </span>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "Mine",
  methods: {
    goTo (path) {
      this.$router.replace(path)
    }
  }
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
.minecard_head{
  display:flex;
}
.minecard-head-content{
  width: 200px;
}
.minecard-head-img {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  overflow: hidden;
  margin: 10px;
}
.minecard-head-icon {
  height: 70px;
}

.mine_card{
  width: 340px;
}
.minecard_body{
  display: flex;

}
.mine-item{
  display:flex;
  text-align:center;
  flex-direction:column;
  align-items:center;
  margin:12px;

}
.mine-item-icon{
  width: 50px;
}
.mine-item-num{
  font-size: 18px;
  padding-bottom: 5px;
}
</style>
