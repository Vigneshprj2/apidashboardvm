import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [apiHits, setApiHits] = useState([]);

  useEffect(() => {
    fetchApiHits();
  }, []);

  const fetchApiHits = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api-hits');
      setApiHits(response.data);
    } catch (error) {
      console.error('Error fetching API hits:', error);
    }
  };

  return (
    <div className="App">
      <h1>API Hit Analytics Dashboard</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Address</th>
            <th>Mobile number</th>
          </tr>
        </thead>
        <tbody>
          {apiHits.map(hit => (
            <tr key={hit.id}>
              <td>{hit.id}</td>
              <td>{hit.name}</td>
              <td>{hit.email}</td>
              <td>{hit.address}</td>
              <td>{hit.mobile}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
