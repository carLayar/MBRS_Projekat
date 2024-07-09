import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ObjectDetails from '../components/ObjectDetails.vue'
import ObjectTable from '../components/ObjectTable.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/table', name: 'Table', component: ObjectTable },
    { path: '/details/:id', name: 'Details', component: ObjectDetails },
    {
      path: '/',
      name: 'home',
      component: HomeView
    }
  ]
})

export default router
