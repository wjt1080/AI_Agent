from crewai import Task
from textwrap import dedent
from datetime import date

class AnalysisTasks():

  def impact_human(self, agent): 
    # def test(x):
    #   print("#########CALL BACK#######")
    #   print(x)
    #   print("#########CALL BACK END#######")
    return Task(description=dedent(f"""
      Thought: Do I need to use a tool? Yes
      Action: Search the internet  
      Action Input: {{"query": "upcoming developments of artificial intelligence in cybersecurity industry"}}                             
      Write a proper analysis about the upcoming developments of artificial intelligence on cybersecurity industry using the Search the internet tool. Use the facts from the tools to help you. 
      Use only English, Make it pretty and well formatted for your readers.       Do not give references.
        If you do your BEST WORK, I'll give you a $10,000 commission!  
      The final answer to the original input question is the full detailed explanation from the Observation.                         Once you have the answer, just output as Final Answer and stop. Do not use "**Final Answer:**" as a header or title.
      Prefix "Final Answer" in your answer.       Final Answer:c

      """),
      agent=agent,
      expected_output="Elaborative and detailed Paragraphs"
      # callback= test
      
    )
  
  # Thought: Do I need to use a tool? Yes
  #     Action: Search the internet      
  #     Action Input: {{"query": "upcoming developments of artificial intelligence in cybersecurity industry"}}                        
  #     Write a proper analysis about the upcoming developments of artificial intelligence on cybersecurity industry using the Search the internet tool. Use the facts from the tools to help you. 
  #     Use only English, Make it pretty and well formatted for your readers.       Do not give references.
  #       If you do your BEST WORK, I'll give you a $10,000 commission!  
  #     The final answer to the original input question is the full detailed explanation from the Observation.                         Once you have the answer, just output as Final Answer and stop. Do not use "**Final Answer:**" as a header or title.
  #     Prefix "Final Answer" in your answer.       Final Answer:c

  def governance(self, agent): 

    return Task(description=dedent(f"""
      Thought: Do I need to use a tool? Yes
      Action: Search the internet                     
      Action Input: {{"query": "AI Governance policies and regulations in the UK, Singapore, USA, China, Saudi Arabia"}}
      Write a proper analysis about the efficacy of the security governance frameworks, policies within the UK, Singapore, USA, China, Saudi Arabia country regarding the regulation and oversight of Artificial Intelligence (AI) systems. This analysis should delve into the specific mechanisms and protocols established to govern the development, deployment, and utilization of AI technologies within various sectors.                             
      Use the facts from the tools to help you. 
      Use only English, Make it pretty and well formatted for your readers.       Do not give references.
      If you do your BEST WORK, I'll give you a $10,000 commission!  
      The final answer to the original input question is the full detailed explanation from the Observation.                         Once you have the answer, just output as Final Answer and stop. Do not use "**Final Answer:**" as a header or title.
      Prefix "Final Answer" in your answer.       Final Answer:c  
                                  
    """),
    agent=agent,
    expected_output="Elaborative and detailed Paragraphs"

  )
  # Action Input: {{"query": "Security Governance Frameworks for AI Systems"}}

  def mandiant(self, agent): 
    # def test(x):
    #   print("#########CALL BACK#######")
    #   print(x)
    #   print("#########CALL BACK END#######")
    return Task(
    
      description=dedent(f"""
      Thought: Do I need to use a tool? Yes
      Action: Search the internet    
      Action Input: {{"query": "The Growing Interest of Threat Actors in Artificial Intelligence (AI) and its Utilization for Malicious Activities"}}                   
      Write a proper analysis about the the interest of threat actors in AI and the utilization of AI capabilities to facilitate various forms of malicious activities using the Search the internet tool. 
      Use the facts from the tools to help you. 
                         
      Use only English, Make it pretty and well formatted for your readers.       Do not give references.
      If you do your BEST WORK, I'll give you a $10,000 commission!  
      The final answer to the original input question is the full detailed explanation from the Observation.                         Once you have the answer, just output as Final Answer and stop. Do not use "**Final Answer:**" as a header or title.
      Prefix "Final Answer" in your answer.       
                          
    """),
  
    agent=agent,
    expected_output="Elaborative and detailed Paragraphs"
    # callback=test
  )
# Action Input: {{"query": "The Growing Interest of Threat Actors in Artificial Intelligence (AI) and its Utilization for Malicious Activities"}}                   

  def introduction (self, agent, list):
    # def test(x):
    #   print("#########CALL BACK#######")
    #   print(x)
    #   print("#########CALL BACK END#######") 
    return Task(description=dedent(f"""
      Write an introduction of a
      Artificial Intelligence landscape report. 
                                    
      For the introduction, State month in report and an appropriate title for the report.
      Use the month and year from this {date.today()} as the published date of this report.                         
      Use only English, Make it pretty and well formatted for your readers.       Do not give references.
      Do not use the words "in conclusion". Do not mention the name of the agent involved in this task.
        If you do your BEST WORK, I'll give you a $10,000 commission!  
      The final answer to the original input question is the full detailed explanation from the Observation.                        Once you have the answer, just output as Final Answer and stop. Do not use "**Final Answer:**" as a header or title.
      Prefix "Final Answer" in your answer.       Final Answer:c                               

    """),
    agent=agent,
    context = list,
    expected_output="summarizing the context given and write an introduction of the report"
    # callback= test

  )   

  def conclusion (self, agent, list): 
    # def test(x):
    #   print("#########CALL BACK#######")
    #   print(x)
    #   print("#########CALL BACK END#######")
    return Task(description=dedent(f"""
      Write a conclusion with prediction about the upcoming TRENDS in Artificial Intelligence cybersecurity.
      Use only English, Make it pretty and well formatted for your readers.       Do not give references.
      Do not mention the name of the agent involved in this task.
      If you do your BEST WORK, I'll give you a $10,000 commission!  
      The final answer to the original input question is the full detailed explanation from the Observation.                         Once you have the answer, just output as Final Answer and stop. Do not use "**Final Answer:**" as a header or title.
      Prefix "Final Answer" in your answer.       Final Answer:c    
                                                               
    """),
    agent=agent,
    context = list,
    expected_output="summarizing the context given and write an introduction of the report"
    # callback= test

  )  

  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $10,000 commission!"