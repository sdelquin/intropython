import requests
from bs4 import BeautifulSoup

# url of Stranger Things
url = 'https://www.netflix.com/es/title/80057281'

response = requests.get(url)
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

# versión clásica
# cast = []
# for span in soup.find_all('span', class_='item-cast'):
#     cast.append(span.string)

# versión de listas por comprensión
cast = [span.string for span in soup.find_all('span', class_='item-cast')]

cast.sort()
print('\n'.join(cast))
