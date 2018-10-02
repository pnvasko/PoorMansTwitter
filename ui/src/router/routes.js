let routes = [
    {
        path: '',
        component: () => import('../layouts/desktop.vue'),
        children: [
            { path: '', component: () => import('../pages/twitterIndex.vue') }
        ]
    }
]

if (process.env.MODE !== 'ssr') {
    routes.push({
        path: '*',
        component: () => import('../pages/error404.vue')
    })
}

export default routes
