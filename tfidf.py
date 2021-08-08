import pandas as pd
import string
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk import pos_tag

df = pd.read_csv("preprocessed_dataset.csv", index_col = 0)

stopwords_list = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
def my_tokenizer(doc):
    words = word_tokenize(doc)    
    pos_tags = pos_tag(words)
    non_stopwords = [w for w in pos_tags if not w[0].lower() in stopwords_list]
    non_punctuation = [w for w in non_stopwords if not w[0] in string.punctuation]
    lemmas = []
    for w in non_punctuation:
        if w[1].startswith('J'):
            pos = wordnet.ADJ
        elif w[1].startswith('V'):
            pos = wordnet.VERB
        elif w[1].startswith('N'):
            pos = wordnet.NOUN
        elif w[1].startswith('R'):
             pos = wordnet.ADV
        else:
            pos = wordnet.NOUN
        lemmas.append(lemmatizer.lemmatize(w[0], pos))
    return lemmas

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(tokenizer=my_tokenizer)
tfidf_matrix = tfidf_vectorizer.fit_transform(tuple(df['Question']))


def ask_question_tfidf(question):
    cos_sim = []
    query_vect = tfidf_vectorizer.transform([question])
    sim = cosine_similarity(query_vect, tfidf_matrix)[0].tolist()  
    for i, s in enumerate(sim):
        tup = (i,s)
        cos_sim.append(tup)
    cos_sim.sort(key=lambda x:x[1])
    i1, _ = cos_sim[-1]
    i2, _ = cos_sim[-2]
    i3, _ = cos_sim[-3]
    return i1, i2, i3   