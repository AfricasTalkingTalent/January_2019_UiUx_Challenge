<template>
<v-app id="inspire">
  <div class="container-fluid">
    <div class="row">
      <div id="logo-section" class="col-md-4">
        <v-container id="content-section">
          <v-layout align-center justify-center id="logo-layout">
            <v-flex sm8>
              <h1>Africa's Talking</h1>
            </v-flex>
          </v-layout>
        </v-container>
      </div>
      <div id="signup-section" class="col-md-8">
        <v-container id="content-section">
          <v-layout justify-center id="form-layout">
            <v-flex sm10>
              <h1>Sign Up</h1>
              <v-stepper v-model=" el">
                <v-stepper-header>
                  <v-stepper-step :complete=" el > 1" step="1">Fill in your details</v-stepper-step>

                  <v-divider></v-divider>

                  <v-stepper-step :complete=" el > 2" step="2">Verification</v-stepper-step>

                  <v-divider></v-divider>

                  <v-stepper-step step="3">Verified and Registered</v-stepper-step>
                </v-stepper-header>

                <v-stepper-items>
                  <v-stepper-content step="1">
                    <v-form id="signup-form" ref="form" v-model="valid" lazy-validation>
                      <v-layout style="margin:auto" row wrap>
                      <v-flex sm5>
                        <v-text-field class="form-field"
                          v-model="fname"
                          :rules="emptyRules"
                          label="Firstname"
                          required
                        ></v-text-field>
                      </v-flex>
                      <v-spacer></v-spacer>
                      <v-flex sm5>
                        <v-text-field class="form-field"
                          v-model="lname"
                          :rules="emptyRules"
                          label="Lastname"
                          required
                        ></v-text-field>
                      </v-flex>
                      <v-flex sm3>
                        <v-text-field class="form-field"
                          v-model="country_code"
                          :rules="emptyRules"
                          label="Country Code"
                          required
                        ></v-text-field>
                      </v-flex>
                      <v-spacer></v-spacer>
                      <v-flex sm5>
                        <v-text-field class="form-field"
                          v-model="phone"
                          :rules="[emptyRules, format]"
                          label="Phone No."
                          required
                        ></v-text-field>
                      </v-flex>
                      <v-flex sm5>
                        <v-text-field class="form-field"
                          v-model="password"
                          :append-icon="showPassword ? 'visibility_off' : 'visibility'"
                          :rules="[passwordRules.required, passwordRules.min]"
                          :type="showPassword ? 'text' : 'password'"
                          label="Password"
                          hint="At least 6 characters"
                          counter
                          @click:append="showPassword = !showPassword"
                        ></v-text-field>
                      </v-flex>
                      <v-spacer></v-spacer>
                      <v-flex sm5>
                        <v-text-field class="form-field"
                          v-model="confirm_password"
                          :rules="[passwordRules.required, passwordConfirm]"
                          type="password"
                          label="Confirm Password"
                        ></v-text-field>
                      </v-flex>
                      </v-layout>

                      <v-btn id="signup-btn"
                        :disabled="!valid"
                        @click="handleSubmit"
                      > 
                        <span v-if="!signingup">sign up</span>
                        <hollow-dots-spinner
                          :animation-duration="1000"
                          :dot-size="9"
                          :dots-num="3"
                          color="#1b576f"
                          v-else
                        />
                      </v-btn>
                     <div v-show="error !== ''">
                      <p style="color:red;">
                        {{error}}
                      </p>
                     </div>
                    </v-form>
                  </v-stepper-content>

                  <v-stepper-content step="2">
                    <p>
                      Code has been sent to your number, Please enter the code to verify
                    </p>
                    <v-flex sm6 style="margin:auto;">
                      <v-text-field class="form-field"
                        v-model="verify_code"
                        :rules="[emptyRules, validCode]"
                        label="Code"
                        required
                      ></v-text-field>
                    </v-flex>
                    <v-btn id="signup-btn"
                        :disabled="codeEmpty"
                        @click="verify"
                      > 
                        <span v-if="!signingup">verify</span>
                        <hollow-dots-spinner
                          :animation-duration="1000"
                          :dot-size="9"
                          :dots-num="3"
                          color="#1b576f"
                          v-else
                        />
                    </v-btn>
                  </v-stepper-content>

                  <v-stepper-content step="3">
                    <p>Registration Successful</p>
                  </v-stepper-content>
                </v-stepper-items>
              </v-stepper>
            </v-flex>
          </v-layout>
        </v-container>
       
      </div>
    </div>
  </div>
</v-app>
</template>

<script>
import { HollowDotsSpinner } from 'epic-spinners'
export default {
  data () {
    return {
      valid: false,
      signingup: false,
      country_code: '',
      fname: '',
      code: '',
      el: 0,
      lname: '',
      phone: '',
      error: '',
      invalid_code: false,
      verify_code: '',
      emptyRules: [
        v => !!v || 'Field is required',
      ],
      showPassword: false,
      password: '',
      confirm_password: '',
      passwordRules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 6 || 'Min 6 characters',
      }
    }
  },
  components: {HollowDotsSpinner},
  computed: {
    // computed values for validations
    passwordConfirm () {
      return this.password === this.confirm_password || `Passwords don't match`
    },
    codeEmpty () {
      return this.verify_code === '' ? true : false
    },
    format () {
      return this.phone.charAt(0) !== '0' || 'Invalid Phone Number, omit leading "0" eg.8138XXXXXX'
    },
    phone_no () {
      return `+${this.country_code}${this.phone}`
    },
    validCode () {
      return !this.invalid_code || 'Code does not match'
    }
  },
  methods : {
    handleSubmit(e){
      e.preventDefault()
      // if form okay send code to phone
      if (this.valid) {
        this.signingup = true
        axios.post(`${location.href}api/message`, {phone_no: this.phone_no})
        .then(response => {
          if(response.data.response.status === 'error'){
            this.error = "An error occured, Please try again later"
            this.signingup = false
          } else {
            this.code = response.data.message // get the code sent so we can validate on client side 
            this.el = 2
            this.signingup = false
          }
        }).catch(error => {
          this.error = "An error occured, Please try again later"
          this.signingup = false
        })
      }
    },
    verify(e){
      e.preventDefault()
      // check if code matches, true ? register user
      this.signingup = true
      if (Number(this.verify_code) === this.code) {
        axios.post(`${location.href}api/register`, {
          first_name: this.fname,
          last_name: this.lname,
          country_code: this.country_code,
          phone_no: this.phone,
          password: this.password
        }).then(response => {
          this.signingup = false
          this.el = 3
        }).catch(error => {
          this.error = "An error occured, Please try again later"
          this.signingup = false
        })
      } else {
        // delay checked response a little so the dot spinner will flex small :)
        setTimeout(()=> {
          this.signingup = false
          this.invalid_code = true
        },3000)
      }
    }
  }
}
</script>

<style>
#logo-layout{
  height: 100vh;
}
#form-layout {
  padding-top: 60px;
}
#content-section {
  padding: 0;
}
#logo-section {
  background-color: skyblue;
}
h1{
  text-align: center;
}
.form-field {
  margin-bottom: 25px;
}
#signup-btn {
  border-radius: 20px;
  height: 41px;
  min-width: 130px;
  font-size: 15px;
}
#signup-btn:focus {
  outline: none;
}
.v-stepper {
  background: transparent !important;
  box-shadow: none;
  text-align: center;
}
.v-stepper p {
  font-size: 17px;
}
</style>
