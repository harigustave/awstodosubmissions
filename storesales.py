products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

totalprice=0
for price in prices:
    totalprice+=price
print(f"Current Total Sales Price Average = {totalprice/len(prices)}$")

#New price list that reduce the current by 5$
newprices=[]
for price in prices:
    price-=5
    newprices.append(price)

print("Current Price List = ",prices)
print("New Price List Reduced By 5$ = ",newprices)
print(f"Current Total Revenue For All Products = {totalprice}$")
print(f"Current Average Daily Revenue For All Products = {totalprice/7}$")

#Products less than 30$ based on new price
newpriceless30=[]
for price in newprices:
    if price<30:
        newpriceless30.append(price)
print("Based On New Price, Products Whose price Less Than 30$ = ",newpriceless30)
print("Based On New Price, Number Of Products Less Than 30$ = ",len(newpriceless30))