import React, {useState} from 'react';

function App() {
    const [expression, setExpression] = useState('');
    const [result, setResult] = useState('');

    const handleClick = async () => {
        const response = await fetch('/api/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({expression}),
        });
        const data = await response.json();
        setResult(data.result);
    };
return (
    <div>
        <h1>Calculette Polonaise Inverse (NPI) </h1>
        <input
            type="text"
            value={expression}
            onChange={(e) => setExpression(e.target.value)}
            placeholder='Entrez une expression NPI'
        />
        <button onClick={handleClick}>Calculer</button>
        {result && <h2>Résultat: {result}</h2>}
    </div>
);
}

export default App;