class Transaction():
    def __init__(self, description, amount, payee, date, category, id = None, submitted = False):
        self.description = description
        self.amount = amount
        self.payee = payee
        self.date = date
        self.category = category
        self.id = id
        self.submitted = submitted

    def mark_submitted(self):
        self.submitted = True