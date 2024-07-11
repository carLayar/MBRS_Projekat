<template>
  <div class="mt-5 w-75 ms-auto me-auto">
    <h1>Bank Branch List</h1>
    <button class="btn btn-success" @click="showAddModal">Add New</button>
    <table class="table">
      <thead>
        <tr>
          <th>id</th>
          <th>branchName</th>
          <th>location</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="object in branches" :key="object.id">
          <td>{{ object.id }}</td>
          <td>{{ object.branchName }}</td>
          <td>{{ object.location }}</td>
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
            <h5 class="modal-title" id="modalAddLabel">Add New Branch</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div>
              <input type="text" class="form-control" placeholder="branchName" v-model="addForm.branchName" required>
              <input type="text" class="form-control" placeholder="location" v-model="addForm.location" required>
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
            <h5 class="modal-title" id="modalUpdateLabel">Update Branch</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div>
              <input type="text" class="form-control" placeholder="branchName" v-model="updateForm.branchName" required>
              <input type="text" class="form-control" placeholder="location" v-model="updateForm.location" required>
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
import BankBranchService from '@/service/BankBranchService';

export default {
  data() {
    return {
      branches: [],
      addForm: {},
      updateForm: {},
    };
  },
  mounted() {
    this.fetchBranches();
  },
  methods: {
    fetchBranches() {
      BankBranchService.getAll().then(res => {
        this.branches = res.data;
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
    showUpdateModal(branch) {
      this.resetForm();
      this.updateForm = { ...branch };
      this.clearModal();
      const modal = new bootstrap.Modal(document.getElementById('modalUpdate'));
      modal.show();
    },
    resetForm() {
      this.addForm = {};
      this.updateForm = {};
    },
    addObject() {
      BankBranchService.create(this.addForm).then(res => {
        this.branches.push(res.data);
        this.fetchBranches();
        this.clearModal();
      }).catch(err => {
        console.log(err);
      });
    },
    updateObject() {
      BankBranchService.update(this.updateForm.id, this.updateForm).then(_res => {
        this.fetchBranches();
        this.clearModal();
      }).catch(err => {
        console.log(err);
      });
    },
    viewDetails(id) {
      this.$router.push({ name: 'BankBranchDetails', params: { id } });
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
