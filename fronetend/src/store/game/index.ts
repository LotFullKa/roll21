import { Module } from 'vuex';
import { actions } from './actions';
import { mutations } from './mutations';
import { GameState } from './types';
import { RootState } from '../types';

export const state: GameState = {
    subjects: []
};

const namespaced: boolean = true;

export const game: Module<GameState, RootState> = {
    namespaced,
    state,
    actions,
    mutations
};