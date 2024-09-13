import React, { useState } from 'react';
import Header from './header.js';
import Sidebar from './sidebar.js';
import Chat from './chat.js';
import './ChatPage.css'; // Estilos básicos que você pode adicionar


function ChatPage() {
  const [messages, setMessages] = useState([
    { text: 'Olá! Como posso te ajudar?', isUser: false },
  ]);

  const [conversations, setConversations] = useState([
    { title: 'Conversa 1' },
    { title: 'Conversa 2' },
  ]);

  const sendMessage = (text) => {
    setMessages([...messages, { text, isUser: true }]);
  };

  const selectConversation = (conversation) => {
    console.log('Conversa selecionada:', conversation.title);
    // Lógica para alterar mensagens da conversa selecionada
  };

  return (
    <div className="chat-container">
      <Header />
      <div className="chat-content">
        <Sidebar conversations={conversations} selectConversation={selectConversation} />
        <Chat messages={messages} sendMessage={sendMessage} />
      </div>
    </div>
  );
}

export default ChatPage;
