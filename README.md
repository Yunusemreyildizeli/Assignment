Smart Budget Tracker (for Personal and Business Use)
====================================================

GitHub Repository:
------------------
The source code for this project is available on GitHub:  
https://github.com/Yunusemreyildizeli/Assignment

Identification:
---------------
Course Code: IY499 - Introduction to Programming

Declaration of Own Work:
-------------------------
I confirm that this assignment is my own work.  
Where I have referred to academic sources, I have provided in-text citations and included the sources in the final reference list.  
Where I have referred to code examples online, I have included comments and links to the original source.

Program Description:
---------------------
Smart Budget Tracker is a financial tracking application built using Python, designed to help individuals and small businesses monitor their income, expenses, and savings. It enables users to categorize transactions, set budget limits, and visualize financial data through interactive charts.

The program provides a graphical interface built using Tkinter where users can input income and expense data. Each transaction includes an amount, category, description, and type (income or expense). All data is stored in CSV files for long-term tracking. Budget limits can be set and loaded for each category to alert the user when they exceed their defined thresholds.

Once transactions are added, users can generate multiple financial charts including:
- A pie chart showing expense distribution by category
- A bar chart comparing income and expenses across categories
- A line chart showing daily expense trends
- A bar chart comparing total income and remaining balance (leftover)

The application uses object-oriented principles, modular structure, exception handling, and follows best software development practices. Data visualization is achieved using matplotlib, and all file operations are handled through CSV files.

Installation Instructions:
---------------------------
Ensure Python 3.x is installed on your computer. Then install the required packages using the following commands in your terminal or command prompt:

1. Install matplotlib:
   pip install matplotlib

2. tkinter is included by default with standard Python installations. No separate installation is required for tkinter on Windows or macOS. If using Linux, it may need to be installed using:
   sudo apt-get install python3-tk

Running the Program:
---------------------
This program was developed using PyCharm. To run it:

1. Open the project folder in PyCharm.
2. Ensure the required libraries are installed as mentioned above.
3. Locate and open the file named 'main.py'.
4. Run the program.

Once executed, a GUI window will appear. The steps to use the application are:

1. Enter the amount in the 'Amount' field.
2. Enter the category of the transaction (e.g., Salaries, Bills, Revenue).
3. Enter a description for the transaction (e.g., March electricity bill, Client payment).
4. Select whether the transaction is an income or an expense using the radio buttons.
5. Click the 'Add Transaction' button to store the transaction in memory.
6. If a budget limit is set for that category and the expense exceeds the limit, a warning message will be shown.
7. To visualize the data, click on the 'Show Chart' button. This will open four separate chart windows:
   - Pie Chart: Expense distribution by category
   - Bar Chart: Income vs Expense comparison
   - Line Chart: Daily expense trends
   - Bar Chart: Total income vs leftover balance
8. To save all transactions to file, click the 'Save Transactions' button. This writes the data to 'transactions.csv' located in the 'data' folder.

Project Structure:
-------------------
SmartBudgetTracker/
├── main.py
├── core/
│   ├── tracker.py
│   ├── transaction.py
│   ├── settings.py
│   ├── exceptions.py
│   └── logger.py
├── utils/
│   ├── visualizer.py
│   ├── file_handler.py
│   └── sort_strategy.py
├── data/
│   ├── transactions.csv
│   └── app.log
├── requirements.txt
└── README.txt

Libraries Used:
----------------
- matplotlib: for generating all data visualizations
- tkinter: for building the graphical user interface
- csv, os, datetime, collections: Python standard libraries used for data handling and processing
