customers = [
  {
  "id": 1,
  "name": "Pouria",
  "email": "pouria@gmail.com",
  "is_active": True
  },
  { 
  "id": 2,
  "name": "Ali",    
  "email": "ali@gmail.com",
  "is_active": False
  },
    { 
  "id": 3,
  "name": "Sara",    
  "email": "sara@gmail.com",
  "is_active": True
  },
  {
    "id": 4,
    "name": "John",
    "is_active": False
  }
]

def get_active_customer_count(customers):
    active_customers = []
    for customer in customers:
        if customer['is_active']:
            active_customers.append(customer)
            
    return len(active_customers)

length_of_active_customer = get_active_customer_count(customers)


class Customer:
  def __init__(self, name, email, is_active):
    self.name = name
    self.email = email
    self.is_active = is_active
  
  def is_active_customer(self):
   return self.is_active

customer = Customer( "Pouria", "pouria@gmail.com", True )
print(customer.is_active_customer())
