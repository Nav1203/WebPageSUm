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

url = "https://training.seer.cancer.gov/"  

driver = webdriver.Chrome()  

driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

text = soup.get_text()

print(text)

driver.quit()

