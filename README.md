# Expense-tracker
An Expense Tracker project is a software application designed to help users record, monitor, and manage their daily income and spending.
# Expense Tracker

## Student Details

**Name:** N. Swathi

**Registration Number:** 24BEC10110

**Course:** Programming in Java - Evaluated Project

**Slot:** B22 + B24

**Date of Submission:** [DD/MM/YYYY]

---

## Project Overview

This project is a simple command-line based **Expense Tracker** designed to help users record and manage their daily expenses.

The system allows users to add, view, update, and delete expense records. It also calculates total expenses and provides category-wise expense information.

The project demonstrates basic programming concepts such as file handling, functions, conditional statements, loops, data validation, and command-line interaction.

---

## Main Features

* Add new expenses
* View all expenses
* Update expense details
* Delete expenses
* Calculate total expenses
* View expenses by category
* Store expense records permanently
* Simple command-line interface

---

## Software and Tools

* Python 3
* CSV
* Git
* GitHub

---

## How the System Works

The user interacts with the Expense Tracker through the command line. The system accepts expense details and stores them in a CSV file.

Users can view, update, or delete their expense records. The system can also calculate the total amount spent and display expenses based on categories.

```text
        User
          |
          v
   Expense Tracker
          |
    +-----+-----+---------+---------+
    |           |         |         |
    v           v         v         v
   Add         View     Update    Delete
 Expense      Expenses  Expense   Expense
    |           |         |         |
    +-----------+---------+---------+
                |
                v
           expenses.csv
```

---

## Project Structure

```text
Expense-Tracker/
│
├── README.md
├── statement.md
├── requirements.txt
├── expense_tracker.py
└── expenses.csv
```

---

## How to Run

### Step 1: Install Python

Install **Python 3.x** on your system.

### Step 2: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### Step 3: Open the Project Folder

```bash
cd Expense-Tracker
```

### Step 4: Run the Program

```bash
python expense_tracker.py
```

The Expense Tracker menu will be displayed in the terminal.

---

## Usage

After running the program, the following menu is displayed:

```text
===== EXPENSE TRACKER =====

1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. View Total Expenses
6. View Expenses by Category
7. Exit

Enter your choice:
```

Enter the corresponding number to perform an operation.

---

## Expense Details

Each expense record contains:

* Expense ID
* Date
* Category
* Description
* Amount

Example:

```text
ID: 1
Date: 15-09-2026
Category: Food
Description: Lunch
Amount: ₹150
```

---

## Data Storage

Expense records are stored permanently in the `expenses.csv` file.

Example:

```text
ID,Date,Category,Description,Amount
1,15-09-2026,Food,Lunch,150
2,15-09-2026,Transport,Bus,40
3,14-09-2026,Education,Notebook,80
```

The stored data can be accessed again when the program is run.

---

## Expected Output

### Adding an Expense

```text
Enter your choice: 1

Enter category: Food
Enter description: Lunch
Enter amount: 150

Expense added successfully!
```

### Viewing Total Expenses

```text
Enter your choice: 5

Total Expenses: ₹270
```

### Viewing Expenses

```text
Enter your choice: 2

ID    Date          Category     Description     Amount
1     15-09-2026    Food         Lunch           ₹150
2     15-09-2026    Transport    Bus             ₹40
3     14-09-2026    Education    Notebook        ₹80
```

---

## Testing

The system is tested for:

* Adding a new expense
* Displaying all expenses
* Updating an expense
* Deleting an expense
* Calculating total expenses
* Viewing expenses by category
* Handling invalid input
* Saving and retrieving expense data

---

## Limitations

* The application is command-line based.
* Expense data is stored locally in a CSV file.
* No graphical user interface is provided.
* No user authentication is implemented.
* The project is developed for educational purposes.

---

## Future Enhancements

* Monthly and yearly expense reports
* Budget management
* Graphical user interface
* Expense charts and visualization
* Export data to Excel
* Search and filter functionality
* Database integration
* User authentication

---

## Documentation

The `statement.md` file contains the project statement and basic project information.

---

## Acknowledgment

This project was developed as part of the **Programming in Java - Evaluated Project**. It provides practical experience in programming, file handling, data management, and command-line application development.
