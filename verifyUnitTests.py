from customer import customerList

cl = customerList()
#d = {'fname':'Testguy','lname':'test',\
#'email':'a@a.com','password':'123','subscribed':'1'}
#cl.add(d)
cl.set('fname','')
cl.set('lname','Test')
cl.set('lastname','Test')
cl.add()
cl.verifyNew()
print(cl.errorList)
#print(cl.data)
cl.insert()
# A 