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


# url = "https://www.isro.gov.in/Making_Chandrayaan3_ISRO_culture.html"  

# driver = webdriver.Chrome()  

# driver.get(url)

# html = driver.page_source

# soup = BeautifulSoup(html, 'html.parser')

# text = soup.get_text()

# print(text)

# driver.quit()

