import React from 'react'

const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.title}</td>
            <td>{item.href}</td>

        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>Title</th>
            <th>Href</th>

            {projects.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}
export default ProjectList