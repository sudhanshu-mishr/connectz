import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import api from '../api'

const MatchesPage = () => {
  const [matches, setMatches] = useState([])
  const [loading, setLoading] = useState(false) // Changed default to false for now

  // Placeholder for fetch
  useEffect(() => {
     // TODO: fetch matches
  }, [])

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Your Matches</h2>
      <div className="grid grid-cols-3 gap-4">
        {matches.map((match) => (
          <Link to={`/chat/${match.id}`} key={match.id} className="flex flex-col items-center">
            <div
              className="w-20 h-20 rounded-full bg-cover bg-center"
              style={{ backgroundImage: `url(${match.photo_url || 'https://via.placeholder.com/150'})` }}
            />
            <span className="mt-2 font-semibold text-sm">{match.full_name}</span>
          </Link>
        ))}
      </div>
      {matches.length === 0 && <p className="text-gray-500 text-center mt-10">No matches yet. Keep swiping!</p>}
    </div>
  )
}

export default MatchesPage
