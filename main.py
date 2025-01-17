class expenseTracker:
    def __init__(self, name, age, occupation, income, expense=0):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.income = income
        self.expense = expense

    def changeIncome(self, newIncome):
        self.income = newIncome

    def addExpense(self, newExpense):
        self.expense = self.expense + newExpense

    def resetExpense(self):
        self.expense = 0

    def viewSavings(self):
        print(f"Your Savings are ₹{self.income-self.expense}")
    def viewTotalExpenses(self):
        print(f"Your total expenses are ₹{self.expense}")
    def viewCurrentIncome(self):
        print(f"Your current income is ₹{self.income}")
    