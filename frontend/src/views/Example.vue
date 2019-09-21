<template>
  <div class="example">
    <h1>First Single File Componenet</h1>
    <h3>{{ message }}</h3>
  </div>
</template>

<script>
export default {
    name: "example",
    data() {
        return {
            message: "Hello World Example!"
        }
    }
}
</script>

<style scoped>
    h1 {
        color: red;
    }


</style>