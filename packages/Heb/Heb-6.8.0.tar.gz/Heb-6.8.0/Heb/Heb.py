import pyperclip
class Heb:
    def p1(self):
        print('''
    import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
import string
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
def preprocess_text(text):
 # Tokenization
 tokens = word_tokenize(text.lower())
 # Remove punctuation
 tokens = [token for token in tokens if token not in string.punctuation]
 # Remove stopwords
 stop_words = set(stopwords.words('english'))
 tokens = [token for token in tokens if token not in stop_words]
 return tokens
def lemmatize(tokens):
 lemmatizer = WordNetLemmatizer()
 lemmas = [lemmatizer.lemmatize(token) for token in tokens]
 return lemmas
def stem(tokens):
 stemmer = PorterStemmer()
 stems = [stemmer.stem(token) for token in tokens]
 return stems
def main():
 # Sample text
 text = "Tokenization is the process of breaking down text into words and phrases. Stemming
and Lemmatization are techniques used to reduce words to their base form."
 # Preprocess text
 tokens = preprocess_text(text)
 # Lemmatization
 lemmas = lemmatize(tokens)
 print("Lemmatization:")
 print(lemmas)
 # Stemming
 stems = stem(tokens)
 print("\nStemming:")
 print(stems)
if __name__ == "__main__":
    main()
''')
    def p2(self):
        print('''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
# Load the financial dataset
data = pd.read_csv("financial_dataset.csv") # Replace "financial_dataset.csv" with your dataset
filename
# Preprocess the data
# Assuming the dataset has two columns: "text" containing the text data and "sentiment" containing
sentiment labels
X = data['text']
y = data['sentiment']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Vectorize the text data using N-gram model
vectorizer = CountVectorizer(ngram_range=(1, 2)) # You can adjust the n-gram range
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
# Train the classifier
classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)
# Predict sentiment on the test set
y_pred = classifier.predict(X_test_vectorized)
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
# Display classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

''')
    def p3(self):
        print('''  
    import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim.models import Word2Vec
# Sample text data
text_data = [
 "This is the first document.",
 "This document is the second document.",
 "And this is the third one.",
 "Is this the first document?",
]
# i) One Hot Encoding
def one_hot_encoding(text_data):
 unique_words = set(" ".join(text_data).split())
 encoded_data = []
 for text in text_data:
 encoded_text = [1 if word in text else 0 for word in unique_words]
 encoded_data.append(encoded_text)
 return np.array(encoded_data)
one_hot_encoded = one_hot_encoding(text_data)
print("One Hot Encoding:")
print(one_hot_encoded)
              
# ii) Bag of Words (BOW)
vectorizer = CountVectorizer()
bow_features = vectorizer.fit_transform(text_data)
print("\nBag of Words (BOW):")
print(bow_features.toarray())
              
# iii) n-grams
ngram_vectorizer = CountVectorizer(ngram_range=(1, 2))
ngram_features = ngram_vectorizer.fit_transform(text_data)
print("\nn-grams:")
print(ngram_features.toarray())
              
# iv) Tf-Idf
tfidf_vectorizer = TfidfVectorizer()
tfidf_features = tfidf_vectorizer.fit_transform(text_data)
print("\nTf-Idf:")
print(tfidf_features.toarray())
              
# v) Custom features (e.g., length of documents)
custom_features = np.array([[len(doc)] for doc in text_data])
print("\nCustom Features:")
print(custom_features)
              
# vi) Word2Vec (Word Embedding)
word2vec_model = Word2Vec([doc.split() for doc in text_data], min_count=1)
word2vec_features = np.array([np.mean([word2vec_model[word] for word in doc.split()],
axis=0) for doc in text_data])
print("\nWord2Vec (Word Embedding) Features:")
print(word2vec_features)
''')
    def p4(self):
        print('''
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer
# Sample text data
documents = [
 "baseball soccer basketball",
 "soccer basketball tennis",
 "tennis cricket",
 "cricket soccer"
]
# Create a CountVectorizer to convert text data into a matrix of token counts
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
# Apply Latent Semantic Analysis (LSA)
lsa = TruncatedSVD(n_components=2) # You can adjust the number of components/topics
lsa.fit(X)
# Extract the components/topics
terms = vectorizer.get_feature_names()
topic_matrix = np.array([lsa.components_[i] / np.linalg.norm(lsa.components_[i]) for i in
range(lsa.components_.shape[0])])
# Print the topics
print("Top terms for each topic:")
for i, topic in enumerate(topic_matrix):
 top_indices = topic.argsort()[-5:][::-1] # Get the top 5 terms for each topic
 top_terms = [terms[index] for index in top_indices]
 print(f"Topic {i + 1}: {' '.join(top_terms)}")

''')
    def p5(self):
        print('''
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
              
# Load the 20 newsgroups dataset (a sample dataset included in scikit-learn)
newsgroups_train = fetch_20newsgroups(subset='train')
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(newsgroups_train.data,
newsgroups_train.target, test_size=0.2, random_state=42)
# Vectorize the text data using TF-IDF representation
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
# Train Naïve Bayes classifier
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_vectorized, y_train)
# Predict using Naïve Bayes classifier
nb_predictions = nb_classifier.predict(X_test_vectorized)
              
# Train SVM classifier
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train_vectorized, y_train)
# Predict using SVM classifier
svm_predictions = svm_classifier.predict(X_test_vectorized)

# Evaluate Naïve Bayes classifier
print("Naïve Bayes Classifier:")
print(classification_report(y_test,nb_predictions,target_names=newsgroups_train.target_
names))
# Evaluate SVM classifier
print("\nSupport Vector Machine (SVM) Classifier:")
print(classification_report(y_test,svm_predictions,target_names=newsgroups_train.target
_names)) 

''')
    def p6(self):
        print('''
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.datasets import fetch_20newsgroups
# Load the 20 newsgroups dataset (a sample dataset included in scikit-learn)
newsgroups = fetch_20newsgroups(subset='all')
# Vectorize the text data using TF-IDF representation
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(newsgroups.data)
# Perform K-means clustering
k = 20 # Number of clusters (you can adjust this)
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)
# Print top terms for each cluster
terms = vectorizer.get_feature_names()
order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
for i in range(k):
 print(f"Cluster {i + 1}:")
 top_terms = [terms[ind] for ind in order_centroids[i, :5]]
 print(top_terms)
''')
    def p7(self):
        print('''

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
# Sample text
text = "John likes to play football with his friends."
# Tokenize the text
tokens = word_tokenize(text)
# Rule-based PoS tagging
def rule_based_pos_tagging(tokens):
 tagged_tokens = []
 for token in tokens:
 if token.lower() in ["john", "he", "his"]:
 tagged_tokens.append((token, 'NNP')) # Proper noun
 elif token.lower() in ["likes", "play"]:
 tagged_tokens.append((token, 'VB')) # Verb
 elif token.lower() in ["to", "with"]:
 tagged_tokens.append((token, 'TO')) # To or preposition
 elif token.lower() in ["football", "friends"]:
 tagged_tokens.append((token, 'NN')) # Noun
 else:
 tagged_tokens.append((token, 'NN')) # Default to noun
 return tagged_tokens
# Statistical PoS tagging
def statistical_pos_tagging(tokens):
 tagged_tokens = pos_tag(tokens)
 return tagged_tokens
# Remove stopwords for better accuracy in statistical PoS tagging
stop_words = set(stopwords.words('english'))
tokens_without_stopwords = [token for token in tokens if token.lower() not in stop_words]
# Perform PoS tagging
rule_based_tags = rule_based_pos_tagging(tokens)
statistical_tags = statistical_pos_tagging(tokens_without_stopwords)
# Display the results
print("Rule-based PoS tagging:")
print(rule_based_tags)
print("\nStatistical PoS tagging:")
print(statistical_tags)

''')
    def p8(self):
        print('''
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from keras.callbacks import LambdaCallback
import random
import sys
# Load and preprocess the text data
with open('text_corpus.txt', 'r', encoding='utf-8') as f:
 text = f.read().lower()
chars = sorted(list(set(text)))
char_indices = {char: i for i, char in enumerate(chars)}
indices_char = {i: char for i, char in enumerate(chars)}
max_len = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - max_len, step):
 sentences.append(text[i: i + max_len])
 next_chars.append(text[i + max_len])

x = np.zeros((len(sentences), max_len, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
 for t, char in enumerate(sentence):
 x[i, t, char_indices[char]] = 1
 y[i, char_indices[next_chars[i]]] = 1
# Define the LSTM model
model = Sequential()
model.add(LSTM(128, input_shape=(max_len, len(chars))))
model.add(Dense(len(chars), activation='softmax'))
# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam')
# Function to sample the next character
def sample(preds, temperature=1.0):
 preds = np.asarray(preds).astype('float64')
 preds = np.log(preds) / temperature
 exp_preds = np.exp(preds)
 preds = exp_preds / np.sum(exp_preds)
 probas = np.random.multinomial(1, preds, 1)
 return np.argmax(probas)
              # Function to generate text
def generate_text(seed_text, temperature=0.5, generated_text_length=400):
 generated_text = seed_text.lower()
 for i in range(generated_text_length):
 x_pred = np.zeros((1, max_len, len(chars)))
 for t, char in enumerate(seed_text):
 x_pred[0, t, char_indices[char]] = 1.
 preds = model.predict(x_pred, verbose=0)[0]
 next_index = sample(preds, temperature)
 next_char = indices_char[next_index]
 generated_text += next_char
 seed_text = seed_text[1:] + next_char
 return generated_text
# Train the model and generate text
def on_epoch_end(epoch, _):
 print()
 print('----- Generating text after Epoch: %d' % epoch)
 start_index = random.randint(0, len(text) - max_len - 1)
 for temperature in [0.2, 0.5, 1.0]:
 seed_text = text[start_index: start_index + max_len]
 generated_text = generate_text(seed_text, temperature)
 print('----- Temperature:', temperature)
 print(seed_text + generated_text)
print_callback = LambdaCallback(on_epoch_end=on_epoch_end)
# Fit the model
model.fit(x, y,
 batch_size=128,
 epochs=30,
 callbacks=[print_callback])


''')
    def p9(self):
        print('''
import numpy as np
from hmmlearn import hmm
from sklearn_crfsuite import CRF
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
# Toy dataset for sequence tagging
X = [['walk', 'in', 'the', 'park'],
 ['eat', 'apple'],  
 ['eat', 'apple', 'in', 'the', 'morning']]
y = [['V', 'P', 'D', 'N'],
 ['V', 'N'],
 ['V', 'N', 'P', 'D', 'N']]
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Hidden Markov Model (HMM)
hmm_model = hmm.MultinomialHMM(n_components=3) # Number of states
hmm_model.fit(np.concatenate(X_train), [len(seq) for seq in X_train], [item for sublist in
y_train for item in sublist])
# Conditional Random Fields (CRF)
crf_model = CRF()
crf_model.fit(X_train, y_train)
# Evaluation
print("HMM Results:")
hmm_pred = hmm_model.predict(np.concatenate(X_test), [len(seq) for seq in X_test])
print(classification_report([item for sublist in y_test for item in sublist], [item for sublist in
hmm_pred for item in sublist]))
print("\nCRF Results:")
crf_pred = crf_model.predict(X_test)
print(classification_report([item for sublist in y_test for item in sublist], [item for sublist in
crf_pred for item in sublist]))
''')