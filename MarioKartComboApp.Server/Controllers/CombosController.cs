using MarioKartComboApp.Server.Data;
using MarioKartComboApp.Server.Enums;
using MarioKartComboApp.Server.Models;
using Microsoft.AspNetCore.Mvc;

namespace MarioKartComboApp.Server.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class CombosController(ILogger<CombosController> logger) : ControllerBase
    {
        // create a combo with data from MKComponentData
        private static readonly Combo combo = new(
            new Dictionary<MKComponentType, MKComponent>
            {
                {
                    MKComponentType.Driver,
                    MKComponentData.Components[MKComponentType.Driver]["Yoshi"]
                },
                {
                    MKComponentType.Body,
                    MKComponentData.Components[MKComponentType.Body]["Teddy Buggy"]
                },
                {
                    MKComponentType.Tires,
                    MKComponentData.Components[MKComponentType.Tires]["Roller"] },
                {
                    MKComponentType.Glider,
                    MKComponentData.Components[MKComponentType.Glider]["Cloud Glider"]
                }
            }
        );

        private readonly ILogger<CombosController> _logger = logger;

        [HttpGet(Name = "GetCombos")]
        public Combo Get()
        {
            return combo;
        }
    }
}