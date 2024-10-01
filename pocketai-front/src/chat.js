import React, { useState } from 'react';
import axios from 'axios';

function Chat({ messages, sendMessage }) {
  const [newMessage, setNewMessage] = useState('');
  const [chatMessages, setChatMessages] = useState(messages);

  const handleSend = async () => {
    if (newMessage.trim()) {
      sendMessage(newMessage);

      
      try {
        const response = await axios.get('/get', {
          params: { message: newMessage }, 
        });

        
        const botResponse = response.data.response; 

       
        setChatMessages((prevMessages) => [
          ...prevMessages,
          { text: botResponse, isUser: false }, 
        ]);
      } catch (error) {
        console.error('Erro ao chamar a API:', error);
      }

      setNewMessage('');
    }
  };

  return (
    <div>
      <div className="chat-window">
        <div className="chat-messages">
          {chatMessages.map((msg, index) => (
            <div key={index} className={msg.isUser ? 'user' : 'bot'}>
              {msg.text}
            </div>
          ))}
        </div>
        <div className="chat-input">
          <input
            type="text"
            value={newMessage}
            onChange={(e) => setNewMessage(e.target.value)}
            placeholder="Digite sua mensagem..."
          />
          <button onClick={handleSend}>Enviar</button>
        </div>
      </div>
    </div>
  );
}

export default Chat;
