from enum import Enum
"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class CommissionTypes(Enum):
    BONUS = 0,
    PER_CONTRACT = 1,
    NONE = 2

class ContractTypes(Enum):
    SALARY = 0,
    HOURLEY = 1


class Commission:
    def __init__(self, commissionType: CommissionTypes, value: float = 0, numberOfContracts: int = 0):
        self.type = commissionType
        self.rate = value
        self.numberOfContracts = numberOfContracts

    def getValue(self):
        if self.type == CommissionTypes.BONUS:
            return self.rate
        else:
            return self.rate * self.numberOfContracts

    def __str__(self):
        if self.type == CommissionTypes.PER_CONTRACT:
            return f' and receives a commission for {self.numberOfContracts} contract(s) at {self.rate}/contract'
        elif self.type == CommissionTypes.BONUS:
            return f' and receives a bonus commission of {self.rate}'
        return ''

class Contract:
    def __init__(self, contractType: ContractTypes, value: float = 0, contractMultiplier: int = 1):
        self.type = contractType
        self.rate = value
        self.contractMultiplier = contractMultiplier

    def getValue(self):
        return self.contractMultiplier * self.rate

    def __str__(self):
        return f'works on a monthly salary of {self.getValue()}' if self.type == ContractTypes.SALARY else f'works on a contract of {self.contractMultiplier} hours at {self.rate}/hour'

class Employee:
    def __init__(self, name: str, commission: Commission, contract: Contract):
        self.name = name
        self.commission = commission
        self.contract = contract

    def get_pay(self):
        return self.contract.getValue() + self.commission.getValue()

    def __str__(self):
        return f'{self.name} {self.contract}{self.commission}.  Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Commission(CommissionTypes.NONE), Contract(ContractTypes.SALARY, 4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Commission(CommissionTypes.NONE), Contract(ContractTypes.HOURLEY, 25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Commission(CommissionTypes.PER_CONTRACT, 200, 4), Contract(ContractTypes.SALARY, 3000))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Commission(CommissionTypes.PER_CONTRACT, 220, 3), Contract(ContractTypes.HOURLEY, 25, 150))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Commission(CommissionTypes.BONUS, 1500), Contract(ContractTypes.SALARY, 2000))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Commission(CommissionTypes.BONUS, 600), Contract(ContractTypes.HOURLEY, 30, 120))
