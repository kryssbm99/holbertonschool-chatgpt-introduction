class Checkbook:
	"""
	A simple checkbook class that allows depositing, withdrawing, and checking balance.

	Attributes:
		balance (float): The current balance in the checkbook.

	Methods:
		deposit(amount): Deposit funds into the checkbook.
		withdraw(amount): Withdraw funds from the checkbook if sufficient balance is available.
		get_balance(): Get the current balance of the checkbook.
	"""

	def __init__(self):
		"""
		Initialize a Checkbook object with a balance of 0.0.
		"""
		self.balance = 0.0

	def deposit(self, amount):
		"""
		Deposit funds into the checkbook.

		Args:
			amount (str or float): The amount to deposit (can be entered as a string or float).

		Raises:
			ValueError: If the input cannot be converted to a valid float.
		"""
		try:
			amount = float(amount)
			if amount > 0:
				self.balance += amount
				print("Deposited ${:.2f}".format(amount))
				print("Current Balance: ${:.2f}".format(self.balance))
			else:
				print("Invalid deposit amount. Please enter a positive number.")
		except ValueError:
			print("Invalid input. Please enter a valid amount.")

	def withdraw(self, amount):
		"""
		Withdraw funds from the checkbook.

		Args:
			amount (str or float): The amount to withdraw (can be entered as a string or float).

		Raises:
			ValueError: If the input cannot be converted to a valid float.
		"""
		try:
			amount = float(amount)
			if amount > 0:
				if amount > self.balance:
					print("Insufficient funds to complete the withdrawal.")
				else:
					self.balance -= amount
					print("Withdrew ${:.2f}".format(amount))
					print("Current Balance: ${:.2f}".format(self.balance))
			else:
				print("Invalid withdrawal amount. Please enter a positive number.")
		except ValueError:
			print("Invalid input. Please enter a valid amount.")

	def get_balance(self):
		"""
		Print the current balance of the checkbook.
		"""
		print("Current Balance: ${:.2f}".format(self.balance))


def main():
	"""
	Main function to interact with the Checkbook class via command-line interface.
	"""
	cb = Checkbook()
	while True:
		action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
		if action.lower() == 'exit':
			print("Exiting the checkbook program. Goodbye!")
			break
		elif action.lower() == 'deposit':
			amount = input("Enter the amount to deposit: $")
			cb.deposit(amount)
		elif action.lower() == 'withdraw':
			amount = input("Enter the amount to withdraw: $")
			cb.withdraw(amount)
		elif action.lower() == 'balance':
			cb.get_balance()
		else:
			print("Invalid command. Please try again.")


if __name__ == "__main__":
	main()
