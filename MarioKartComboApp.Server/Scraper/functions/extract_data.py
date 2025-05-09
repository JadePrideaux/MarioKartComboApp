from bs4 import BeautifulSoup
from constants.constants import TABLE_CONFIGS, SHARED_STATS, STAT_KEY_MAP, TYPE_KEY_MAP


def extract_data(html):
    # Parse HTML data and find the tables
    tables = select_tables(html)
    structured_data = {}
    # Iterate through tables
    for table in tables:
        # Get all the components from that table
        components = process_table_data(table)

        # For each component, get its type and its name
        for component in components:
            comp_type = TYPE_KEY_MAP.get(component["type"], component["type"])
            name = component["name"]
            component["type"] = comp_type

            # If the component type has not been processed yet, create it
            if comp_type not in structured_data:
                structured_data[comp_type] = {}

            # Add the new component to the structured data under its type and its name
            structured_data[comp_type][name] = component

    return structured_data


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

    # Check the table has an associated config
    config = TABLE_CONFIGS.get(title)
    if not config:
        print(f"No config found for table: {title}")
        return

    # Get the columns to skip from the config
    skip_cols = config["skip_cols"]
    name_index = config["name_index"]

    # Get all the standard rows from the table, skipping the headers.
    rows = table.find_all('tr')[2:]

    # Create empty components array to store the components from this table
    components = []

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
        for (group, sub), cell in zip(SHARED_STATS, stat_cells):
            print(f"Processing: Group = {group}, Sub = {sub}, Value = {cell.get_text(strip=True)}")
            # Get the text content from that cell and convert it to an integer
            value = cell.get_text(strip=True)
            try:
                value = int(value)
            except ValueError:
                print(f"Skipping non-integer value: {cell.get_text(strip=True)}")
                continue

            # Get the mapped stat key
            mapped_key = STAT_KEY_MAP.get(sub or group)

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

            components.append(component)

    return components


'''
    Issues:
    - Only the first row with the same size in the driver table is being checked 
    since the cell spans across all rows with the same value

'''
