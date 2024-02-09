import pickle
import os
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
import string
stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)

def preprocess_text(text):
    text = text.lower()
    
    tokens = wordpunct_tokenize(text)
    
    tokens = [token for token in tokens if token not in stop_words]
    
    for token in tokens:
        for char in token:
            if char in punctuation:
                tokens.remove(token)
                break
    tokens = [token for token in tokens if token not in punctuation]

    tokens = [token for token in tokens if token.strip()]

    preprocessed_text =tokens
    
    return preprocessed_text

def load_positional_index(filename):
    with open(filename+'.pkl', 'rb') as file:
        return pickle.load(file)

def phrase_query(index, phrase):
    terms=preprocess_text(phrase)
    matching_documents = None
    for term in terms:
        postings_list = index.get(term, []) 
        if not matching_documents:
            matching_documents = set(postings_list)
        else:
            matching_documents = matching_documents.intersection(postings_list)
  
    result = []
    for doc_id in matching_documents:
        positions = [index[term][doc_id] for term in terms]
        for pos in positions[0]:
            if all(pos + i in positions[i] for i in range(1, len(positions))):
                result.append(doc_id)
                break

    return result
#input
queries=[]
N=int(input("Enter the number of queries: "))
for i in range(N):
    phrase=input(f"Enter phrase {i+1}:")
    queries.append(phrase)

filename = "Positional_Index"
#main
positional_index=load_positional_index(filename)
for phrase in queries:
    result=phrase_query(positional_index,phrase)
    print(f"Number of documents retrieved for query {queries.index(phrase)} using positional index: {len(result)}")
    print(f"Names of documents retrieved for query {queries.index(phrase)} using positional index: {result}")
    
