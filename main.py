import requests

apiKey = "054fc0d3da9f4b22bae3746c43b6fb7d"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-1" \
      "0&sortBy=publishedAt&apiKey=054fc0d3da9f4b22bae3746c43b6fb7d"

# Make request
getRequest = requests.get(url=url)

# Get a dictionary with data
content = getRequest.json()

# Access the article titles and description
for articles in content["articles"]:
    print(articles["title"])
    print(articles["description"])
