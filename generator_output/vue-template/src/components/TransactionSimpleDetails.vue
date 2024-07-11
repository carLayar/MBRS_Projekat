<template>
    <div class="mt-1 w-75 ms-auto me-auto">
      <div v-if="transaction">
        <p>id: {{ transaction.id }}</p>
        <p>amount: {{ transaction.amount }}</p>
        <p>transactionDate: {{ formatDate(transaction.transactionDate) }}</p>
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
    },
    methods: {
      formatDate(date) {
        const year = date[0]; 
        const month = String(date[1]).padStart(2, '0');
        const day = String(date[2]).padStart(2, '0');
        const hour = String(date[3]).padStart(2, '0');
        const minute = String(date[4]).padStart(2, '0');

        const formattedDate = `${day}.${month}.${year}. ${hour}:${minute}`;
        return formattedDate
      },
    }
  };
  </script>
  