import pandas as pd

# Create an empty list to store the goods sold
goods_sold = []

# Get the goods sold and price from the user
while True:
    item = input("Enter the item name (or 'q' to quit): ")
    if item == 'q':
        break
    quantity = int(input("Enter the quantity sold: "))
    price = float(input("Enter the price: "))
    total_price = price * quantity
    goods_sold.append([item, quantity, price, total_price])

# Create a DataFrame from the goods sold
goods_df = pd.DataFrame(goods_sold, columns=["Item", "Quantity", "Price", "Total Price"])

# Print the total price
print("Total Price: ",goods_df["Total Price"].sum())

# Print the most sold item
most_sold_item = goods_df.loc[goods_df["Quantity"].idxmax()]
print("Most Sold Item: ",most_sold_item["Item"])

# Print the goods sold in tabular form
print(goods_df)

