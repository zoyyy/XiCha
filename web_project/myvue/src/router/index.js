import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld,
      meta:{
        showFooter:true
      }
    },
    {
      path:'/goods',
      name:'Goods',
      component:() => import('../views/Goods'),
      meta:{
        showFooter:true
      }
    },
    {
      path:'/mine',
      name:'Mine',
      component:() => import('../views/Mine'),
      meta:{
        showFooter:true
      }
    },{
      path:'/myorders',
      name:'MyOrders',
      component:() => import('../views/MyOrders'),
      meta:{
        showFooter:true
      }
    },
    {
      path:'/order',
      name:'Order',
      component:() => import('../views/Order'),
      meta:{
        showFooter:true
      }
    }
  ]
})
