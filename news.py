# import requests
# from bs4 import BeautifulSoup

# # Send a GET request to the URL
# # url = "https://agrinews.in/latest-news/"
# url="https://agrinews.in/farming/"

# response = requests.get(url)

# # Parse the HTML content
# soup = BeautifulSoup(response.content, "html.parser")

# # Find the relevant HTML elements containing the news links
# news_links = soup.find_all("a", class_="fa-post-thumbnail")

# # Extract the URLs and print them
# for link in news_links:
#     news_url = link["href"]
#     print(news_url)
import csv
import requests
from bs4 import BeautifulSoup
from datetime import date
# List of URLs to scrape
urls = [
    "https://agrinews.in/latest-news/",
    "https://agrinews.in/farming/",
    "https://agrinews.in/livestock/",
    "https://agrinews.in/technology/",
    "https://agrinews.in/food/",
    "https://agrinews.in/agrievents/",
    "https://agrinews.in/agriland/",
    "https://agrinews.in/agri-start-up/"
]

# List to store all the extracted links
all_links = []

# Scrape each URL
for url in urls:
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the relevant HTML elements containing the news links
    news_links = soup.find_all("a", class_="fa-post-thumbnail")

    # Extract the URLs and append them to the list
    links = [link["href"] for link in news_links]
    current_date = date.today().strftime("%Y-%m-%d")

    # Save the data in a CSV file
    csv_filename = f"news_data.csv"
    with open(csv_filename, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:  # Check if the file is empty
            writer.writerow(["News Links",])  # Write the header
        writer.writerows([[link, current_date] for link in links])

    print(f"Successfully saved the news data to {csv_filename}.")
