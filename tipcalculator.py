foodprice=input("Enter Food Price:")
foodprice=float(foodprice)

tipprice=(foodprice*18)/100
taxprice=(foodprice*7)/100
grandtotal=foodprice+tipprice+taxprice

print(f"Food Price = {foodprice}$")

print(f"Tip Price = {tipprice}$")
print(f"Tax Price = {taxprice}$")

print(f"Grand Total = {grandtotal}$")