<script setup>
</script>

<template>
    <div class="d-flex justify-content-center">
        <div>
            <h3>Congratulations on successfully generating your app</h3>

            <div class="link">To take a peek at your customer table, go to <a href="/customer/table">/customer/table</a> url</div>
            <div class="link">To take a peek at your account table, go to <a href="/account/table">/table</a> url</div>
            <div class="link">To take a peek at your bank branch table, go to <a href="/bankBranch/table">/table</a> url</div>
            <div class="link">To take a peek at your transaction table, go to <a href="/transaction/table">/table</a> url</div>
        </div>
    </div>
</template>

<style scoped>
a {
    border: 1px solid black;
    padding: 5px 10px;
    border-radius: 7px;
    text-decoration: none;
}

.link {
    margin: 30px 0;
}
</style>
