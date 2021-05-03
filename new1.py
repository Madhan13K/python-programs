class kettle(object):
    power_source="madhan"
    def __init__(self,make,price):
        self.make=make
        self.price=price
        self.on=False

    def switch_on(self):
        self.on=True
kenwood=kettle("kenwood",99)
print(kenwood.make)
print(kenwood.price)
hamilton=kettle("hamilton",67)
print("models are {} and {}".format(hamilton.make,hamilton.price))
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

kettle.switch_on(hamilton)
print(kenwood.on)
kenwood.switch_on()
print("*"*80)
kenwood.power=1.7
print(kenwood.power)
kettle.power_source="atom"
print(kettle.power_source)
print(kenwood.power_source)
kenwood.power_source='mad'
print(kenwood.power_source)
print(hamilton.power_source)
hamilton.power_source="atm"
print(hamilton.power_source)
print(kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
