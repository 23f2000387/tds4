# main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
import json
import re
from functions import get_ticket_status, schedule_meeting, get_expense_balance, calculate_performance_bonus, report_office_issue

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Function to parse the query and extract parameters
def parse_query(q: str) -> Dict:
    # Ticket Status
    ticket_match = re.search(r"ticket (\d+)", q)
    if "status of ticket" in q.lower() and ticket_match:
        return {"name": "get_ticket_status", "arguments": json.dumps({"ticket_id": int(ticket_match.group(1))})}

    # Meeting Scheduling
    meeting_match = re.search(r"on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)", q)
    if "schedule a meeting" in q.lower() and meeting_match:
        date, time, room = meeting_match.groups()
        return {"name": "schedule_meeting", "arguments": json.dumps({"date": date, "time": time, "meeting_room": room})}

    # Expense Balance
    expense_match = re.search(r"employee (\d+)", q)
    if "expense balance" in q.lower() and expense_match:
        return {"name": "get_expense_balance", "arguments": json.dumps({"employee_id": int(expense_match.group(1))})}

    # Performance Bonus
    bonus_match = re.search(r"employee (\d+) for (\d{4})", q)
    if "performance bonus" in q.lower() and bonus_match:
        emp_id, year = bonus_match.groups()
        return {"name": "calculate_performance_bonus", "arguments": json.dumps({"employee_id": int(emp_id), "current_year": int(year)})}

    # Office Issue
    issue_match = re.search(r"issue (\d+) for the (.+) department", q)
    if "report office issue" in q.lower() and issue_match:
        code, dept = issue_match.groups()
        return {"name": "report_office_issue", "arguments": json.dumps({"issue_code": int(code), "department": dept})}

    return {"name": "unknown", "arguments": "{}"}

# GET endpoint
@app.get("/execute")
def execute(q: str = Query(..., description="The query to process")):
    result = parse_query(q)
    return result
