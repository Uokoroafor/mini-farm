import "../../styles/ToDoListsSummary.css";
import { useRef } from "react";
import { BiSolidTrash } from "react-icons/bi";

function ToDoListsSummary({
  listSummaries,
  handleSelectList,
  handleNewToDoList,
  handleDeleteToDoList,
}) {
  const labelRef = useRef();
  console.log("listSummaries:", listSummaries);

  if (listSummaries === null) {
    return <div className="ToDoListsSummary loading">Loading to-do lists ...</div>;
  } else if (listSummaries.length === 0) {
    return (
      <div className="ToDoListsSummary">
        <div className="box">
          <label>
            New To-Do List:&nbsp;
            <input id={labelRef} type="text" />
          </label>
          <button
            onClick={() =>
              handleNewToDoList(document.getElementById(labelRef).value)
            }
          >
            New
          </button>
        </div>
        <p>There are no to-do lists!</p>
      </div>
    );
  }
  return (
    <div className="ToDoListsSummary">
      <h1>All To-Do Lists</h1>
      <div className="box">
        <label>
          New To-Do List:&nbsp;
          <input id={labelRef} type="text" />
        </label>
        <button
          onClick={() =>
            handleNewToDoList(document.getElementById(labelRef).value)
          }
        >
          New
        </button>
      </div>
      {listSummaries.map((summary) => {
        return (
          <div
            key={summary.id}
            className="summary"
            onClick={() => handleSelectList(summary.id)}
          >
            <span className="name">{summary.name} </span>
            <span className="count">({summary.item_count} items)</span>
            <span className="flex"></span>
            <span
              className="trash"
              onClick={(evt) => {
                evt.stopPropagation();
                handleDeleteToDoList(summary.id);
              }}
            >
              <BiSolidTrash />
            </span>
          </div>
        );
      })}
    </div>
  );
}

export default ToDoListsSummary;
