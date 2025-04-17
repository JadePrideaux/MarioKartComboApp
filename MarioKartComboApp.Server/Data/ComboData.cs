using MarioKartComboApp.Server.Models;

namespace MarioKartComboApp.Server.Data
{
    public static class CombosData
    {
        public static Combo DefaultCombo => new Combo(
            driver: ComponentData.Drivers.First(component => component.Name == "Yoshi"),
            body: ComponentData.Bodies.First(component => component.Name == "Teddy Buggy"),
            tires: ComponentData.Tires.First(component => component.Name == "Roller"),
            glider: ComponentData.Gliders.First(component => component.Name == "Cloud Glider")
        );
    }
}
