from customer import customerList
import time

cl = customerList()
cl.getById(5)
print(cl.data)
cl.data[0]['fname'] = 'Tyler' 
cl.update()

