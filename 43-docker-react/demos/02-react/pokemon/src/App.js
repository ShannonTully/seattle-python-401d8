import './App.css'
import React, { Component } from 'react'
import MainHeader from './main-header/main-header'
import PokemonData from './pokemon-data/pokemon-data'
import PokemonSearch from './pokemon-search/pokemon-search'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      results: undefined,
    }
  }

  render() {
    return (
      <div className="App">
        <MainHeader/>
        <PokemonSearch setAppState={this.setState.bind(this)}/>

        { this.state.results ?
          <PokemonData results={this.state.results} />
          :
          undefined
        }

      </div>
    )
  }
}

export default App



// if (condition) {
//   // do thing
// } else {
//   // do other thing
// }

// condition ? '//do thing' : '// do other thing'
