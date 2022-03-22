#클래스 문제

class Purchase():
    def __init__(self, article, price, quantity):
        self.article = article
        self.price = price
        self.quantity = quantity


Cart = []

while True:
    article = input('Enter description of article : ')
    price = int(input('Enter price of article : '))
    quantity = int(input('Enter quantity of article : '))
    Cart.append(Purchase(article,price,quantity))
    conti = input('Do you want to enter more articles?(Y/N) ')
    if conti == 'N' or conti != 'Y':
        break;

total = 0
slist = ["article","price","quantity"]
data4 = [w.upper() for w in slist]
for i in data4:
    print(i,end="  ")
for i in Cart:
    print(f'{i.article}  ${i.price:.2f}  {i.quantity}')
    total += i.price * i.quantity

print(f'TOTAL COST: ${total:.2f}')