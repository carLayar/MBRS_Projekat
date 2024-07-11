<template>
  <div class="mt-5 w-75 ms-auto me-auto">
    <h1>Bank Branch Details</h1>
    <div v-if="branch">
      <p>id: {{ branch.id }}</p>
      <p>branchName: {{ branch.branchName }}</p>
      <p>location: {{ branch.location }}</p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script>
import BankBranchService from '@/service/BankBranchService';

export default {
  data() {
    return {
      branch: null,
    };
  },
  created() {
    BankBranchService.getById(this.$route.params.id).then(res => {
      this.branch = res.data;
    }).catch(err => {
      console.log(err);
    });
  }
};
</script>
