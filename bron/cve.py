from datetime import datetime
import requests
import gzip
import json
import os
import argparse

CVE_BASE_URL = "https://nvd.nist.gov/feeds/json/cve/1.1"
file_path = "raw/raw_CVE.json.gz"


def download_cve(cve_years):
    combined_cve = {"CVE_Items": []}
    for year in cve_years:
        # Download CVE data for each year
        cve_url = os.path.join(CVE_BASE_URL, f"nvdcve-1.1-{year}.json.gz")
        response = requests.get(cve_url, stream=True)
        year_file_path = f"raw_CVE_{year}.json.gz"
        with open(year_file_path, "wb") as fd:
            for chunk in response.iter_content(chunk_size=128):
                fd.write(chunk)

        # Combine CVE data into one json.gz file
        cve_path = f"raw_CVE_{year}.json.gz"
        with gzip.open(cve_path, "rt", encoding="utf-8") as f:
            cve_data = json.load(f)
        combined_cve["CVE_Items"].extend(cve_data["CVE_Items"])
    json_string = json.dumps(combined_cve)
    encoded = json_string.encode("utf-8")
    with gzip.GzipFile(file_path, "w") as f:
        f.write(encoded)

    assert os.path.exists(file_path)
    print(f"Downloaded CVEs from {CVE_BASE_URL} for {cve_years} to {file_path}")
    # remove individual year files
    for year in cve_years:
        os.remove(f"raw_CVE_{year}.json.gz")
    # remove downloaded file
    # os.remove(file_path)


def parse_cve():
    with gzip.open(file_path, "rt", encoding="utf-8") as f:
        cve_data = json.load(f)
    print(f"Loaded {len(cve_data['CVE_Items'])} CVEs from {file_path}")
    # iterate over each CVE, write to file
    with open("raw/cve.csv", "w") as f:
        for cve in cve_data["CVE_Items"]:
            cve_id = cve["cve"]["CVE_data_meta"]["ID"].strip()
            cve_description = cve["cve"]["description"]["description_data"][0]["value"].strip()
            cve_description = cve_description.replace(","," ").replace("\n","").replace("\r","")
            f.write(f'{cve_id},"{cve_description}"\n')
    print(f"Wrote CVEs text with labels to cve.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # 2 modes: download and parse
    parser.add_argument("mode", choices=["download", "parse"])
    # download mode: specify start and end years
    parser.add_argument("--start_year", type=int, default=2002)
    # end year default to current year, using datetime
    parser.add_argument("--end_year", type=int, default=datetime.now().year)
    args = parser.parse_args()
    # print(parser)
    if args.mode == "download":
        download_cve(range(args.start_year, args.end_year + 1))
    elif args.mode == "parse":
        parse_cve()
