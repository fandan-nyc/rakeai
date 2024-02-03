<template>
  <header class="header-global">
    <base-nav class="navbar-main" transparent type="" effect="light" expand>
      <router-link slot="brand" class="navbar-brand mr-lg-5" to="/">
        <img src="img/brand/rakeai_white.png" alt="logo" />
      </router-link>

      <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
        <router-link v-if="!$store.state.user.userInfo.username">
          <a slot="title" href="/login" class="nav-link" data-toggle="dropdown" role="button">
            <i class="ni ni-ui-04 d-lg-none"></i>
            <span class="nav-link-inner--text">Log in</span>
          </a>
        </router-link>
        <a slot="title" href="#" class="nav-link" data-toggle="dropdown" role="button">
          <i class="ni ni-ui-04 d-lg-none"></i>
          <span class="nav-link-inner--text">{{ $store.state.user.userInfo.username }}</span>
        </a>
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
};
</script>
<style></style>
