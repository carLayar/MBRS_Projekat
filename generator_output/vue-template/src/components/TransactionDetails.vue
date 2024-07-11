<template>
  <div class="mt-5 w-75 ms-auto me-auto">
    <h1>Transaction Details</h1>
    <div v-if="transaction">
      <p>id: {{ transaction.id }}</p>
      <p>amount: {{ transaction.amount }}</p>
      <p>date: {{ transaction.transactionDate }}</p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script>
import TransactionService from '@/service/TransactionService';

export default {
  data() {
    return {
      transaction: null,
    };
  },
  created() {
    TransactionService.getById(this.$route.params.id).then(res => {
      this.transaction = res.data;
    }).catch(err => {
      console.log(err);
    });
  }
};
</script>
