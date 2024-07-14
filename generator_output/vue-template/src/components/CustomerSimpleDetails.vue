<template>
    <div class="mt-1 ms-5 p-3 card shadow-sm w-75">
      <div v-if="customer" class="d-flex flex-column">
        <label class="my-1">id</label>
        <input class="p-1" :value="customer.id" disabled />
        
        <label class="my-1">name</label>
        <input class="p-1":value="customer.name" disabled />
        
        <label class="my-1">surname</label>
        <input class="p-1" :value="customer.surname" disabled />
        
        <label class="my-1">email</label>
        <input class="p-1" :value="customer.email" disabled />
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
  