import React from 'react'
import TinderCard from 'react-tinder-card'

const SwipeCard = ({ user, onSwipe }) => {
  return (
    <div className="absolute w-full h-full max-w-sm flex justify-center items-center">
      <TinderCard
        className="absolute w-[90%] h-[70vh] max-w-sm bg-white shadow-xl rounded-2xl overflow-hidden cursor-grab"
        key={user.id}
        onSwipe={(dir) => onSwipe(dir, user.id)}
        preventSwipe={['up', 'down']}
      >
        <div
          style={{ backgroundImage: `url(${user.photo_url || 'https://via.placeholder.com/400x600'})` }}
          className="relative w-full h-full bg-cover bg-center"
        >
          <div className="absolute bottom-0 left-0 w-full bg-gradient-to-t from-black to-transparent p-4 text-white">
            <h3 className="text-2xl font-bold">{user.full_name}, {user.age}</h3>
            {user.bio && <p className="text-sm mt-1 line-clamp-2">{user.bio}</p>}
          </div>
        </div>
      </TinderCard>
    </div>
  )
}

export default SwipeCard
