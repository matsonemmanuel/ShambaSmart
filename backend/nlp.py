from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample training questions mapped to intents
training_data = {
    "maize_planting": [
        "when to plant maize",
        "best time to grow maize",
        "when should I plant corn"
    ],
    "maize_fertilizer": [
        "fertilizer for maize",
        "what fertilizer for corn",
        "how to fertilize maize"
    ],
    "poultry_feeding": [
        "what do chickens eat",
        "feeding poultry",
        "broiler feeding guide"
    ]
}

# Flatten training data
sentences = []
labels = []

for label, texts in training_data.items():
    for text in texts:
        sentences.append(text)
        labels.append(label)

vectorizer = CountVectorizer().fit(sentences)
sentence_vectors = vectorizer.transform(sentences)


def predict_intent(user_input):
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, sentence_vectors)
    best_match_index = similarities.argmax()
    return labels[best_match_index]