import axios from 'axios'
import React from 'react'

function GroupItem(props) {
    const deleteGroupHandler = (title) => {
    axios.delete(`http://localhost:8000/api/group/${title}`)
        .then(res => console.log(res.data)) }

        let group = props.group.task || []
    return (
        <div>
            <p>
            <span style={{ fontWeight: 'bold, underline' }}>{props.group.title} : </span>
            <ol>
                {group.map(group => (
                <li key={group}>{group}</li>
                ))}
            </ol>
                <button onClick={() => deleteGroupHandler(props.group.title)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>X</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default GroupItem;