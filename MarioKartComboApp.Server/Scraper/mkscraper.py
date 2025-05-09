from functions.get_page import get_page
from functions.extract_data import extract_data
from functions.save_to_json import save_to_json

url = "https://www.mariowiki.com/Mario_Kart_8_Deluxe_in-game_statistics"

# Get the HTML of the webpage
html = get_page(url)

# Extract Data from the HTML page
data = extract_data(html)

# Save the data to a JSON
save_to_json(data)
