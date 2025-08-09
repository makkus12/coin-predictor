from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow CORS for all origins (frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict/{symbol}")
def predict(symbol: str):
    # Get latest price from Binance API
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}USDT"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Symbol not found or API error"}
    
    data = response.json()
    price = float(data["price"])

    # Example target calculation (simple percentages)
    targets = {
        "price": price,
        "target1": round(price * 1.05, 4),  # +5%
        "target2": round(price * 1.10, 4),  # +10%
        "target3": round(price * 1.20, 4),  # +20%
    }

    return targets
