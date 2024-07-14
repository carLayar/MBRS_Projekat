<template>
  <div class="py-5 min-vh-100 is-fullheight">
    <div class="w-50 ms-auto me-auto">
      <h1>Account Details</h1>
      <div v-if="account" class="d-flex flex-column card bg-light shadow p-4 contain">
        <label class="my-1">id</label>
        <input :value="account.id" disabled />

        <label class="my-1">accountNumber</label>
        <input :value="account.accountNumber" disabled />

        <label class="my-1">balance</label>
        <input :value="account.balance" disabled />

        <label class="my-1">customer</label>
        <CustomerSimpleDetails :id="account.customerId" />
        <label class=my-1>transactions</label>
        <div v-for="item in account.transactionIds" :key="item">
          <TransactionSimpleDetails :id="item"/>
        </div>
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
    </div>
  </div>
  </template>
  
  <script>
  import AccountService from '@/service/AccountService';
  import CustomerSimpleDetails from '@/components/CustomerSimpleDetails.vue';
  import TransactionSimpleDetails from '@/components/TransactionSimpleDetails.vue'

  export default {
    components: {
      CustomerSimpleDetails,
      TransactionSimpleDetails
    },
    data() {
      return {
        account: null,
      };
    },
    created() {
      AccountService.getById(this.$route.params.id).then(res => {
        this.account = res.data;
      }).catch(err => {
        console.log(err);
      })
    }
  };
  </script>
  
  <style scoped>
    input {
      width: fit-content;
      padding: 4px 7px;
    }
    label {
      font-weight: 600;
      font-size: 18px;
    }
  </style>