import React, { useState } from 'react';
import axios from 'axios';

function Home() {
    const [newSearch, setNewSearch] = useState('');

    const handleSearch = async () => {

        try {
            const response = await axios.get('/crawl', {
                params: { search_term: newSearch },
            });

            const searchResult = response.data;
            console.log(searchResult)
        } catch (error) {
            console.error('Erro ao chamar a API:', error);
        }
    };

    return (
        <div>
            <div className="search-window">
                <input
                    type="text"
                    value={newSearch}
                    onChange={(e) => setNewSearch(e.target.value)}
                    placeholder="Faça sua pesquisa..."
                />
                <button onClick={handleSearch}>Pesquisar</button>
            </div>
        </div>
    );
}

export default Home;
