import { useCallback, useState } from "react";

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

export const useCombo = () => {
  const [combo, setCombo] = useState<Combo | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // only create a new combo if necessary (useCallback), prevents unnecessary repeated calls
  const fetchCombo = useCallback(async () => {
    setLoading(true);

    try {
      const response = await fetch("combo/randomcombo");

      if (!response.ok) {
        console.error(
          `Server returned status ${response.status}: ${response.statusText}`
        );
        setError("Could not load combo. Please try again.");
        setCombo(null);
        return;
      }
      const data = await response.json();
      setCombo(data);
      setError(null);
    } catch (e) {
      console.error("Fetch error:", e);
      setError("Could not load combo. Please try again.");
      setCombo(null);
    } finally {
      setLoading(false);
    }
  }, []);

  // returns the combo, the loading state and the fetch combo method
  return { combo, loading, fetchCombo, error };
};
