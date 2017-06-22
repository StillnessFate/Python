class BankAccount :
	__no_of_accounts = 0

	def __init__(self, name, balance = 0) :
		"""
		initializes object
		<arguments>
			name : owner name
			balance : account balance. 0 or more
		"""
		self.__name = name
		if balance < 0 :
			balance = 0
		self.__balance = balance

		BankAccount.__no_of_accounts += 1

		print("A bank account for " + self.__name + " is open.")
		print("Your currect balance is " + str(self.__balance) + " won.")

	def __str__(self) :
		"""
		string representation
		\"<name>'s BankAccount object\"
		"""
		return self.__name + "'s BankAccount object"

	def show_balance(self) :
		"""
		show account balance
		\"<name>'s balance is <balance> won.\"
		"""
		print(self.__name + "'s balance is " + str(self.__balance) + " won.")

	def deposit(self, amount) :
		"""
		deposit to account
		<arguments>
			amount : amount to deposit
		\"<balance> won has been successfully deposited.\"
		"""
		if 0 <= amount :
			self.__balance += amount
			print(str(self.__balance) + " won has been successfully deposited.")
		else :
			print("Deposit failed.")
		self.show_balance()

	def withdraw(self, amount) :
		"""
		withdraw to account
		<arguments>
			amount : amount to withdraw
		\"<balance> won has been successfully withdrawn.\"
		"""
		if (0 <= amount) and (amount <= self.__balance) :
			self.__balance -= amount
			print(str(self.__balance) + " won has been successfully withdrawn.")
		else :
			print("Withdraw failed.")
		self.show_balance()

	@staticmethod
	def count_accounts() :
		"""
		total number of accounts
		"""
		return BankAccount.__no_of_accounts