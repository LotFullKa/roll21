export interface GameState {
  subjects?: Subject[];
  activeSubject: Subject | null;
  myId?: number;
  xSize: number;
  ySize: number;
  updateRate: number;
  moveSpeed: number;
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

export type TypeOfSubject = "human" | "goblin";
export type Color = "red" | "blue" | "green";
