from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
# print(soup.prettify())  # The entire html, formatted
print(soup.a)  # The first anchor tag

all_anchor_tags = soup.findAll(name="a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")  # finds the first match
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
# note: 'class' is reserved keyword, so this attribute is called "class_"

company_URL = soup.select_one(selector="p a")
# refined search using html selector, this is an <a> that sits inside a <p>
# similarly, we can also use #id or .class_name to search for id tag or class







