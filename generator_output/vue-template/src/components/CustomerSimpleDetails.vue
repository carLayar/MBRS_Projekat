<template>
    <div class="mt-1 ms-5 p-3 card shadow-sm w-75">
      <div v-if="customer" class="d-flex flex-column">
        <p class="my-1">id: {{ customer.id }}</p>
        <p class="my-1">name: {{ customer.name }}</p>
        <p class="my-1">surname: {{ customer.surname }}</p>
        <p class="my-1">email: {{ customer.email }}</p>
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
  