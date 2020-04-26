import { GameState, Subject } from "@/store/game/types";
import { RootState } from "@/store/types";
import { GetterTree } from "vuex";

export const getters: GetterTree<GameState, RootState> = {
  subjectByCoord: (state: GameState) => (
    xPos: number,
    yPos: number
  ): Subject | null => {
    if (!state.subjects) return null;
    const subject = state.subjects.find(
      subj => subj.xPos === xPos && subj.yPos === yPos
    );
    return subject ? subject : null;
  },
  cellHighlight: (state: GameState) => (
    cellX: number,
    cellY: number
  ): boolean => {
    if (!state.subjects || !state.activeSubject) return false;
    return (
      (cellX - state.activeSubject.xPos) ** 2 +
        (cellY - state.activeSubject.yPos) ** 2 <=
      state.moveSpeed ** 2
    );
  },
  getMySubject: (state: GameState): Subject | null => {
    if (!state.subjects || !state.myId) return null;
    const subject = state.subjects.find(subj => {
      return subj.id === state.myId;
    });
    return subject ? subject : null;
  }
};
