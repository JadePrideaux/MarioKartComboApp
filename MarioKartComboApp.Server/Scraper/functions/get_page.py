import requests


def load_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Response OK!")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
