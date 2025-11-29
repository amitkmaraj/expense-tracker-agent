# PRD: Recurring Expense Tracking

## Problem Statement
Users need to track recurring monthly expenses (rent, subscriptions, insurance) without manually entering them each month.

## Goals
1. Allow users to mark expenses as recurring
2. Automatically project future spending based on recurring expenses
3. Alert users about upcoming recurring expenses
4. Generate monthly budget forecasts

## Requirements

### Functional Requirements
1. Add recurring expense with frequency (weekly/monthly/yearly)
2. List all recurring expenses
3. Calculate projected spending for next N months
4. Optional: Set reminders for recurring payments

### Data Model
```python
@dataclass
class RecurringExpense:
    id: str
    amount: float
    category: str
    description: str
    frequency: str  # 'weekly', 'monthly', 'yearly'
    start_date: datetime
    end_date: Optional[datetime]  # None = ongoing
    next_due: datetime
```

### Agent Tools to Add

1. `add_recurring_expense(amount, category, description, frequency, start_date)`  
2. `list_recurring_expenses(category=None)`  
3. `project_spending(months=3)`  
4. `mark_recurring_paid(expense_id, date)`

## Implementation Notes

- Store in separate table `recurring_expenses`  
- Use datetime calculations for projections  
- Update `next_due` when marked as paid  
- Follow existing tool patterns from expense\_agent.py
- Try to follow DRY principles as much as possible. Keep all code in files they should live in. For example, dataclasses and tools should live in separate files.

## Success Metrics

- Users can add recurring expenses in one command  
- Projection accuracy within 5% of actual spending  
- Zero duplicate entries for recurring expenses

## Out of Scope (V2)

- Calendar integration  
- Email reminders  
- Multi-currency support
