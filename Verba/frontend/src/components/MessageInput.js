import React, { useState } from 'react';
import './MessageInput.css';

const MessageInput = ({ onSend }) => {
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (input.trim() === '') return;
    onSend(input);
    setInput('');
  };

  return (
    <div className="message-input">
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type a message and press Enter to send..."
        onKeyDown={(e) => e.key === 'Enter' && handleSend()}
      />
    </div>
  );
};

export default MessageInput;
