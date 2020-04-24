import { ActionTree } from 'vuex';
import { GameState } from './types';
import { RootState } from '../types';
import axios from 'axios';

export const actions: ActionTree<GameState, RootState> = {
    fetchData({ commit }): any {
        axios.get('http://127.0.0.1:8000/api/subjects/')
            .then(response=> {
                commit('setStructure', response.data)
            }
        )
    }
};
