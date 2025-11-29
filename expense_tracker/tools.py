from .models import Expense, RecurringExpense
from datetime import datetime, timedelta
from typing import Optional

# In-memory databases
expenses_db: list[Expense] = []
recurring_expenses_db: list[RecurringExpense] = []

def add_expense(amount: float, category: str, description: str) -> str:
    """
    Adds an expense to the tracker.

    Args:
        amount: The numerical amount of the expense.
        category: The category of the expense.
        description: A brief description of the expense.
    
    Returns:
        A confirmation message that the expense has been added.
    """
    expense = Expense(amount=amount, category=category, description=description)
    expenses_db.append(expense)
    print(f"Added expense to db: {expense}")
    return f"Successfully added expense: {description} ({amount}) in {category}"

def calculate_total_spending() -> str:
    """Calculates the sum of all expenses recorded."""
    total = sum(e.amount for e in expenses_db)
    return f"Your total spending is ${total:.2f}."

def get_spending_by_category(category: str) -> str:
    """
    Calculates the total spending for a specific category.

    Args:
        category: The category to filter expenses by.
    """
    total = sum(e.amount for e in expenses_db if e.category.lower() == category.lower())
    return f"Your total spending for '{category}' is ${total:.2f}."

def list_recent_expenses(count: int = 5) -> str:
    """
    Lists the most recent expenses, up to a specified count.

    Args:
        count: The number of recent expenses to list. Defaults to 5.
    """
    if not expenses_db:
        return "There are no expenses recorded yet."
    
    recent = expenses_db[-count:]
    formatted_expenses = [f"- {e.description} $({e.amount:.2f} in {e.category})" for e in recent]
    
    return "Here are your recent expenses:\n" + "\n".join(formatted_expenses)

def add_recurring_expense(amount: float, category: str, description: str, frequency: str, start_date: str) -> str:
    """
    Adds a recurring expense to the tracker.

    Args:
        amount: The numerical amount of the expense.
        category: The category of the expense.
        description: A brief description of the expense.
        frequency: Frequency of the expense (e.g., 'weekly', 'monthly', 'yearly').
        start_date: The start date of the recurring expense in YYYY-MM-DD format.
    
    Returns:
        A confirmation message that the recurring expense has been added.
    """
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    next_due_date = start_date_obj
    if frequency == 'weekly':
        next_due_date += timedelta(weeks=1)
    elif frequency == 'monthly':
        next_due_date += timedelta(days=30)
    elif frequency == 'yearly':
        next_due_date += timedelta(days=365)
    
    recurring_expense = RecurringExpense(
        amount=amount,
        category=category,
        description=description,
        frequency=frequency,
        start_date=start_date_obj,
        next_due_date=next_due_date
    )
    recurring_expenses_db.append(recurring_expense)
    return f"Successfully added recurring expense: {description} ({amount}) in {category}, starting on {start_date}."

def list_recurring_expenses(category: Optional[str] = None) -> str:
    """
    Lists all recurring expenses, with an option to filter by category.

    Args:
        category: The category to filter expenses by.
    
    Returns:
        A formatted string of recurring expenses.
    """
    if not recurring_expenses_db:
        return "There are no recurring expenses recorded yet."
    
    filtered_expenses = recurring_expenses_db
    if category:
        filtered_expenses = [e for e in recurring_expenses_db if e.category.lower() == category.lower()]
    
    if not filtered_expenses:
        return f"No recurring expenses found for category '{category}'."
    
    formatted_expenses = [
        f"- {e.description} (${e.amount:.2f} every {e.frequency}, next due on {e.next_due_date.strftime('%Y-%m-%d')})"
        for e in filtered_expenses
    ]
    
    return "Here are your recurring expenses:\n" + "\n".join(formatted_expenses)

def project_spending(months: int = 3) -> str:
    """
    Calculates projected spending for a given number of future months based on recurring expenses.

    Args:
        months: The number of months to project spending for.
    
    Returns:
        A formatted string of the projected spending.
    """
    projected_total = 0
    for expense in recurring_expenses_db:
        if expense.frequency == 'monthly':
            projected_total += expense.amount * months
        elif expense.frequency == 'weekly':
            projected_total += expense.amount * 4 * months
        elif expense.frequency == 'yearly':
            projected_total += expense.amount * (months / 12)
            
    return f"Your projected spending for the next {months} months is ${projected_total:.2f}."
