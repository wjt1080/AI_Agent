from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
import pandas as pd
import os

# create a sentence transformer model
sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
kw_model = KeyBERT(model=sentence_model)

# read in cwe.csv
cwe = pd.read_csv(
    "raw/cwe.csv",
    header=None,
    names=["cwe_id", "description"],
    sep=",",
    quotechar='"',
    skipinitialspace=True,
    encoding="utf-8",
)
cwe_long = pd.read_csv(
    "raw/cwe_long.csv",
    header=None,
    names=["cwe_id", "description"],
    sep=",",
    quotechar='"',
    skipinitialspace=True,
    encoding="utf-8",
)
# extract keywords from cwe descriptions
# cwe["keywords"] = cwe["description"].apply(lambda x: kw_model.extract_keywords(x,
#                                         keyphrase_ngram_range=(1, 3),
#                                         stop_words="english",
#                                         use_maxsum=True, nr_candidates=20, top_n=5))

cwe["keywords"] = cwe["description"].apply(
    lambda x: kw_model.extract_keywords(
        x,
        keyphrase_ngram_range=(1, 3),
        stop_words="english",
        use_mmr=True,
        diversity=0.9,
        top_n=3,
    )
)

cwe_long["keywords"] = cwe_long["description"].apply(
    lambda x: kw_model.extract_keywords(
        x,
        keyphrase_ngram_range=(1, 3),
        stop_words="english",
        use_mmr=True,
        diversity=0.9,
        top_n=3,
    )
)


# write out cwe_kw.csv
cwe.to_csv("parsed/cwe_kw.csv", index=False)
cwe_long.to_csv("parsed/cwe_kw_long.csv", index=False)

# # store keywords in a list
# cwe_kw = []
# for i in range(len(cwe)):
#     for j in range(len(cwe["keywords"][i])):
#             cwe_kw.append(cwe["keywords"][i][j][0])

# # remove duplicates
# cwe_kw = list(dict.fromkeys(cwe_kw))

# with open("parsed/cwe_kw_top_1.txt", "w") as fd:
#     for kw in cwe_kw:
#         fd.write(kw)
#         fd.write(os.linesep)


# # remove non nouns
# import nltk
# cwe_kw = [word for word, pos in nltk.pos_tag(cwe_kw) if pos.startswith('NN')]

# # write to file
# with open("parsed/cwe_kw_top_1_nouns_only.txt", "w") as fd:
#     for kw in cwe_kw:
#         fd.write(kw)
#         fd.write(os.linesep)
