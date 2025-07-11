import { useEffect } from "react";
import { useCombo } from "../hooks/useCombo";
import ComboComponents from "./ComboComponents";
import ComboStats from "./ComboStats";
import ErrorMessage from "./ErrorMessage";
import LoadMessage from "./LoadMessage";

function Combo() {
  const { combo, loading, fetchCombo, error } = useCombo();

  useEffect(() => {
    fetchCombo();
  }, [fetchCombo]);

  return (
    <>
      <button onClick={fetchCombo}>Get Random Combo</button>

      {loading && <LoadMessage />}
      {error && <ErrorMessage message={error} />}

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
