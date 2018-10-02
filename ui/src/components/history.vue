<template>
<div class="twitter-msg">
    <div class="container">
        <div class="row">
            <div class="col-lg-12" >
                <b-card class="mb-2">
                    <twitters-list limit="0"></twitters-list>
                </b-card>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import TwittersList from './twittersList'
export default {
    name: 'TwitterHistory',
    components: {
        TwittersList
    },
    data () {
        return { }
    }
}
</script>
<style scoped> </style>
