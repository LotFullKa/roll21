import { MutationTree } from 'vuex';
import { GameState, Subject } from './types';

export const mutations: MutationTree<GameState> = {
    setStructure(state, payload: Subject[]) {
        state.subjects = payload;
    },
};