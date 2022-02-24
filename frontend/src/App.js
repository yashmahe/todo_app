import React, { useState, useEffect} from 'react';
import './App.css';
import TodoView from './components/TodoListView';
import GroupView from './components/GroupListView.js';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'; 


function App() {

  const [todoList, setTodoList] = useState([{}])
  const [id, setId] = useState('') 
  const [task, setTask] = useState('') 
  const [due_date, setDueDate] = useState('') 
  const [is_completed, setIsCompleted] = useState('') 
  const [assigned_to, setAssignedTo] = useState('') 
  const [group_title, setGroupTitle] = useState('') 

  const [groupList, setGroupList] = useState([{}])
  const [title, setTitle] = useState('') 
  const [grpId, setGroupId] = useState('') 
  const [grpDueDate, setGroupDueDate] = useState('') 
  const [grpIsCompleted, setGroupIsCompleted] = useState('') 
  const [grpAssignedTo, setGroupAssignedTo] = useState('') 
  
    

  // Read all todos
  useEffect(() => {
    axios.get('http://localhost:8000/api/todo')
      .then(res => {
        console.log(res)
        setTodoList(res.data)
      })
  },todoList);

  useEffect(() => {
    axios.get('http://localhost:8000/api/group')
      .then(res => {
        console.log(res)
        setGroupList(res.data)
      })
  },groupList);

  // Post a todo
  const addTodoHandler = () => {
    axios.post('http://localhost:8000/api/todo/', { 'id':id, 'task': task, 'due_date':due_date,'is_completed':is_completed,'assigned_to':assigned_to, 'group_title': group_title})
      .then(res => console.log(res))
};

  return (
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}} >
      <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">Todo Task Manager</h1>
      {/* <h6 className="card text-white bg-primary mb-3">FASTAPI - React - MongoDB</h6> */}
     <div className="card-body">
      <h5 className="card text-white bg-dark mb-3">Add Your Task</h5>
      <span className="card-text"> 
        <input className="mb-2 form-control idIn" onChange={event => setId(event.target.value)} placeholder='id'/> 
        <input className="mb-2 form-control taskIn" onChange={event => setTask(event.target.value)}   placeholder='task'/>
        <input className="mb-2 form-control due_dateIn" onChange={event => setDueDate(event.target.value)} placeholder='due_date'/> 
        <input className="mb-2 form-control is_completedIn" onChange={event => setIsCompleted(event.target.value)}   placeholder='is_completed'/>
        <input className="mb-2 form-control assigned_toIn" onChange={event => setAssignedTo(event.target.value)} placeholder='assigned_to'/> 
        <input className="mb-2 form-control group_titleIn" onChange={event => setGroupTitle(event.target.value)}   placeholder='group_title'/>
      <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}}  onClick={addTodoHandler}>Add Task</button>
      </span>
      <h5 className="card text-white bg-dark mb-3">Your Tasks</h5>
      <div >
      <TodoView todoList={todoList} />
      </div>
      <h5 className="card text-white bg-dark mb-3">Your Groups</h5>
      <div >
      <GroupView groupList={groupList} />
      </div>
      </div>
      {/* <h6 className="card text-dark bg-warning py-1 mb-0" >Copyright 2021, All rights reserved &copy;</h6> */}
    </div>
  );
}

export default App