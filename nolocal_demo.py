
def make_withdraw(balance):

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "insufficient"
        else:
            balance = balance - amount
        return balance
    return withdraw

wd = make_withdraw(100)
print(wd(20))
