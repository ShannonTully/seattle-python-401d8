import React from 'react'
import AuthForm from './authform/authform'

export default class Landing extends React.Component {
  render() {
    console.log('__LANDING_PROPS__', this.props)

    let { params } = this.props.match
    let handleComplete = params.auth === 'signin'
      ? this.props.signin
      : this.props.signup

    return (
      <div className="landing-container">
        <AuthForm buttonText={params.auth} onComplete={handleComplete} />
      </div>
    )
  }
}
