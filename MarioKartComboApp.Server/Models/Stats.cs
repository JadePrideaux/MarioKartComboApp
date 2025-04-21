namespace MarioKartComboApp.Server.Models
{
    /* 
        Stats object mirrors the layout in the json and on the website, 
        grouping Speed and Handling stats into their own sub classes.
    */

    public class Stats
    {
        public SpeedStats Speed { get; set; } = new();
        public HandlingStats Handling { get; set; } = new();
        public int Acceleration { get; set; }
        public int Weight { get; set; }
        public int OffRoadTraction { get; set; }
        public int OnRoadTraction { get; set; }
        public int MiniTurbo { get; set; }
        public int Invincibility { get; set; }

        public Stats() { }

        // Helper method to add stats, for each stat, add this stat value to the other stat value
        public void Add(Stats other)
        {
            Speed.Ground += other.Speed.Ground;
            Speed.Water += other.Speed.Water;
            Speed.Air += other.Speed.Air;
            Speed.AntiGravity += other.Speed.AntiGravity;

            Handling.Ground += other.Handling.Ground;
            Handling.Water += other.Handling.Water;
            Handling.Air += other.Handling.Air;
            Handling.AntiGravity += other.Handling.AntiGravity;

            Acceleration += other.Acceleration;
            Weight += other.Weight;
            OffRoadTraction += other.OffRoadTraction;
            OnRoadTraction += other.OnRoadTraction;
            MiniTurbo += other.MiniTurbo;
            Invincibility += other.Invincibility;
        }

        // Converts the sum stats to their combo values
        public Stats FinalizeStats()
        {
            return new Stats
            {
                Speed = new SpeedStats
                {
                    Ground = (Speed.Ground + 3) / 4,
                    Water = (Speed.Water + 3) / 4,
                    Air = (Speed.Air + 3) / 4,
                    AntiGravity = (Speed.AntiGravity + 3) / 4,
                },
                Handling = new HandlingStats
                {
                    Ground = (Handling.Ground + 3) / 4,
                    Water = (Handling.Water + 3) / 4,
                    Air = (Handling.Air + 3) / 4,
                    AntiGravity = (Handling.AntiGravity + 3) / 4,
                },
                Acceleration = (Acceleration + 3) / 4,
                Weight = (Weight + 3) / 4,
                OffRoadTraction = (OffRoadTraction + 3) / 4,
                OnRoadTraction = (OnRoadTraction + 3) / 4,
                MiniTurbo = (MiniTurbo + 3) / 4,
                Invincibility = (Invincibility + 3) / 4,
            };
        }
    }

    public class SpeedStats
    {
        public int Ground { get; set; }
        public int Water { get; set; }
        public int Air { get; set; }
        public int AntiGravity { get; set; }
    }

    public class HandlingStats
    {
        public int Ground { get; set; }
        public int Water { get; set; }
        public int Air { get; set; }
        public int AntiGravity { get; set; }
    }
}
