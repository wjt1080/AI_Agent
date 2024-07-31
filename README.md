# Horizon Scanning - data extration and filtration

## Introduction
This module blongs to Horizon Scanning project, mainly focused on the data extraction part, as well as some documentation powerpoints on the HS project. The data extraction part extraction part covers the datasets: CVE(based on Nicholas's work, arxiv paper, google patent, ad-hoc url listing sites- LLMsecurity). Also the report generation part using CrewAI(also refer to Jue Lin's work).

### Requirements
* Python 3
* anaconda

### Code Structure

#### Folders:
* `HS/arxiv_filter/` - script to extract and filter arxiv metadata to AI security related
* `HS/bron/` - base on Nicholas's work on CVE, script to filter with AI security related
* `HS/LLMsecurity/` - script to extract and filter urls on listing sites to AI security related
* `HS/patent_filter/` - script to extract and filter google patent data to AI security related
* `HS/CrewAI/` - report generation with LLMs


#### Files:
* arxiv_filter
  * `HS/arxiv_filter/arxiv_filter_final.ipynb` - Script to filter Arxiv metadata with AI security related
  * `HS/arxiv_filter/final_filter_results.json` - Sample results in json format
  * `HS/arxiv_filter/filtered_papers_eventual.json` - Sample results in xlsx format
* BRON
  * `HS/bron/cve_kw.ipynb` - Script to filter CVE with AI security related
  * rest please refer to Nicholas's `keyword extraction` work
* LLMsecurity
  * `HS/LLMsecurity/llmsecurity_net.ipynb` - Script to scrape and extract url links from llmsecurity site
  * `HS/LLMsecurity/ad_god_url_sites.ipynb` - Script to scrape and extract url links from other sites
  * `HS/LLMsecurity/llmsecurity_scraped_metadata_manualdone.json` -  Sample results in json format
  * other txt files:  Sample results of url links only in txt format(work with Zi An's AI downloader url uploading mode)
* patent_filter
  * `HS/patent_filter/google_patent_api.ipynb` -  Script to scrape and extract google patent through SerpAPI to find AI security related ones
  * `HS/patent_filter/raw_metadata` -  Sample scraped raw metadata in json format 
  * `HS/patent_filter/extracted_data` -  Sample parsed result data in json format 
  * `HS/patent_filter/all_extracted_data` -  Sample final merged result data in json format  
  * `HS/patent_filter/csv_all_extracted_data` -  Sample final merged result data in csv format  
* CrewAI
  * `HS/CrewAI/AI_agent.py` - Script that defines agent roles for crewai framework
  * `HS/CrewAI/AI_task.py` - Script that defines agent tasks for crewai framework
  * `HS/CrewAI/AI_main.py` - Script to define and excute the agent work process for crewai framework
  * `HS/CrewAI/tools/search_tools.py` - Script that defines the tool that will be used by agents
* Powerpts
  * `HS/crewAI_model_gap_analysis.ppt` - powerpts documenting the work for comparing different LLM models for CrewAI
  * `HS/data_source_filtration.ppt` - powerpts documenting the work for data extration and filtration
  * `HS/Horizon Scanning.ppt` - powerpts documenting the idea of Horizon Scanning project


## Usage

### Set up environment and Install dependencies
* `conda create --name horizon` - Creates a conda environment for the module
* `conda activate horizon` - Activates the conda environment we just created
* `pip install -r requirements.txt` - Install dependencies for the module

## Todo

Add what needs to be continued on or further implementations 

## POC

* Wu Jiantao
