from bs4 import BeautifulSoup
import requests

# <editor-fold desc="Notes on Beautiful soup">
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# # print(soup.prettify())  # The entire html, formatted
# print(soup.a)  # The first anchor tag
#
# all_anchor_tags = soup.findAll(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")  # finds the first match
# print(heading.getText())
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# # note: 'class' is reserved keyword, so this attribute is called "class_"
#
# company_URL = soup.select_one(selector="p a")
# # refined search using html selector, this is an <a> that sits inside a <p>
# # similarly, we can also use #id or .class_name to search for id tag or class
# </editor-fold>


# <editor-fold desc="Web scraping from live websites">

response = requests.get('https://news.ycombinator.com/')
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
article_tags = soup.findAll(name="a", class_="titlelink")

article_texts = []
article_links = []

for article in article_tags:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

print(article_texts)
print(len(article_texts))
print(article_links)
print(len(article_links))

print(len(soup.findAll(name="span", class_="score")))

article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]
print(article_upvotes)
print(len(article_upvotes) )

largest_num = max(article_upvotes)
largest_index = article_upvotes.index(largest_num)

print(largest_num)
print(article_texts[largest_index])

# </editor-fold>
