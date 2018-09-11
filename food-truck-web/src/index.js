import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App arr={['1', '2', '3']} />, document.getElementById('root'));
registerServiceWorker();
