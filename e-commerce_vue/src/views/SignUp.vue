<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="columns is-4 is-offset-4">
                <h1 class="title">  Sign Up  </h1>


                <form @submit.prevent="submitForm">
                   <div class="field">
                       <label>Username</label>
                       <div class="control">
                           <input type="text" class="input" v-model="username">
                       </div>

                   </div>

                   <div class="field">
                       <label>Passsword</label>
                       <div class="control">
                           <input type="password" class="input" v-model="passsword">
                       </div>
                    </div>

                    <div class="field">
                       <label>Repeat Passsword</label>
                       <div class="control">
                           <input type="password" class="input" v-model="passsword2">
                       </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error"> {{ error }} </p>
                    </div>

                    <div class="field">
                       <div class="control">
                           <button class="button is-dark">Sign Up</button>
                        </div>
                    </div>

                    <hr>

                    or <router-link to="/log-in">click here</router-link> to log in!

                </form>

            </div>

        </div>
    </div>
</template>


<script>
import axios from 'axios'
import { toast} from 'bulma-toast'


export default  {
  name:'SignUp',
  data() {
      return {
          username:'',
          passsword:'',
          passsword2:'',
          errors:[]
    } 
  },
  methods: {
      submitForm() {
          this.errors = []

          if (this.username === '') {
              this.error.push('The username is missing')
          }

          if (this.password === '') {
              this.error.push('The password is too short')
          }

          if (this.password !== this.passsword2) {
              this.error.push('The password doesn\'t match')
          }

          if (!this.errors.length){
              const formData = {
                  username: this.username,
                  passsword: this.passsword
              }
              axios
              .post('/api/v1/users/', formData)
              .then(response =>{
                  toast ({
                      message: 'Account created, please log in!',
                      type: 'is-success',
                      dismissible: true,
                      pauseOnHover: true,
                      duration: 2000,
                      position: 'bottom-right',
                  })

                  this.$router.push('/log-in')
              })
            }
        }

    }
  
} 
</script>