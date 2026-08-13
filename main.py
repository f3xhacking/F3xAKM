from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# الروابط الخاصة بمشروعك (تكون مخفية داخل السيرفر الوسيط فقط)
GITHUB_CONFIG_URL = "https://raw.githubusercontent.com/f3xhacking/F3xAKM/main/config.json"
FIREBASE_URL = "https://f3xakm-default-rtdb.firebaseio.com"

@app.get("/")
def home():
    return {"status": "Server is running successfully"}

@app.get("/get-config")
def get_config():
    """جلب إعدادات config.json"""
    try:
        response = requests.get(GITHUB_CONFIG_URL, timeout=5)
        return response.json()
    except Exception:
        raise HTTPException(status_code=500, detail="Error fetching config")

@app.get("/get-db")
def get_db():
    """جلب بيانات Firebase"""
    try:
        response = requests.get(f"{FIREBASE_URL}/.json", timeout=5)
        return response.json()
    except Exception:
        raise HTTPException(status_code=500, detail="Error fetching database")