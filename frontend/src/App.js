// To do:
// - dynamoDB bazu trebam dodat, zasad objave u lokalnoj meoriji radi sa frondendom
// - vise scrapera za razlicite stranice
// - filter objava
// - Docker

import React, { useState, useEffect } from "react";

function App() {
  const [listings, setListings] = useState([]);
  const [message, setMessage] = useState("");
  const [MaxPages, setMaxPages]= useState(1); //hocu imat da korisnik odabere koliko strnica da scrape-a

  useEffect(() => {//test
      fetch("http://localhost:8000/root")
            .then((response) => response.json())
            .then((data) => setMessage(data.message))
            .catch((error) => console.error("Error fetching root:", error));
  }, []);
    // Mondo nekretnine Url:  http://127.0.0.1:8000/listings?url=https://mondo-nekretnine.hr/hr/list?offer_type=&category=&location_id=&area_lo=&area_hi=&price_lo=&price_hi=&dist_center_hi=&dist_sea_hi=&orderby=price&orderdir=1&custom_id=
    // basic funkcija koja fetcha objave sa prosljedene stranice
    const fetchListings = (url) => {
      fetch(`${url}&max_pages=${MaxPages}`)
        .then((response) => response.json())
        .then((data) => {
          console.log("data:", data);
          setListings(data.podaci); // dio objekta koji mi sadrzi podatke o listings
        })
        .catch((error) => {
          console.error("Error fetching listings:", error);
        });
    };

  return (
    <div className="App">
      <h1>Real Estate Listings</h1>
      <h1>{message}</h1>

      {/* div za MAX PAGE */}
      <div>
        <label htmlFor="max-pages">Koliko stranica zelis scrape-at: </label>
        <input
          type="number"
          id="max-pages"
          value={MaxPages}
          onChange={(e) => setMaxPages(e.target.value)}
          min="1"
        />
      </div>

      {/* div za buttons */}

      <div>
      <button onClick={() => fetchListings("http://127.0.0.1:8000/listings?url=https://mondo-nekretnine.hr/hr/list?offer_type=&category=&location_id=&area_lo=&area_hi=&price_lo=&price_hi=&dist_center_hi=&dist_sea_hi=&orderby=price&orderdir=1&custom_id=")}>
      Mondo Nekretnine</button>

      <button onClick={() => fetchListings("http://127.0.0.1:8000/listings?url=")}>
        stranica druga
</button>
      </div>

      {/* div za objave */}
      {listings.length === 0 ? (
        <p>ucitavanje...</p> 
      ) : (
      <ul>
        {listings.map((listing, index) => (
          <li key={listing.id ||index} >
            <h2>{listing.title}</h2>
             {/* Display image if URL is available */}
             {listing.image_url ? (
                <img src={listing.image_url} alt={listing.title} style={{ width: "200px", height: "auto" }} />
              ) : (
                <p>Slika nije dostupna</p>
              )}
            <p>m2 and price: {listing.size_price}</p>
            <p>Location: {listing.location}</p>
          </li>
        ))}
      </ul>
      )}
    </div>
  );
}

export default App;
