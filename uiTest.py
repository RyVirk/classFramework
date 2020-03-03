from customer import customerList


c = customerList()

for fn in c.fnl:
    var = input("Enter " + fn + "\n")
    c.set(fn,var)
c.add()
c.insert()
print(c.data)
