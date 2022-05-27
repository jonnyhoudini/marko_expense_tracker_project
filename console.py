import pdb
from models.payee import *
from models.category import *
from models.transaction import Transaction

import repositories.payee_repository as payee_repository
import repositories.category_repository as category_repository
import repositories.transaction_repository as transaction_repository

# Deleting everything to reseed the database
payee_repository.delete_all()
category_repository.delete_all()

# Checking the create and read functions for payees
payee1 = Payee("La Vita")
payee_repository.save(payee1)

payee2 = Payee("Apex Hotel")
payee_repository.save(payee2)

payee3 = Payee("Esso")
payee_repository.save(payee3)

# Checking the update function for payees
payee3.name = "Esso Garage"
payee_repository.update(payee3)

payee_repository.delete(payee2.id)

all_payees = payee_repository.select_all()

find_payee1_by_select_id = payee_repository.select(payee1.id) 
if find_payee1_by_select_id.name == "La Vita":
    print("The select by id function for payees is working!")

for payee in all_payees:
    print(payee.__dict__)

# Checking the create and read functions for category

category1 = Category("Food")
category_repository.save(category1)

category2 = Category("Fuel")
category_repository.save(category2)

all_categories = category_repository.select_all()

for category in all_categories:
    print(category.__dict__)

find_category1_by_select_id = category_repository.select(category1.id)
if  find_category1_by_select_id.name == "Food":
    print("The select by id function for categories is working!")

# Checking the delete by id function for categories

# category_repository.delete(category1.id)

all_categories = category_repository.select_all()

for category in all_categories:
    print(category.__dict__)

# Checking the update function

category2.name = "Diesel"
category_repository.update(category2)
check = category_repository.select(category2.id)
print(check.name)

# Checking the transaction save and select all functions

transaction1 = Transaction("Lunch with client", 45, payee1, "27 May 2022",  category1)
transaction2 = Transaction("Fill up the car", 70, payee3, "20 May 2022", category2)

transaction_repository.save(transaction1)
transaction_repository.save(transaction2)

all_transactions = transaction_repository.select_all()

for transaction in all_transactions:
    print(transaction.__dict__)

pdb.set_trace()