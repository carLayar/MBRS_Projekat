<template>
    <div class="mt-1 w-75 ms-auto me-auto">
      <div v-if="customer">
        <p>id: {{ customer.id }}</p>
        <p>name: {{ customer.name }}</p>
        <p>surname: {{ customer.surname }}</p>
        <p>email: {{ customer.email }}</p>
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
    </div>
  </template>
  
  <script>
  import CustomerService from '@/service/CustomerService';

  export default {
    props: ['id'],
    data() {
      return {
        customer: null,
      };
    },
    created() {
      CustomerService.getById(this.id).then(res => {
        this.customer = res.data;
      }).catch(err => {
        console.log(err);
      })
    }
  };
  </script>
  