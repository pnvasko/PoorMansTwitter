<template>
  <div class="twitter-msg">
    <div class="container">
      <div class="row">
        <div class="col-lg-12" v-if="currentName!==''" >
          You nick name: {{currentName}}
            <b-card class="mb-2">
              <twitters-list
                      :update="newTwitt"
                      limit="20"
                      @load-complete="loadComplete"></twitters-list>
            </b-card>
            <div class="container-fluid">
              <div class="row">
                <div class="col-lg-10">
                  <b-form-input
                          type="text"
                          v-model="message"
                          maxlength="50"
                          placeholder="Enter you message"></b-form-input>
                  <div class="invalid-feedback" :class="{visible: error.message }">
                    Please type you message.
                  </div>
                </div>
                <div class="col-md-auto">
                  <b-button variant="primary" @click="newTwitter">Post</b-button>
                </div>
              </div>
            </div>
        </div>
        <div class="col-lg-4" v-if="currentName===''">
            <b-card title="Join to twitter" style="max-width: 20rem;" class="mb-2">
              <b-form-input type="text"
                            v-model="nameSelected"
                            placeholder="Enter you nick name"></b-form-input>
              <div class="invalid-feedback" :class="{visible: error.nameSelected }">
                Please type you nick name.
              </div>
            </b-card>
            <b-button variant="primary" @click="join">Join</b-button>
        </div>
      </div>

    </div>


  </div>
</template>

<script>
import TwittersList from './twittersList'
export default {
    name: 'Twitter',
    props: ['username'],
    components: {
        TwittersList
    },
    data () {
        return {
            newTwitt: false,
            message: '',
            nameSelected: '',
            error: {
                nameSelected: false,
                message: false
            }
        }
    },
    computed: {
       currentName () {
           return this.username ? this.username : ''
       }
    },
    methods: {
        join () {
          console.log('join')
          this.error.nameSelected = (this.nameSelected === '')
          if (this.error.nameSelected) {
              return false
          }
          this.$emit('join-to-twitter', this.nameSelected)
        },
        newTwitter () {
            this.error.message = (this.message === '')
            if (this.error.message) {
                return false
            }
            (async () => {
                const rawResponse = await fetch('http://localhost:8000/api/v1/twitter', {
                    method: 'POST',
                    headers: {'Accept': 'application/json','Content-Type': 'application/json'},
                    body: JSON.stringify({nick: this.currentName, tweet: this.message})
                })
                const content = await rawResponse.json()
            })();

            this.message = ''
            this.error.message = false
            this.newTwitt = true
        },
        loadComplete () {
            this.newTwitt = false
        }
    }
}
</script>
<style scoped>
  .twitter-msg{
    padding-top: 15px;
  }
  .visible {
    display: block;
  }
</style>
