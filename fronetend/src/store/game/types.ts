export interface GameState {
    subjects?: Subject[];
    myId?: number;
    xSize: number;
    ySize: number;
}

export interface Subject {
    id: number;
    xPos: number;
    yPos: number;
    hp: number;
    isDead: boolean;
    name: string;
    color: Color;
}

export type Color = 'red'|'blue'|'green';