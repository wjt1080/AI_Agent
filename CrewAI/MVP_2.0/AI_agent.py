from crewai import Agent
from tools.search_tools import SearchTools
import requests
from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
import time
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
from langchain_anthropic import ChatAnthropic
from langchain.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq
import os
import re



class AnalysisAgents():
  def __init__(self):
    # self.gemini = ChatGoogleGenerativeAI(model="gemini-pro",
    #                             verbose=True,
    #                             temperature=0.2,
    #                             google_api_key="",
    #                             max_output_tokens = 2048)
    
    #self.gpt = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106",openai_api_key="")

#     model_url = "http://127.0.0.1:5000/v1"
#   # Send HTTP post request to webui API
#     print("Loading Model")
#     HOST = 'localhost:5000'
#     URI = f'http://{HOST}/v1'
#     model = "mixtral-8x7b-instruct-v0.1.Q3_K_M.gguf"
#     # check if llava is loaded. If not, load llava
# #http://127.0.0.1:7860
#     request = {'model_name': model}
#     response = requests.post(f'{URI}/internal/model/load', json=request)

#     # while response.status_code != 200:
#     #     print("tryagain")
#     #     sleep(1)
        
#     self.gemini = ChatOpenAI(
#         openai_api_base = model_url,
#         openai_api_key="",
#         model_name="abcd",
#         max_tokens=2048
#     )

    #self.mixtral = Ollama(model = "mixtral:8x7b-instruct-v0.1-q3_K_M")
    # self.mixtral = Ollama(model = "mixtral:latest",temperature = 0) #mixtral-8x7B q4 rerun not good. uses word for word but hallucinates and gives instructions on the task instead of writing about the task
    # print(self.mixtral)
    #self.mixtral = Ollama(model = "mistral-instr") #mistral 7B instruct v0.2 q4 first task use 1 article extract point but 2nd task hallucinates, 3rd task did not use tool for last task
    #self.mixtral = Ollama(model = "rubra11B") #only extract 1 point
    #self.mixtral = Ollama(model = "mistral-instr-slerp")
    #self.mixtral = Ollama(model = "qwen:32b-chat",temperature =0)
    #self.mixtral = Ollama(model = "qwen:32b-chat-v1.5-q8_0",temperature =0)
    #self.mixtral = Ollama(model = "nous-hermes2-mixtral:8x7b-dpo-q4_K_M",temperature = 0)
    #self.mixtral = Ollama(model = "spooknik/hermes-2-pro-mistral-7b:q8",temperature = 0)
    #self.mixtral = Ollama(model = "cas/nous-hermes-2-mistral-7b-dpo",temperature = 0)
    # self.mixtral = Ollama(model = "wizardlm2:7b-fp16",temperature = 0)
    self.mixtral = Ollama(model = "wizardlm2",temperature = 0)
    
    
    
    
    


    # self.mixtral = ChatGroq(
    #   temperature=0, 
    #   groq_api_key = '',
    #   model_name='mixtral-8x7b-32768',
    #   max_tokens=32768
    # )
  
    #self.mixtral = ChatAnthropic(temperature=0,anthropic_api_key="",model_name="claude-3-haiku-20240307")
    
    #Store callback results
    self.result = None

    self.ref = {1:[],2:[],3:[]}

  def AI_Industry_Analyst(self):
    
    class Document:
      def __init__(self,page_content,metadata):
          self.page_content = page_content
          self.metadata = metadata
          #print(page_content)
          #print(metadata)
    
    def test(x):
      print("\n")
      print("#########CALL BACK IN AGENT#######")
      print(x)
      
      try:
        for item in [x[0][1].substring(1, x[0][1].length-1)]:
            print("here",item, item.metadata['source'])
            self.ref[1].append(item.metadata['source'])
              
      except (AttributeError, IndexError, KeyError):
          pass
      print("#########CALL BACK END IN AGENT#######")
      print("\n")
    

    return Agent(
      role='AI Industry Analyst',
      goal="""AI Industry Analysts Always using the Search the Internet tools, monitor significant events, 
      market sentiments, and analysts' perspectives 
      to provide insights into the evolving landscape of 
      artificial intelligence. They focus particularly on how 
      AI technologies are influencing and shaping 
      various aspects of society. 
      """,
      backstory="""Possess a background in technology, computer science, 
      or a related field. They have strong research and analytical 
      skills, allowing them to interpret complex information and 
      distill key findings. Additionally, effective communication 
      skills are crucial as AI Industry Analysts are tasked 
      with presenting their analyses and insights in a 
      comprehensive report format.
      """,
      verbose=True,
      tools=[
        #BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet
        #CalculatorTools.calculate,
        #SECTools.search_10q,
        #SECTools.search_10k
      ],
      allow_delegation=False,
      llm=self.mixtral,
      # max_iter = 2
      #memory=True
      # step_callback=test
    )

  
  def Cybersecurity_Analyst(self):
    def test(x):
      print("\n")
      print("#########CALL BACK IN AGENT#######")
      try:
        for item in x:
            
            self.ref[2].append(item.metadata['source'])
              
      except (AttributeError, IndexError, KeyError):
          pass
      print("#########CALL BACK END IN AGENT#######")
      print("\n")
      print(self.ref[2])

    return Agent(
      role='Cybersecurity Analyst',
      goal="""Always using the Search the Internet tools. It plays a crucial role in ensuring the security and integrity of AI systems by conducting thorough analyses, evaluating stakeholders' responsibilities, and staying informed about the latest trends in AI security.""",
      backstory="""Several years of experience in cybersecurity, particularly in analyzing security governance frameworks and trends in Artificial Intelligence (AI). They evaluate how these frameworks align with industry best practices and regulatory requirements, identifying strengths, weaknesses, and areas for improvement.""",
      verbose=True,
      tools=[
        
        SearchTools.search_internet
       
      ],
      allow_delegation=False,
      llm=self.mixtral,
      # max_iter = 2
      # memory=True
      # step_callback=test
  )

  

  def editor_advisor(self):
    def test(x):
      print("\n")
      print("#########CALL BACK IN AGENT#######")
      try:
        for item in x:
            self.ref[3].append(item.metadata['source'])
              
      except (AttributeError, IndexError, KeyError):
          pass
      print("#########CALL BACK END IN AGENT#######")
      print("\n")
      print(self.ref[3])

    return Agent(
      role='Editor advisor',
      goal="""Edit the full report to ensure that it is comprehensive""",
      backstory="""You're the most experienced editor""",
      verbose=True,
      # tools=[
      #   SearchTools.search_internet,
      # ],
      allow_delegation=False,
      llm=self.mixtral,
      # max_iter = 2
      # step_callback=test
    )
