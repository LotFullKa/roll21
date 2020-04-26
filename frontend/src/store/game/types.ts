export interface GameState {
    subjects?: Subject[];
    myId?: number;
    xSize: number;
    ySize: number;
    updateRate: number;
}

export interface Subject {
    id: number;
    xPos: number;
    yPos: number;
    hp: number;
    isDead: boolean;
    name: string;
    color: Color;
    typeOfSubject: TypeOfSubject;
}

export type TypeOfSubject = 'human'|'goblin';
export type Color = 'red'|'blue'|'green';
