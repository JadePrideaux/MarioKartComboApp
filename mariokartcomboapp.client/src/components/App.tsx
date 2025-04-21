import { useEffect, useState } from "react";
import "../styles/App.css";

interface Combo {
  mkComponents: {
    [key: string]: {
      name: string;
      type: string;
      imgURL?: string | null;
    };
  };
  stats: {
    speed: {
      ground: number;
      water: number;
      air: number;
      antiGravity: number;
    };
    acceleration: number;
    weight: number;
    handling: {
      ground: number;
      water: number;
      air: number;
      antiGravity: number;
    };
    miniTurbo: number;
    invincibility: number;
    offRoadTraction: number;
    onRoadTraction: number;
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
              {/*If there is an imgURL, render the image*/}
              {component.imgURL && (
                <div>
                  <img
                    src={component.imgURL}
                    alt={component.name}
                    style={{ width: "100px", height: "auto" }}
                  />
                </div>
              )}
            </li>
          ))}
        </ul>

        <h2>Stats:</h2>
        <ul>
          {Object.entries(combo.stats).map(([statName, statValue]) => (
            <li key={statName}>
              {/*If value type is number, print the stat*/}
              {/*Else If value type is object, list each stat in the object*/}
              <b>{statName}</b>:
              {typeof statValue === "number" ? (
                <>{statValue.toFixed(2)}</>
              ) : (
                <ul>
                  {Object.entries(statValue).map(
                    ([subStatName, subStatValue]) => (
                      <li key={subStatName}>
                        {subStatName}: {subStatValue.toFixed(2)}
                      </li>
                    )
                  )}
                </ul>
              )}
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
