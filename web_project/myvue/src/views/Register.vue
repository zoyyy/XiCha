<template style="text-align: center;width:375px">
  <div id="register" v-loading="false">
    <div class="register-container">
      <el-form :model="FormData" :rules="rules"
               status-icon
               ref="FormData"
               label-position="left"
               label-width="80px"
               class=" register-page">
        <h3 class="title">用户注册</h3>
        <el-form-item prop="username" label="用户名">
          <el-input type="text"
                    v-model="FormData.username"
                    auto-complete="off"
                    placeholder="用户名"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password" label="密码">
          <el-input type="password"
                    v-model="FormData.password"
                    auto-complete="off"
                    placeholder="密码"
          ></el-input>
        </el-form-item>
        <el-form-item label="再次输入" prop="repassword">
          <el-input type="password"
                    v-model="FormData.repassword"
                    placeholder="请再次输入密码"
          ></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="FormData.email"
                    placeholder="请输入邮箱地址"
          ></el-input>
        </el-form-item>
        <el-form-item label="手机" prop="mobile">
          <el-input v-model="FormData.mobile"
                    placeholder="请输入手机号码"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitd('FormData')">提交</el-button>
          <el-button @click="resetForm('FormData')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Register',
  data() {
    // 检测第二次输入的密码
    var checkPassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.FormData.password) {
        callback(new Error('两次输入的密码不一致.'))
      } else {
        callback()
      }
    }
    // 检测用户名是否已经被注册
    var dulaUsername = (rule, value, callback) => {
      // 验证用户名是否存在.  一会再写
      if (value.length < 3) {
        callback(new Error('你的用户名太短了！'))
      } else if (value.length > 18) {
        callback(new Error('你的用户名太长了！'))
      } else {
        this.$axios.post('http://localhost:8000/register/?select=1', {
          select_username: value
        })
          .then(response => {
            if (response.data.is_indb === 1) {
              callback(new Error('该用户名已经被注册'))
            } else {
              callback();
            }
          })
      }
    }

    // 检测密码的长度
    var checkLen = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('密码长度不能小于6位'))
      } else if (value.length > 18) {
        callback(new Error('密码长度不能超过18位'))
      } else {
        callback()
      }
    }

    //检查是否为11位手机号码
    var checkMobile = (rule, value, callback) => {
      const reg =/^[1][3,4,5,7,8][0-9]{9}$/;
      if(value==''||value==undefined||value==null){
        callback();
      }else {
        if ((!reg.test(value)) && value != '') {
          callback(new Error('请输入正确的电话号码'));
        } else {
          callback();
        }
      }
    }

    return {
      FormData: {
        username: "",
        password: "",
        repassword: "",
        email: "",
        mobile: ""
      },
      rules: {
        username: [{required: true, message: '这是必填项', trigger: 'blur'}, {validator: dulaUsername, trigger: 'blur'}],
        password: [{required: true, message: "这是必填项", trigger: 'blur'}, {validator: checkLen, trigger: 'blur'}],
        repassword: [{required: true, message: '这是必填项', trigger: 'blur'}, {validator: checkPassword, trigger: 'blur'}],
        email: [{required: true, message: "请输入邮箱地址", trigger: 'blur'}, {type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change']}],
        mobile: [{required: true, message: "请输入手机号码", trigger: 'blur'}, {validator: checkMobile, trigger: ['blur', 'change']}]
      }
    }
  },
  methods: {
    submitd: function (formdata) {
      this.$refs[formdata].validate((valid) => {
        if (valid) {
          // 成功.
          this.$axios.post('http://localhost:8000/register/', {
            username: this.FormData.username,
            password: this.FormData.password,
            email: this.FormData.email,
            mobile: this.FormData.mobile
          })
            .then(response => {
              if (response.data.status === 0) {
                alert("注册成功！")
                this.$router.push({path: '/'})
                window.location.reload()
              } else {
                return false
              }
            })

        } else {
          return false;
        }
      });
    },
    resetForm: function (formdata) {
      this.$refs[formdata].resetFields()
    }
  }
}
</script>



<style scoped>


#register {
  /*background-image: url("../assets/login.jpg");*/
  width: 100%;
  height: 100%;
  position:fixed;
  /*margin-top: -10px;*/
  left: 0;
  /* margin-left: -10px; */
  /*background-size:100% 100%;*/
  margin:0;
  padding:0;
}
.register-page {
  -webkit-border-radius: 5px;
  border-radius: 15px;
  margin: 100px auto;
  width: 250px;
  padding: 35px 35px 15px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 15px #cac6c6;
}
label.el-checkbox.rememberme {
  margin: 0px 0px 15px;
  text-align: left;
}
</style>
