# main.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

@app.get("/execute")
def execute(q: str = Query(...)):
    # Match ticket status
    m = re.match(r"What is the status of ticket (\d+)\?", q)
    if m:
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({"ticket_id": int(m.group(1))})
        }

    # Fallback
    return {"name": "unknown", "arguments": "{}"}
