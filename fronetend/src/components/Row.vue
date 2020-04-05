<template>
  <div class="row">
    <Cell
      v-for="j in cellCount"
      :key="`row${rowId}cell${j}`"
      :row-id="rowId"
      :cell-id="j"
    />
  </div>
</template>

<script lang="ts">
import Cell from "@/components/Cell.vue";
import { Vue, Component, Prop } from "vue-property-decorator";
@Component({
  components: { Cell }
})
export default class Row extends Vue {
  @Prop() rowId!: number;
  @Prop() cellCount!: number;
}
</script>

<style scoped lang="sass">
.row
  display: flex
  flex-wrap: nowrap
  justify-content: center
</style>
