from functions.get_page import get_page
from functions.extract_data import extract_data

url = "https://www.mariowiki.com/Mario_Kart_8_Deluxe_in-game_statistics"

# Get the HTML of the webpage
html = get_page(url)

# Extract Data from the HTML page
extract_data(html)
