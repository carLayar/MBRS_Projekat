<template>
  <h1>Object List</h1>
  <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#modalAdd"
    @click="showAddModal">Add New</button>
  <table class="table">
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="object in objects" :key="object.id">
        <td>{{ object.id }}</td>
        <td>{{ object.name }}</td>
        <td>
          <button class="btn btn-primary mr-2" @click="viewDetails(object.id)">Details</button>
          <button class="btn btn-secondary" @click="showUpdateModal(object)"
          data-bs-toggle="modal" data-bs-target="#modalUpdate">Update</button>
        </td>
      </tr>
    </tbody>
  </table>

  <div class="modal fade" id="modalAdd" tabindex="-1" aria-labelledby="modalAddLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalAdd">Add New Object</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div>
            <input type="text" class="form-control" placeholder="Name" id="newName" v-model="addForm.name" required>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-success" type="submit">Add</button>
        </div>
      </div>
    </div>
  </div>

  <div class="modal fade" id="modalUpdate" tabindex="-1" aria-labelledby="modalUpdateLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalAdd">Update Object</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div>
            <input type="text" class="form-control" placeholder="Name" id="newName" v-model="updateForm.name" required>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-secondary" type="submit">Update</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      objects: [
        { id: 1, name: 'Object 1' },
        { id: 2, name: 'Object 2' },
      ],
      addForm: {
        name: '',
      },
      updateForm: {
        id: null,
        name: '',
      },
    };
  },
  methods: {
    showAddModal() {
      this.isAddModalVisible = true;
    },
    closeAddModal() {
      this.isAddModalVisible = false;
    },
    addObject() {
      const newId = this.objects.length ? Math.max(...this.objects.map(obj => obj.id)) + 1 : 1;
      const newObject = {
        id: newId,
        name: this.addForm.name,
      };
      this.objects.push(newObject);
      this.addForm.name = '';
      this.closeAddModal();
    },
    viewDetails(id) {
      this.$router.push({ name: 'Details', params: { id } });
    },
    showUpdateModal(object) {
      this.updateForm.id = object.id;
      this.updateForm.name = object.name;
    },
    closeUpdateModal() {
      this.isUpdateModalVisible = false;
    },
    updateObject() {
      const object = this.objects.find(obj => obj.id === this.updateForm.id);
      if (object) {
        object.name = this.updateForm.name;
      }
      this.closeUpdateModal();
    },
  },
};
</script>

<style scoped>

</style>
