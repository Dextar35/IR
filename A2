import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

docs = [
    ["d1","Welcome to hotel heaven such a lovely place"],
    ["d2","She is buying a stairway to heaven"],
    ["d3","Don't make it bad"],
    ["d4","Take me to the heaven"]
]

best_matches = []
exact_matches = []

query = input("Enter query : ").strip()
if not query:
    print ("Empty query")
else:
    query_tokens = [t.lower() for t in word_tokenize(query) if t.isalnum() and t.lower() not in stop_words]
    for doc_id, text in docs:
        doc_tokens = [t.lower() for t in word_tokenize(text) if t.isalnum() and t.lower() not in stop_words]

        # Best Matches
        any_overlap = any(tokens in doc_tokens for tokens in query_tokens)
        if any_overlap:
            best_matches.append(doc_id)

        # Exact Matches
        if query_tokens and set(query_tokens).issubset(doc_tokens):
            if doc_id in best_matches:
                best_matches.remove(doc_id)
            exact_matches.append(doc_id)

    print ("Best Matches : ",best_matches)
    print ("Exact Matches : ",exact_matches)