from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load Excel data
df = pd.read_excel("dummy_sensor_data.xlsx")

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/sensor-data")
def get_sensor_data():
    # Convert DataFrame to JSON
    return df.to_dict(orient="records")


import webbrowser
import threading

def open_browser():
    webbrowser.open("http://127.0.0.1:8000/sensor-data")

# Only run if script is main
if __name__ == "__main__":
    # Open the browser after a short delay
    threading.Timer(1.0, open_browser).start()
    
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)

