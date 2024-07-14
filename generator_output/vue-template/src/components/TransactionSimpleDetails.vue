<template>
    <div class="mt-1 ms-5 p-3 card shadow-sm w-75">
      <div v-if="transaction" class="d-flex flex-column">
        <label class="my-1">id</label>
        <input class="p-1" :value="transaction.id" disabled />

        <label class="my-1">amount</label>
        <input class="p-1" :value="transaction.amount" disabled />

        <label class="my-1">transactionDate</label>
        <input class="p-1" :value="formatDate(transaction.transactionDate)" disabled />
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

