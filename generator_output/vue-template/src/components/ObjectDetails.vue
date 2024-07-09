<template>
  <div class="mt-5 w-75 ms-auto me-auto">
    <h1>Object Details</h1>
    <div v-if="object">
      <p>ID: {{ object.id }}</p>
      <p>Name: {{ object.name }}</p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      object: null,
    };
  },
  created() {
    this.getObjectDetails(this.$route.params.id);
  },
  methods: {
    getObjectDetails(id) {
      const mockObjects = [
        { id: 1, name: 'Object 1' },
        { id: 2, name: 'Object 2' },
      ];
      this.object = mockObjects.find((obj) => obj.id === parseInt(id));
    },
  },
};
</script>
