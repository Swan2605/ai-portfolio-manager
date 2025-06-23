from firebase_admin import credentials, firestore, initialize_app
import datetime

cred = credentials.Certificate("MY-firebase-key.json")
initialize_app(cred)
db = firestore.client()

trade_log = {
    'buy': ['GOOGL'],
    'sell': ['TSLA'],
    'timestamp': datetime.datetime.now()
}
db.collection('trades').add(trade_log)
