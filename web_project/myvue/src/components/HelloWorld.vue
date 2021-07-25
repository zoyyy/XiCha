<template>
  <div class="index">
    <!--    轮播图-->
    <div style="width:375px;margin: 0 auto">
      <slider :sliderArray="sliderArray"></slider>
    </div>
    <div class="hello">
<!--    //第一个卡片（门店自取/外卖）-->
    <div class="partone">
      <el-card class="Card_1">
        <div class="Card1_pic">
        <img src="@/assets/010.png" @click="goTo('/order')" style="height: 120px;margin-top: -15px;padding: 23px"/>
        <img src="@/assets/011.png" style="height: 120px;margin-top: -10px;padding: 17px"/>
        </div>
        <hr noshade="true" style="height:1px;background-color:#FAFAFA;border: none">
        <div class="Card1_body">
          <el-button style="float: left; padding: 14px 0;font-size: 10px;border:none" type="text_m1">好友拼单</el-button>
          <el-button style="float: right; padding: 14px 0;font-size: 5px;border:none" type="text_s1">拼单喝茶，分账更方便</el-button>
        </div>
      </el-card>
    </div>
<!--  第二个卡片-->

    <div class="parttwo">
      <el-card :body-style="{ padding: '0px' }" class="Card_2">
        <img src="@/assets/013.png" @click="goTo('/goods')" style="height: 120px" class="card2_image"/>
      </el-card>
      <el-card :body-style="{ padding: '0px' }" class="Card_2">
        <img src="@/assets/014.png" style="height: 120px" class="card2_image"/>
      </el-card>
      <el-card :body-style="{ padding: '0px' }" class="Card_2">
        <img src="@/assets/015.png" style="height: 120px" class="card2_image"/>
      </el-card>
    </div>
    <!--最后一个小盒子~-->
    <div class="partthree">
    </div>
  </div>
  </div>
</template>

<script>
import slider from "./Slider/slider"
import banner1 from "../assets/banner1.png"
import banner2 from "../assets/banner2.png"
import banner3 from "../assets/banner3.png"
export default {
  methods: {
    goTo (path) {
      this.$router.replace(path)
    }
  },
  components:{
    slider:slider,
  },
  data(){
    return{
      sliderArray:[banner1,banner2,banner3]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
*{
  padding: 0;
  margin: 0;
 }
html{
  height: 667px;
  margin: 0;
  padding: 0;
  /*background-image: linear-gradient(to bottom,#F7F7F7,#FFFFFF);*/
}
body {
  height: 100%;
  margin: 0;
  padding: 0;
}
.index{
  height: 667px;
}
.hello{
  position: absolute;
  margin-top:-40px;
  left: 17px;
  z-index:0
}
.Card_1{
    width:340px;
    background:#FFFFFF ;
    border-radius: 5px;
    margin:10px auto;
}
.Card1_pic{
  width: 300px;
  margin:0 auto;
  display:-webkit-flex;
  display: flex;
  justify-content: space-around;
}
.parttwo{
  width: 340px;
  margin:0 auto;
  display:-webkit-flex;
  display: flex;
  justify-content: space-around;
}
.Card_2{
  width: 106px;
  height:120px;
  border-radius: 5px;
  margin:0 auto;
  float: left;
  border: 0;
}
</style>
