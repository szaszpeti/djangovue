<template>
  <div id="app">
    <div id="nav">
     <NavbarComponent />
     <router-view />
    </div>
    
  </div>
</template>

<script>
import NavbarComponent from "./components/Navbar.vue"
import { apiService } from "@/common/api.service.js"


export default {
  name:"App",
  components: {
    NavbarComponent,
  },
  methods: {
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      //this is the browser localstorage
      window.localStorage.setItem("username", requestUser);
      
    }
  },
  created() {
    this.setUserInfo()
  }

}

</script>

<style>
 html, body {
        height: 100%;
        font-family: "Playfair Display", serif;
    }

    /* no page refreshing, without this after pressing the button will stay pressed*/
    .btn:focus {
      box-shadow: none !important;
    }
</style>
