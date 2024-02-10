<template>
    <section class="section section-shaped section-lg my-0">
        <div class="shape shape-style-1 bg-gradient-default">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </div>
        <div class="container pt-lg-md pt-100 pb-100">
            <div class="row justify-content-center">
                <div class="col-lg-5">
                    <card type="secondary" shadow
                          header-classes="bg-white pb-5"
                          body-classes="px-lg-5 py-lg-5"
                          class="border-0">
                        <!-- <template>
                            <div class="text-muted text-center mb-3">
                                <small>Sign in with</small>
                            </div>
                            <div class="btn-wrapper text-center">
                                <base-button type="neutral">
                                    <img slot="icon" src="img/icons/common/github.svg">
                                    Github
                                </base-button>

                                <base-button type="neutral">
                                    <img slot="icon" src="img/icons/common/google.svg">
                                    Google
                                </base-button>
                            </div>
                        </template> -->
                        <template>
                            <!-- <div class="text-center text-muted mb-4">
                                <small>Or sign in with credentials</small>
                            </div> -->
                            <form role="form">
                                <base-input v-model="username"
                                            alternative
                                            class="mb-3"
                                            placeholder="Account"
                                            addon-left-icon="ni ni-user-run">
                                </base-input>
                                <base-input v-model="password"
                                            alternative
                                            type="password"
                                            placeholder="Password"
                                            addon-left-icon="ni ni-lock-circle-open">
                                </base-input>
                                <base-checkbox v-model="rememberMe">
                                    Remember me
                                </base-checkbox>
                                <div class="text-center">
                                    <base-button type="primary" class="my-4" @click="userLogin">Sign In</base-button>
                                </div>
                            </form>
                        </template>
                    </card>
                    <div class="row mt-3">
                        <div class="col-6">
                            <a href="#" class="text-light">
                                <small>Forgot password?</small>
                            </a>
                        </div>
                        <div class="col-6 text-right">
                            <a href="#" class="text-light">
                                <small>Create new account</small>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
// import login from "../plugins/login";
import apiInstance from "../plugins/interceptor";
export default {
  data() {
    return {
      username: '',
      password: '',
      rememberMe: false,
    };
  },
  methods: {
    async userLogin() {
      if (this.username == "" || this.username == null){
        alert("account should not be empty");
      }
      else{
        await this.login(this.username, this.password);
      }
    },

    async login(username, password) {
        try {
            const hashedPassword = await this.hashPassword(password);
            // 调用登录API`
            const response = await apiInstance.post("/login", { username, password: hashedPassword });

            // 处理登录成功的逻辑
            if (response.data.success) {
            // 更新用户信息
            console.log(response.data.cookie);
            this.$store.commit("user/setUser", {userName: username, cookie: response.data.cookie});
            this.$router.push({name: 'home'})
            } else {
            // 处理登录失败的逻辑
            console.error(response.data.message);
            return false; // 表示登录失败
            }
        } catch (error) {
            // 处理登录过程中的错误
            console.error(error);
            return false; // 表示登录失败
        }
    },
    async hashPassword(password) {
        const encoder = new TextEncoder();
        const data = encoder.encode(password);

        const hashBuffer = await crypto.subtle.digest("SHA-256", data);

        const hashArray = Array.from(new Uint8Array(hashBuffer));
        const hashHex = hashArray.map(byte => byte.toString(16).padStart(2, "0")).join("");

        return hashHex;
    }

  },
};
</script>
<style>
</style>
