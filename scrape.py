from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.ibm.com/topics/data-science"

driver = webdriver.Chrome()  

driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

paragraphs = soup.find_all(['li','p','h1','h2','h3','h4','h5','h6'])
for element in paragraphs:
    print(element.get_text())

driver.quit()
