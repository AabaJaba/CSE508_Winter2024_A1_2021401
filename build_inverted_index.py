import pickle
import os
from collections import defaultdict

def build_unigram_index(dataset_path):
    inverted_index = defaultdict(list)
    for filename in os.listdir(dataset_path):
        with open(os.path.join(dataset_path, filename), 'r') as file:
            tokens = file.read().split()
            for token in tokens:
                inverted_index[token].append(filename)
    return inverted_index

def save_unigram_index(inverted_index, filename):
    with open(filename + ".pkl", 'wb') as file:
        pickle.dump(inverted_index, file)

def load_unigram_index(filename):
    with open(filename + ".pkl", 'rb') as file:
        inverted_index = pickle.load(file)
    return inverted_index

dataset_path = r"G:\My Drive\code\IR ass 1\preprocessed"
filename = "Inverted_Index"

unigram_index = build_unigram_index(dataset_path)
save_unigram_index(unigram_index, filename)
print("Inverted Unigram Index has been BUILT and SAVED.")
