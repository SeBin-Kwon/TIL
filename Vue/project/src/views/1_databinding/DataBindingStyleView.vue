<template>
  <div>
    <div :style="style1">스타일 바인딩: 글씨는 green, 폰트크기: 30px</div>
    <button @click="style1.color='blue'">색상 바꾸기</button>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      style1: {
        color: 'green',
        fontSize: '30px'
      }
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
