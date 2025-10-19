import re
import json

def parse_query(q: str) -> dict:
    q_clean = q.lower().strip()

    # Ticket Status
    ticket_match = re.search(r"ticket (\d+)", q_clean)
    if "status of ticket" in q_clean and ticket_match:
        return {"name": "get_ticket_status", "arguments": json.dumps({"ticket_id": int(ticket_match.group(1))})}

    # Meeting Scheduling
    meeting_match = re.search(r"on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)", q_clean)
    if "schedule a meeting" in q_clean and meeting_match:
        date, time, room = meeting_match.groups()
        return {"name": "schedule_meeting", "arguments": json.dumps({"date": date, "time": time, "meeting_room": room.strip()})}

    # Expense Balance
    expense_match = re.search(r"employee (\d+)", q_clean)
    if "expense balance" in q_clean and expense_match:
        return {"name": "get_expense_balance", "arguments": json.dumps({"employee_id": int(expense_match.group(1))})}

    # Performance Bonus
    bonus_match = re.search(r"employee (\d+) for (\d{4})", q_clean)
    if "performance bonus" in q_clean and bonus_match:
        emp_id, year = bonus_match.groups()
        return {"name": "calculate_performance_bonus", "arguments": json.dumps({"employee_id": int(emp_id), "current_year": int(year)})}

    # Office Issue
    issue_match = re.search(r"issue (\d+) for the (.+) department", q_clean)
    if "report office issue" in q_clean and issue_match:
        code, dept = issue_match.groups()
        return {"name": "report_office_issue", "arguments": json.dumps({"issue_code": int(code), "department": dept.strip()})}

    # If no match
    return {"name": "unknown", "arguments": "{}"}
