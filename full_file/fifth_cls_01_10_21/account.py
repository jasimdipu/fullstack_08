from full_file.fifth_cls_01_10_21.student_impl import StudentImpl


class Account(StudentImpl):

    def __init__(self, name, dept, credit, amount, waver=0):
        super(Account, self).__init__(name=name, dept=dept)
        self.credit = credit
        self.amount = amount
        self.waver = waver
        self.payment = 0.0

    def get_total_sem_fees(self):
        return self.credit * self.amount

    def get_payment_amount_without_waver(self):
        if self.waver == 0:
            self.payment = self.credit * self.amount
            return "You have no waver" + self.payment
        else:
            self.payment = (self.credit * self.amount) - self.waver
            return self.payment

    def make_payment(self, amount):
        self.payment = self.payment - amount
        return self.payment


account = Account("Nasim Haidar", "CSE", 20, 5000, 25000)

print(account.getName(), account.getDept())
print(account.get_total_sem_fees())
print(account.get_payment_amount_without_waver())
account.make_payment(25000)
print(account.make_payment(25000))
