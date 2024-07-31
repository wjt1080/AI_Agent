from crewai import Task
from textwrap import dedent
from datetime import date

class AnalysisTasks():
  def __init__(self):
    pass

  def weak_signal_detection_task(self, agent):
    return Task(
      description=dedent("""                             
                Identify and collect information on weak signals in the AI cybersecurity industry that could indicate emerging threats or opportunities. Use the Search the internet tool to gather the latest data.
                Expected actions:
                - Search the internet for "emerging threats in AI cybersecurity"
                - Analyze the relevance and impact of detected signals.
                - Collate findings into a preliminary analysis report.
                Use only English, formatted well for clarity. Do not include references in the output.
                """),
      agent=agent,
      expected_output="Detailed analysis of detected weak signals"
    )

  def signal_analysis_and_amplification_task(self, agent, previous_task_output):
    return Task(
      description=dedent(f"""
                Analyze the weak signals identified from the previous task to assess potential trends and implications. Utilize advanced analytical tools to amplify these signals.
                Context: {previous_task_output}
                Expected actions:
                - Assess the impact and likelihood of each identified trend.
                - Project how these trends could evolve over time.
                - Prepare a detailed trend analysis report.
                Use only English, ensure the report is well-structured and clear. Do not include references.
                """),
      agent=agent,
      expected_output="Comprehensive report on amplified signals and trend analysis"
    )

  def report_generation_task(self, agent, previous_task_output):
    return Task(
      description=dedent(f"""
                Generate a comprehensive AI cybersecurity future prediction report based on the analyzed data from previous tasks.
                Context: {previous_task_output}
                Expected actions:
                - Summarize key findings and predictions.
                - Format the report to include sections on methodology, analysis, and implications.
                - Ensure the report is reader-friendly and professionally formatted.
                Use only English, and format the document for executive presentation. Do not include references.
                """),
      agent=agent,
      expected_output="Final AI cybersecurity future prediction report"
    )

  # Example additional tasks like introduction or conclusion based on your requirements
  def introduction(self, agent):
    return Task(
      description=dedent("""
                Write an introduction for the AI cybersecurity report, outlining the scope and purpose of the analysis.
                Use the current date for the report's timestamp.
                Use only English, formatted well for readability. Do not include references.
                """),
      agent=agent,
      expected_output="Introduction section of the AI cybersecurity report"
    )

  def conclusion(self, agent, analysis_context):
    return Task(
      description=dedent(f"""
                Draft the conclusion of the AI cybersecurity report, summarizing the findings and offering predictions on future trends.
                Context: {analysis_context}
                Use only English, formatted clearly and professionally. Do not include references.
                """),
      agent=agent,
      expected_output="Conclusion and future outlook section of the report"
    )

