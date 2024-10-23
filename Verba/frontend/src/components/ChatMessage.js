import React from 'react';
import './ChatMessage.css';

const ChatMessage = ({ sender, text }) => {
  return (
    <div className={`chat-message ${sender}`}>
      <span className="message-text">{text}</span>
    </div>
  );
};

export default ChatMessage;
