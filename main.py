import requests
from send_mail import sendMail as se

apiKey = "054fc0d3da9f4b22bae3746c43b6fb7d"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2023-05-10&sortBy=publishedAt&apiKey=054fc0d3da9f4b22bae3746c43b6fb7d"

# Make request
getRequest = requests.get(url=url)

# Get a dictionary with data
content = getRequest.json()


# Access the article titles and description
count = 0
body = ""
for article in content["articles"]:
    if count <= 5:
        if article["title"] is not None:
            # body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"
            body = body + f"Title: {article['title']}" + "\n" + f"Article: {str({article['description']})}" + 2*"\n"
    else:
        body_enc = body.encode("utf-8")
        se(message=body_enc)
        break

    count = count + 1

   # body = body.encode("utf-8")
    # se(message=body)
