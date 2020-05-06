<template>
  <div class="field">
    <Row
      v-for="i in ySize"
      :key="`row${i - 1}`"
      :cell-count="xSize"
      :row-id="i - 1"
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
  @gameModule.Action("fetchData") fetchData!: () => void;

  interval!: number;

  created(): void {
    this.fetchData();
    this.interval = setInterval(this.loadUpdate, 1000);
  }

  beforeDestroy(): void {
    clearInterval(this.interval);
  }

  loadUpdate(): void {
    // this.fetchData();
    console.log("UPDATE");
  }
}
</script>

<style scoped lang="sass"></style>
