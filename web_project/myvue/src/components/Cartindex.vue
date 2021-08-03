<template>
  <div class="cart">
    <cartcontrol></cartcontrol>
  </div>
</template>

<script>
import Cartcontrol from "./Cartcontrol";

export default {
  name: "Cartindex",
  components:{
    cartcontrol: Cartcontrol,
  },
}
</script>

<style scoped>

</style>
