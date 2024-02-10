// main.js 或者其他入口文件
import axios from "axios";
import serverUrl from "./config";
import Vue from "vue";
import store from "./store"

const apiInstance = axios.create({
  baseURL: serverUrl, // 设置基础URL
  timeout: 5000, // 请求超时时间
});

// 请求拦截器
apiInstance.interceptors.request.use(
  config => {
    if(store.state.userInfo && store.state.userInfo.cookie){
      const cookie = store.state.userInfo.cookie;
      config.headers["cookie"] = cookie;
    }
    return config;
  },
  error => {
    // 对请求错误做些什么
    return Promise.reject(error);
  }
);

// 响应拦截器
apiInstance.interceptors.response.use(
  response => {
    // 对响应数据做些什么
    return response;
  },
  error => {
    // 对响应错误做些什么
    return Promise.reject(error);
  }
);

// 将axios实例挂载到Vue原型上，方便在组件中使用
Vue.prototype.$api = apiInstance;
export default apiInstance;
