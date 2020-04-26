import { ActionTree } from "vuex";
import { GameState, Subject } from "./types";
import { RootState } from "../types";
import axios, { AxiosResponse } from "axios";

export const actions: ActionTree<GameState, RootState> = {
  fetchData({ commit }): void {
    axios
      .get("http://127.0.0.1:8000/api/subjects/")
      .then((response: AxiosResponse<Subject[]>) => {
        commit("setStructure", response.data);
      });
  }
};
