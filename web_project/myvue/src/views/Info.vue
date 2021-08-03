<template>
<!--这是个人资料页面-->
  <div class="info-wrapper">
    <div class="info-img">
      <img class="info-icon" src="../assets/mine/a.jpg"/>
    </div>
    <div class="info-item">
      <div class="info-nickname">
        <span class="info-item-title">昵称</span>
        <span class="info-item-content"></span>
      </div>
      <div class="info-mobile">
        <span class="info-item-title">手机</span>
        <span class="info-item-content"></span>
      </div>
      <div class="info-gender">
        <span class="info-item-title">性别</span>
        <span class="info-item-content"></span>
      </div>
      <div class="info-birthday">
        <span class="info-item-title">生日</span>
        <span class="info-item-content"></span>
      </div>
    </div>
    <div class="info-save">
      <button class="info-save-bottom" @click="submitd('FormData')">保存</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Info"
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
  margin: 0 ;
  padding: 0;
  height: 100%;
}
.info-wrapper{
  margin-top: 50px;

}
.info-img{
  width: 90px;
  height: 90px;
  border-radius: 50%;
  overflow: hidden;
  margin: 20px;
}
.info-icon{
  height: 90px;
}
.info-item{
  font-size: 35px;
  background: #FFFFFF;
}
.info-item-title{
  padding: 0px 40px 0px 20px;
  width: 50px;
}
.info-item-content{

}
.info-save{
  text-align: center;
}
.info-save-bottom{
  width: 330px;
  height: 45px;
  background: #333333;
  font-size: 15px;
  color: #FAFAFA;
  border: none;
  margin-top:20px ;
}
span{

}
</style>
