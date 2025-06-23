import requests, datetime
from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("MY-firebase-key.json")
initialize_app(cred)
db = firestore.client()

NEWS_API_KEY = "eb625df88f9448ceb0a7b73546d8ae62"
url = f"https://newsapi.org/v2/top-headlines?category=business&language=en&apiKey={NEWS_API_KEY}"

res = requests.get(url).json()
for article in res.get("articles", []):
    db.collection('news').add({
        'title': article['title'],
        'description': article['description'],
        'publishedAt': article['publishedAt'],
        'timestamp': datetime.datetime.now()
    })
