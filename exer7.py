class BankAccount:
    interest_rate = 0.3

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, number):
        self.balance += number
        print("deposited amount: ", number)
        print(f"Net balance: {self.balance}")
        return self.balance

    def withdraw(self, number):
        if number <= self.balance:
            self.balance -= number
            print("withdrawn amount = ", number)
            print(f"Net balance: {self.balance}")
        else:
            print(f"You tried to withdraw {number}, you only have {self.balance} in your account")
            print("Insufficient Funds")
        return self.balance

    def add_interest(self):
        compute_interest = self.balance * self.interest_rate
        self.balance = self.balance + compute_interest
        print(f"Interest at 30% = {compute_interest}")
        print(f"Net balance after interest: {self.balance}")


class StudentAccount(BankAccount):
    def withdraw(self, number):
        if number > 1000 or self.balance < number:
            print("You tried withdrawing more than 1000, Please try again")
            pass
        else:
            self.balance -= number
            print("withdrawn amount= ", number)
            print(f"Net balance: {self.balance}")


def main():
    inp_1 = input("Enter name: ")
    inp_2 = int(input("Enter balance: "))

    person = BankAccount(name=inp_1, balance=inp_2)

    deposit_amount = int(input("Enter amount to be deposited: "))
    person.deposit(deposit_amount)

    withdraw_amount= int(input("Enter amount to withdraw: "))
    person.withdraw(withdraw_amount)

    print("Adding interest")
    person.add_interest()

    # Student instance
    print("*\n" * 5)
    print("-" * 10)
    inp_1 = input("Enter student name: ")
    inp_2 = int(input("Enter balance: "))
    student_account = StudentAccount(name=inp_1, balance=inp_2)

    student_deposit_amount = int(input("Enter account deposit amount: "))
    student_account.deposit(number=student_deposit_amount)

    student_withdraw_amount = int(input("Enter account withdraw amount: "))
    student_account.withdraw(number=student_withdraw_amount)

    print("Adding interest")
    student_account.add_interest()


if __name__ == '__main__':
    main()
