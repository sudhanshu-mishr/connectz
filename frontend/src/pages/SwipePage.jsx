import React, { useState, useEffect } from 'react'
import SwipeCard from '../components/SwipeCard'
import api from '../api'

const SwipePage = () => {
  const [users, setUsers] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchCandidates()
  }, [])

  const fetchCandidates = async () => {
    try {
      const res = await api.get('/swipe/candidates')
      setUsers(res.data)
    } catch (err) {
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const handleSwipe = async (direction, userId) => {
    try {
      const isLike = direction === 'right'
      await api.post('/swipe/', { likee_id: userId, is_like: isLike })
      // Remove user from list
      setUsers((prev) => prev.filter((u) => u.id !== userId))
    } catch (err) {
      console.error(err)
    }
  }

  if (loading) return <div className="flex justify-center items-center h-full">Loading...</div>
  if (users.length === 0) return <div className="flex justify-center items-center h-full">No more profiles!</div>

  return (
    <div className="relative w-full h-full flex justify-center items-center">
      {users.map((user) => (
        <SwipeCard key={user.id} user={user} onSwipe={handleSwipe} />
      ))}
    </div>
  )
}

export default SwipePage
