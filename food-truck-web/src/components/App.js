import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Card from './Card';
import Promise from 'bluebird';
import { routerReducer } from 'react-router-redux';

import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';


import * as actionCreators from '../actions/actionCreators';

class App extends Component {

  mapArray = (arr) => (
    arr.map((str, key) =>
      <Card item={str} flipCard={() => this.props.flipCard(key)} />
    )
  );

  componentDidMount() {
    this.props.fetchAccounts();
  }

  render() {
    console.log(this.props);
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Food Truck Finder</h1>
        </header>
        <div style={{display: 'flex', flexDirection: 'row', justifyContent: 'center'}}>
          {this.mapArray(this.props.cards)}
        </div>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    cards: state.cards,
  }
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(actionCreators, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(App);
