from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.blackwhitereadallover.com/').text

soup = BeautifulSoup(source, 'lxml')

article = source.find('h2', class_= 'c-entry-box--compact_title').a.text

#headline = article.h2.a.text

print(article)  

#######################################################################
# Njihovo rješenje

# import requests
# from bs4 import BeautifulSoup
 
# base_url = 'http://www.nytimes.com'
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text)
 
# for story_heading in soup.find_all(class_="story-heading"): 
#     if story_heading.a: 
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else: 
#         print(story_heading.contents[0].strip())


##############################################################
# Rješenje od user-a

# import requests
# from bs4 import BeautifulSoup

# r_html = requests.get('https://www.blackwhitereadallover.com/')
# soup = BeautifulSoup(r_html.content, "lxml")
# lines = soup.find_all("h2",{"class": "c-entry-box--compact_title"})

# for line in lines:
# 	print(line.text)
 
