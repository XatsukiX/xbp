import requests
from bs4 import BeautifulSoup

html = BeautifulSoup("<html><head></head><body></body></html>", "html.parser")
head = html.head
body = html.body
main = html.new_tag("main")
header = html.new_tag("header")
main.append(header)
nav = html.new_tag("nav")
header.append(nav)
ul = html.new_tag("ul")
nav.append(ul)
li = html.new_tag("li")
ul.append(li)
a = html.new_tag("a")
li.append(a)
body.append(main)
div = html.new_tag("div")
main.append(div)
p = html.new_tag("p")
div.append(p)
footer = html.new_tag("footer")
main.append(footer)
footer.append(ul)
ul.append(li)
li.append(a)
footer.append(p)
print(html.prettify())

with open("my_page.html", "w") as file:
    file.write(str(html))