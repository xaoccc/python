class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if self.amount + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self.amount += transaction_amount
        self._transactions.append(transaction_amount)
        return f"New balance: {self.amount}"
        
    def add_transaction(self, amount):
        if type(amount) != int:
            raise ValueError("please use int for amount")
        return self.handle_transaction(amount)
    
    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"
        
    @property
    def balance(self):
        return self.amount
        
    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"
        
    def __len__(self):
        return len(self._transactions)
        
    def __getitem__(self, i):
        return self._transactions[i]
        
    def __reversed__(self):
        return reversed(self._transactions)
        
    def __lt__(self, other):
        return self.amount < other.amount
        
    def __le__(self, other):
        return self.amount <= other.amount 
        
    def __eq__(self, other):
        return self.amount == other.amount

    def __add__(self, other):
        combined_transactions = self._transactions + other._transactions
        new_acc = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new_acc._transactions = combined_transactions
        return new_acc
