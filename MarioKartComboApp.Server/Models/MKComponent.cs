using MarioKartComboApp.Server.Enums;

namespace MarioKartComboApp.Server.Models
{
    public class MKComponent
    {
        public string Name { get; set; } = string.Empty;
        public Dictionary<StatType, int> Stats { get; set; } = new();
        public MKComponentType Type { get; set; }

        public MKComponent() { }

        public MKComponent(string name, Dictionary<StatType, int> stats, MKComponentType type)
        {
            Name = name;
            Stats = stats ?? new();
            Type = type;
        }
    }
}
