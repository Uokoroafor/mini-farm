import { useContext } from "react";
import { ToDoContext } from "./ToDoContext";


export function useToDo() {
  return useContext(ToDoContext);
}
