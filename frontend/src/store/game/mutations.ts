import { MutationTree } from "vuex";
import { GameState, Subject } from "./types";

export const mutations: MutationTree<GameState> = {
  setStructure(state: GameState, payload: Subject[]): void {
    state.subjects = payload;
  },
  setActiveSubject(state: GameState, payload: Subject | null): void {
    state.activeSubject = payload;
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
    payload: { subject: Subject; x: number; y: number }
  ): void {
    if (!state.subjects) return;
    const index: number = state.subjects.findIndex(
      value => value === payload.subject
    );
    if (index === -1) return;
    state.subjects[index].xPos = payload.x;
    state.subjects[index].yPos = payload.y;
  },
  updateSubject(state: GameState, payload: Subject) {
    if (!state.subjects) return;
    const index: number = state.subjects.findIndex(value => value === payload);
    if (index === -1) return;
    state.subjects[index] = payload;
  }
};
