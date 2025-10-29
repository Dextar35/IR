import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt_tab')

example_sent = """This is a sample sentence,
                showing off the stop words filtration."""

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)
# converts the words in word_tokens to lower case and then checks whether
#they are present in stop_words or not
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
#with no lower case conversion
filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Sample dataset
dataset = ["The quick brown fox jumps over the lazy dog",
           "Python is a high-level programming language",
           "Data science is an interdisciplinary field"]

# Initialize the stemmer
stemmer = PorterStemmer()

# Perform stemming on the dataset
stemmed_dataset = []
for sentence in dataset:
    words = word_tokenize(sentence)
    stemmed_words = [stemmer.stem(word) for word in words]
    stemmed_sentence = " ".join(stemmed_words)
    stemmed_dataset.append(stemmed_sentence)

# Print the stemmed dataset
print(stemmed_dataset)