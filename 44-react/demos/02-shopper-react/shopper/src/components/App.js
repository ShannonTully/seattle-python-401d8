import React from 'react'
import superagent from 'superagent'
import Navbar from './navbar/navbar'
import Landing from './landing/landing'
import { BrowserRouter, Route } from 'react-router-dom'

export default class App extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      token: undefined,
    }
    this.signin = this.signin.bind(this)
    this.signup = this.signup.bind(this)
  }

  signin(credentials) {
    let { username, password } = credentials
    // return superagent.post(`${process.env.REACT_APP_API_URL}/user/`)
    return superagent.post('http://localhost:8000/api/v1/login')
    .send({ username, password })
    .then(res => this.setState({ token: res.body.token }))
    .then(() => localStorage.setItem('token', JSON.stringify(this.state.token)))
    // .then(() => window.location.pathname = '/store')
    .catch(console.error)
  }

  signup(credentials) {
    let { username, password, email } = credentials

    return superagent.post('http://localhost:8000/api/v1/user/')
      .send({ username, password, email })
      .then(() => window.location.pathname = '/welcome/signin')
      .catch(console.error)
  }

  render() {
    return (
      <div className="App">
        <BrowserRouter>
          <React.Fragment>
            <Navbar />
            <Route path="/welcome/:auth" component={(props) =>
                <Landing {...props} signin={this.signin} signup={this.signup} />} />
          </React.Fragment>
        </BrowserRouter>
      </div>
    )
  }
}
