import React from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { User, MessageCircle, Flame } from 'lucide-react'

const Header = ({ user, onLogout }) => {
  const navigate = useNavigate()

  return (
    <div className="flex justify-between items-center p-4 border-b bg-white shadow-sm">
      <Link to="/profile">
        <User className="h-8 w-8 text-gray-500" />
      </Link>

      <Link to="/swipe">
        <div className="bg-gradient-to-r from-pink-500 to-orange-500 p-1 rounded-full">
            <Flame className="h-8 w-8 text-white" fill="white" />
        </div>
      </Link>

      <Link to="/matches">
        <MessageCircle className="h-8 w-8 text-gray-500" />
      </Link>
    </div>
  )
}

export default Header
