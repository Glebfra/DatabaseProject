import Navigation from "./modules/Navigation/Navigation";
import React from "react";
import {Carousel, Container} from "react-bootstrap";
import axios from "axios";


class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            carousel: []
        }

        axios.get(
            'api/carousel/'
        ).then(response => {
            this.setState({carousel: response.data})
        });
    }

    render() {
        console.log(this.state.carousel)

        return (
            <div className="App">
                <header>
                    <Navigation/>
                </header>
                <Container className='d-flex'>
                    <Carousel style={{height: 768, width: 1366}}>
                        {this.state.carousel.map(item => (
                            <Carousel.Item>
                                <img src={item.image} style={{height: 768, width: 1366}}/>
                                <Carousel.Caption>
                                    <h3>{item.caption}</h3>
                                    <p>{item.body}</p>
                                </Carousel.Caption>
                            </Carousel.Item>
                        ))}
                    </Carousel>
                </Container>
            </div>
        );
    }
}

export default App;
