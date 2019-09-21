<template>
    <div id="app">
        <NavbarComponent />
        <!-- <div id="nav">
            <router-link to="/">Home</router-link>|
            <router-link to="/about">About</router-link>|
            <router-link to="/example">Example</router-link>
        </div> -->
        <router-view />
    </div>
</template>

<script>
import NavbarComponent from "./components/Navbar.vue"
export default {
  name:"App",
  components: {
    NavbarComponent
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
