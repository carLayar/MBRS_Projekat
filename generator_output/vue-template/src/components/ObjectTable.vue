<template>
  <div>
    <h1>Object List</h1>
    <button @click="showAddModal">Add New</button>
    <table>
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
            <button @click="viewDetails(object.id)">Details</button>
            <button @click="showUpdateModal(object)">Update</button>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-if="isAddModalVisible" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeAddModal">&times;</span>
        <h2>Add New Object</h2>
        <form @submit.prevent="addObject">
          <div>
            <label for="newName">Name:</label>
            <input type="text" id="newName" v-model="addForm.name" required>
          </div>
          <button type="submit">Add</button>
        </form>
      </div>
    </div>

    <div v-if="isUpdateModalVisible" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeUpdateModal">&times;</span>
        <h2>Update Object</h2>
        <form @submit.prevent="updateObject">
          <div>
            <label for="updateName">Name:</label>
            <input type="text" id="updateName" v-model="updateForm.name" required>
          </div>
          <button type="submit">Update</button>
        </form>
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
      isAddModalVisible: false,
      isUpdateModalVisible: false,
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
      this.isUpdateModalVisible = true;
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

<style>
.modal {
  display: flex;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: gray;
  color: white;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 500px;
}

.close {
  color: white;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>
