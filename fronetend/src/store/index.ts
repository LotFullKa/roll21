import {game} from "@/store/game";
import {RootState} from './types';
import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';

Vue.use(Vuex);

const store: StoreOptions<RootState> = {
    state: {
        version: '1.0.0'
    },
    modules: {
        game
    }
};

export default new Vuex.Store<RootState>(store);