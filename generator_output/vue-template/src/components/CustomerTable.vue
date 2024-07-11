<template>
  <div class="mt-5 w-75 ms-auto me-auto">
    <h1>Customer List</h1>
    <button class="btn btn-success" @click="showAddModal">Add New</button>
    <table class="table">
      <thead>
        <tr>
          <th>id</th>
          <th>name</th>
          <th>surname</th>
          <th>email</th>
          <th>bankBranch</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="customer in customers" :key="customer.id">
          <td>{{ customer.id }}</td>
          <td>{{ customer.name }}</td>
          <td>{{ customer.surname }}</td>
          <td>{{ customer.email }}</td>
          <td>{{ customer.bankBranchId }}</td>
          <td>
            <button class="btn btn-primary me-2" @click="viewDetails(customer.id)">Details</button>
            <button class="btn btn-secondary" @click="showUpdateModal(customer)">Update</button>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="modal fade" id="modalAdd" tabindex="-1" aria-labelledby="modalAddLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="modalAddLabel">Add New Customer</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div>
              <input type="text" class="form-control mb-2" placeholder="Name" v-model="addForm.name" required>
              <input type="text" class="form-control mb-2" placeholder="Surname" v-model="addForm.surname" required>
              <input type="email" class="form-control mb-2" placeholder="Email" v-model="addForm.email" required>
              <input type="number" class="form-control mb-2" placeholder="Bank Branch ID" v-model="addForm.bankBranch.id" required>
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
            <h5 class="modal-title" id="modalUpdateLabel">Update Customer</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div>
              <input type="text" class="form-control mb-2" placeholder="Name" v-model="updateForm.name" required>
              <input type="text" class="form-control mb-2" placeholder="Surname" v-model="updateForm.surname" required>
              <input type="email" class="form-control mb-2" placeholder="Email" v-model="updateForm.email" required>
              <input type="number" class="form-control mb-2" placeholder="Bank Branch ID" v-model="updateForm.bankBranch.id" required>
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
import CustomerService from '@/service/CustomerService';

export default {
  data() {
    return {
      customers: [],
      addForm: {
        name: '',
        surname: '',
        email: '',
        bankBranch: {
          id: null,
        },
      },
      updateForm: {
        id: null,
        name: '',
        surname: '',
        email: '',
        bankBranch: {
          id: null,
        },
      },
    };
  },
  mounted() {
    this.fetchCustomers();
  },
  methods: {
    fetchCustomers() {
      CustomerService.getAll().then(res => {
        this.customers = res.data;
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
    showUpdateModal(customer) {
      this.resetForm();
      this.updateForm = {
        ...customer,
        bankBranch: { id: customer.bankBranchId },
      };
      this.clearModal();
      const modal = new bootstrap.Modal(document.getElementById('modalUpdate'));
      modal.show();
    },
    resetForm() {
      this.addForm = {
        name: '',
        surname: '',
        email: '',
        bankBranch: {
          id: null,
        },
      };
      this.updateForm = {
        id: null,
        name: '',
        surname: '',
        email: '',
        bankBranch: {
          id: null,
        },
      };
    },
    addObject() {
      const customerData = {
        ...this.addForm,
      };
      CustomerService.create(customerData).then(res => {
        this.customers.push(res.data);
        this.fetchCustomers();
        this.clearModal();
      }).catch(err => {
        console.log(err);
      });
    },
    updateObject() {
      const customerData = {
        ...this.updateForm,
      };
      CustomerService.update(this.updateForm.id, customerData).then(_res => {
        this.fetchCustomers();
        this.clearModal();
      }).catch(err => {
        console.log(err);
      });
    },
    viewDetails(id) {
      this.$router.push({ name: 'CustomerDetails', params: { id } });
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
