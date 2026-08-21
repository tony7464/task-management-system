from datetime import datetime

def validate_task_title(title):
    if title is None or len(title) == 0:
        raise ValueError("Title cannot be empty.")

def validate_task_description(description):
    if description is None or len(description) == 0:
        raise ValueError("Description cannot be empty.")

def validate_due_date(due_date):
    if due_date is None or len(due_date) == 0:
        raise ValueError("Due date cannot be empty.")
    datetime.strptime(due_date, "%Y-%m-%d")
