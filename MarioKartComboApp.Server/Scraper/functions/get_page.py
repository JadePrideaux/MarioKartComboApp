import requests
import os


def get_page(url, filename="./data/page.html"):
    try:
        # If the html file exists locally, open the file.
        if os.path.exists(filename):
            print("Loading HTML from local file...")
            # "r": opens file in read mode
            with open(filename, "r", encoding="utf-8") as file:
                html = file.read()
        # Otherwise, load the html file from the webpage.
        else:
            print("Fetching HTML from website...")
            html = load_page(url)
            # If the loaded file is not null
            if html:
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(html)
            else:
                raise ValueError("Failed to fetch page, no HTML returned.")
        return html
    except Exception as e:
        print(f"Error in get_page: {e}")
        return None


def load_page(url):
    try:
        response = requests.get(url)
        # raise an exception if the status code suggests an error
        response.raise_for_status()
        print("Response OK!")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
