import React, { useState, useEffect } from "react";

function App() {
  const [listings, setListings] = useState([]);

  //  kao primjer nznaci bacim test preko thunder-a da dobim session id
  //  i onda ga ubacim tu da vidim dal mi dohvaca podatke sa backend
  useEffect(() => {
    const sessionId = "cs9tq9KZT8ePKzPhTy113g==";
    fetch(`http://127.0.0.1:8000/listings?session_id=${sessionId}`)
      .then((response) => response.json())
      .then((data) => {
        setListings(data.listings);
      })
      .catch((error) => {
        console.error("greska", error);
      });
  }, []);

  return (
    <div className="App">
      <h1>Real Estate Listings</h1>
      <ul>
        {listings.map((listing) => (
          <li key={listing.id}>
            <h2>{listing.name}</h2>
            <p>Price: ${listing.price}</p>
            <p>Location: {listing.location}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
