import { useEffect, useState } from "react";
import "../styles/App.css";

interface Combo {
  // (Dicts are serialised into JSON as an object)
  mkComponents: {
    [key: string]: {
      name: string;
      type: string;
    };
  };
  stats: {
    [key: string]: number;
  };
}

function App() {
  const [combo, setCombo] = useState<Combo | null>(null);

  useEffect(() => {
    fetchCombo();
  }, []);

  async function fetchCombo() {
    const response = await fetch("combos");
    if (response.ok) {
      const data = await response.json();
      setCombo(data);
    } else {
      console.error("Failed to fetch combo data");
    }
  }

  const contents =
    combo === null ? (
      <p>
        <em>
          Loading... Please refresh once the ASP.NET backend has started. See{" "}
          <a href="https://aka.ms/jspsintegrationreact">
            https://aka.ms/jspsintegrationreact
          </a>{" "}
          for more details.
        </em>
      </p>
    ) : (
      <>
        <h2>Components:</h2>
        <ul>
          {Object.entries(combo.mkComponents).map(([key, component]) => (
            <li key={key}>
              <b>{component.type}</b>: {component.name}
            </li>
          ))}
        </ul>

        <h2>Stats:</h2>
        <ul>
          {Object.entries(combo.stats).map(([statName, statValue]) => (
            <li key={statName}>
              <b>{statName}</b>: {statValue.toFixed(2)}
            </li>
          ))}
        </ul>
      </>
    );

  return (
    <div>
      <h1 id="tableLabel">Mario Kart 8 Deluxe Combo</h1>
      {contents}
      <p>
        Combo stats are a sum of the components pluss three, then divided by
        four.
      </p>
      <p>
        {" "}
        All stats are taken from{" "}
        <a href="https://www.mariowiki.com/Mario_Kart_8_Deluxe_in-game_statistics">
          the Mario Wiki
        </a>
      </p>
    </div>
  );
}

export default App;
