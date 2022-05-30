class Category():
    def __init__(self, name, id = None):
        self.name = name
        self.id = id
        self.number_of_transactions = 0
        self.amount_of_transactions = 0

    
    def get_total_amount_of_transactions(self, transactions):
        total_amount = 0
        for transaction in transactions:
            if self.id == transaction.category.id:
                total_amount += transaction.amount
        return total_amount

    def get_total_number_of_transactions(self, transactions):
        total_number = 0
        for transaction in transactions:
            if self.id == transaction.category.id:
                total_number += 1
        return total_number
        