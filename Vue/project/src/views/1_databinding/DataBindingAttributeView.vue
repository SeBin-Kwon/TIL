<template>
  <div>
    <input type="text" name="" id="" v-bind:value="userId" readonly />
    <input type="text" name="" id="" :value="userId" readonly />
    <br>
    <img :src="imgSrc" alt="" style="width:100px; height:auto;">
    <br>
    <input type="search" name="" id="" v-model="txt1" />
    <button :disabled="txt1 ===''">조회</button>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      userId: 'sebin',
      imgSrc: 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Vue.js_Logo_2.svg/1184px-Vue.js_Logo_2.svg.png',
      txt1: ''
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>

<style scoped></style>
