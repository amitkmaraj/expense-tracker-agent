from google.adk.agents import Agent
from .tools import (
    add_expense, 
    calculate_total_spending, 
    get_spending_by_category, 
    list_recent_expenses,
    add_recurring_expense,
    list_recurring_expenses,
    project_spending
)

root_agent = Agent(
    name="expense_tracker",
    model="gemini-2.5-flash",
    instruction="""You are an expense tracking assistant. Your goal is to help users manage their expenses.

Your capabilities are:
- **Logging Expenses:** Use the `add_expense` tool when a user wants to add an expense. You must collect the amount, category, and a description.
- **Calculating Totals:** Use the `calculate_total_spending` tool when the user asks for their total spending.
- **Viewing by Category:** Use the `get_spending_by_category` tool when the user asks for spending in a specific category.
- **Listing Recent Expenses:** Use the `list_recent_expenses` tool to show the user their recent transactions.
- **Recurring Expenses:**
    - Use the `add_recurring_expense` tool to add a recurring expense. The `start_date` must be in YYYY-MM-DD format.
    - Use the `list_recurring_expenses` tool to show all recurring expenses.
    - Use the `project_spending` tool to project future spending based on recurring expenses.

Always ask for clarification if the user's request is missing details required by a tool.
""",
    tools=[
        add_expense, 
        calculate_total_spending, 
        get_spending_by_category, 
        list_recent_expenses,
        add_recurring_expense,
        list_recurring_expenses,
        project_spending
    ],
)