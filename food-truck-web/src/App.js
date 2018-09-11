import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Promise from 'bluebird';
import { routerReducer } from 'react-router-redux';

class App extends Component {

  foodTruckArray = [
    {name: 'Kobe Beef Truck', genres: ['Korean', 'Mexican'], id: null, link: "https://scontent-lax3-2.cdninstagram.com/vp/d69d9739429c9d348dc76a397a76c88c/5C2F39B7/t51.2885-15/sh0.08/e35/s640x640/40981020_242615889930356_7485854080686633982_n.jpg"},
    {name: 'Grilled Cheesewich', genres: ['American'], id: null, link: "https://scontent-lax3-2.cdninstagram.com/vp/d69d9739429c9d348dc76a397a76c88c/5C2F39B7/t51.2885-15/sh0.08/e35/s640x640/40981020_242615889930356_7485854080686633982_n.jpg"},
  ];

  mapArray = (arr) => (
    arr.map(str =>
      <div className='App-card' >
        <img src={str.link} className='Image-dims'/>
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
