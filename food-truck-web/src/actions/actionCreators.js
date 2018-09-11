export const fetchAccounts = () => {
    const cards = [
      {front: true, name: 'Kobe Beef Truck', genres: ['Korean', 'Mexican'], id: null, link: "https://scontent-lax3-2.cdninstagram.com/vp/d69d9739429c9d348dc76a397a76c88c/5C2F39B7/t51.2885-15/sh0.08/e35/s640x640/40981020_242615889930356_7485854080686633982_n.jpg"},
      {front: true,name: 'Grilled Cheesewich', genres: ['American'], id: null, link: "https://scontent-lax3-2.cdninstagram.com/vp/d69d9739429c9d348dc76a397a76c88c/5C2F39B7/t51.2885-15/sh0.08/e35/s640x640/40981020_242615889930356_7485854080686633982_n.jpg"},
    ];
    return {
      type: 'FETCH_ACCOUNTS',
      cards,
    }
};

export const flipCard = (key) => ({
    type: 'FLIP_CARD',
    key,
});

export const getTweets = (key) => ({
    type: 'FETCH_TWEETS',
    key,
})