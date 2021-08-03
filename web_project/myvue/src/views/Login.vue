<template>
  <div id="login" v-loading="false">
    <div class="login-container" >
      <el-form :model="FormDatas" :rules="rules"
               status-icon
               ref="FormDatas"
               label-position="left"
               label-width="70px"
               class="demo-ruleForm login-page">
        <h3 class="title" style="margin-bottom: 30px">登录</h3>
        <el-form-item label="用户名" prop="username" >
          <el-input type="text"
                    v-model="FormDatas.username"
                    auto-complete="off"
                    placeholder="用户名"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password" label="密码">
          <el-input type="password"
                    v-model="FormDatas.password"
                    auto-complete="off"
                    placeholder="密码"
          ></el-input>
        </el-form-item>
        <el-checkbox
          v-model="checkedRememberMe"
          class="rememberme"
        >下次自动登录</el-checkbox>
        <el-form-item>
          <el-button type="primary" style="width:50%;margin-left: -70px" @click="submitd('FormDatas')">登录</el-button>
        </el-form-item>
        <el-form-item>
          <div style="margin-left: -70px">没有帐号?
            <el-button type="text" ><router-link to="/register">点我注册</router-link></el-button>
          </div>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data(){
    return {
      FormDatas: {
        username: 'admin',
        password: '123456',
      },
      rules: {
        username: [{required: true, message: '请输入用户名！', trigger: 'blur'}],
        password: [{required: true, message: '请输入密码！', trigger: 'blur'}]
      },
      checkedRememberMe: false
    }
  },
  methods: {
    submitd: function (Dataset) {
      this.$refs[Dataset].validate((valid) => {
        if (valid) {
          // 成功
          this.$axios.post("http://localhost:8000/login/", {
            username: this.FormDatas.username,
            password: this.FormDatas.password,
          })
            .then(response => {
              if (response.data.status === 0) {
                //登录成功
                this.$store.commit('changeLogin',{ Authorization: response.data.status+'', username: response.data.username, remember: this.checkedRememberMe });
                this.$router.push({path: "/"});
                window.location.reload();
              } else {
                this.$notify({
                  title: '登录失败',
                  message: response.data.message,
                  type: 'error'
                })
              }

            })
        } else {
          return false;
        }
      })
    }
  }
};
</script>

<style scoped>
#login{
  /*background-image: url("../assets/login.jpg");*/
  width: 100%;
  height: 100%;
  position:fixed;
  /*margin-top: -10px;*/
  left: 0;
  /* margin-left: -10px; */
  background-size:100% 100%;
  margin:0;
  padding:0;
}
.login-container {
  width: 100%;
  height: 100%;
}
.login-page {
  -webkit-border-radius: 5px;
  border-radius: 15px;
  margin: 100px auto;
  width: 250px;
  padding: 35px 35px 15px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 15px #cac6c6;
}
.rememberme {
  margin: 0px 0px 15px;
  text-align: left;
}
</style>
