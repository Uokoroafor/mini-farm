import React, { createContext, useState, useEffect } from "react";
import api from "../api";

export const ToDoContext = createContext();

export const ToDoProvider = ({ children }) => {
  const [listSummaries, setListSummaries] = useState([]);

  useEffect(() => {
    reloadData();
  }, []);

  const reloadData = async () => {
    const response = await api.get(`/api/lists`);
    setListSummaries(response.data);
  };

  const createList = async (name) => {
    await api.post(`/api/lists`, { name });
    reloadData();
  };

  const deleteList = async (id) => {
    await api.delete(`/api/lists/${id}`);
    reloadData();
  };

  return (
    <ToDoContext.Provider value={{ listSummaries, reloadData, createList, deleteList }}>
      {children}
    </ToDoContext.Provider>
  );
};
