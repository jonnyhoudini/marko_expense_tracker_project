class Category():
    def __init__(self, name, id = None):
        self.name = name
        self.id = id
        self.number_of_transactions = 0
        self.amount_of_transactions = 0

    
    # Define function that takes in an array of transactions and calculates the total amount of spending in a given category
    def get_total_amount_of_transactions(self, transactions):
        # Create a total variable and assign it as 0
        total_amount = 0
        # Loop through the transactios
        for transaction in transactions:
            # IF the given category is the same as the transaction's category
            if self.id == transaction.category.id:
                # THEN add the amount of that transaction to the total variable
                total_amount += transaction.amount
        # Return the total outside the for loop
        return total_amount

    def get_total_number_of_transactions(self, transactions):
        total_number = 0
        for transaction in transactions:
            if self.id == transaction.category.id:
                total_number += 1
        return total_number
        