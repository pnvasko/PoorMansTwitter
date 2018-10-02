<template>
    <div class="desktop-layout">
        <div class="top-head left">
            <div class="container">
                <div class="row">
                    <div class="col-md-8 col-lg-6">
                        <h1>Poor Man's Twitter <br/><small>v.0.0.1</small></h1>
                    </div>
                    <div class="col-md-6 col-lg-3 ml-auto admin-bar hidden-sm-down">
                        <nav class="nav nav-inline">
                            <a href="#" class="nav-link"><span class="ping"></span><i class="fa fa-envelope-o"></i></a>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
        <router-view></router-view>
    </div>
</template>
<script>
    export default {
        name: 'DesktopLayouts'
    }
</script>
<style>
    h1 {
        display: block;
    }
    .top-head {
        background: #141517;
        width: 100%;
        float: left;
        height: 100px;
    }
    .top-head h1 {
        color: #fff;
        font-size: 36px;
        font-weight: 600;
        margin: 18px 0 0;
    }
    .container {
        width: 100%;
        padding-right: 15px;
        padding-left: 15px;
        margin-right: auto;
        margin-left: auto;
    }
</style>
