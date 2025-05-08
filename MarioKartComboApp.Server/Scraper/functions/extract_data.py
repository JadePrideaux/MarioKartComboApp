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
    # Get Table title
    title = table.find('th').get_text(strip=True)
    print(f"Table: {title}")

    # Define the columns to skip for each table, number to skip, index to start from
    table_configs = {
        "Drivers (DV)": {"skip_cols": 2, "name_index": 1},
        "Bodies (BD)": {"skip_cols": 1, "name_index": 0},
        "Tires (TR)": {"skip_cols": 1, "name_index": 0},
        "Gliders (WG)": {"skip_cols": 1, "name_index": 0},
    }

    # The stats that are shared between each table and their structure.
    shared_stats = [
        ("Speed", "Ground (SL)"), ("Speed", "Water (SW)"), ("Speed", "Air (SA)"), ("Speed", "Anti-Gravity (SG)"),
        ("Acceleration", None),
        ("Weight", None),
        ("Handling", "Ground (TL)"), ("Handling", "Water (TW)"), ("Handling", "Air (TA)"), ("Handling", "Anti-Gravity (TG)"),
        ("Traction (Off-Road)", None),
        ("Mini-Turbo", None),
        ("Invincibility", None),
        ("Traction (On-Road)", None)
    ]

    # Check that the table has a config
    config = table_configs.get(title)
    if not config:
        print(f"No config found for table: {title}")
        return

    skip_cols = config["skip_cols"]
    name_index = config["name_index"]

    rows = table.find_all('tr')[2:]  # skip header rows

    # For each row in the table
    for row in rows:
        cells = row.find_all(['td', 'th'])
        if not cells or len(cells) < skip_cols + len(shared_stats):
            continue

        # Find the name of the component
        a = cells[name_index].find('a')
        if not a or not a.get('title'):
            continue
        name = a['title']

        # Find the image
        img_tag = a.find('img')
        img_url = img_tag['src'] if img_tag else ""

        # Build component
        component = {
            "name": name,
            "type": title,
            "imgURL": img_url,
            "stats": {}
        }

        # Add size value for drivers
        if title == "Drivers (DV)":
            component["size"] = cells[0].get_text(strip=True)

        # Fill the stats dictionary in the component
        for (group, sub), cell in zip(shared_stats, cells[skip_cols:]):
            value = cell.get_text(strip=True)
            try:
                value = int(value)
            except ValueError:
                pass

            if sub:
                component["stats"].setdefault(group, {})[sub] = value
            else:
                component["stats"][group] = value

        print(component)


'''
    Problems:
    
    - Only the first component per row is created
    - Stat names do not match how they should be in the JSON
    - Separate function into separate smaller functions

'''