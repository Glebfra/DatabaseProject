import React from "react";
import {Button, Container, Modal, Nav, Navbar, NavDropdown} from 'react-bootstrap'
import {Link} from "react-router-dom";


class Navigation extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            showLogout: false,
            seed: Math.random()
        };
    }

    handleLogoutClose = () => {
        this.setState({showLogout: !this.state.showLogout});
    }

    handleLogout = () => {
        localStorage.removeItem('access');
        localStorage.removeItem('refresh');
        this.handleLogoutClose();
        this.refreshNavigation();
    }

    refreshNavigation = () => {
        this.setState({seed: Math.random()});
    }

    getAccountView = () => {
        if (localStorage.getItem('access') != null) {
            return (
                <NavDropdown title='Account' id='basic-nav-dropdown'>
                    <NavDropdown.Item href='/account'>Account</NavDropdown.Item>
                    <NavDropdown.Item href='/settings'>Settings</NavDropdown.Item>
                    <NavDropdown.Item onClick={this.handleLogoutClose}>Log out</NavDropdown.Item>
                </NavDropdown>
            )
        } else {
            return (
                <Nav.Link href='/login'>Log in</Nav.Link>
            )
        }
    }

    getLogoutModal = () => (
        <Modal show={this.state.showLogout} onHide={this.handleLogoutClose} className='d-flex'>
            <Modal.Header closeButton>
                <Modal.Title>Log out</Modal.Title>
            </Modal.Header>

            <Modal.Body>
                <p>Are you really want to log out?</p>
            </Modal.Body>

            <Modal.Footer>
                <Button variant='outline-primary' onClick={this.handleLogout}>Yes</Button>
                <Button variant='outline-secondary' onClick={this.handleLogoutClose}>No</Button>
            </Modal.Footer>
        </Modal>
    )

    render() {
        return (
            <div key={this.state.seed}>
                <Navbar expland='lg' className='bg-body-tertiary'>
                    <Container>
                        <Link to='/' className='text-decoration-none'>
                            <Navbar.Brand href='/'>Database</Navbar.Brand>
                        </Link>
                        <Navbar.Collapse>
                            <Nav className='me-auto'>
                                <Link to='/phase' className='text-decoration-none'>
                                    <Nav.Link href='/phase'>Phase</Nav.Link>
                                </Link>
                                <Link to='/saturation' className='text-decoration-none'>
                                    <Nav.Link href='/saturation'>Saturation</Nav.Link>
                                </Link>
                                <Link to='/storage' className='text-decoration-none'>
                                    <Nav.Link href='/storage'>Storage</Nav.Link>
                                </Link>
                            </Nav>
                        </Navbar.Collapse>
                        {this.getAccountView()}
                    </Container>
                </Navbar>
                {this.getLogoutModal()}
            </div>
        );
    }
}

export default Navigation;