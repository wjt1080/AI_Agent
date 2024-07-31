import json
import os

import requests
from langchain.tools import tool

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import PydanticOutputParser
from langchain.text_splitter import CharacterTextSplitter
from textwrap import dedent

class SearchTools():
  @tool("Search the internet")
  def search_internet(query):
      """always use this tool. It is used to search the internet 
      about a given topic and return relevant results"""
      top_result_to_return = 5
      url = "https://google.serper.dev/search"
      payload = json.dumps({"q": query})
      headers = {
          'X-API-KEY': '',
          'content-type': 'application/json'
      }
      response = requests.request("POST", url, headers=headers, data=payload)
      results = response.json()['organic']

      print(f""" response : {response} """)
      urls = []
      for result in results[:top_result_to_return]:
          try:
              if (result['link'] == "https://www.centripetal.ai/blog/cyber-threats-targeting-casinos/" or 
              result['link'] == "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8844981/" or 
              result['link'] == "https://www.esscholars.com/en/qatar/insights/global-ai-regulatory-update-december-2023"):
                 pass
              elif ".pdf" in result['link']:
                 pass
              else:
                urls.append(result['link'])
          except KeyError:
              pass
      print(urls)

      
      #after getting links, split data into chunks

    #   urls = ['https://www.unodc.org/roseap/en/2024/casinos-casinos-cryptocurrency-underground-banking/story.html', 
    #           'https://www.cybersecuritydive.com/news/ransomware-targets-casinos-fbi/699313/', 'https://www.techtarget.com/searchsecurity/news/366558813/FBI-Ransomware-actors-hacking-casinos-via-third-parties', 'https://arcticwolf.com/resources/blog/casinos-can-t-roll-the-dice-in-terms-of-cybersecurity/']
     
      docs = [WebBaseLoader(url).load() for url in urls]
      # print("START DOCS")
      # print(docs)
      # print("END DOCS")
      docs_list = [item for sublist in docs for item in sublist]

      
      text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=5000, chunk_overlap=1000)
      doc_splits = text_splitter.split_documents(docs_list)
      # print(doc_splits)
      # print("#########Printing doc split###########")
      # print(doc_splits[0])
   
      # create simple ids
      ids = [str(i) for i in range(1, len(doc_splits) + 1)]

      # 2. Convert documents to Embeddings and store them
      vectorstore = Chroma.from_documents(
          documents=doc_splits,
          collection_name="rag-chroma-new",
          embedding=OllamaEmbeddings(model='nomic-embed-text'),
          ids = ids
      )
      print("Retrieving info from vector database")
      print(f""" Query: {query} """)
      retriever = vectorstore.similarity_search(query)
    #   instructions = dedent(f"""
  
      # delete the last document
      print("count before", vectorstore._collection.count())
      vectorstore._collection.delete(ids=ids)
      print("count after", vectorstore._collection.count())
      return retriever 


  
