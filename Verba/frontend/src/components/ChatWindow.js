import React, { useState } from 'react';
import ChatMessage from './ChatMessage';
import './ChatWindow.css';

const ChatWindow = () => {
  const [messages, setMessages] = useState([
    { sender: 'bot', text: 'How many Indian languages have you been trained with.' },
    { sender: 'user', text: 'Is compiler a system software?' }
  ]);

  return (
    <div className="chat-window">
      {messages.map((msg, index) => (
        <ChatMessage key={index} sender={msg.sender} text={msg.text} />
      ))}
    </div>
  );
};

export default ChatWindow;
