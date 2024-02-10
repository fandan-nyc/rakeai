<template>
  <header class="header-global">
    <base-nav class="navbar-main" transparent type="" effect="light" expand>
      <router-link slot="brand" class="navbar-brand mr-lg-5" to="/">
        <img src="img/brand/rakeai_white.png" alt="logo" />
      </router-link>
      <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
        <router-link to="/login" v-if="!isUserLoggedIn" class="nav-link" data-toggle="dropdown" role="button">
            <i class="ni ni-ui-04 d-lg-none"></i>
            <span class="nav-link-inner--text">Log in</span>
        </router-link>
        <div v-if="isUserLoggedIn" style="cursor: pointer" data-toggle="dropdown" role="button">
          
          <base-dropdown tag="li" class="nav-item">
            <div slot="title" class="nav-link" data-toggle="dropdown" role="button">
                <i class="ni ni-collection d-lg-none"></i>
                <span class="nav-link-inner--text">{{ $store.state.user.userInfo.userName }}</span>
            </div>
            <router-link to="/profile" class="dropdown-item">Profile</router-link>
            <span @click="userLogout" class="dropdown-item">Log out</span>
          </base-dropdown>
        </div>
      </ul>
    </base-nav>
  </header>
</template>
<script>
import BaseNav from "@/components/BaseNav";
import BaseDropdown from "@/components/BaseDropdown";
import CloseButton from "@/components/CloseButton";

export default {
  components: {
    BaseNav,
    CloseButton,
    BaseDropdown,
  },
  methods: {
    async userLogout() {
      this.$store.commit("user/clearUser");
      this.$router.push({name: 'home'});
    },
  },
  computed: {
    // 计算属性定义在这里
    isUserLoggedIn() {
      // 使用双感叹号 !! 来将值转换为布尔类型
      // 如果 userName 存在且非空，则返回 true；否则返回 false
      return !!this.$store.state.user.userInfo.userName;
    },
  }
};
</script>
<style></style>
