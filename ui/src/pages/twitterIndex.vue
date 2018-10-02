<template>
  <div class="twitter-index">
    <b-button variant="primary" @click="selectMode()">{{selectButtonTxt}}</b-button>
    <twitter
            v-if="modeTwitter"
            :username="currentusername"
            @join-to-twitter="userJoinToTwitter">
    </twitter>
    <history v-if="!modeTwitter"></history>
  </div>
</template>

<script>
import Twitter from '../components/twitter'
import History from '../components/history'
export default {
  name: 'TwitterIndex',
  components: {
      Twitter,
      History
  },
  data () {
      return {
          currentusername: '',
          modeTwitter: true,
          selectButtonTxt: 'Go history'
      }
  },
  methods: {
      selectMode () {
        this.modeTwitter = ! this.modeTwitter
        this.selectButtonTxt = !this.modeTwitter ? 'Go twitter' : 'Go history'
      },
      userJoinToTwitter (nickname) {
          this.currentusername = nickname
      }

  }
}
</script>

<style scoped>
    .twitter-index {
      padding-top: 125px;
      padding-left: 25px;
    }
</style>
