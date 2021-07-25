<template>
  <div class="footer_guide">
    <span class="guide_item" :class="{on: '/'===$route.path}" @click="goTo('/')">
      <span class="item_icon">
        <i class="el-icon-house" ></i>
      </span>
      <span>首页</span>
    </span>
    <span class="guide_item" :class="{on: '/order'===$route.path}" @click="goTo('/order')">
      <span class="item_icon">
        <i class="el-icon-milk-tea"></i>
      </span>
      <span>点单</span>
    </span>
    <span class="guide_item" :class="{on: '/goods'===$route.path}" @click="goTo('/goods')">
      <span class="item_icon">
        <i class="el-icon-shopping-bag-2"></i>
      </span>
      <span>百货</span>
    </span>
    <span class="guide_item" :class="{on: '/myorders'===$route.path}" @click="goTo('/myorders')">
      <span class="item_icon">
        <i class="el-icon-tickets"></i>
      </span>
      <span>订单</span>
    </span>
    <span class="guide_item" :class="{on: '/mine'===$route.path}" @click="goTo('/mine')">
      <span class="item_icon">
        <i class="el-icon-user"></i>
      </span>
      <span>我的</span>
    </span>
  </div>
</template>

<script>
export default {
  methods: {
    goTo (path) {
      this.$router.replace(path)
    }
  }
}
</script>

<style >

.footer_guide {
  border-top:1px solid #d2d2d2;;
  position:fixed;
  z-index :100;
  left :0;
  right :0;
  bottom :0;
  background-color:#F7F7F7;
  width: 100%;
  height: 50px;
  display: flex;
}
  .guide_item {
    display:flex;
    flex :1;
    text-align:center;
    flex-direction:column;
    align-items:center;
    margin:8px;
    color :#BBBBBB;
  }
    span{
      font-size:10px;
      margin-top:0px;
      margin-bottom:0px;
     }
      /*.iconfont{*/
      /*  font-size:22px;*/
      /*}*/
.item_icon{
  font-size: 20px;
}
.on{
  color: #1A1A1A;
}
</style>
