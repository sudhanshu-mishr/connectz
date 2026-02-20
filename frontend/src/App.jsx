import React, { useState, useEffect } from 'react'
import { Routes, Route, useNavigate, Navigate, useParams } from 'react-router-dom'
import Auth from './components/Auth'
import Layout from './components/Layout'
import SwipePage from './pages/SwipePage'
import MatchesPage from './pages/MatchesPage'
import ProfilePage from './pages/ProfilePage'
import ChatWindow from './components/ChatWindow'
import api from './api'

function App() {
  const [token, setToken] = useState(localStorage.getItem('token'))
  const [user, setUser] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    if (token) {
      localStorage.setItem('token', token)
      api.get('/users/me')
        .then(res => setUser(res.data))
        .catch(() => {
          setToken(null)
          localStorage.removeItem('token')
        })
    } else {
      localStorage.removeItem('token')
      setUser(null)
    }
  }, [token])

  const handleLogin = (newToken) => {
    setToken(newToken)
  }

  const handleLogout = () => {
    setToken(null)
    localStorage.removeItem('token')
    navigate('/')
  }

  if (!token) {
    return <Auth onLogin={handleLogin} />
  }

  return (
    <Layout user={user} onLogout={handleLogout}>
      <Routes>
        <Route path="/swipe" element={<SwipePage />} />
        <Route path="/matches" element={<MatchesPage />} />
        <Route path="/profile" element={<ProfilePage user={user} onLogout={handleLogout} />} />
        <Route
          path="/chat/:matchId"
          element={
            <ChatWrapper user={user} />
          }
        />
        <Route path="*" element={<Navigate to="/swipe" replace />} />
      </Routes>
    </Layout>
  )
}

const ChatWrapper = ({ user }) => {
  const { matchId } = useParams()
  return <ChatWindow matchId={matchId} currentUserId={user?.id} />
}

export default App
