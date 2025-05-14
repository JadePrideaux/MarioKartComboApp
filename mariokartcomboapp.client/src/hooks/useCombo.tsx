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

  // only create a new combo if necessary (useCallback), prevents unnecessary repeated calls
  const fetchCombo = useCallback(async () => {
    // show the loading component
    setLoading(true);

    try {
      const response = await fetch("combo/randomcombo");
      if (response.ok) {
        const data = await response.json();
        setCombo(data);
      } else {
        console.error("Failed to fetch combo data");
      }
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  }, []);

  // returns the combo, the loading state and the fetch combo method
  return { combo, loading, fetchCombo };
};
