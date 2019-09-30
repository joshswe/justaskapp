<template>
    <div id="app">
        <NavbarComponent />
        <router-view />
    </div>
</template>

<script>
import NavbarComponent from "./components/Navbar.vue"
import { apiService } from "./common/api.service.js"
export default {
  name:"App",
  components: {
    NavbarComponent
  },
  methods: {
    // Set the user info into window local storage
    async setUserInfo(){
      // The await operator is used to wait for a Promise. It can only be used inside an async function.
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      window.localStorage.setItem("username", requestUser);

    }
  },
  created(){
    this.setUserInfo()
  }
}
</script>

<style>
    html,body {
        height: 100%;
        font-family: "Playfair Display", serif;
    }

    .btn:focus {
      box-shadow: none !important;
    }
</style>
