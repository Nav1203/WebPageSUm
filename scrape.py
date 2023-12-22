# from bs4 import BeautifulSoup
# from selenium import webdriver

# url = "https://ellicium.com/blog/5-efficient-ways-to-extract-text-from-articles/#:~:text=Html2text,designed%20for%20article%20text%20extraction."

# driver = webdriver.Chrome()  

# driver.get(url)

# html = driver.page_source

# soup = BeautifulSoup(html, 'html.parser')

# paragraphs = soup.find_all(['li','p','h1','h2','h3','h4','h5','h6'])
# for element in paragraphs:
#     print(element.get_text())

# driver.quit()

from bs4 import BeautifulSoup
from selenium import webdriver
class GetWebpageData:
    def __init__(self):
        self.driver=webdriver.Chrome()
    def getTextfromURL(self,url):
        self.driver.get(url)
        html=self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        return text

# import requests
# from bs4 import BeautifulSoup
# url = "https://www.isro.gov.in/Making_Chandrayaan3_ISRO_culture.html"  
# response = requests.get(url)
# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     all_elements = []
#     lines = soup.find_all('li',class_ = False,id = False)
#     paragraphs = soup.find_all('p',id = False)
#     title = soup.find('title')
#     headings = soup.find_all(['h1', 'h2', 'h3', 'h4'])
#     for line in lines:
#         if not line.find_all():
#             all_elements.append(line)

#     all_elements.extend(paragraphs)
#     if title:
#         all_elements.append(title)
#     all_elements.extend(headings)

#     for element in all_elements:
#         text = element.get_text(strip=True)
#         print(text)

# else:
#     print(f"Failed to retrieve the web page. Status code: {response.status_code}")

import requests
from bs4 import BeautifulSoup
url = "https://www.brookings.edu/articles/how-artificial-intelligence-is-transforming-the-world/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.descendants
    all_elements = []
    def has_span_ancestor(element):
        return any(ancestor.name == 'span' for ancestor in element.parents)
    for element in elements:
        if element.name == 'li' and not element.find_all() and not element.has_attr('class') and not element.has_attr('id') and not has_span_ancestor(element):
            text = element.get_text(strip=True)
            all_elements.append(text)
        if element.name in ['title','h1','h2','h3','h4'] and not has_span_ancestor(element):
            text = element.get_text(strip=True)
            all_elements.append(text)
        if element.name == 'p' and not element.has_attr('id') and not has_span_ancestor(element):
            text = element.get_text(strip=True)
            all_elements.append(text)
    return '\n'.join(all_elements)
    print(all_elements)
    # for element in all_elements:
    #     print(element)
    # elements = soup.find_all(['p','li','h1','h2','h3','h4'])
    # for element in elements:
    #     text = element.get_text(strip=True)
    #     print(text)
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")