using MarioKartComboApp.Server.Enums;
using MarioKartComboApp.Server.Interfaces;
using MarioKartComboApp.Server.Models;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace MarioKartComboApp.Server.Data
{
    public class MKComponentDataLoader(string filePath) : IMKComponentDataLoader
    {
        private readonly string _filePath = filePath;

        public async Task<Dictionary<MKComponentType, Dictionary<string, MKComponent>>> LoadComponentAsync()
        {
            var jsonData = await File.ReadAllTextAsync(_filePath);

            var options = new JsonSerializerOptions
            {
                // Make properties not case sensitive
                PropertyNameCaseInsensitive = true,
                // Convert the strings in the json data to enums
                Converters = { new JsonStringEnumConverter() }
            };

            var components = JsonSerializer.Deserialize<Dictionary<MKComponentType, Dictionary<string, MKComponent>>>(jsonData, options);

            // if null, throw exception.
            return components ?? throw new Exception("Failed to load components, data is null.");
        }
    }
}
