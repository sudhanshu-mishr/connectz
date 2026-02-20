import React from 'react'
import Header from './Header'

const Layout = ({ children }) => {
  return (
    <div className="flex flex-col h-screen overflow-hidden">
      <Header />
      <main className="flex-1 overflow-hidden relative bg-gray-50">
        {children}
      </main>
    </div>
  )
}

export default Layout
