#!/usr/bin/env bash

function run_python_setup {
    source ../env/bin/activate
}

function clear_assets_folder {
    cd assets
    rm -rf css
    rm -rf js
    cd ..
}
function clear_index_template {
    cd templates
    rm -f index.html
    cd ..
}
function build_vue_app {
    cd ui
    yarn build
    cd ..
}

function copy_css_file {
    mkdir assets/css
    cp ui/dist/css/* assets/css
}

function copy_js_file {
    mkdir assets/js
    cp ui/dist/js/* assets/js
}

function copy_html_file {
    cp ui/dist/index.html templates/
}

main () {
    clear_assets_folder
    clear_index_template
    build_vue_app
    copy_css_file
    copy_js_file
    copy_html_file
}

main
