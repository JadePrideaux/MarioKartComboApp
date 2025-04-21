using MarioKartComboApp.Server.Enums;

namespace MarioKartComboApp.Server.Models
{
    public class MKComponent
    {
        public string Name { get; set; } = string.Empty;
        public MKComponentType Type { get; set; }
        public string? ImgURL { get; set; }
        public SizeType? Size { get; set; }
        public required Stats Stats { get; set; }

        public MKComponent() { }

        public MKComponent
        (
            string name,
            MKComponentType type,
            string? imgURL,
            SizeType? size,
            Stats stats
        )
        {
            Name = name;
            Type = type;
            ImgURL = imgURL;
            Size = size;
            Stats = stats;

        }

    }
}
