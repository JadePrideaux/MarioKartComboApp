import { useEffect } from "react";
import { useCombo } from "../hooks/useCombo";
import ComboComponents from "./ComboComponents";
import ComboStats from "./ComboStats";
import LoadMessage from "./LoadMessage";

function Combo() {
  const { combo, loading, fetchCombo } = useCombo();

  useEffect(() => {
    fetchCombo();
  }, [fetchCombo]);

  return (
    <>
      <button onClick={fetchCombo}>Get Random Combo</button>

      {loading && <LoadMessage />}

      {combo && (
        <>
          <ComboComponents mkComponents={combo.mkComponents} />
          <ComboStats stats={combo.stats} />
        </>
      )}
    </>
  );
}

export default Combo;
