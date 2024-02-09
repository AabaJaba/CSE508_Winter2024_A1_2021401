import os
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
import string

stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)

s_count=0

def preprocess_text(text):
    global s_count
    if s_count<=5: print(f"Initial text: {text}\n")
    text = text.lower()
    if s_count<=5: print(f"Lowercased : {text}\n")
    
    tokens = wordpunct_tokenize(text)
    if s_count<=5: print(f"Tokenized : {tokens}\n")
    
    tokens = [token for token in tokens if token not in stop_words]
    if s_count<=5: print(f"Removed stopwords: {tokens}\n")
    
    for token in tokens:
        for char in token:
            if char in punctuation:
                tokens.remove(token)
                break
        
    tokens = [token for token in tokens if token not in punctuation]
    if s_count<=5: print(f"Removed punctuations: {tokens}\n")

    tokens = [token for token in tokens if token.strip()]
    if s_count<=5: print(f"Removed blank tokens : {tokens}\n")

    preprocessed_text = ' '.join(tokens)
    s_count=s_count+1
    
    return preprocessed_text

#FOLDER PATHS
input_folder_path = r'G:\My Drive\code\IR ass 1\input'
output_folder_path = r'G:\My Drive\code\IR ass 1\preprocessed'


for filename in os.listdir(input_folder_path):
    if filename.endswith('.txt'):
        
        input_file_path = os.path.join(input_folder_path, filename)
        output_file_path = os.path.join(output_folder_path, filename)
        
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        if s_count<=5: print(filename)
        preprocessed_text = preprocess_text(text)
        
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(preprocessed_text)
