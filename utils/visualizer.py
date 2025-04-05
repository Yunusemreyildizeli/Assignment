# visualizer.py

import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime


def show_expense_chart(transactions):
    """
    Displays multiple financial charts based on transaction data.

    Charts generated:
        1. Pie chart of expense distribution by category
        2. Bar chart comparing income and expense by category
        3. Line chart of daily expenses
        4. Bar chart comparing total income vs leftover balance (savings)

    Args:
        transactions (list[dict]): List of transaction records containing
                                   type, amount, category, description, and date.
    """

    # Aggregate totals by category and date
    expense_totals = defaultdict(float)
    income_totals = defaultdict(float)
    daily_expense = defaultdict(float)

    total_income = 0
    total_expense = 0

    # Categorize each transaction by type
    for t in transactions:
        date_str = t['date'].split()[0]  # Extract date (exclude time)
        if t['type']=='expense':
            expense_totals[t['category']] += t['amount']
            daily_expense[date_str] += t['amount']
            total_expense += t['amount']
        elif t['type']=='income':
            income_totals[t['category']] += t['amount']
            total_income += t['amount']

    if not expense_totals and not income_totals:
        print("No data to display.")
        return

    # Prepare category-wise bar chart data
    categories = sorted(set(expense_totals.keys()) | set(income_totals.keys()))
    income_values = [income_totals.get(cat, 0) for cat in categories]
    expense_values = [expense_totals.get(cat, 0) for cat in categories]
    x = range(len(categories))
    bar_width = 0.35

    # Prepare date-wise line chart data
    sorted_dates = sorted(daily_expense.keys(), key=lambda d: datetime.strptime(d, "%Y-%m-%d"))
    expense_by_date = [daily_expense[date] for date in sorted_dates]
    leftover = total_income - total_expense
