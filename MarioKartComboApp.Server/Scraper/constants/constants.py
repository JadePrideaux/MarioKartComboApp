# Configure which columns to skip in the tables when reading stats
# (number to skip, index of the row that contains the name)
TABLE_CONFIGS = {
    "Drivers (DV)": {"skip_cols": 2, "name_index": 1},
    "Bodies (BD)": {"skip_cols": 2, "name_index": 0},
    "Tires (TR)": {"skip_cols": 1, "name_index": 0},
    "Gliders (WG)": {"skip_cols": 1, "name_index": 0},
}

# The stats that are shared by all component types
SHARED_STATS = [
    ("Speed", "Ground (SL)"),
    ("Speed", "Water (SW)"),
    ("Speed", "Air (SA)"),
    ("Speed", "Anti-Gravity (SG)"),
    ("Acceleration", None),
    ("Weight", None),
    ("Handling", "Ground (TL)"),
    ("Handling", "Water (TW)"),
    ("Handling", "Air (TA)"),
    ("Handling", "Anti-Gravity (TG)"),
    ("Traction (Off-Road)", None),
    ("Mini-Turbo", None),
    ("Invincibility", None),
    ("Traction (On-Road)", None)
]


# Map the stat stings in the html to their JSON values
STAT_KEY_MAP = {
    "Ground (SL)": "Ground",
    "Water (SW)": "Water",
    "Air (SA)": "Air",
    "Anti-Gravity (SG)": "AntiGravity",
    "Acceleration": "Acceleration",
    "Weight": "Weight",
    "Ground (TL)": "Ground",
    "Water (TW)": "Water",
    "Air (TA)": "Air",
    "Anti-Gravity (TG)": "AntiGravity",
    "Traction (Off-Road)": "OffRoadTraction",
    "Mini-Turbo": "MiniTurbo",
    "Invincibility": "Invincibility",
    "Traction (On-Road)": "OnRoadTraction"
}

# Map the types strings from their HTML to their JSON values
TYPE_KEY_MAP = {
    "Drivers (DV)": "Driver",
    "Bodies (BD)": "Body",
    "Tires (TR)": "Tires",
    "Gliders (WG)": "Glider"
}
