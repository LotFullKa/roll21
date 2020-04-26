import { MutationTree } from "vuex";
import { GameState, Subject } from "./types";

export const mutations: MutationTree<GameState> = {
  setStructure(state: GameState, payload: Subject[]): void {
    state.subjects = payload;
  },
  toggleActiveSubject(state: GameState, payload: Subject | null): void {
    state.activeSubject = state.activeSubject === payload ? null : payload;
  },
  setSubjectHp(state: GameState, payload: { id: number; hp: number }): void {
    if (!state.subjects) return;
    const index: number | null = state.subjects.findIndex(
      value => value.id === payload.id
    );
    if (!index) return;
    state.subjects[index].hp = payload.hp;
  },
  setSubjectPos(
    state: GameState,
    payload: { id: number; x: number; y: number }
  ): void {
    if (!state.subjects) return;
    const index: number | null = state.subjects.findIndex(
      value => value.id === payload.id
    );
    if (!index) return;
    state.subjects[index].xPos = payload.x;
    state.subjects[index].yPos = payload.y;
  }
};
