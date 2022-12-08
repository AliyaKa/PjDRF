import axios from 'axios'
import React from 'react';
import './App.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import ToDoList from './components/ToDo.js';
import Menu from "./components/Menu.js";
import Footer from "./components/Footer.js";
import {BrowserRouter, Route, Routes, Link} from "react-router-dom";

class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todo': [],
        }
    }

    componentDidMount() {

            axios.get('http://127.0.0.1:8000/api/users/').then(response => {
                  this.setState(
                    {
                        'users': response.data
                    }
                )
            }).catch(error => console.log(error))

            axios.get('http://127.0.0.1:8000/api/projects/').then(response => {
                  this.setState(
                    {
                        'todo.projects': response.data
                    }
                )
            }).catch(error => console.log(error))

            axios.get('http://127.0.0.1:8000/api/todo/').then(response => {
                  this.setState(
                    {
                        'item': response.data
                    }
                )
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
                        <Route exact path='/users' element={<UserList users={this.state.users} />}/>
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />}/>
                        <Route exact path='/todo' element={<ToDoList todo={this.state.todo} />}/>
                    </Routes>
                </BrowserRouter>
                <Footer />
            </div>
        )
    }
}

export default App;