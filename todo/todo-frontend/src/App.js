import React from 'react';
import logo from './logo.svg';

import './bootstrap/css/bootstrap.min.css'
import './bootstrap/css/sticky-footer-navbar.css'
import Footer from './components/Footer.js'
import Navbar from './components/Menu.js'
import UserList from './components/User.js'
import ProjectList from './components/Project.js'
import UserProjects from './components/UserProject.js'
import Er404  from './components/Er404.js'
import axios from 'axios'
import {HashRouter, Route, Routes, Navigate, BrowserRouter} from 'react-router-dom'


const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects':[],
            'todos':[],
        }
    }

 componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState({
                    'users': users,
                })
            })
        .catch(error => {
            console.log(error)
            })
        axios.get('http://127.0.0.1:8000/api/todos')
            .then(response => {

            const todos = response.data.results
                this.setState(
                {
                    'todos': todos
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/param')
            .then(response => {

                const projects = response.data.results
                this.setState(
                    {
                    'projects': projects
                    }
                )
                }).catch(error => console.log(error))

  }
     render() {
        return (
            <div className="App">

                <BrowserRouter>
                    <Routes>
                    <Route exact path='/users' component={() => <UserList users={this.state.users} />} />
                    <Route exact path='/todo' component={() => <ToDoList todos={this.state.todos} />} />
                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />}/>
                    <Route path="user/:username">
                        <UserProjects items={this.state.projects} />
                    </Route>
                    <Navigate from='/u' to='/users'/>
                    <Route component={Er404} />
                </Routes>
                </BrowserRouter>
                <Footer/>
            </div>
    )
  }
}

export default App;