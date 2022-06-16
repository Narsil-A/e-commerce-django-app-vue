<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="columns is-12">
                <h1 class="title">  my Account </h1>
            </div>
            <div class="columns is-12">
                <button @click="logout()" class= "button is-dark">Log out</button>
            </div>
        </div>         
    </div>   

</template>

<script>
import axios from 'axios'


export default {
    name: 'MyAccount',
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}





</script>