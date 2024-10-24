import React, {useState} from 'react';
import './index.css';
import {URL} from './env';

function App() {
    const [expression, setExpression] = useState('');
    const [result, setResult] = useState('');
    const [error, setError] = useState('');

    const handleClick = async () => {

        setError('');
        if (!expression) {
            setError('Veuillez entrer une expression');
            return;
        }

        if(expression < 0){
            setError('Veuillez entrer des nombres positifs');
            return;
        }

        // vérification d'espace entre chaque élément
        const elements = expression.split(' ');
        if(elements.length < 3 || elements.some(el => el === '')) {
            setError('Expression invalide, veuillez mettre un espace entre chaque élément');
            return;
        }

        // vérification de la validité des opérators
        const validOperator = ['+', '-', '*', '/'];
        for (let el of elements){
            if(isNaN(el) && !validOperator.includes(el)){
                setError('Expression invalide, veuillez entrer des nombres ou des opérateurs valides');
            return;
            }
        }

        const response = await fetch(URL+'/api/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({expression}),
        });
        if (!response.ok) {
            console.error('Erreur lors de la requête:', response.status, response.statusText);
            return;
        }
        const data = await response.json();
        setResult(data.result);
    };

    const handleDownload = async () => {
        try{
            const response = await fetch(URL+'/api/exportCalcul', {
                method: 'GET',
                
            });
        if (!response.ok) {
            console.error('Erreur lors de la requête:', response.status, response.statusText);
            return;
        }

        const blob = await response.blob();
        const url = window.URL.createObjectURL(new Blob ([blob]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'calculs.csv');
        document.body.appendChild(link);
        link.click();
        link.parentNode.removeChild(link);
        }catch (error) {
            console.error('Erreur lors de la requête:', error);
        }
    };
return (
    <div className='container'>
        <h1 className='title'>Calculette Polonaise Inverse (NPI) </h1>
        <input
            type="text"
            value={expression}
            onChange={(e) => setExpression(e.target.value)}
            placeholder='Entrez une expression NPI'
        />
        <div className='buttonContainer'>
            <button onClick={handleClick}>Calculer</button>
            <button onClick={handleDownload}>Télécharger les calculs</button>
        </div>
        {result && <h2 className='result'>Résultat: {result}</h2>}
        {error && <h2 className='error'>{error}</h2>}
    </div>
);
}

export default App;