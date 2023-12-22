from langchain.vectorstores import FAISS
from langchain.text_splitter import TokenTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
import requests
from bs4 import BeautifulSoup

class VectorDB:
    def __init__(self,url) -> None:
        self.vectordb=None
        self.url=url
        self.data=None
    def scrape_data(self):
        # url = "https://www.brookings.edu/articles/how-artificial-intelligence-is-transforming-the-world/"
        response = requests.get(self.url)
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
            
            splitter=TokenTextSplitter(chunk_size=300, chunk_overlap=0)
            self.data= '\n'.join(all_elements)
            docs=splitter.split_text(self.data)
            self.vectordb=FAISS.from_texts(docs,HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-l6-v2")).
            # print(all_elements)
            # for element in all_elements:
            #     print(element)
            # elements = soup.find_all(['p','li','h1','h2','h3','h4'])
            # for element in elements:
            #     text = element.get_text(strip=True)
            #     print(text)
        else:
            print(f"Failed to retrieve the web page. Status code: {response.status_code}")
    