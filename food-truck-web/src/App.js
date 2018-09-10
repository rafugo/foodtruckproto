import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Promise from 'bluebird';

class App extends Component {

  foodTruckArray = [
    {name: 'Kobe Beef Truck', genres: ['Korean', 'Mexican'], id: null},
    {name: 'Grilled Cheesewich', genres: ['American'], id: null},
  ];

  mapArray = (arr) => (
    arr.map(str =>
      <div className='App-box' >
        <p>{str.name}</p>
        <p>{str.genres.reduce((acc, cur) => acc === '' ? cur : `${acc}, ${cur}`, '')}</p>
      </div>
    )
  );

  render() {
    const testDiv = this.mapArray(this.foodTruckArray);
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to the project</h1>
        </header>
        <div style={{display: 'flex', flexDirection: 'row', justifyContent: 'center'}}>
          {testDiv}
        </div>
      </div>
    );
  }
}

export default App;
