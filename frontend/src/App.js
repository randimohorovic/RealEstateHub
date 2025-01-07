import React, { useState, useEffect } from "react";

function App() {
  const [listings, setListings] = useState([]);
  const [message, setMessage] = useState("");

  //  kao primjer nznaci bacim test preko thunder-a da dobim session id
  //  i onda ga ubacim tu da vidim dal mi dohvaca podatke sa backend
  useEffect(() => {
    // const sessionId = "";
    fetch(`http://localhost:8000/listings`) // inace session id u querry ubacis..
      .then((response) => response.json())
      .then((data) => {
        console.log("data:", data);
        setListings(data.podaci);
      })
      .catch((error) => {
        console.error("greska", error);
      });
      fetch("http://localhost:8000/root")
            .then((response) => response.json())
            .then((data) => setMessage(data.message))
            .catch((error) => console.error("Error fetching root:", error));
  }, []);

  return (
    <div className="App">
      <h1>Real Estate Listings</h1>
      <h1>{message}</h1>
      {listings.length === 0 ? (
        <p>ucitavanje...</p> 
      ) : (
      <ul>
        {listings.map((listing) => (
          <li key={listing.id}>
            <h2>{listing.name}</h2>
            <p>Price: ${listing.price}</p>
            <p>Location: {listing.location}</p>
          </li>
        ))}
      </ul>
      )}
    </div>
  );
}

export default App;
