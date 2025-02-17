import "../../styles/App.css";
import { useToDo } from "../../contexts/ToDoContext";
import ListToDoLists from "../todo/ListTodoLists";
import ToDoList from "../todo/ToDoList";

function Dashboard() {
  const {
    listSummaries,
    selectedItem,
    handleSelectList,
    handleNewToDoList,
    handleDeleteToDoList,
    backToList,
  } = useToDo();
  console.log("Dashboard rendering with listSummaries:", listSummaries);
  
    return (
      
      <div className="App">
        {selectedItem === null? (
        <ListToDoLists
          listSummaries={listSummaries}
          handleSelectList={handleSelectList}
          handleNewToDoList={handleNewToDoList}
          handleDeleteToDoList={handleDeleteToDoList}
        />): (
        <ToDoList listId={selectedItem} handleBackButton={backToList} />)}
      </div>
    );
  }
export default Dashboard;