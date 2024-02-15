# CSE508_Winter2024_A1_2021401

Sure, I can expand the README document to provide a more detailed explanation of each script, their functionalities, usage instructions, dependencies, and additional information about the information retrieval system. Here's the expanded README:

Information Retrieval System
This repository contains a Python-based Information Retrieval (IR) system designed to process and retrieve documents based on user queries. The system consists of several scripts for preprocessing text, building inverted and positional indexes, and processing queries efficiently.

Features:
Preprocessing of text data to enhance search accuracy.
Construction of inverted indexes for fast retrieval of documents containing specific terms.
Creation of positional indexes for phrase-based queries.
Support for processing boolean queries with AND, OR, AND_NOT, and OR_NOT operators.
Files:
preprocess.py:

This script preprocesses text data by performing the following steps:
Converting text to lowercase.
Tokenizing text into words.
Removing stopwords (commonly occurring words like 'and', 'the', 'is', etc.).
Removing punctuations.
The preprocessed text is then saved in an output folder for further processing.
build_inverted_index.py:

This script builds an inverted index for unigram terms.
It reads preprocessed text files, identifies unique terms, and maps each term to the documents containing it.
The inverted index is then saved to a pickle file for efficient retrieval.
build_positional_index.py:

This script constructs a positional index for terms, which allows for phrase-based queries.
It reads preprocessed text files, identifies terms along with their positions in each document, and creates a positional index.
The positional index is saved to a pickle file for later use in processing phrase queries.
process_phrases_Q3.py:

This script handles phrase queries using the positional index.
It loads the positional index, preprocesses input phrases, and retrieves documents containing the specified phrases.
The retrieved documents are then displayed along with the number of occurrences of the phrases in each document.
process_queries_Q2.py:

This script processes boolean queries using the inverted index.
It loads the inverted index, preprocesses input queries, and retrieves documents based on the boolean operations specified in the queries.
The retrieved documents are displayed along with the number of occurrences of each term in each document.
Usage:
Installation:

Ensure Python 3.10 and the necessary dependencies (such as NLTK) are installed on your system.
Preprocessing:

Run preprocess.py to preprocess the text data. Adjust input and output folder paths as needed.
Building Indexes:

Run build_inverted_index.py to build the inverted index.
Run build_positional_index.py to build the positional index.
Processing Queries:

For boolean queries, execute process_queries_Q2.py and input the desired queries.
For phrase queries, run process_phrases_Q3.py and input the phrases to search for.
Dependencies:
Python 3.10
NLTK (Natural Language Toolkit) for text preprocessing.
Additional Information:
This IR system provides basic functionalities for document retrieval. It can be extended to support more advanced features such as relevance ranking, term weighting, and query expansion.
The provided scripts are designed to handle relatively small datasets. For larger datasets, consider optimizing the code for efficiency and scalability.
