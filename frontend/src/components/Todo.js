import axios from 'axios'
import React from 'react'

function TodoItem(props) {
    const deleteTodoHandler = (id) => {
    axios.delete(`http://localhost:8000/api/todo/${id}`)
        .then(res => console.log(res.data)) }
        //console.log({props})
    return (
        <div>
            <p>
            <span style={{ fontWeight: 'bold, underline' }}>{props.todo.id} : </span>
            <span>{props.todo.task}</span>
                 {/* <span>{props.todo.task}{props.todo.due_date}{props.todo.is_completed}
                 {props.todo.assigned_to}{props.todo.group_title} 
                 </span>  */}
                <button onClick={() => deleteTodoHandler(props.todo.id)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>X</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default TodoItem;