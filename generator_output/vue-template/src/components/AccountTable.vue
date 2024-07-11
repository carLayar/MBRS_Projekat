<template>
  <div class="mt-5 w-75 ms-auto me-auto">
    <h1>Account List</h1>
    <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#modalAdd" @click="showAddModal">Add New</button>
    <table class="table">
      <thead>
        <tr>
          <th>id</th>
          <th>accountNumber</th>
          <th>balance</th>
          <th>customerId</th>
          <th>transactionIds</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="object in accounts" :key="object.id">
          <td>{{ object.id }}</td>
          <td>{{ object.accountNumber }}</td>
          <td>{{ object.balance }}</td>
          <td>{{ object.customerId }}</td>
          <td>{{ parseListProperty(object.transactionIds) }}</td>
          <td>
            <button class="btn btn-primary me-2" @click="viewDetails(object.id)">Details</button>
            <button class="btn btn-secondary" @click="showUpdateModal(object)"
            data-bs-toggle="modal" data-bs-target="#modalUpdate">Update</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>


  <div class="modal fade" id="modalAdd" tabindex="-1" aria-labelledby="modalAddLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalAdd">Add New Account</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div>
            <label>accountNumber</label>
            <input type="text" class="form-control" placeholder="accountNumber" id="newAccountNumber" v-model="addForm.accountNumber" required>
            <label>balance</label>
            <input type="number" class="form-control" placeholder="balance" id="newBalance" v-model="addForm.balance" required>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-success" type="submit" @click="addObject">Add</button>
        </div>
      </div>
    </div>
  </div>

  <div class="modal fade" id="modalUpdate" tabindex="-1" aria-labelledby="modalUpdateLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalAdd">Update Account</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div>
            <label>accountNumber</label>
            <input type="text" class="form-control" placeholder="accountNumber" id="newAccountNumber" v-model="updateForm.accountNumber" required>
            <label>balance</label>
            <input type="number" class="form-control" placeholder="balance" id="newBalance" v-model="updateForm.balance" required>
            
            <label>customer</label>
            <select class="form-select" v-model="selectedCustomer">
              <option :value="null">None</option>
              <option v-for="item in customers" :key="item.id" :value="item">{{item.id}}</option>
            </select>

            <label>transactions</label>
            <div v-for="item in currentTransactions" :key="item.id" class="d-flex justify-content-between list-item">
              <p>
                {{ item.id }}
              </p>
              <button type="button" @click="removeTransaction(item.id)">Delete</button>
            </div>
            <select class="form-select" v-model="newSelectedTransaction" @change="addTransaction">
              <option v-for="item in transactions" :key="item.id" :value="item">{{item.id}} - Mika </option>
            </select>            

          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-secondary" type="submit" @click="updateObject">Update</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AccountService from '@/service/AccountService';
import CustomerService from '@/service/CustomerService';
import TransactionService from '@/service/TransactionService';

export default {
  data() {
    return {
      accounts: [],
      addForm: {},
      updateForm: {},
      customers: [],
      transactions: [],

      selectedCustomer: null,

      currentTransactions: [],
      newSelectedTransaction: null
    };
  },

  mounted() {
    AccountService.getAll().then(res => {
      this.accounts = res.data;
    }).catch(err => {
      console.log(err);
    });

    CustomerService.getAll().then(res => {
      this.customers = res.data;
    }).catch(err => {
      console.log(err);
    });

    TransactionService.getAll().then(res => {
      this.transactions = res.data;
    }).catch(err => {
      console.log(err);
    });
  },

  methods: {
    showAddModal() {
      this.isAddModalVisible = true;
    },

    closeAddModal() {
      document.getElementById('modalAdd').click();
    },

    addObject() {
      AccountService.create(this.addForm).then(res => {
        this.accounts.push(res.data);
        this.resetForm();
        this.closeAddModal();
      }).catch(err => {
        console.log(err);
      });
    },

    viewDetails(id) {
      this.$router.push({ name: 'AccountDetails', params: { id } });
    },

    showUpdateModal(object) {
      this.selectedCustomer = null;
      this.updateForm = {...object};
      this.setSelectedCustomer(object.id);
      this.setCurrentTransactions(object.id);
    },

    closeUpdateModal() {
      document.getElementById('modalUpdate').click();
    },

    updateObject() {
      let payload = {...this.updateForm};
      payload.customer = this.selectedCustomer;
      payload.transactions = this.currentTransactions;
      AccountService.update(payload.id, payload).then(_res => {
        this.resetForm();
        window.location.reload();
      }).catch(err => {
        console.log(err);
      });
      this.closeUpdateModal();
    },

    resetForm() {
      this.addForm = {};
      this.updateForm = {};
    },

    setSelectedCustomer(accountId) {
      const obj = this.accounts.find(x => x.id === accountId);
      if (obj === undefined) {
        return;
      }
      const customerObj = this.customers.find(x => x.id === obj.customerId);
      if (customerObj === undefined) {
        return;
      }
      this.selectedCustomer = customerObj;
    },

    setCurrentTransactions(accountId) {
      const obj = this.accounts.find(x => x.id === accountId);
      if (obj === undefined) {
        return;
      }
      this.currentTransactions = this.transactions.filter(x => obj.transactionIds.includes(x.id));
    },

    addTransaction() {
      this.currentTransactions.push(this.newSelectedTransaction);
      this.newSelectedTransaction = null;
    },

    removeTransaction(transactionId) {
      this.currentTransactions = this.currentTransactions.filter(x => x.id !== transactionId);
    },

    parseListProperty(list) {
      if (!list) {
        return "";
      }
      return list.map(x => x.toString()).join(", ");
    }
  },
};
</script>

<style scoped>

</style>
  