<template>
    <div class="banner-container">
      <ul class="images" :style="{
        width:sliderArray.length*100+'%',
        marginLeft:-index*100+'%'
      }">
        <li v-for="(item,i) of sliderArray" :key="i" @mouseleave="autoStart" @mouseenter="autoStop">
          <a href="javascript:void(0)"><img :src=item alt=""></a>
        </li>
      </ul>
      <ul class="dots">
        <li v-for="(item,i) of sliderArray" :class="{
          active:i===index
        }" :key="i" @click="index=i"></li>
      </ul>
    </div>
</template>

<script>
export default {
      name: "slider",
      props:{
          sliderArray:{
            require:true,
            type:Array,
          }
      },
      data(){
          return{
            index:0,
            timer:null
          }
      },
      mounted(){
        this.autoStart()
      },
      destroyed(){
          this.autoStop()
      },
      methods:{
          autoStart(){
            if(this.timer){
              return
            }
            this.timer=setInterval(()=>{
              this.index=(this.index+1)%this.sliderArray.length;
            },2000)
          },
          autoStop(){
            clearInterval(this.timer);
            this.timer=null;
          }
      }
   }
</script>

<style scoped>
  /* 样式 */
  .banner-container {
    position: relative;
    overflow: hidden;
  }
  .banner-container li {
      display: block;
    /*width: 1080px;*/
    height: 100%;
    float: left;
  }
  .images {
    height: 100%;
    transition: 0.5s;
 }
  .banner-container img {
    width: 375px;
    height: 100%;
  }
  .dots {
    position: absolute;
    bottom: 35px;
    right: 160px;
    display: flex;
  }
 .dots li {
    width: 7px;
    cursor: pointer;
    height: 7px;
    margin: 0 5px;
    border-radius: 50%;
    border: 0;
    color: #fff;
   background: #999999;
  }
  .dots li.active {
    background: #5E5E5E;
  }
</style>
