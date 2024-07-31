from crewai import Agent

from tools.search_tools import SearchTools
# from tools.search_tools_copy import SearchToolss

import requests
from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
import time
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
from langchain_anthropic import ChatAnthropic
from langchain_community.tools import DuckDuckGoSearchRun
import os

class AnalysisAgents():
  def __init__(self):
    self.gemini = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest",
                                verbose=True,
                                temperature=0,
                                google_api_key="",
                                max_output_tokens = 8192)
    
    #self.gpt = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106",openai_api_key="")

    #self.mixtral = Ollama(model = "mixtral:8x7b-instruct-v0.1-q3_K_M")
    #self.mixtral = Ollama(model = "mixtral:latest",temperature = 0) #mixtral-8x7B q4 rerun not good. uses word for word but hallucinates and gives instructions on the task instead of writing about the task
    #self.mixtral = Ollama(model = "mistral-instr") #mistral 7B instruct v0.2 q4 first task use 1 article extract point but 2nd task hallucinates, 3rd task did not use tool for last task
    #self.mixtral = Ollama(model = "rubra11B") #only extract 1 point
    #self.mixtral = Ollama(model = "mistral-instr-slerp")

    # self.mixtral = ChatGroq(
    #   temperature=0, 
    #   groq_api_key = '',
    #   model_name='mixtral-8x7b-32768',
    #   max_tokens=32768
    # )
  
    #self.gemini = ChatAnthropic(temperature=0,anthropic_api_key="",model_name="claude-3-haiku-20240307")
    
    #Store callback results
    # self.result = None

  def weak_signal_detection_agent(self):
    return Agent(
      role='Weak Signal Detection Specialist',
      goal="""Identify subtle hints and unusual patterns in AI cybersecurity data that could indicate emerging trends or threats.""",
      backstory="""Specialist in detecting faint signals in vast data sets, skilled in data analysis and anomaly detection.""",
      verbose=True,
      tools=[SearchTools.search_internet],  # This agent gathers data from the internet
      allow_delegation=True,
      llm=self.gemini,
      memory=True
    )

  def signal_analysis_and_amplification_agent(self):
    return Agent(
        role='Signal Analysis and Amplification Expert',
        goal="""Analyze detected weak signals to identify potential trends and amplify them for better visibility and understanding.""",
        backstory="""Expert in statistical analysis and trend forecasting, uses advanced algorithms to enhance signal clarity and predict future implications.""",
        verbose=True,
        allow_delegation=True,
        llm=self.gemini,
        memory=True
    )

  def report_generation_agent(self):
    return Agent(
      role='AI Cybersecurity Future Prediction Report Generator',
      goal="""Generate detailed and actionable reports on future trends and threats in AI cybersecurity based on analyzed and amplified signals.""",
      backstory="""Skilled in narrative generation and data visualization, combines analytical insights with clear reporting.""",
      verbose=True,
      allow_delegation=True,
      llm=self.gemini,
      memory=True
    )
