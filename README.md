# MARKO Expense Tracker

![alt text](https://images2.imgbox.com/72/a8/epymwR98_o.png)

MARKO tracks your business-related expenditure to make it easier when you need to submit an expenses claim to your employer.

## Brief

The app was created as a solo project during week 5 of the CodeClan Professional Software Development course. It meets all of the minimum requirements outined in the brief:

1. The app should allow the user to create and edit payees, e.g. Tesco, Amazon, ScotRail

2. The app should allow the user to create and edit categories for their spending, e.g. groceries, entertainment, transport

3. The user should be able to assign categories and payees to a transaction, as well as an amount spent on each transaction.

4. The app should display all the transactions a user has made in a single view, with each transaction's amount, payee and category, and a total for all transactions.

I have also added the following extensions:

1. The user should be able to supply a budget, and the app should alert the user somehow when when they are nearing this budget or have gone over it.

2. The user should be able to filter their view of transactions, for example, to view all transactions with a given payee or category.

https://user-images.githubusercontent.com/72469020/171380895-b079f405-f9ed-4ab3-9306-c9b9fa4d0759.mp4

## Technology

This is the first full-stack app I have made, using the technologies and concepts learned during the first four weeks of CodeClan:

- Object oriented programming with Python
- Test Driven Development
- Web Programming (REST, MVC)
- Interacting with a SQLite database (CRUD)

## Usage

After cloning the repo you need to set up the database in SQLite3, run the console to seed the database and run Flask.

```bash
sqlite3 db/expenses_tracker.db < db/expenses_tracker.sql
```
```bash
python3 console.py
```
```bash
flask run
```
   
