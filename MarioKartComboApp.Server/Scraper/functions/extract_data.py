from bs4 import BeautifulSoup


def extract_data(html):
    # Parse HTML data and find the tables
    tables = select_tables(html)
    # Iterate through tables
    for table in tables:
        process_table_data(table)
    # Store Extracted Data


def select_tables(html):
    soup = BeautifulSoup(html, 'html.parser')
    print(f"Page title: {soup.title.string}")

    # Select all the necessary tables by checking the class
    tables = soup.find_all('table', class_='sortable scrollable')

    # Check that there are 4 tables (drivers, bodies, tires and gliders)
    if len(tables) != 4:
        print(f"Warning: Expected 4 tables, but found {len(tables)}.")
    else:
        print(f"Found {len(tables)} tables, as expected.")

    return tables


def process_table_data(table):
    title = table.find('th').get_text(strip=True)
    print(f"Table: {title}")

    # Configure which columns to skip in the tables when reading stats
    # (number to skip, index of the row that contains the name)
    table_configs = {
        "Drivers (DV)": {"skip_cols": 2, "name_index": 1},
        "Bodies (BD)": {"skip_cols": 1, "name_index": 0},
        "Tires (TR)": {"skip_cols": 1, "name_index": 0},
        "Gliders (WG)": {"skip_cols": 1, "name_index": 0},
    }

    # The stats that are shared by all component types
    shared_stats = [
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
    stat_key_map = {
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

    # Check the table has an associated config
    config = table_configs.get(title)
    if not config:
        print(f"No config found for table: {title}")
        return

    # Get the columns to skip from the config
    skip_cols = config["skip_cols"]
    name_index = config["name_index"]

    # Get all the standard rows from the table, skipping the headers.
    rows = table.find_all('tr')[2:]

    # Loop though each row in the table
    for row in rows:
        # Find all the individual table cells
        cells = row.find_all(['td', 'th'])
        # Make sure we only check the cells that have not been skipped
        if len(cells) < skip_cols + 1:
            continue

        # Get all the <a> tags inside the cell that contains the component images
        name_cell = cells[name_index]
        a_tags = name_cell.find_all('a', title=True)
        if not a_tags:
            continue

        # Get the cells that contain the stats (the ones after the cells that need to be skipped)
        stat_cells = cells[skip_cols:]

        stats = {}

        # Iterate though each pair from the shared stats and the cells
        for (group, sub), cell in zip(shared_stats, stat_cells):

            # Get the text content from that cell and convert it to an integer
            value = cell.get_text(strip=True)
            try:
                value = int(value)
            except ValueError:
                continue

            # Get the mapped stat key
            mapped_key = stat_key_map.get(sub or group)

            if not mapped_key:
                continue  # Skip if there's no mapped key

            # Add the value either to the sub category or group
            if sub:
                stats.setdefault(group, {})[mapped_key] = value
            else:
                stats[mapped_key] = value

        # Get the size value if its the Drivers Table
        size = cells[0].get_text(strip=True) if title == "Drivers (DV)" else None

        # For each <a> tag, create a new component and add the data in.
        for a in a_tags:
            name = a.get('title')
            img_tag = a.find('img')
            img_url = img_tag['src'] if img_tag else ""

            component = {
                "name": name,
                "type": title,
                "imgURL": img_url,
                "stats": stats.copy()
            }
            if size:
                component["size"] = size

            print(component)


'''
    Problems:
    
    - Separate function into separate smaller functions

'''