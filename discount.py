def calculate_discount(price, discount_percent):
    """Calculate the final price after applying discount if applicable"""
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Display result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price: ${original_price:.2f}")