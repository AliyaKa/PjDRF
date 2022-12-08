import React from 'react'

const ToDoItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.body}</td>
            <td>{item.created}</td>
            <td>{item.updated}</td>
            <td>{item.is_complete}</td>
        </tr>
    )
}

const ToDoList = ({todo}) => {
    return (
        <table>
            <th>ID</th>
            <th>Body</th>
            <th>Created</th>
            <th>Updated</th>
            <th>Is complete</th>
            {todo.map((item) => <ToDoItem item={item} />)}
        </table>
    )
}
export default ToDoList