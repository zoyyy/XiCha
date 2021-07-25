<template>
<!--  <h1>这是“点单“页面</h1>-->
  <div class="order">
    <div class="shop">
      <div class="shop-content">
        <div class="shop-name">武汉光谷天地店</div>
        <div class="shop-extra">距离您xxkm</div>
      </div>
    </div>
    <div class="down">
      <div class="menu-wrapper">
      <ul>
        <li class="menu-item">
          <p class="menu-text">当季限定</p>
          <i class="num" style="display: none;">0</i>
        </li>
        <li class="menu-item">
          <p class="menu-text">人气必喝榜</p>
          <i class="num" style="display: none;">0</i>
        </li>
        <li class="menu-item">
          <p class="menu-text">每日鲜食</p>
          <i class="num" style="display: none;">0</i>
        </li>
        <li class="menu-item">
          <p class="menu-text">瓶装饮品</p>
          <i class="num" style="display: none;">0</i>
        </li>
        <li class="menu-item">
          <p class="menu-text">喜茶制冰</p>
          <i class="num" style="display: none;">0</i>
        </li>
        <li class="menu-item">
          <p class="menu-text">果茶家族</p>
          <i class="num" style="display: none;">0</i>
        </li>
        <li class="menu-item">
          <p class="menu-text">爆柠家族</p>
          <i class="num" style="display: none;">0</i>
        </li>
        <li class="menu-item">
          <p class="menu-text">茗茶/牛乳茶</p>
          <i class="num" style="display: none;">0</i>
        </li>
      </ul>
    </div>
      <div class="drinks-wrapper">
        <ul>
          <li class="container-list">
<!--            <div style="width:290px;margin: 0 auto">-->
<!--              <slider :sliderArray="sliderArray"></slider>-->
<!--            </div>-->
            <div></div>
          </li>
          <li class="drinks-hook">
            <div class="title">当季限定</div>
            <ul>
              <li class="drinks-item">
<!--                <div class="drinks-icon" style="background:url('../assets/drink01.png'); "></div>-->
<!--                <div class="drinks-icon" >-->
                  <img class="drinks-icon" src="../assets/drink01.png" />
<!--                </div>-->
                <div class="drinks-content">
                  <div class="drinks-name">浓爆柠</div>
                  <div class="drinks-extra">原创</div>
                  <p class="drinks-price">￥21</p>
                </div>
              </li>
              <li class="drinks-item">
                <!--                <div class="drinks-icon" style="background:url('../assets/drink01.png'); "></div>-->
                <!--                <div class="drinks-icon" >-->
                <img class="drinks-icon" src="../assets/drink01.png" />
                <!--                </div>-->
                <div class="drinks-content">
                  <div class="drinks-name">浓爆柠</div>
                  <div class="drinks-extra">原创</div>
                  <p class="drinks-price">￥21</p>
                </div>
              </li>
              <li class="drinks-item">
                <!--                <div class="drinks-icon" style="background:url('../assets/drink01.png'); "></div>-->
                <!--                <div class="drinks-icon" >-->
                <img class="drinks-icon" src="../assets/drink01.png" />
                <!--                </div>-->
                <div class="drinks-content">
                  <div class="drinks-name">浓爆柠</div>
                  <div class="drinks-extra">原创</div>
                  <p class="drinks-price">￥21</p>
                </div>
              </li>
              <li class="drinks-item">
                <!--                <div class="drinks-icon" style="background:url('../assets/drink01.png'); "></div>-->
                <!--                <div class="drinks-icon" >-->
                <img class="drinks-icon" src="../assets/drink01.png" />
                <!--                </div>-->
                <div class="drinks-content">
                  <div class="drinks-name">浓爆柠</div>
                  <div class="drinks-extra">原创</div>
                  <p class="drinks-price">￥21</p>
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
import slider from "../components/Slider/slider"
import banner1 from "../assets/banner1.png"
import banner2 from "../assets/banner2.png"
import banner3 from "../assets/banner3.png"
export default {
  name: "Order",
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
  padding: 11px 11px 0 11px;
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
.drinks-price{
  margin-bottom: 10px;
  margin-left: 10px;
}
ul{
  list-style:none;
}

</style>
