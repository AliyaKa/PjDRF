import axios from 'axios'
import React from 'react';
import './App.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import TodoList from './components/ToDo.js';
import ProjectsUser from './components/ProjectsUser.js';
import Menu from "./components/Menu.js";
import Footer from "./components/Footer.js";
import NotFound404 from "./components/NotFound404.js";
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom";

class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todo': []
        }
    }

    componentDidMount() {

            axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
               this.setState({'users': response.data})
            }).catch(error => console.log(error))

            axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
               this.setState({'projects': response.data})
            }).catch(error => console.log(error))

            axios.get('http://127.0.0.1:8000/api/todo/').then(response => {
                  this.setState({'todo': response.data})
            }).catch(error => console.log(error))
    }
    render () {
        return (
            <div>
                <Menu />
                <BrowserRouter>
                    <nav>
                        <li>
                            <Link to='/users'>Users</Link>
                        </li>
                        <li>
                            <Link to='/projects'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/todo'>ToDo</Link>
                        </li>
                    </nav>
                    <Routes>
                        <Route exact path='/' element={<Navigate to='/users'/>}/>
                        <Route path='/users'>
                            <Route index element={<UserList users={this.state.users}/>}/>
                            <Route path=':userId' element={<ProjectsUser projects={this.state.projects}/>}/>
                        </Route>
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/todo' element={<TodoList todo={this.state.todo} />}/>
                        <Route path='*' element={<NotFound404/>}/>
                    </Routes>
                </BrowserRouter>
                <Footer />
            </div>
        )
    }
}

export default App;