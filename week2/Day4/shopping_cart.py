# Shopping cart price calculator with exception handling

items = {"apple" : 100, "banana" : 150, "kiwi":200, "milk":250}

try:
    item = input("Enter the product you want to buy(apple/banana/kiwi/milk: ").lower()
    quantity = int(input("Enter quantity: "))
    
    if item not in items:
        raise KeyError("Item not available")
    else:
     price = items[item] * quantity
     print(f"✅ Total price for {quantity} {item}(s) = {price} PKR")

except ValueError:
   print("Error! Quantity should be a number")
except KeyError as e:
   print(e)

finally:
   print("Thanks for shopping with us!")

 
