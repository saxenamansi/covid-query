import pandas as pd
import re
from sklearn.metrics.pairwise import cosine_similarity
from gensim.parsing.preprocessing import remove_stopwords

df = pd.read_csv("preprocessed_dataset.csv", index_col = 0)

def clean_sentence(sentence, stopwords=False):   
    sentence = sentence.lower().strip()
    sentence = re.sub(r'[^a-z0-9\s]', '', sentence)
    
    if stopwords:
         sentence = remove_stopwords(sentence)
    return sentence

from sentence_transformers import SentenceTransformer
sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')

import pickle
infile = open("sent_bertphrase_embeddings",'rb')
sent_bertphrase_embeddings = pickle.load(infile)
infile.close()

def ask_question_bert(question):
    question = clean_sentence(question, stopwords=False)
    question_embedding = sbert_model.encode([question])
    cos_sim = []
    for index,faq_embedding in enumerate(sent_bertphrase_embeddings):
        sim=cosine_similarity(faq_embedding,question_embedding)[0][0]
        tup = (index, sim)
        cos_sim.append(tup)
    cos_sim.sort(key=lambda x:x[1])
    i1, _ = cos_sim[-1]
    i2, _ = cos_sim[-2]
    i3, _ = cos_sim[-3]
    return i1, i2, i3

