from textblob import TextBlob
from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("MY-firebase-key.json")
initialize_app(cred)
db = firestore.client()

docs = db.collection('news').stream()
for doc in docs:
    text = doc.to_dict().get('description', '')
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    risk_score = 1 - sentiment
    db.collection('risk_scores').add({
        'news_id': doc.id,
        'risk_score': risk_score
    })
