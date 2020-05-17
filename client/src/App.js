import React, { Component } from 'react';
import Response from './components/response';

class App extends Component {

  state = {
    response: []
  }

  componentDidMount() {
    fetch('http://localhost:8081/api/v1')
      .then(res => res.json())
      .then((data) => {
        this.setState({ response: data })
      })
      .catch(console.log)
  }

  render() {
    return ( 
      <Response data={this.state.response} />
    )
  }
}

export default App;