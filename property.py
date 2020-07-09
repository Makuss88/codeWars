class Money:
    def __init__(self, dollars, cents):
        # self.dollars = dollars
        # self.cents = cents
        self.total_cent = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cent // 100

    @dollars.setter
    def dollars(self, new_dollars):
        self.total_cent = new_dollars * 100 + self.cents

    @property
    def cents(self):
        return self.total_cent % 100

    @cents.setter
    def cents(self, new_cents):
        self.total_cent = self.dollars * 100 + new_cents


print ('-'*50)
m = Money(27, 35)

print("Mamy tutaj {} dolarów i {} centów".format(m.dollars, m.cents))
print ('-'*50)

m.dollars += 2
print("Mamy tutaj {} dolarów i {} centów".format(m.dollars, m.cents))

print ('-'*50)

m.cents += 10
print("Mamy tutaj {} dolarów i {} centów".format(m.dollars, m.cents))
print ('-'*50)
