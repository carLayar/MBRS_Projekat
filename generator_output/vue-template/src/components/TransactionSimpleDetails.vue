<template>
    <div class="mt-1 w-75 ms-auto me-auto">
      <div v-if="transaction">
        <p>id: {{ transaction.id }}</p>
        <p>amount: {{ transaction.amount }}</p>
        <p>transactionDate: {{ transaction.transactionDate }}</p>
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
    </div>
  </template>
  
  <script>
  import TransactionService from '@/service/TransactionService';

  export default {
    props: ['id'],
    data() {
      return {
        transaction: null,
      };
    },
    created() {
      TransactionService.getById(this.id).then(res => {
        this.transaction = res.data;
      }).catch(err => {
        console.log(err);
      })
    }
  };
  </script>
  