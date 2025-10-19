from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import json
import re

app = FastAPI()

# Enable CORS for any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

@app.get("/execute")
def execute(q: str = Query(...)):
    # Default response
    result = {"name": "unknown", "arguments": "{}"}

    # Ticket status
    m = re.match(r"What is the status of ticket (\d+)\?", q)
    if m:
        result = {
            "name": "get_ticket_status",
            "arguments": json.dumps({"ticket_id": int(m.group(1))})
        }

    # Schedule meeting
    m = re.match(r"Schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.", q)
    if m:
        result = {
            "name": "schedule_meeting",
            "arguments": json.dumps({
                "date": m.group(1),
                "time": m.group(2),
                "meeting_room": m.group(3)
            })
        }

    # Expense balance
    m = re.match(r"Show my expense balance for employee (\d+)\.", q)
    if m:
        result = {
            "name": "get_expense_balance",
            "arguments": json.dumps({"employee_id": int(m.group(1))})
        }

    # Performance bonus
    m = re.match(r"Calculate performance bonus for employee (\d+) for (\d+)\.", q)
    if m:
        result = {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({
                "employee_id": int(m.group(1)),
                "current_year": int(m.group(2))
            })
        }

    # Office issue reporting
    m = re.match(r"Report office issue (\d+) for the (.+) department\.", q)
    if m:
        result = {
            "name": "report_office_issue",
            "arguments": json.dumps({
                "issue_code": int(m.group(1)),
                "department": m.group(2)
            })
        }

    # Return exact JSON string to prevent double-encoding
    return Response(content=json.dumps(result), media_type="application/json")
