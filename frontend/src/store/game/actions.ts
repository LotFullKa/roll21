import { ActionTree } from "vuex";
import { GameState, Subject } from "./types";
import { RootState } from "../types";
import axios, { AxiosResponse, AxiosError } from "axios";

export const actions: ActionTree<GameState, RootState> = {
  fetchData({ commit }): void {
    axios
      .get("http://127.0.0.1:8000/api/subjects/")
      .then((response: AxiosResponse<Subject[]>) => {
        commit("setStructure", response.data);
      });
  },
  cellClick(
    { commit, getters, state, dispatch },
    payload: { x: number; y: number }
  ): void {
    if (!state.subjects) return;
    const subject: Subject | null = getters.subjectByCoord(
      payload.x,
      payload.y
    );
    if (!!subject && state.activeSubject === subject)
      commit("setActiveSubject", null);
    else if (subject) commit("setActiveSubject", subject);
    else if (
      !!state.activeSubject &&
      getters.cellHighlight(payload.x, payload.y)
    )
      dispatch("moveSubject", { subject: state.activeSubject, ...payload });
  },
  moveSubject(
    { commit },
    payload: { subject: Subject; x: number; y: number }
  ): void {
    console.log("MOVE", payload);
    axios
      .post(`http://127.0.0.1:8000/api/subjects/${payload.subject.id}/move/`, {
        xPos: payload.x,
        yPos: payload.y
      })
      .then((response: AxiosResponse<Subject>) => {
        commit("updateSubject", response);
      })
      .catch((err: AxiosError) => {
        commit("updateSubject", {
          ...payload.subject,
          xPos: payload.x,
          yPos: payload.y
        });
      });
    commit("setSubjectPos", payload);
  }
};
