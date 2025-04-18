using MarioKartComboApp.Server.Enums;

namespace MarioKartComboApp.Server.Models
{
    public class Combo
    {
        public Dictionary<MKComponentType, MKComponent> MKComponents { get; set; } = [];
        public Dictionary<StatType, float> Stats { get; set; } = [];

        public Combo(Dictionary<MKComponentType, MKComponent> components)
        {
            MKComponents = components;
            Stats = CalculateStats();
        }

        // Calculates the combo stats from the components
        public Dictionary<StatType, float> CalculateStats()
        {
            Dictionary<StatType, int> statTotals = [];

            foreach (MKComponent component in MKComponents.Values)
            {
                foreach (KeyValuePair<StatType, int> stat in component.Stats)
                {
                    // if the stat exist, add it, otherwise set it
                    statTotals[stat.Key] = statTotals.TryGetValue(stat.Key, out int existingValue)
                    ? existingValue + stat.Value
                    : stat.Value;
                }
            }

            Dictionary<StatType, float> comboStats = [];

            // calculate the combo stats based on the (total + 3) / 4
            foreach (KeyValuePair<StatType, int> stat in statTotals)
            {
                float calculatedStat = (stat.Value + 3) / 4f;
                comboStats.Add(stat.Key, calculatedStat);
            }

            return comboStats;
        }
    }
}
