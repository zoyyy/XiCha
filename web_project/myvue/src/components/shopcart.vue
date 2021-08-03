<template>
  <div claa="shopcart" :class="{'highligh':totalCount>0}">
    <div class="shopcart-wrapper">
      <!-- 左=>内容包含购物车icon 金额 配送费 -->
      <div class="content-left">
        <div class="logo-wrapper" :class="{'highligh':totalCount>0}" @click="toggleList">
          <span class="icon-shopping_cart logo" :class="{'highligh':totalCount>0}"></span>
          <i class="num" v-show="totalCount">{{totalCount}}</i>
        </div>
        <div class="desc-wrapper">
          <p class="total-price" v-show="totalPrice">￥{{totalPrice}}</p>
        </div>
      </div>
      <!-- 去结算 -->
      <div class="content-right" :class="{'highligh':totalCount>0}">
        {{payStr}}
      </div>
<!--      1.list-hearder，左右结构包括全选与清空购物袋-->
<!--      2.list-content 列表，存放我们选择的奶茶-->
<!--      2.1左边是我们的食物名字，商品描述（包括加的小料）；右侧是数量，加减商品的组件。-->

      <div class="shopcart-list" v-show="listShow" :class="{'show':listShow}">
        <!--全选 清空功能-->
        <div class="list-header">
          <div class="title">全选</div>
          <div class="empty" @click="emptyFn">
            <img src="../assets/menu_icon_empty.png" />
            <span>清空购物车</span>
          </div>
        </div>
        <!--所选商品列表-->
        <div class="list-content" ref='listContent'>
          <ul>
            <li class="food-item" v-for="food in selectFoods">
              <div class="drink-img">
                <img src="../assets/drink01.png">
              </div>
              <div class="desc-wrapper">
                <!--左侧-->
                <div class="desc-left">
                  <!--所选商品名字-->
                  <p class="name">{{food.name}}</p>
                  <!--所选商品描述 unit 例 des 霆锋苦辣鸡腿堡1个-->
                  <p class="unit" v-show="!food.description">{{food.unit}}</p>
                  <p class="description" v-show="food.description">{{food.description}}</p>
                </div>
                <!--商品单价-->
                <div class="desc-right">
                  <span class="price">￥{{food.min_price}}</span>
                </div>
              </div>
              <!--复用商品增减组件 Cartcontrol-->
              <div class="cartcontrol-wrapper">
                <Cartcontrol :food='food'></Cartcontrol>
              </div>
            </li>
          </ul>
        </div>
        <div class="list-bottom"></div>
      </div>

    </div>
  </div>
</template>

<script>
// 导入BScroll
import BScroll from 'better-scroll'
// 导入Cartcontrol
import Cartcontrol from 'components/Cartcontrol/Cartcontrol'

export default {
  name: "shopcart",
  data() {
    return {
      fold: true
    }
  },
  props: {
    poiInfo: {
      type: Object,
      default: {}
    },
    selectFoods: {
      type: Array,
      default() {
        return [
          //                        {
          //                            min_price: 10,
          //                            count: 3
          //                        },
          //                        {
          //                            min_price: 7,
          //                            count: 1
          //                        }
        ];
      }
    }
  },
  computed: {
    // 总个数
    totalCount() {
      let num = 0;
      this.selectFoods.forEach((food) => {
        num += food.count;
      });

      return num;
    },
    // 总金额
    totalPrice() {
      let total = 0;
      this.selectFoods.forEach((food) => {
        total += food.min_price * food.count;
      });

      return total;
    },
    payStr() {
      if(this.totalCount > 0) {
        return "去结算";
      } else {
        return this.poiInfo.min_price_tip;
      }
    },
    listShow() {
      if(!this.totalCount) { // 个数为0
        this.fold = true;

        return false;
      }

      let show = !this.fold;

      // BScoll相关
      if(show) {
        this.$nextTick(() => {
          if(!this.shopScroll) {
            this.shopScroll = new BScroll(this.$refs.listContent, {
              click: true
            });
          } else {
            this.shopScroll.refresh();
          }
        });
      }

      return show;
    }
  },
  methods: {
    toggleList() {
      if(!this.totalCount) { // 个数为0
        return;
      }
      this.fold = !this.fold;
    },
    emptyFn() {
      this.selectFoods.forEach((food) => {
        food.count = 0;
      });
    },
    hideMask() {
      this.fold = true;
    }
  },
  components: {
    Cartcontrol,
    BScroll
  }
}
</script>

<style scoped>

</style>
