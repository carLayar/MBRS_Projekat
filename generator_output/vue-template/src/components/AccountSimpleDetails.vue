<template>
    <div class="mt-5 w-75 ms-auto me-auto">
      <div v-if="account">
        <p>id: {{ account.id }}</p>
        <p>accountNumber: {{ account.accountNumber }}</p>
        <p>balance: {{ account.balance }}</p>
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
    </div>
  </template>
  
  <script>
  import AccountService from '@/service/AccountService';

  export default {
    props: ['id'],
    data() {
      return {
        account: null,
      };
    },
    created() {
      AccountService.getById(this.id).then(res => {
        this.account = res.data;
      }).catch(err => {
        console.log(err);
      })
    },
    methods: {
    },
  };
  </script>
  