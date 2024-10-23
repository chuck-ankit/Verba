import React from 'react';
import './Sidebar.css';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>Chats</h2>
      <div className="chat-list">
        <div className="chat-item">First Chat</div>
        <div className="chat-item">Untitled</div>
      </div>
    </div>
  );
};

export default Sidebar;
