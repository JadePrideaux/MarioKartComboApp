using MarioKartComboApp.Server.Enums;
using MarioKartComboApp.Server.Models;

namespace MarioKartComboApp.Server.Interfaces
{
    public interface IMKComponentDataLoader
    {
        Task<Dictionary<MKComponentType, Dictionary<string, MKComponent>>> LoadComponentAsync();
        // For each component type there will be a dict with the component name and the component
    }
}
