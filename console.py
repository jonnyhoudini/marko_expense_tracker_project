import pdb
from models.payee import Payee

import repositories.payee_repository as payee_repository

payee1 = Payee("La Vita")
print(payee1.__dict__)
payee_repository.save(payee1)
print(payee1.__dict__)

pdb.set_trace()