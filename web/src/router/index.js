import Vue from 'vue'
import Router from 'vue-router'

// in development-env not use lazy-loading, because lazy-loading too many pages will cause webpack hot update too slow. so only in production use lazy-loading;
// detail: https://panjiachen.github.io/vue-element-admin-site/#/lazy-loading

Vue.use(Router)

/* Layout */

import Layout from '../views/layout/Layout'

/**
 * hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
 *                                if not set alwaysShow, only more than one route under the children
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noredirect           if `redirect:noredirect` will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar,
  }
 **/

export const constantRouterMap = [
  {path: '/login', component: () => import('@/views/login/index'), hidden: true},
  {path: '/404', component: () => import('@/views/404'), hidden: true},

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    name: 'Dashboard',
    meta: {title: 'SCRIPTS', icon: 'example'},
    hidden: true,
    children: [{
      path: 'dashboard',
      component: () => import('@/views/scripts/fieldTemplate')
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/scripts',
    name: 'scripts',
    meta: {title: 'SCRIPTS', icon: 'example'},
    children: [
      {
        path: 'fieldTemplate',
        name: 'fieldTemplate',
        component: () => import('@/views/scripts/fieldTemplate'),
        meta: {title: '字段模板', icon: 'table'}
      },
      {
        path: 'workTicket',
        name: 'workTicket',
        component: () => import('@/views/scripts/workTicket'),
        meta: {title: '工单生成', icon: 'table'}
      },
      {
        path: 'sqlAdapter',
        name: 'sqlAdapter',
        component: () => import('@/views/scripts/sqlAdapter'),
        meta: {title: 'SQL转换', icon: 'table'}
      },
      {
        path: 'strUtil',
        name: 'strUtil',
        component: () => import('@/views/scripts/stringUtil'),
        meta: {title: '字符串转换', icon: 'table'}
      },
      {
        path: 'attachment/:id',
        name: 'attachment',
        component: () => import('@/views/scripts/attachment'),
        meta: {title: '附件上传', icon: 'table', noCache: true},
        hidden: true
      },

      {
        path: 'market',
        name: 'market',
        component: () => import('@/views/shopping/market'),
        meta: {title: '超市管理', icon: 'table'}
      },
      {
        path: 'goodsClass',
        name: 'goodsClass',
        component: () => import('@/views/shopping/goodsClass'),
        meta: {title: '商品分类', icon: 'table'}
      },
      {
        path: 'repository',
        name: 'repository',
        component: () => import('@/views/shopping/repository'),
        meta: {title: '商品管理', icon: 'table'}
      },
      {
        path: 'show',
        name: 'show',
        component: () => import('@/views/shopping/show'),
        meta: {title: '货架管理', icon: 'table'}
      },
      {
        path: 'attachment/:id',
        name: 'attachment',
        component: () => import('@/views/shopping/attachment'),
        meta: {title: '图片上传', icon: 'table', noCache: true},
        hidden: true
      }
    ]
  },
]

export default new Router({
  // mode: 'history', //后端支持可开
  scrollBehavior: () => ({y: 0}),
  routes: constantRouterMap
})
