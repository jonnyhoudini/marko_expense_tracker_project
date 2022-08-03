import pdb
from models.payee import *
from models.category import *
from models.transaction import Transaction
from models.user import *

import repositories.payee_repository as payee_repository
import repositories.category_repository as category_repository
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository

# Deleting everything to reseed the database
transaction_repository.delete_all()
payee_repository.delete_all()
category_repository.delete_all()
user_repository.delete_all()


# Creating a user using the default limit
user = User("Theodore Templeton")
user_repository.save(user)

# Checking the create and read functions for payees
payee1 = Payee("La Vita")
payee_repository.save(payee1)

payee2 = Payee("Apex Hotel")
payee_repository.save(payee2)

payee3 = Payee("Esso")
payee_repository.save(payee3)

payee4 = Payee("Scotrail")
payee_repository.save(payee4)

category1 = Category("Food")
category_repository.save(category1)

category2 = Category("Fuel")
category_repository.save(category2)

category3 = Category("Accommodation")
category_repository.save(category3)

category4 = Category("Travel")
category_repository.save(category4)

transaction1 = Transaction("Lunch with client", 45, payee1, "27 May 2022",  category1)
transaction_repository.save(transaction1)

transaction2 = Transaction("Fill up the car", 70, payee3, "20 May 2022", category2)
transaction_repository.save(transaction2)

transaction3 = Transaction("Conference in London", 350, payee2, "16 May 2022", category3)
transaction_repository.save(transaction3)

transaction4 = Transaction("Train to London", 120, payee4, "16 May 2022", category4)
transaction_repository.save(transaction4)

transaction5 = Transaction("Coffee", 3, payee1, "15 May 2022", category1)
transaction_repository.save(transaction5)

# Fetching all my saved transactions from the database
results = transaction_repository.select_all()
# Finding the ID of the first result
id = results[0].id
# Using my select function to search my SQLite database for a particular transaction ID and returining only that transaction
search_by_id = transaction_repository.select(id)
# Printing out the transaction as a dictionary
print(f'The result of my search is: {search_by_id.__dict__}')

pdb.set_trace()