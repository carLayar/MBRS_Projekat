<template>
  <div class="mt-5 w-75 ms-auto me-auto">
    <h1>Transaction List</h1>
    <button class="btn btn-success" @click="showAddModal">Add New</button>
    <table class="table">
      <thead>
        <tr>
          <th>id</th>
          <th>amount</th>
          <th>transactionDate</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="object in transactions" :key="object.id">
          <td>{{ object.id }}</td>
          <td>{{ object.amount }}</td>
          <td>{{ formatTransactionDate(object.transactionDate) }}</td>
          <td>
            <button class="btn btn-primary me-2" @click="viewDetails(object.id)">Details</button>
            <button class="btn btn-secondary" @click="showUpdateModal(object)">Update</button>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="modal fade" id="modalAdd" tabindex="-1" aria-labelledby="modalAddLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="modalAddLabel">Add New Transaction</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div>
              <input type="number" class="form-control" placeholder="amount" v-model="addForm.amount" required>
              <input type="date" class="form-control" placeholder="date" v-model="addForm.date" required>
              <!-- <input type="time" class="form-control" placeholder="time" v-model="addForm.time" required> -->
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
            <h5 class="modal-title" id="modalUpdateLabel">Update Transaction</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div>
              <input type="number" class="form-control" placeholder="amount" v-model="updateForm.amount" required>
              <input type="date" class="form-control" placeholder="date" v-model="updateForm.date" required>
              <input type="time" class="form-control" placeholder="time" v-model="updateForm.time" required>
            </div>
          </div>
          <div class="modal-footer">
            <button class="btn btn-secondary" type="submit" @click="updateObject">Update</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import TransactionService from '@/service/TransactionService';

export default {
  data() {
    return {
      transactions: [],
      addForm: {},
      updateForm: {},
    };
  },
  mounted() {
    this.fetchTransactions();
  },
  methods: {
    formatTransactionDate(date) {
      const year = date[0]; 
      const month = String(date[1]).padStart(2, '0');
      const day = String(date[2]).padStart(2, '0');
      const hour = String(date[3]).padStart(2, '0');
      const minute = String(date[4]).padStart(2, '0');

      const formattedDate = `${year}/${month}/${day} ${hour}:${minute}`;
      return formattedDate
    },
    fetchTransactions() {
      TransactionService.getAll().then(res => {
        this.transactions = res.data;
      }).catch(err => {
        console.log(err);
      });
    },
    showAddModal() {
      this.resetForm();
      this.clearModal();
      const modal = new bootstrap.Modal(document.getElementById('modalAdd'));
      modal.show();
    },
    showUpdateModal(transaction) {
      this.resetForm();
      this.updateForm = { ...transaction };
      
      const dateArray = transaction.transactionDate;
      const date = `${dateArray[0]}-${String(dateArray[1]).padStart(2, '0')}-${String(dateArray[2]).padStart(2, '0')}`;
      const time = `${String(dateArray[3]).padStart(2, '0')}:${String(dateArray[4]).padStart(2, '0')}`;

      this.updateForm.date = date;
      this.updateForm.time = time;
      this.clearModal();
      const modal = new bootstrap.Modal(document.getElementById('modalUpdate'));
      modal.show();
    },
    resetForm() {
      this.addForm = {};
      this.updateForm = {};
    },
    addObject() {
      const payload = {
        ...this.addForm,
        transactionDate: `${this.addForm.date}T00:00`,
      };
      TransactionService.create(payload).then(res => {
        this.transactions.push(res.data);
        this.fetchTransactions();
        this.clearModal();
      }).catch(err => {
        console.log(err);
      });
    },
    updateObject() {
      const payload = {
        ...this.updateForm,
        transactionDate: `${this.updateForm.date}T${this.updateForm.time}`,
      };
      TransactionService.update(payload.id, payload).then(_res => {
        this.fetchTransactions();
        this.clearModal();
      }).catch(err => {
        console.log(err);
      });
    },
    viewDetails(id) {
      this.$router.push({ name: 'TransactionDetails', params: { id } });
    },
    clearModal() {
      const modalAdd = document.getElementById('modalAdd');
      if (modalAdd) {
        modalAdd.classList.remove('show');
        document.body.classList.remove('modal-open');
        const modalBackdrop = document.querySelector('.modal-backdrop');
        if (modalBackdrop) {
          modalBackdrop.parentNode.removeChild(modalBackdrop);
        }
      }
      const modalUpdate = document.getElementById('modalUpdate');
      if (modalUpdate) {
        modalUpdate.classList.remove('show');
        document.body.classList.remove('modal-open');
        const modalBackdrop = document.querySelector('.modal-backdrop');
        if (modalBackdrop) {
          modalBackdrop.parentNode.removeChild(modalBackdrop);
        }
      }
    }
  }
};
</script>

