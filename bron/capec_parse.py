#!/usr/bin/env python3

import json
import sys
import re


def read_clean_write():
    with open(sys.argv[1], "r") as f, open(sys.argv[2], "w") as g, open(
        sys.argv[3], "w"
    ) as h:
        data = json.load(f)

        objects = data["objects"]
        prev_capec_id = None
        for i in objects:
            try:
                if i["type"] == "attack-pattern":
                    name = i["name"]
                    desc = i["description"]
                    external = i["external_references"][0]
                    x = 1

                    while external["source_name"] != "capec":
                        external = i["external_references"][x]
                        x += 1

                    # clean text
                    desc = clean_text(desc)
                    if desc is None:
                        continue

                    g.write(f"{external['external_id']},\"{name}\"\n")
                    prev_capec_id = external["external_id"]

                elif i["type"] == "course-of-action":
                    if prev_capec_id is None:
                        continue

                    name = i["name"]
                    desc = i["description"]

                    # clean text
                    desc = clean_text(desc)
                    if desc is None:
                        continue

                    h.write(f'{prev_capec_id},{name},"{desc}"\n')
            except:
                pass


def clean_text(text):
    # remove all xhtml tags
    text = re.sub("<[^<]+?>", "", text)
    # remove all multiple spaces
    text = re.sub(" {2,}", " ", text)
    # remove all leading and trailing spaces
    text = text.strip()
    # remove all blank lines
    if text == "":
        return None
    return text


if __name__ == "__main__":
    read_clean_write()
