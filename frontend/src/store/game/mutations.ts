import { MutationTree } from 'vuex';
import { GameState, Subject } from './types';

export const mutations: MutationTree<GameState> = {
    setStructure(state, payload: Subject[]) {
        state.subjects = payload;
    },
    setSubjectHp(state, payload: {id: number, hp: number}) {
        if (!state.subjects) return;
        const index = state.subjects.findIndex(value => value.id === payload.id);
        if (!index) return;
        state.subjects[index].hp = payload.hp
    },
    setSubjectPos(state, payload: {id: number, x: number, y: number}) {
        if (!state.subjects) return;
        const index = state.subjects.findIndex(value => value.id === payload.id);
        if (!index) return;
        state.subjects[index].xPos = payload.x;
        state.subjects[index].yPos = payload.y;
    }
};