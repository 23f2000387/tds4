from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import re
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

def parse_query(q: str):
    q_lower = q.lower()
    # Ticket status
    match = re.search(r"ticket (\d+)", q_lower)
    if "status of ticket" in q_lower and match:
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({"ticket_id": int(match.group(1))})
        }
    return {"name": "unknown", "arguments": "{}"}

@app.get("/execute")
def execute(q: str = Query(...)):
    return parse_query(q)
