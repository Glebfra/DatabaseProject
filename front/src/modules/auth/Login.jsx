import React from "react";
import {Alert, Button, Container, FloatingLabel, Form} from "react-bootstrap";
import Navigation from "../Navigation/Navigation";
import axios from "axios";
import {withRouter} from "../withRouter";


class Login extends React.Component {
    login = () => {
        axios.post(
            '/token/',
            {
                'username': this.state.username,
                'password': this.state.password
            }
        ).then(response => {
            localStorage.setItem('access', response.data.access);
            localStorage.setItem('refresh', response.data.refresh);
            this.props.navigate('/');
        }).catch(error => {
            this.setState({error: true});
        });
    }

    showErrorMessage = () => {
        if (this.state.error) {
            return (
                <Alert variant='danger' dismissible onClose={() => this.setState({error: false})}>
                    Невозможно найти учетную запись с такими данными
                </Alert>
            )
        } else {
            return null;
        }
    }

    constructor(props) {
        super(props);

        this.state = {
            username: null,
            password: null,
            error: false
        };

        this.login = this.login.bind(this);
    }

    render() {
        return (
            <div>
                <Navigation/>
                <Container>
                    <div className='position-absolute top-50 start-50 translate-middle d-flex'>
                        <div className='box border border-secondary rounded p-5 text-center'>
                            <Form>
                                <Form.Label>Login</Form.Label>
                                <Form.Group className='mb-3' controlId='formUsername'>
                                    <FloatingLabel label='Username'>
                                        <Form.Control type='text' placeholder='Username' onChange={(props) => {
                                            this.setState({username: props.target.value})
                                        }}/>
                                    </FloatingLabel>
                                </Form.Group>
                                <Form.Group className='mb-3'>
                                    <FloatingLabel label='Password' controlId='formPassword'>
                                        <Form.Control type='password' placeholder='Password' onChange={(props) => {
                                            this.setState({password: props.target.value})
                                        }}/>
                                    </FloatingLabel>
                                </Form.Group>
                                <Button variant='outline-primary' onClick={this.login} className='my-3'>Log in</Button>
                            </Form>
                            {this.showErrorMessage()}
                        </div>
                    </div>
                </Container>
            </div>
        );
    }
}

export default withRouter(Login);
