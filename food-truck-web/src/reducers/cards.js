const cards = (state = {}, action) => {
    switch (action.type) {
        case 'FETCH_ACCOUNTS':
            return [...state, ...action.cards]
        case 'FLIP_CARD':
            return [
                ...state.slice(0, action.key),
                {...state[action.key], front: !state[action.key].front},
                ...state.slice(action.key + 1)]
        default:
            return state;
    }
}

export default cards;