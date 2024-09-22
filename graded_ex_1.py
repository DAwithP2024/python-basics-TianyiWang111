# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 1),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    return sorted(products_list, key=lambda x: x[1], reverse=sort_order != 1)

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")

def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return
    total_cost = sum(price * quantity for price, quantity in cart)
    for product, quantity in cart:
        print(f"{product} - Quantity: {quantity}")
    print(f"Total cost: ${total_cost}")

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Receipt for {name}")
    print(f"Email: {email}")
    print("Products:")
    for product, quantity in cart:
        print(f"{product} - Quantity: {quantity}")
    print(f"Total cost: ${total_cost}")
    print(f"Delivery address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email

def main():
    name = input("Enter your name: ")
    email = None
    
    while not validate_name(name):
        print("Invalid name. Please enter your first and last name.")
        name = input("Enter your name: ")
    
    while not email or not validate_email(email):
        email = input("Enter your email address: ")
        if not validate_email(email):
            print("Invalid email address. Please include '@' in your email.")
    
    display_categories()
    while True:
        category_choice = int(input("Enter the category number to explore: ")) - 1
        if category_choice < 1 or category_choice >= len(products):
            print("Invalid category choice. Please enter a valid number.")
            continue
        
        category = list(products.keys())[category_choice]
        display_products(products[category])
        while True:
            print("\n1. Select a product to buy\n2. Sort the products by price\n3. Go back to category selection\n4. Finish shopping")
            choice = input("Enter your choice: ")
            if choice == "1":
                product_choice = int(input("Enter the product number: ")) - 1
                if 0 <= product_choice < len(products[category]):
                    quantity = int(input("Enter the quantity: "))
                    add_to_cart(cart, products[category][product_choice], quantity)
                else:
                    print("Invalid product choice.")
            elif choice == "2":
                sort_order = int(input("Sort by 1 for ascending or 2 for descending: ")) - 1
                sorted_products = display_sorted_products(products[category], sort_order)
                display_products(sorted_products)
            elif choice == "3":
                break
            elif choice == "4":
                cart = []
                display_cart(cart)
                if cart:
                    address = input("Enter your delivery address: ")
                    total_cost = sum(price * quantity for price, quantity in cart)
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
