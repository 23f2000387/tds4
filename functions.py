# functions.py

def get_ticket_status(ticket_id: int):
    return f"Ticket {ticket_id} status: Open"

def schedule_meeting(date: str, time: str, meeting_room: str):
    return f"Meeting scheduled on {date} at {time} in {meeting_room}"

def get_expense_balance(employee_id: int):
    return f"Employee {employee_id} expense balance: $500"

def calculate_performance_bonus(employee_id: int, current_year: int):
    return f"Employee {employee_id} performance bonus for {current_year}: $2000"

def report_office_issue(issue_code: int, department: str):
    return f"Issue {issue_code} reported for {department} department"
