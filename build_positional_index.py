import os
import pickle


def create_positional_index(dataset_folder):
    positional_index = {}
    for filename in os.listdir(dataset_folder):
        with open(os.path.join(dataset_folder, filename), 'r') as file:
            document_id = filename.split('.')[0]  # Extract document ID
            tokens = file.read().split()  # Tokenize document
            for position, token in enumerate(tokens):
                if token not in positional_index:
                    positional_index[token] = {}
                if document_id not in positional_index[token]:
                    positional_index[token][document_id] = []
                positional_index[token][document_id].append(position)
    return positional_index

def save_positional_index(positional_index, filename):
    with open(filename+".pkl", 'wb') as file:
        pickle.dump(positional_index, file)

dataset_path = r"G:\My Drive\code\IR ass 1\preprocessed"
filename = "Positional_Index"

positional_index=create_positional_index(dataset_path)
save_positional_index(positional_index,filename)