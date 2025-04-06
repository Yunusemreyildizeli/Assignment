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

    # ---------------------- Chart 1: Pie Chart (Expenses) ----------------------
    fig1 = plt.figure("1: Expense Pie Chart", figsize=(7, 5))
    plt.pie(
        list(expense_totals.values()),
        labels=list(expense_totals.keys()),
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 10}
    )
    plt.title("Expense Distribution by Category", fontsize=13)
    plt.axis("equal")  # Ensures the pie chart is circular

    # ---------------------- Chart 2: Income vs Expense Bar Chart ----------------------
    fig2 = plt.figure("2: Income vs Expense", figsize=(10, 6))
    bars1 = plt.bar(x, income_values, width=bar_width, label='Income', color='green')
    bars2 = plt.bar([i + bar_width for i in x], expense_values, width=bar_width, label='Expense', color='red')

    # Add value labels to each bar
    for bar in bars1 + bars2:
        height = bar.get_height()
        if height > 0:
            plt.text(bar.get_x() + bar.get_width() / 2, height + 10000, f'{height:,.0f}', ha='center', fontsize=8)

    plt.title("Income vs Expense by Category")
    plt.xticks([i + bar_width / 2 for i in x], categories, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()

    # ---------------------- Chart 3: Daily Expense Trend (Line Chart) ----------------------
    fig3 = plt.figure("3: Daily Expense Trend", figsize=(10, 5))
    plt.plot(sorted_dates, expense_by_date, marker='o', color='orange')
    plt.title("Daily Expense Trend")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # ---------------------- Chart 4: Income vs Leftover ----------------------
    fig4 = plt.figure("4: Total Income vs Leftover", figsize=(6, 5))
    bars = plt.bar(["Total Income", "Leftover"], [total_income, leftover], color=["blue", "purple"])

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 10000, f'{height:,.0f}', ha='center', fontsize=10)

    plt.title("Total Income vs Leftover (Savings)")
    plt.ylabel("Amount")
    plt.tight_layout()

    # Display all chart windows
    plt.show()
