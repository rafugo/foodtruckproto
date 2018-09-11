import { combineReducers, createStore } from 'redux';

import cards from './cards';

const defaultState = {
    cards: [],
}

const rootReducer = combineReducers({cards});

const store = createStore(rootReducer, defaultState);

export default store;
