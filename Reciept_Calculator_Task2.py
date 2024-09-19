n=int(input("Enter the number of products: "))
product=[]
total_bill=0
for i in range(n):
    name=input("Enter the name: ")
    quantity=float(input("Enter the quantity: "))
    price=float(input("Enter price: "))
    product.append((name,quantity,price))
print("    ===WELCOME===")
print("  ===No Discount====")
print("Item\t Qty\t Price\t Total\t")
for item in product:
    total=item[2]*item[1]
    total_bill=total_bill+total
    print(f"{item[0][0:5]}\t{item[1]:3.3f}\t {item[2]:3.3f}\t {total:3.2f}")
    total_bill=total_bill+total
print("\n Total Bill=",total_bill)
print("===Thanks for shopping===")
print("=======Visit Again=======")

                   
