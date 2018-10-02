<template>
<div>
    <div ref="twitterList" class="twitter-list" >
        <table class="table" v-if="twitters.length > 0">
            <tbody>
            <tr v-for="row, id in twitters">
                <td>{{formatDate(row.tweetdate).t}}</td><td>{{row.nick}}</td> <td>{{row.tweet}}</td></tr>
            </tbody>
        </table>
        <p v-if="twitters.length === 0">No tweet's now</p>
    </div>
    <div>
        Default sort:
        <b-button-group class="mx-1">
            <b-btn @click="sortByNick" :class="{activ: sort==='nick'}">By nick</b-btn>
            <b-btn @click="sortByTweetdate" :class="{activ: sort==='tweetdate'}">By time</b-btn>
        </b-button-group>
    </div>
</div>
</template>

<script>
export default {
    name: 'TwittersList',
    props: ['update', 'limit'],
    data () {
        return {
            sort: 'tweetdate',
            twitters: [],
            interval: null,
        }
    },
    mounted () {
        this.loadData()
        this.interval = setInterval(() => {
            this.loadData()
        }, 10000)
    },
    beforeDestroy () {
        clearInterval(this.interval);
    },
    methods: {
        sortByNick () {
            this.sort = 'nick'
            this.loadData()
        },
        sortByTweetdate () {
            this.sort = 'tweetdate'
            this.loadData()
        },
        loadData () {
            let sortOptions = this.sort ? `?ordering=${this.sort}` : ''
            fetch(`http://localhost:8000/api/v1/twitters${sortOptions}`)
                .then((resp) => {
                    return resp.json()
                }).then((json) => {
                    this.twitters = json
                    this.$emit('load-complete', true)
                    this.scrollToEnd()
                })
        },
        formatDate (date) {
            let dd = new Date(date)
            return {t: dd.toTimeString().substr(0, 8)}
        },
        scrollToEnd: function () {
            let twitterList = this.$refs.twitterList
            twitterList.scrollTop = twitterList.scrollHeight
        }
    },
    watch: {
        update: function (val) {
            if (val) {
                this.loadData()
            }
        }
    }
}
</script>
<style scoped>
    .twitter-list {
        height:450px;
        overflow-y: auto;
    }
    .activ {
        background-color: cadetblue
    }
</style>
