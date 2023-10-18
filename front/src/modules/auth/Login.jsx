import React from "react";
import axios from "axios";
import './Login.css'


class Login extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className='login-wrapper'>
                <h1> Log in </h1>
                <form>
                    <label>
                        <p>Username</p>
                        <input type='text'/>
                    </label>
                    <label>
                        <p>Password</p>
                        <input type='password'/>
                    </label>
                    <div>
                        <button type='submit' onSubmit={this.sendData}> Submit </button>
                    </div>
                </form>
            </div>
        );
    }
}

export default Login;
