export interface GameState {
    subjects?: Subject[]
}

export interface Subject {
    id: number,
    xPos: number,
    yPos: number,
    hp: number,
    isDead: number,
    name: string,
    color: Color
}

export type Color = 'red'|'blue'|'green';