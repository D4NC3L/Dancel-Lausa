inventory = {}

while True:
    print("\n1. Add Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Exit")
    
    choice = input("Choose an option: ") [cite: 15, 16]

    if choice == '1':
        name = input("Enter product name: ").lower() [cite: 17]
        price = float(input("Enter product price: ")) [cite: 18]
        inventory[name] = price
        print("Product added successfully.") [cite: 19]

    elif choice == '2':
        print("\nProduct List:")
        for name, price in inventory.items():
            print(f"{name} : {price:.1f}") [cite: 25]

    elif choice == '3':
        search_name = input("Enter product name to search: ").lower() [cite: 31]
        if search_name in inventory:
            print(f"Price: {inventory[search_name]:.1f}") [cite: 32]
        else:
            print("Product not found.")

    elif choice == '4':
        break [cite: 15]