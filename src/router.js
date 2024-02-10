import Vue from "vue";
import Router from "vue-router";
import AppHeader from "./layout/AppHeader";
import AppFooter from "./layout/AppFooter";
import Home from "./views/Home.vue";
import Components from "./views/Components.vue";
import Landing from "./views/Landing.vue";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";
import Profile from "./views/Profile.vue";
import store from './plugins/store';

Vue.use(Router);

const router = new Router({
  linkExactActiveClass: "active",
  mode: "history", // 启用"history"模式
  routes: [
    {
      path: "/",
      name: "home",
      components: {
        header: AppHeader,
        default: Home,
        footer: AppFooter,
      },
    },
    // {
    //   path: "/",
    //   name: "aboutus",
    //   components: {
    //     header: AppHeader,
    //     default: Aboutus,
    //     footer: AppFooter,
    //   },
    // },
    // {
    //   path: "/components",
    //   name: "components",
    //   components: {
    //     header: AppHeader,
    //     default: Components,
    //     footer: AppFooter
    //   }
    // },
    // {
    //   path: "/landing",
    //   name: "landing",
    //   components: {
    //     header: AppHeader,
    //     default: Landing,
    //     footer: AppFooter
    //   }
    // },
    {
      path: "/login",
      name: "login",
      components: {
        header: AppHeader,
        default: Login,
        footer: AppFooter,
      },
    },
    // {
    //   path: "/register",
    //   name: "register",
    //   components: {
    //     header: AppHeader,
    //     default: Register,
    //     footer: AppFooter
    //   }
    // },
    {
      path: "/profile",
      name: "profile",
      components: {
        header: AppHeader,
        default: Profile,
        footer: AppFooter
      },
      meta: { requiresAuth: true },
    }
  ],
  scrollBehavior: to => {
    if (to.hash) {
      return { selector: to.hash };
    } else {
      return { x: 0, y: 0 };
    }
  },
});
export default router;
router.beforeEach((to, from, next) => {
  // 检查即将进入的路由是否需要认证
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // 这里检查认证状态，例如检查 Vuex store 或 cookies
    if (store.state.user.userInfo.cookie) {
      next(); // 如果已认证，继续导航
    } else {
      next({ name: 'login' }); // 如果未认证，重定向到登录页面
    }
  } else {
    next(); // 如果路由不需要认证，正常导航
  }
})