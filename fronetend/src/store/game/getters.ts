import {GameState, Subject} from "@/store/game/types";
import {RootState} from "@/store/types";
import {GetterTree} from "vuex";


export const getters: GetterTree<GameState, RootState> = {
    subjectByCoord: (state) => (xPos: number, yPos: number): Subject|null => {
        if (!state.subjects) { return null; }
        const subject = state.subjects.find(subj => subj.xPos === xPos && subj.yPos === yPos);
        return subject ? subject : null
    }
};