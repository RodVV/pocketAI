import React from 'react';

function Sidebar({ conversations, selectConversation }) {
  return (
    <aside className="chat-sidebar">
      <ul>
        {conversations.map((conv, index) => (
          <li key={index} onClick={() => selectConversation(conv)}>
            {conv.title}
          </li>
        ))}
      </ul>
    </aside>
  );
}

export default Sidebar