# main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import re

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

# Function mapping
FUNCTIONS = {
    "ticket_status": "get_ticket_status",
    "schedule_meeting": "schedule_meeting",
    "expense_balance": "get_expense_balance",
    "performance_bonus": "calculate_performance_bonus",
    "office_issue": "report_office_issue"
}

# Endpoint to execute queries
@app.get("/execute")
def execute(q: str = Query(..., description="Task query")):
    q = q.strip()

    # Check each type of query
    if m := re.search(r"ticket (\d+)", q, re.IGNORECASE):
        ticket_id = int(m.group(1))
        return {"name": FUNCTIONS["ticket_status"], "arguments": json.dumps({"ticket_id": ticket_id})}

    elif m := re.search(r"meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)", q, re.IGNORECASE):
        date, time, room = m.groups()
        return {"name": FUNCTIONS["schedule_meeting"], "arguments": json.dumps({"date": date, "time": time, "meeting_room": room})}

    elif m := re.search(r"expense balance for employee (\d+)", q, re.IGNORECASE):
        employee_id = int(m.group(1))
        return {"name": FUNCTIONS["expense_balance"], "arguments": json.dumps({"employee_id": employee_id})}

    elif m := re.search(r"performance bonus for employee (\d+) for (\d+)", q, re.IGNORECASE):
        employee_id, year = map(int, m.groups())
        return {"name": FUNCTIONS["performance_bonus"], "arguments": json.dumps({"employee_id": employee_id, "current_year": year})}

    elif m := re.search(r"office issue (\d+) for the (.+) department", q, re.IGNORECASE):
        issue_code, department = m.groups()
        return {"name": FUNCTIONS["office_issue"], "arguments": json.dumps({"issue_code": int(issue_code), "department": department})}

    else:
        return {"error": "Query not recognized."}

