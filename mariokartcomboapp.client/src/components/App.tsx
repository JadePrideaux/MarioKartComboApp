import { useEffect, useState } from "react";
import "../styles/App.css";
import ComboComponents from "./ComboComponents";
import ComboStats from "./ComboStats";
import Footer from "./Footer";
import LoadMessage from "./LoadMessage";

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
    const response = await fetch("combo/randomcombo");
    if (response.ok) {
      const data = await response.json();
      setCombo(data);
    } else {
      console.error("Failed to fetch combo data");
    }
  }

  const contents =
    combo === null ? (
      <LoadMessage />
    ) : (
      <>
        <ComboComponents mkComponents={combo.mkComponents} />
        <ComboStats stats={combo.stats} />
      </>
    );

  return (
    <>
      <h1 id="tableLabel">Mario Kart 8 Deluxe Combo</h1>
      <button onClick={fetchCombo}>Get Random Combo</button>
      {contents}
      <Footer />
    </>
  );
}

export default App;
