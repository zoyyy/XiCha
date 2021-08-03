<template>
<!--  <h1>这是“点单“页面</h1>-->
  <div class="order">
    <div class="shop">
        <div class="star">
          <img style="width: 20px" src="../assets/order/star_normal.png"/>
          <div class="shop-name">武汉光谷天地店</div>
        </div>
        <div class="shop-extra">距离您xxkm</div>
    </div>
    <div class="down">
      <div class="menu-wrapper">
      <ul>
        <li class="menu-item">
          <img :src="categories.category_image_url" v-if="categories.category_image" class="icon">
          <p class="menu-text">{{categories.name}}</p>
          <i class="num" style="display: none;">0</i>
        </li>
      </ul>
    </div>
      <div class="drinks-wrapper">
        <ul>
<!--          两个轮播图-->
          <li class="container-list">
            <div style="width:290px;margin: 0 auto">
              <slider :sliderArray="sliderArray"></slider>
            </div>
            <div style="width:290px;margin: 0 auto">
              <slider :sliderArray="sliderArray1"></slider>
            </div>
            <div></div>
          </li>
          <li class="drinks-hook">
            <div class="title">当季限定</div>
            <ul>
              <li class="drinks-item">
                  <img class="drinks-icon" src="../assets/drink01.png" />
                <div class="drinks-content">
                  <div class="drinks-name">浓爆柠</div>
                  <div class="drinks-extra">原创</div>
                  <div class="drinks-choose">
                    <div class="drinks-price">￥21</div>
                    <div class="buy">选规格</div>
                  </div>
                </div>

              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import slider2 from "../components/Slider/slider2"
import banner1 from "../assets/slider1/banner1.png"
import banner2 from "../assets/slider1/banner2.png"
import banner3 from "../assets/slider1/banner3.png"
import banner4 from "../assets/slider2/banner1.png"
import banner5 from "../assets/slider2/banner2.png"
import banner6 from "../assets/slider2/banner3.png"
import BScroll from "better-scroll";

export default {
  name: "Order",
  components:{
    slider:slider2,
    BScroll,
  },
  data(){
    return{
      sliderArray:[banner1,banner2,banner3],
      sliderArray1:[banner4,banner5,banner6],
      categories:{}
    }
  },
  created() {
    this.$axios
      .get("/drinks/")
      .then(response => {
        let json = response.data;
        if (json.code === 0){
          this.categories = json.categories;

        }
        }
      )
  }
}
</script>

<style scoped>
*{
  padding: 0;
  margin: 0;
}
html{
  height: 667px;
  margin: 0;
  padding: 0;
}
body {
  height: 100%;
  margin: 0;
  padding: 0;
}
.down{
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  position: absolute;
  top: 70px;
  bottom: 51px;
  /*overflow: hidden;*/
  width: 100%;
}
.shop{
  height: 70px;
  background: #ffffff;
}
.shop-content{
  margin-left: 14px;
}
.shop-name{
  font-size: 18px;
  /*margin-top: 5px;*/
  padding-top: 5px;
  padding-bottom: 5px;
}
.shop-extra{
  font-size: 10px;
  color:#999999 ;
}
.menu-wrapper{
  -webkit-box-flex: 0;
  -ms-flex: 0 0 85px;
  flex: 0 0 85px;
  background: #f4f4f4;
}
.menu-item{
  padding: 15px 0px 15px 0px;
  position: relative;
}
.menu-text{
  font-size: 10px;
  color: #999999;
  margin-left: 6px;
}
.drinks-wrapper{
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
  margin-left: 10px;
}
.container-list{
  width: 290px;
  padding: 0;
  border-bottom: 1px solid #e4e4e4;
}
.title{
  height: 13px;
  font-size: 10px;
  padding-left: 7px;
  margin-top: 10px;
  margin-bottom: 15px;
  color: #999999;
}
.drinks-item{
  display: flex;
  margin-bottom: 40px;
  position: relative;
}
.drinks-icon{
  flex: 0 0 20px;
  height: 90px;
}
.drinks-content{
  flex: 1;
  width: 200px;
}
.drinks-name{
  font-size: 15px;
  line-height: 21px;
  color: #333333;
  margin-bottom: 10px;
  margin-left: 10px;
}
.drinks-extra{
  font-size: 5px;
  line-height: 21px;
  color: #999999;
  margin: 11px;
}
.drinks-choose{
  display:flex;
}
.drinks-price{
  margin-bottom: 10px;
  margin-left: 10px;
  width: 100px;
}
.buy{
  margin-bottom: 10px;

}
ul{
  list-style:none;
}

</style>
