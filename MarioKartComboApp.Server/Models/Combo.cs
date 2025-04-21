using MarioKartComboApp.Server.Enums;

namespace MarioKartComboApp.Server.Models
{
    public class Combo
    {
        public Dictionary<MKComponentType, MKComponent> MKComponents { get; set; } = [];
        public Stats Stats { get; set; }

        public Combo(Dictionary<MKComponentType, MKComponent> components)
        {
            MKComponents = components;
            Stats = CalculateStats();
        }

        // Calculates the combo stats from the components
        public Stats CalculateStats()
        {
            Stats combinedStats = new();

            foreach (MKComponent component in MKComponents.Values)
            {
                combinedStats.Add(component.Stats);
            }

            return combinedStats.FinalizeStats();
        }
    }
}
