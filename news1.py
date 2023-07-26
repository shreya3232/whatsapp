# import requests
# from lxml import etree

# # Send a GET request to the URL
# url = "https://www.agriculture.com/news/crops"
# response = requests.get(url)

# # Create an lxml HTML parser
# parser = etree.HTMLParser()

# # Parse the HTML content
# tree = etree.fromstring(response.content, parser)

# # Define the XPath expression to find the news links
# xpath_expression = '//*[@id="mntl-card-list-items_2-0-36"]'

# # Find all the news links using XPath
# news_links = tree.xpath(xpath_expression)

# # Extract the href attribute from each news link
# news_urls = [link.get("href") for link in news_links]

# # Print the scraped news links
# for news_url in news_urls:
#     print(news_url)
import requests
from lxml import etree

# Send a GET request to the URL
url = "https://www.agriculture.com/news/crops"
response = requests.get(url)

# Create an lxml HTML parser
parser = etree.HTMLParser()

# Parse the HTML content
tree = etree.fromstring(response.content, parser)

# Define the XPath expression to find the news links
xpath_expression = '/html/body/main/section/div[3]/div[1]/div[4]/div[1]/a[1]'

# Find all the news links using XPath on the tree element
news_links = tree.xpath(xpath_expression)

# Extract the href attribute from each news link
news_urls = [link.get("href") for link in news_links]

# Print the scraped news links
for news_url in news_urls:
    print(news_url)
