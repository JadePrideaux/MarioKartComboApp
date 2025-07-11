using MarioKartComboApp.Server.Enums;
using MarioKartComboApp.Server.Interfaces;
using MarioKartComboApp.Server.Models;
using Microsoft.AspNetCore.Mvc;

namespace MarioKartComboApp.Server.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class ComboController
    (
        ILogger<ComboController> logger,
        IMKComponentDataLoader dataLoader
    ) : ControllerBase
    {
        private readonly ILogger<ComboController> _logger = logger;
        private readonly IMKComponentDataLoader _dataLoader = dataLoader;

        [HttpGet("combo", Name = "GetCombo")]
        public async Task<ActionResult<Combo>> Get()
        {
            var components = await _dataLoader.LoadComponentAsync()
                ?? throw new Exception("Failed to load components.");

            // Create a new combo with preset values for components.
            var combo = new Combo(new Dictionary<MKComponentType, MKComponent>
            {
                { MKComponentType.Driver, components[MKComponentType.Driver]["Yoshi"] },
                { MKComponentType.Body, components[MKComponentType.Body]["Mr. Scooty (Mr Scooty)"] },
                { MKComponentType.Tires, components[MKComponentType.Tires]["Roller"] },
                { MKComponentType.Glider, components[MKComponentType.Glider]["Cloud Glider"] }
            });

            return combo;
        }

        [HttpGet("randomcombo", Name = "GetRandomCombo")]
        public async Task<ActionResult<Combo>> GetRandom()
        {
            var components = await _dataLoader.LoadComponentAsync()
                ?? throw new Exception("Failed to load components.");

            var random = new Random();

            // Create a dictionary of random components
            var comboComponents = components.ToDictionary(
                kvp => kvp.Key,
                kvp => kvp.Value.ElementAt(random.Next(kvp.Value.Count)).Value
            );

            // return a new combo using the random component dictionary
            return new Combo(comboComponents);
        }
    }
}