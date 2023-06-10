import requests
from send_mail import sendMail as se


topic = "tesla"
apiKey = "054fc0d3da9f4b22bae3746c43b6fb7d"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-05-10&sortBy=publishedAt&" \
      "apiKey=054fc0d3da9f4b22bae3746c43b6fb7d&" \
      "language=en"

# Make request
getRequest = requests.get(url=url)

# Get a dictionary with data
content = getRequest.json()


# Access the article titles and description
count = 0
body = ""
for article in content["articles"][:20]:
    if article['title'] is not None:
        body = "Subject: News Daily" \
               + "\n" + body + article['title'] \
               + "\n" + article['description'] \
               + "\n" + article['url'] + 2*"\n"

body_enc = body.encode("utf-8")
se(body_enc)