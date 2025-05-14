interface ComboStats {
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

type Props = {
  stats: ComboStats["stats"];
};

const ComboStats = (props: Props) => {
  return (
    <>
      <h2>Stats:</h2>
      <ul>
        {Object.entries(props.stats).map(([statName, statValue]) => (
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
};

export default ComboStats;
