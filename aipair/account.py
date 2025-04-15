class Account:
    def __init__(self, acno, customer_name, balance=0.0):
        """
        Initialize the account with account number, customer name, and balance.
        """
        self.acno = acno
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        Raises ValueError if the amount is not positive.
        """
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient balance exists.
        Raises ValueError if the amount is invalid or insufficient balance.
        """
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        else:
            self.balance -= amount

    def get_balance(self):
        """
        Return the current balance of the account.
        """
        return self.balance

    def display(self):
        """
        Display the account details.
        """
        print(self)

    def __str__(self):
        """
        Return a string representation of the account details.
        """
        return (f"Account Number: {self.acno}\n"
                f"Customer Name: {self.customer_name}\n"
                f"Balance: {self.balance}")

# Example usage
if __name__ == "__main__":
    try:
        account = Account(101, "John Doe", 500.0)
        account.display()
        account.deposit(200)
        print(f"Balance after deposit: {account.get_balance()}")
        account.withdraw(100)
        print(f"Balance after withdrawal: {account.get_balance()}")
        account.withdraw(700)  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")