import React, { useState, useEffect, useRef } from 'react'

const ChatWindow = ({ matchId, currentUserId }) => {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const ws = useRef(null)

  useEffect(() => {
    // Determine WebSocket URL
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:'
    const host = window.location.host
    const wsUrl = `${protocol}//${host}/api/ws/chat/${matchId}`

    ws.current = new WebSocket(wsUrl)

    ws.current.onopen = () => {
      console.log('Connected to chat')
    }

    ws.current.onmessage = (event) => {
      const message = event.data
      setMessages((prev) => [...prev, { text: message, senderId: 0 }])
    }

    ws.current.onclose = () => {
      console.log('Disconnected')
    }

    return () => {
      ws.current.close()
    }
  }, [matchId])

  const sendMessage = () => {
    if (input.trim() && ws.current) {
      ws.current.send(input)
      setMessages((prev) => [...prev, { text: input, senderId: currentUserId }])
      setInput('')
    }
  }

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto p-4 space-y-2">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`p-2 rounded-lg max-w-[80%] ${msg.senderId === currentUserId ? 'bg-blue-500 text-white self-end ml-auto' : 'bg-gray-200 self-start'}`}
          >
            {msg.text}
          </div>
        ))}
      </div>
      <div className="p-4 border-t flex">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 border rounded-l-lg p-2"
          placeholder="Type a message..."
        />
        <button
          onClick={sendMessage}
          className="bg-blue-500 text-white p-2 rounded-r-lg"
        >
          Send
        </button>
      </div>
    </div>
  )
}

export default ChatWindow
