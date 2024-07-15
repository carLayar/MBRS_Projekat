import { createRouter, createWebHistory } from 'vue-router'
import AccountTable from '../components/AccountTable.vue'
import AccountDetails from '../components/AccountDetails.vue'
import CustomerTable from '@/components/CustomerTable.vue';
import CustomerDetails from '@/components/CustomerDetails.vue';
import TransactionTable from '@/components/TransactionTable.vue';
import TransactionDetails from '@/components/TransactionDetails.vue';
import BankBranchTable from '@/components/BankBranchTable.vue';
import BankBranchDetails from '@/components/BankBranchDetails.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/account/table', name: 'AccountTable', component: AccountTable },
    { path: '/account/details/:id', name: 'AccountDetails', component: AccountDetails },
    {
      path: '/customer/table',
      name: 'CustomerTable',
      component: CustomerTable
    },
    {
      path: '/customer/details/:id',
      name: 'CustomerDetails',
      component: CustomerDetails,
      props: true
    },
    {
      path: '/transaction/table',
      name: 'TransactionTable',
      component: TransactionTable
    },
    {
      path: '/transaction/details/:id',
      name: 'TransactionDetails',
      component: TransactionDetails,
      props: true
    },
    {
      path: '/bankBranch/table',
      name: 'BankBranchTable',
      component: BankBranchTable
    },
    {
      path: '/bankBranch/details/:id',
      name: 'BankBranchDetails',
      component: BankBranchDetails,
      props: true
    }
  ]
})

export default router