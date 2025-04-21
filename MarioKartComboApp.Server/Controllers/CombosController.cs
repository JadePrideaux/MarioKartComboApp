using MarioKartComboApp.Server.Enums;
using MarioKartComboApp.Server.Interfaces;
using MarioKartComboApp.Server.Models;
using Microsoft.AspNetCore.Mvc;

namespace MarioKartComboApp.Server.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class CombosController
    (
        ILogger<CombosController> logger,
        IMKComponentDataLoader dataLoader
    ) : ControllerBase
    {
        private readonly ILogger<CombosController> _logger = logger;
        private readonly IMKComponentDataLoader _dataLoader = dataLoader;


        [HttpGet(Name = "GetCombos")]
        public async Task<Combo> Get()
        {
            var components = await _dataLoader.LoadComponentAsync() ?? throw new Exception("Failed to load components.");

            var combo = new Combo(new Dictionary<MKComponentType, MKComponent>
            {
                { MKComponentType.Driver, components[MKComponentType.Driver]["Yoshi"] },
                { MKComponentType.Body, components[MKComponentType.Body]["Mr. Scooty"] },
                { MKComponentType.Tires, components[MKComponentType.Tires]["Roller"] },
                { MKComponentType.Glider, components[MKComponentType.Glider]["Cloud Glider"] }
            });

            return combo;
        }
    }
}