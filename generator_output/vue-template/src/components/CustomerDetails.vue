<template>
  <div class="mt-5 w-75 ms-auto me-auto">
    <h1>Customer Details</h1>
    <div v-if="customer">
      <p>id: {{ customer.id }}</p>
      <p>name: {{ customer.name }}</p>
      <p>surname: {{ customer.surname }}</p>
      <p>email: {{ customer.email }}</p>
      <p>bankBranch: {{ customer.bankBranchId }}</p>
      <p>Accounts</p>
      <div v-for="account in customer.accounts" :key="account.id">
        <p>Account ID: {{ account.id }}</p>
        <p>Account Number: {{ account.accountNumber }}</p>
        <p>Balance: {{ account.balance }}</p>
        <hr>
      </div>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script>
import CustomerService from '@/service/CustomerService';

export default {
  data() {
    return {
      customer: null,
    };
  },
  created() {
    CustomerService.getById(this.$route.params.id).then(res => {
      this.customer = res.data;
    }).catch(err => {
      console.log(err);
    });
  }
};
</script>
