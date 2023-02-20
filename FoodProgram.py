import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0

"""
cus1 = fc.Customer(
    570,
    "Danni Sellyar",
    "97 Mitchell Way Hewitt Texas 76712",
    "dsellyarft@gmpg.org",
    "254-555-9362",
    False,
)
"""
cus1 = fc.Customer(
    569,
    "Aubree Himsworth",
    "1172 Moulton Hill Waco Texas 76710",
    "ahimsworthfs@list-manage.com",
    "254-555-2273",
    True,
)


transaction = []
costs = []
item_names = []

for key, values in dict.items():
    date, item_name, cost, customerid = values

    if customerid == cus1.get_customerid():
        customer = cus1
        member_status = customer.get_member_status()
        costs.append(cost)
        item_names.append(item_name)

    else:
        continue

    transaction = fc.Transaction(date, item_name, cost, customerid)
    order_total += transaction.get_cost()

if member_status == True:
    discount = order_total * 0.2
    # order_total -= discount
else:
    discount = 0

print(f"Customer name: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")
for j in range(len(costs)):
    print(f"Order Item: {item_names[j]} Price: ${costs[j]:.2f}")
print(f"Total Cost: ${order_total:.2f}")
if discount > 0:
    print(f"Member Discount: ${discount:.2f}")
    print(f"Total Cost after discount: ${order_total-discount:.2f}")
