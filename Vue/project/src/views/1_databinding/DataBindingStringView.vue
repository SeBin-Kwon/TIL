<template>
  <div>
    <h1>Hello {{ userName }}</h1>
    <p>{{ message }}</p>
  </div>
</template>
<script>
export default {
  data() {
    return {
      userName: 'John Doe',
      message: 'Welcome 세빈이의 뷰 연습',
      arr: [],
      obj: {}
    }
  }
}
</script>
<style scoped>
</style>
