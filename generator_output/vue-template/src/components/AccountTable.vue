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
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="object in accounts" :key="object.id">
          <td>{{ object.id }}</td>
          <td>{{ object.accountNumber }}</td>
          <td>{{ object.balance }}</td>
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
            <label class="my-1">accountNumber</label>
            <input type="text" class="form-control" id="newAccountNumber" v-model="addForm.accountNumber" required>

            <label class="my-1">balance</label>
            <input type="number" class="form-control" id="newBalance" v-model="addForm.balance" required>
            
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
            <label class="my-1">accountNumber</label>
            <input type="text" class="form-control" id="newAccountNumber" v-model="updateForm.accountNumber" required>
            <label class="my-1">balance</label>
            <input type="number" class="form-control" id="newBalance" v-model="updateForm.balance" required>
            
            <label class="my-1">customer</label>
            <!-- dropbox -->
            <select class="form-select" v-model="selectedCustomer">
              <option :value="null">None</option>
              <option v-for="item in customers" :key="item.id" :value="item">{{item.id}}</option>
            </select>

            <label class="my-1">transactions</label>

            <!-- display selected transactions -->
            <div v-for="item in currentTransactions" :key="item.id" class="d-flex justify-content-between list-item">
              <div>
                {{ item.id }}
              </div>
              <button type="button" @click="removeTransaction(item.id)" class="btn-delete-item">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="28" viewBox="0 0 24 24">
                  <path fill="#ffffff" d="M3 6v18h18v-18h-18zm5 14c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm4-18v2h-20v-2h5.711c.9 0 1.631-1.099 1.631-2h5.315c0 .901.73 2 1.631 2h5.712z"/>
                </svg>
              </button>
            </div>
            
            <!-- dropbox -->
            <select class="form-select mt-3" v-model="newSelectedTransaction" @change="addTransaction">
              <option :value="null">None</option>
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
// import service of generated type
import AccountService from '@/service/AccountService';

// import services for all linked types
import CustomerService from '@/service/CustomerService';
import TransactionService from '@/service/TransactionService';

export default {
  data() {
    return {
      accounts: [],   // list of entities for dispplay
      addForm: {},
      updateForm: {},

      customers: [],        // linked entity list used for update
      transactions: [],     // linked entity list used for update

      // [for single linked entity add selected{{model.class_name}} property]
      selectedCustomer: null,   // used for update

      // [for multiple linked entity add current{{model.class_name}}s property]
      currentTransactions: [],    // used for update
      // [for multiple linked entity add newSelected{{model.class_name}}]
      newSelectedTransaction: null, // used for update
    };
  },

  mounted() {
    // get all entities of generated type
    AccountService.getAll().then(res => {
      this.accounts = res.data;
    }).catch(err => {
      console.log(err);
    });

    // get all entities of linked type
    CustomerService.getAll().then(res => {
      this.customers = res.data;
    }).catch(err => {
      console.log(err);
    });

    // get all entities of linked type
    TransactionService.getAll().then(res => {
      this.transactions = res.data;
    }).catch(err => {
      console.log(err);
    });
  },

  methods: {

    // BEGIN Add related methods 
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

    // END Add related methods

    
    // BEGIN Update related methods
    showUpdateModal(object) {
      this.updateForm = {...object};

      // for single linked entity
      this.setSelectedCustomer(object.id);

      // for multiple linked entity
      this.setCurrentTransactions(object.id);
    },

    closeUpdateModal() {
      document.getElementById('modalUpdate').click();
    },

    updateObject() {
      let payload = {...this.updateForm};

      payload.customer = this.selectedCustomer;           // this is dynamic
      payload.transactions = this.currentTransactions;    // this is dynamic

      AccountService.update(payload.id, payload)
      .then(_res => {
        this.resetForm();
        window.location.reload();
      })
      .catch(err => {
        console.log(err);
      });

      this.closeUpdateModal();
    },

    // update util
    setSelectedCustomer(accountId) {
      this.selectedCustomer = null;

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

    // update util
    setCurrentTransactions(accountId) {
      const obj = this.accounts.find(x => x.id === accountId);
      if (obj === undefined) {
        return;
      }
      this.currentTransactions = this.transactions.filter(x => obj.transactionIds.includes(x.id));
    },

    // update util, [for multiple linked entity]
    addTransaction() {
      this.currentTransactions.push(this.newSelectedTransaction);
      this.newSelectedTransaction = null;
    },
    // update util
    removeTransaction(transactionId) {
      this.currentTransactions = this.currentTransactions.filter(x => x.id !== transactionId);
    },

    // END Update related methods

    // BEGIN Details related methods 
    viewDetails(id) {
      this.$router.push({ name: 'AccountDetails', params: { id } });
    },
    // END Details related methods

    // util methods
    resetForm() {
      this.addForm = {};
      this.updateForm = {};
    },

  },
};
</script>

<style scoped>
.list-item {
  border: 1px solid #bdc5ca;
  margin-bottom: 2px;
  border-radius: 4px;
  padding: 3px 5px 3px 10px;
  display: flex;
  align-items: center;
}

.btn-delete-item {
  background-color: #d53243;
  border: none;
  border-radius: 3px;
  padding: 3px 7px;
}
</style>
  