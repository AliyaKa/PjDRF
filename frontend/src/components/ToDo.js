import React from 'react'


const TodoItem = ({item}) => {
    return (
        <tr>
            <td>{item.body}</td>
            <td>{item.user}</td>
            <td>{item.is_complete}</td>
        </tr>
    )
}

const TodoList = ({todo}) => {
    return (
        <table>
            <th>Body</th>
            <th>UserName</th>
            <th>Is complete</th>
                {todo.map((item) => <TodoItem item={item} />)}
        </table>
    )
}
export default TodoList