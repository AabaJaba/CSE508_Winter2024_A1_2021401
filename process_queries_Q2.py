import pickle
import os
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
import string
stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)

def load_unigram_index(filename):
    with open(filename + ".pkl", 'rb') as file:
        inverted_index = pickle.load(file)
    return inverted_index

dataset_path = r"G:\My Drive\code\IR ass 1\preprocessed"
filename = "Inverted_Index"

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

def preprocess_query(query):
    processed_queries=[]
    for sequence, operator in query:
        sequence_list=preprocess_text(sequence)
        operator_list=operator.split(',')
        temp_list= [None]*(len(sequence_list)+len(operator_list))
        temp_list[::2]=sequence_list
        temp_list[1::2]=operator_list
        query_str=" ".join(temp_list)
        processed_queries.append(query_str)
    return processed_queries         

def process_query(query, inverted_index):
    q=query.split()
    
    documents = set(inverted_index[q[0]])
    print(documents)
    for i in range(1, len(q), 2):
        operator = q[i]
        term = q[i+1]
        if operator == "AND":
            documents = documents.intersection(inverted_index[term])
        elif operator == "OR":
            documents = documents.union(inverted_index[term])
        elif operator == "AND_NOT":
            documents = documents.difference(inverted_index[term])
        elif operator == "OR_NOT":
            documents = documents.union(set(os.listdir(dataset_path))).difference(inverted_index[term])
    return documents

#input
queries=[]
N=int(input("Enter the number of queries: "))
for _ in range(N):
    sequence=input("Enter the input sequence: ")
    operation=input("Enter operations seprated by commas: ")
    queries.append((sequence,operation))

#main
inverted_index=load_unigram_index(filename)
query_list=preprocess_query(queries)
for q in query_list:
    ans=process_query(q,inverted_index)
    print(f'Query{query_list.index(q)+1}: {q}')
    print(f'Number of documents retrieved for query{query_list.index(q)+1}: {len(ans)}')
    print(ans)

