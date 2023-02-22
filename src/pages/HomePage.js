import React, { useState } from 'react';

const HomePage = () => {
  const [search, setSearch] = useState();
  const [weather, setWeather] = useState({});

  const api_key = 'e34323ec7e274ae5d886f444c2eb4823';
  const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${search}&appid=${api_key}`;

  const searchPressed = () => {
    fetch(apiUrl)
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setWeather(result);
      });
  };

  return (
    <>
      {/* Search Box */}
      <input
        type="text"
        placeholder="Enter city/town..."
        onChange={(e) => setSearch(e.target.value)}
      />

      <button onClick={searchPressed}>Search</button>
      {typeof weather.main != 'undefined' ? (
        <div>
          {/* Location */}
          <p>{weather.name}</p>

          {/* Temperature F/C */}
          <p>{weather.main.temp} F</p>

          {/* Condition Sunny */}
          <p>{weather.weather[0].main}</p>
          <p>{weather.weather[0].description}</p>
        </div>
      ) : (
        ''
      )}
    </>
  );
};

export default HomePage;
