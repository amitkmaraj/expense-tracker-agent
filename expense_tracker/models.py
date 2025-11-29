from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
import uuid

class Expense(BaseModel):
    """Data model for a single expense."""
    amount: float = Field(description="The numerical amount of the expense.")
    category: str = Field(description="The category of the expense (e.g., Food, Transport, Bills).")
    description: str = Field(description="A brief description of the expense.")

class RecurringExpense(BaseModel):
    """Data model for a recurring expense."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier for the recurring expense.")
    amount: float = Field(description="The numerical amount of the expense.")
    category: str = Field(description="The category of the expense.")
    description: str = Field(description="A brief description of the expense.")
    frequency: str = Field(description="Frequency of the expense (e.g., 'weekly', 'monthly', 'yearly').")
    start_date: datetime = Field(description="The start date of the recurring expense.")
    end_date: Optional[datetime] = Field(default=None, description="The end date of the recurring expense.")
    next_due_date: datetime = Field(description="The next due date of the recurring expense.")
