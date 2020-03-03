from customer import customerList

c = customerList()
c.set('fname','Testguy')
c.set('lname','Test')
c.set('email','a@a.com')
c.set('subscribed','True')
c.set('password','12345')
c.add()
# A - show the mysql table

c.insert()

# B - show c.data

c.data[0]['lname'] = 'newname'
c.insert()

# C - show the mysql table and c.data 