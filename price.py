from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import re
url = "https://pricehistoryapp.com/product/govo-gobold-600-bluetooth-wireless-on-ear-headphones-with-mic-15h-play-time-40mm-driver-bluetooth-5-2-passive-noise-cancellation"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract title
title_element = soup.find("h1", class_="font-semibold text-lg")
title = title_element.text.strip() if title_element else "Title not found"

# Extract price
price_element = soup.find("div", class_="relative false")
price = price_element.text.strip() if price_element else "Price not found"

# Extract graph
graph_element = soup.find("img", attrs={"src": re.compile(r".*graph\.png")})
graph = graph_element['src'] if graph_element else None
print("Title:", title)
print("Price:", price)
print(graph)
if graph:
    response = requests.get(graph)
    with open("graph.png", "wb") as file:
        file.write(response.content)

    # Display the graph using matplotlib
    img = plt.imread("graph.png")
    plt.imshow(img)
    plt.axis('off')
    plt.show()
