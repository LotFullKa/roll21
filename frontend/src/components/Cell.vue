<template>
  <div
    class="cell"
    :highlight="isHighlighted"
    @click="cellClick({ x: cellId, y: rowId })"
  >
    <div
      class="subject"
      v-if="!!subject"
      :title="subject.name"
      :color="subject.color"
      :isDead="subject.isDead"
    >
      <template v-if="!subject.isDead">{{ subject.id }}</template>
    </div>
  </div>
</template>

<script lang="ts">
import { Subject } from "@/store/game/types";
import { Component, Prop, Vue } from "vue-property-decorator";
import { namespace } from "vuex-class";

const gameModule = namespace("game");

@Component
export default class Cell extends Vue {
  @Prop() rowId!: number;
  @Prop() cellId!: number;

  @gameModule.Getter
  subjectByCoord!: (posX: number, posY: number) => Subject | null;
  @gameModule.Getter
  cellHighlight!: (cellX: number, cellY: number) => boolean;
  @gameModule.Action("cellClick") cellClick!: (payload: {
    x: number;
    y: number;
  }) => void;

  get subject(): Subject | null {
    return this.subjectByCoord(this.cellId, this.rowId);
  }

  get isHighlighted(): boolean {
    return this.cellHighlight(this.cellId, this.rowId);
  }
}
</script>

<style scoped lang="sass">
.cell
  display: flex
  height: 30px
  width: 30px
  border: 1px solid black
  align-items: center
  justify-content: center

  &[highlight]
    background-color: lightgreen

.subject
  border-radius: 20px
  border: solid transparent
  color: white
  font-weight: bold
  height: 20px
  width: 20px
  display: inline-flex
  align-items: center
  justify-content: center
  position: relative

  &[color="red"]
    background-color: red

  &[color="blue"]
    background-color: blue

  &[color="green"]
    background-color: green

  &[isDead]
    background-color: gray

    &:after
      position: absolute
      content: "\274c"
      font-size: 20px
      font-weight: lighter
</style>
