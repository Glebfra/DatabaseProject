import React from 'react'
import Navigation from "../Navigation/Navigation";
import {Container} from "react-bootstrap";


class Account extends React.Component {
    render() {
        return (
            <div className='account'>
                <header>
                    <Navigation/>
                </header>
                <Container>
                    <h1>
                        Account View
                    </h1>
                </Container>
            </div>
        )
    }
}

export default Account
