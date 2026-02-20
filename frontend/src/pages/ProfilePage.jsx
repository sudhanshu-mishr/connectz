import React from 'react'

const ProfilePage = ({ user, onLogout }) => {
  return (
    <div className="p-4 flex flex-col items-center">
      <div
        className="w-32 h-32 rounded-full bg-gray-300 bg-cover bg-center mb-4"
        style={{ backgroundImage: `url(${user?.photo_url || 'https://via.placeholder.com/150'})` }}
      />
      <h2 className="text-2xl font-bold">{user?.full_name}</h2>
      <p className="text-gray-600">{user?.email}</p>
      <div className="mt-8">
        <button
          onClick={onLogout}
          className="bg-red-500 text-white px-4 py-2 rounded"
        >
          Logout
        </button>
      </div>
    </div>
  )
}

export default ProfilePage
