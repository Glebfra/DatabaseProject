import React from 'react'
import axios from 'axios'


class Line extends React.Component {
    loadData = () => {
        axios.get(
            'http://localhost:8000/api/database/saturation'
        ).then(response => {
            this.setState('data', response.data)
        })
    }

    render() {
        this.loadData()
        return (
            this.state.data
        );
    }
}

export default Line;
