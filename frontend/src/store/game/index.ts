import { getters } from "@/store/game/getters";
import { Module } from "vuex";
import { actions } from "./actions";
import { mutations } from "./mutations";
import { GameState } from "./types";
import { RootState } from "../types";

export const state: GameState = {
  subjects: undefined,
  activeSubject: null,
  myId: 1,
  xSize: 15,
  ySize: 15,
  updateRate: 1000,
  moveSpeed: 4
};

const namespaced = true;

export const game: Module<GameState, RootState> = {
  namespaced,
  state,
  actions,
  mutations,
  getters
};
