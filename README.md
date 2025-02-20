# Information Retrieval Project

## Overview
This repository contains the implementation of various information retrieval tasks as part of the **CSE508 - Information Retrieval** course's **Assignment 1**. The project involves preprocessing text data, building an **inverted index**, supporting **Boolean queries**, constructing a **positional index**, and implementing **phrase search queries**.

## Dataset
The dataset consists of **999 text files** and can be accessed using the following link:
[Dataset Link](https://drive.google.com/drive/folders/1E-SSg8SzJQCY2lSLN45eiareFIfuMYcL)

## Project Structure
```
|-- preprocess.py               # Preprocesses text files (lowercasing, tokenization, stopword removal, etc.)
|-- build_inverted_index.py     # Builds and saves a unigram inverted index
|-- build_positional_index.py   # Builds and saves a positional index
|-- process_queries_Q2.py       # Processes Boolean queries using the inverted index
|-- process_phrases_Q3.py       # Processes phrase queries using the positional index
|-- Inverted_Index.pkl          # Pickle file storing the unigram inverted index
|-- Positional_Index.pkl        # Pickle file storing the positional index
|-- CSE508_Winter2024_A1.pdf    # Assignment description file
```

## Features
### 1. Data Preprocessing
- Converts text to lowercase
- Tokenizes text
- Removes stopwords and punctuations
- Saves preprocessed files for further processing

### 2. Inverted Index & Boolean Queries
- Creates a **unigram inverted index**
- Supports Boolean operations:
  - `T1 AND T2`
  - `T1 OR T2`
  - `T1 AND NOT T2`
  - `T1 OR NOT T2`
- Handles multiple Boolean queries

### 3. Positional Index & Phrase Queries
- Creates a **positional index**
- Supports phrase search by checking term positions across documents
- Retrieves documents where the phrase appears in sequence

## How to Run
### Step 1: Preprocess Data
```bash
python preprocess.py
```

### Step 2: Build Indexes
#### Inverted Index
```bash
python build_inverted_index.py
```
#### Positional Index
```bash
python build_positional_index.py
```

### Step 3: Query Processing
#### Boolean Queries
```bash
python process_queries_Q2.py
```
#### Phrase Queries
```bash
python process_phrases_Q3.py
```

## Sample Input/Output
### Boolean Query Example
#### Input:
```
2
Car bag in a canister
OR, AND NOT
Coffee brewing techniques in cookbook
AND, OR NOT, OR
```
#### Output:
```
Query 1: car OR bag AND NOT canister
Number of documents retrieved for query 1: 3
Names of documents retrieved: a.txt, b.txt, c.txt

Query 2: coffee AND brewing OR NOT techniques OR cookbook
Number of documents retrieved for query 2: 2
Names of documents retrieved: d.txt, e.txt
```

### Phrase Query Example
#### Input:
```
2
Car bag in a canister
Coffee brewing techniques in cookbook
```
#### Output:
```
Number of documents retrieved for query 1 using positional index: 2
Names of documents retrieved: a.txt, b.txt

Number of documents retrieved for query 2 using positional index: 2
Names of documents retrieved: a.txt, b.txt
```

## Requirements
- Python 3.x
- `nltk`
- `pickle`

To install dependencies:
```bash
pip install nltk
```

## Notes
- The dataset should be placed in the appropriate directory before running the scripts.
- Ensure that the required Python libraries are installed.
- The pickle files generated (`Inverted_Index.pkl` and `Positional_Index.pkl`) store the indexes for efficient query retrieval.

## Author
Navnoor Singh

## License
This project is for educational purposes as part of the **CSE508 - Information Retrieval** course at IIITD.

