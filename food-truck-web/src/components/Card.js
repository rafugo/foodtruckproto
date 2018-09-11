import './App.css';
import React from 'react';

export default function Card(props) {
  const str = props.item;

  if (str.front) {
    return (
      <div className='App-card' onClick={() => props.flipCard()} >
        <img 
          src={str.link}
          className='Image-dims'
        />
        <p>{str.name}</p>
        <p>{str.genres.reduce((acc, cur) => acc === '' ? cur : `${acc}, ${cur}`, '')}</p>
      </div>
    );
  }

  return (
    <div className='App-card' onClick={() => props.flipCard()} >
      <h4>Tweets:</h4>
    </div>
  )
}