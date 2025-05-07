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
    # Get and Print table title
    title = table.tbody.tr.th.big.big.string
    print(f"Table: {title}")

    # Get all rows in the tbody
    rows = table.tbody.find_all('tr')

    for row in rows:
        # Find the <a> tag and print the component name (title)
        a = row.find('a')
        if not a or not a.get('title'):
            continue

        print(a['title'])

        # Find the <img> tag and print the link
        img = a.find('img')
        if not img or not a.find('img'):
            continue

        print(img['src'])


'''
{'Glider': [],
 'Speed': ['Water(SW)',
           'Air(SA)',
           'Anti-Gravity(SG)',
           'Ground(TL)'],
 'Acceleration(AC)': [],
 'Weight(WG)': [],
 'Handling': ['Ground(TL)',
              'Water(TW)',
              'Air(TA)',
              'Anti-Gravity(TG)'],
 '(Off-Road) Traction(OF)': [],
 'Mini-Turbo(MT)': [],
 'Invincibility(IV)': [],
 'On-Road Traction(ON)1': []
 }
'''