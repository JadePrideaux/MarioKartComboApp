using MarioKartComboApp.Server.Enums;

namespace MarioKartComboApp.Server.Models
{
    public class Combo
    {
        // Dictionary of the components within the combo
        public Dictionary<MKComponentType, MKComponent> MKComponents { get; set; } = [];
        // Stats object for the combo
        public Stats Stats { get; set; }

        public Combo(Dictionary<MKComponentType, MKComponent> components)
        {
            MKComponents = components;
            Stats = CalculateStats();
        }

        // Calculates the combo stats from the components
        public Stats CalculateStats()
        {
            // Create new Stats object
            Stats combinedStats = new();

            // For each component add the stats to the sum
            foreach (MKComponent component in MKComponents.Values)
            {
                combinedStats.Add(component.Stats);
            }
            // Return the resulting stats, after the overall formular
            return combinedStats.FinalizeStats();
        }
    }
}
