<template>
  <div class="field">
    <Row
      v-for="i in ySize"
      :key="`row${i}`"
      :cell-count="xSize"
      :row-id="i"
    ></Row>
  </div>
</template>

<script lang="ts">
import Row from "@/components/Row.vue";
import { Component, Vue } from "vue-property-decorator";
import { namespace } from "vuex-class";

const gameModule = namespace("game");
@Component({
  components: { Row }
})
export default class Field extends Vue {
  @gameModule.State(state => state.xSize) xSize!: number;
  @gameModule.State(state => state.ySize) ySize!: number;
}
</script>

<style scoped lang="sass">
</style>
