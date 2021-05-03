import datetime
import pytz


class accounts:
    """ simple account class with balance """
    @staticmethod
    def _current_time():
        utc_now=datetime.datetime.utcnow()
        return pytz.utc.localize(utc_now)
    def __init__(self,name,balance):
        self.name=name

        self.balance=balance
        self.transaction=[((accounts._current_time(),balance))]
        print("account created by {}".format(self.name))

    def deposits(self,amount):
        if amount>  0:
            self.balance+=amount
            # self.show_balance()
            self.transaction.append((accounts._current_time(),amount))

    def withdraw(self,amount):
        if 0<amount<self.balance:
            self.balance -= amount
        else:
            print("not allowed")

    def show_balance(self):
        print("balance is {}".format(self.balance))

    def show_transactions(self):
        for date,amount in self.transaction:
            if amount>0:
                trans_type="deposited"
            else:
                trans_type="withdrawn"
                amount+=-1
            print("{:6} {} on {} (local time is {})".format(amount,trans_type,date,date.astimezone()))
if __name__=="__main__" :
    tim=accounts("tim",0)
    tim.show_balance()
    tim.deposits(10000)
    tim.show_balance()
    tim.withdraw(50000)
    tim.show_balance()
    tim.show_transactions()
    steph=accounts("steph",199)