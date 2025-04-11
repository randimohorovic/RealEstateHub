import React, { useState, useEffect } from "react";

function App() {
  const [listings, setListings] = useState([]);
  const [message, setMessage] = useState("");
  const [maxPages, setMaxPages] = useState(1);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // pri pokretanju ako postoji neka greska
  useEffect(() => {
    fetch("http://localhost:8000/root")
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch(() => setError("Greška u povezivanju s backendom"));
  }, []);

  // funkcija za dohvat podataka s Mondo Nekretnina
  const fetchMondo = () => {
    setLoading(true);
    setError(null);

    fetch(`http://localhost:8000/listings?url=https://mondo-nekretnine.hr/hr/list&max_pages=${maxPages}`)
      .then((res) => res.json())
      .then((data) => setListings(data.podaci || []))
      .catch(() => setError("Greška kod dohvaćanja Mondo podataka"))
      .finally(() => setLoading(false));
  };

  // funkcija za dohvat podataka s Njuskala
  const fetchNjuskalo = () => {
    setLoading(true);
    setError(null);

    fetch(`http://localhost:8000/njuskalo-listings?url=https://www.njuskalo.hr/prodaja-kuca&max_pages=${maxPages}`)
      .then((res) => res.json())
      .then((data) => setListings(data.podaci || []))
      .catch(() => setError("Greška kod dohvaćanja Njuskalo podataka"))
      .finally(() => setLoading(false));
  };

  return (
    <div className="App">
      <h1>Real Estate Listings</h1>
      {message && <h2>{message}</h2>}
      {error && <div className="error">{error}</div>}

      <div className="controls">
        <div>
          <label htmlFor="max-pages">Broj stranica za scraping: </label>
          <input
            type="number"
            id="max-pages"
            value={maxPages}
            onChange={(e) => setMaxPages(Math.max(1, parseInt(e.target.value) || 1))}
            min="1"
          />
        </div>

        <div className="buttons">
          <button onClick={fetchMondo} disabled={loading}>
            Mondo Nekretnine
          </button>
          <button onClick={fetchNjuskalo} disabled={loading}>
            Njuskalo
          </button>
        </div>
      </div>

      {loading ? (
        <p>Učitavanje...</p>
      ) : listings.length > 0 ? (
        <div className="listings-grid">
          {listings.map((listing, index) => (
            <div key={listing.id || index} className="listing-card">
              {listing.image_url ? (
                <img
                  src={listing.image_url}
                  alt={listing.title}
                  onError={(e) => (e.target.style.display = "none")}
                />
              ) : (
                <div className="no-image">Nema slike</div>
              )}
              <h3>{listing.title}</h3>
              <div className="details">
                <p>{listing.size_price}</p>
                <p>{listing.location}</p>
              </div>
            </div>
          ))}
        </div>
      ) : (
        !error && <p>Nema dostupnih oglasa</p>
      )}
    </div>
  );
}

export default App;
