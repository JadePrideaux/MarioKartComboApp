using MarioKartComboApp.Server.Enums;
using MarioKartComboApp.Server.Models;

namespace MarioKartComboApp.Server.Data
{
    public class MKComponentData
    {
        private static readonly List<MKComponent> drivers = new()
        {
            new MKComponent("Yoshi", new Dictionary<StatType, int>
            {
                { StatType.GroundSpeed, 6 },
                { StatType.MiniTurbo, 4 }
            }, MKComponentType.Driver)
        };

        private static readonly List<MKComponent> bodies = new()
        {
            new MKComponent("Teddy Buggy", new Dictionary<StatType, int>
            {
                { StatType.GroundSpeed, 2 },
                { StatType.MiniTurbo, 6 }
            }, MKComponentType.Body)
        };

        private static readonly List<MKComponent> tires = new()
        {
            new MKComponent("Roller", new Dictionary<StatType, int>
            {
                { StatType.GroundSpeed, 0 },
                { StatType.MiniTurbo, 6 }
            }, MKComponentType.Tires)
        };

        private static readonly List<MKComponent> gliders = new()
        {
            new MKComponent("Cloud Glider", new Dictionary<StatType, int>
            {
                { StatType.GroundSpeed, 0 },
                { StatType.MiniTurbo, 2 }
            }, MKComponentType.Glider)
        };

        // moves a component list to a dictionary with the name value of the object as the key
        public static Dictionary<string, MKComponent> ToDictionaryByName(List<MKComponent> components)
        {
            return components.ToDictionary(component => component.Name, component => component);
        }

        // Automatically generate the dictionary from the lists
        private static readonly Dictionary<MKComponentType, Dictionary<string, MKComponent>> components = new()
        {
            {
                MKComponentType.Driver,
                ToDictionaryByName(drivers)
            },
            {
                MKComponentType.Body,
                ToDictionaryByName(bodies)
            },
            {
                MKComponentType.Tires,
                ToDictionaryByName(tires)
            },
            {
                MKComponentType.Glider,
                ToDictionaryByName(gliders)
            }
        };

        public static Dictionary<MKComponentType, Dictionary<string, MKComponent>> Components => components;
    }
}
