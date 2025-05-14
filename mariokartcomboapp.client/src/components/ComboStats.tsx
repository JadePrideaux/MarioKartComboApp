import styles from "../styles/ComboStats.module.css";

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
  // Manage rendering of subcategories
  const renderSubStats = (
    mainStat: string, // the parent stat
    statObj: Record<string, number> // an object containing all the subcategories of the stats names and values
  ) => {
    const entries = Object.entries(statObj); // convert object to an array of key value pairs

    // create a row for each subcategory and rowspan the main category name across each row
    return entries.map(([subName, value], index) => (
      <tr key={`${mainStat}-${subName}`}>
        {index === 0 && (
          <td rowSpan={entries.length} className={styles.groupCell}>
            {mainStat}
          </td>
        )}
        <td>{subName}</td>
        <td>{value.toFixed(2)}</td>
      </tr>
    ));
  };

  // Render the single stat names to span both columns
  const renderSingularStat = (name: string, value: number) => (
    <tr key={name}>
      <td colSpan={2} className={styles.singularCell}>
        {name}
      </td>
      <td>{value.toFixed(2)}</td>
    </tr>
  );

  return (
    <>
      <h2>Stats:</h2>
      <table className={styles.statsTable}>
        <thead>
          <tr>
            <th>Stat</th>
            <th>Subcategory</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {renderSubStats("Speed", props.stats.speed)}
          {renderSingularStat("Acceleration", props.stats.acceleration)}
          {renderSingularStat("Weight", props.stats.weight)}
          {renderSubStats("Handling", props.stats.handling)}
          {renderSingularStat("Mini-Turbo", props.stats.miniTurbo)}
          {renderSingularStat("Invincibility", props.stats.invincibility)}
          {renderSingularStat("Off-Road Traction", props.stats.offRoadTraction)}
          {renderSingularStat("On-Road Traction", props.stats.onRoadTraction)}
        </tbody>
      </table>
    </>
  );
};

export default ComboStats;
