<script setup>
</script>

<template>
    <div class="d-flex justify-content-center">
        <div>
            <h3>Congratulations on successfully generating your app</h3>
            <div class="contain card shadow">
                <div class="card-body">
                    <div class="link">To take a peek at your <b>&nbsp;customer&nbsp;</b> table, go to <a href="/customer/table">/customer/table</a></div>
                    <div class="link">To take a peek at your <b>&nbsp;account&nbsp;</b> table, go to <a href="/account/table">/account/table</a></div>
                    <div class="link">To take a peek at your <b>&nbsp;bank branch&nbsp;</b> table, go to <a href="/bankBranch/table">/bankBranch/table</a></div>
                    <div class="link">To take a peek at your <b>&nbsp;transaction&nbsp;</b> table, go to <a href="/transaction/table">/transaction/table</a></div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
h3 {
    font-weight: 600;
    margin-top: 35px;
}

a {
    margin-left: 5px;
    border: 1px solid #0d6efd;
    padding: 1px 7px;
    border-radius: 3px;
    text-decoration: none;
    background-color: #0d6efd;
    color: white;
    font-weight: 600;
}

a:hover {
    background-color: #0d5fda;
    text-decoration: underline;
}

.link {
    margin: 20px 0;
    display: flex;
    justify-content: left;
}

.contain {
    margin-top: 50px;
}
</style>
