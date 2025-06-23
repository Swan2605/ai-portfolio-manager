from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("MY-firebase-key.json")
initialize_app(cred)
db = firestore.client()

portfolio = {'AAPL': 0.3, 'TSLA': 0.3, 'GOOGL': 0.4}

# Example: TSLA risk is high
portfolio['TSLA'] -= 0.1
portfolio['GOOGL'] += 0.1

db.collection('portfolio_weights').add(portfolio)
