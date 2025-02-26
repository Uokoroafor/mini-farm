import { createContext, useState, useEffect, useContext } from "react";
import api from "../api";

const ToDoContext = createContext();

export const ToDoProvider = ({ children }) => {
  const [listSummaries, setListSummaries] = useState([]);
  const [selectedItem, setSelectedItem] = useState(null);

  useEffect(() => {
    reloadData().catch(console.error);
  }, []);

  async function reloadData() {
    try{
    const response = await api.get(`/api/lists`);
    setListSummaries(response.data);} catch (error) {
      console.error(error);
    }
  }

  function handleNewToDoList(newName) {
    const updateData = async () => {
      const newListData = {
        name: newName,
      };

      await api.post(`/api/lists`, newListData);
      reloadData().catch(console.error);
    };
    updateData();
  }

  function handleDeleteToDoList(id) {
    const updateData = async () => {
      await api.delete(`/api/lists/${id}`);
      reloadData().catch(console.error);
    };
    updateData();
  }

  function handleSelectList(id) {
    console.log("Selecting item", id);
    setSelectedItem(id);
  }

  function backToList() {
    setSelectedItem(null);
    reloadData().catch(console.error);
  }

  return (
    <ToDoContext.Provider value={{ listSummaries,
      selectedItem,
      handleSelectList,
      handleNewToDoList,
      handleDeleteToDoList,
      backToList,}}>
      {children}
    </ToDoContext.Provider>
  );
};

export function useToDo() {
  return useContext(ToDoContext);
}