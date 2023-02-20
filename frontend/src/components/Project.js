import React from 'react'
import {Link} from 'react-router-dom'
const ProjectItem = ({item}) => {
    return (
        <tr>
            <td><Link to={`/projects/${item.id}`}>{item.title}</Link></td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>Title</th>
                {projects.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}
export default ProjectList