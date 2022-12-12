import React from 'react'
const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.title}</td>
            <td>{item.users}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>Id</th>
            <th>Title</th>
            <th>UserName</th>
                {projects.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}
export default ProjectList