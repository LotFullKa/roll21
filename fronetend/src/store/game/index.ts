import {getters} from "@/store/game/getters";
import { Module } from 'vuex';
import { actions } from './actions';
import { mutations } from './mutations';
import { GameState } from './types';
import { RootState } from '../types';

export const state: GameState = {
    subjects: [
        {
            id: 1,
            xPos: 5,
            yPos: 5,
            name: 'Andrey',
            color: 'blue',
            hp: 100,
            isDead: false
        }
    ],
    myId: 1,
    xSize: 15,
    ySize: 15,
};

const namespaced = true;

export const game: Module<GameState, RootState> = {
    namespaced,
    state,
    actions,
    mutations,
    getters
};