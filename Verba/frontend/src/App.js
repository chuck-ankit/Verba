import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import ChatWindow from './components/ChatWindow';
import MessageInput from './components/MessageInput';
import './App.css';
import { sendMessageToBackend } from './api';

function App() {
  const [messages, setMessages] = useState([]);

  const handleSend = async (newMessage) => {
    setMessages([...messages, { sender: 'user', text: newMessage }]);
    const botResponse = await sendMessageToBackend(newMessage);
    setMessages((prevMessages) => [
      ...prevMessages,
      { sender: 'bot', text: botResponse }
    ]);
  };

  return (
    <div className="app">
      <Sidebar />
      <div className="main-window">
        <ChatWindow messages={messages} />
        <MessageInput onSend={handleSend} />
      </div>
    </div>
  );
}

export default App;
