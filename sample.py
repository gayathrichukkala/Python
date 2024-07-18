cost=100
quant=int(input("enter the quantity:"))
total=cost*quant
if total>=1000:
    discount=total*(10/100)
    price=total-discount
    print("dicount applied",price)
else:
    print("dicount not applied",total)    