products = []

def add_product():
    name = input("Enter product name: ")
    category = input("Enter category: ")
    cost = float(input("Enter cost price: "))
    profit_percentage = float(input("Enter profit percentage: "))

    sale_price = cost + (cost * profit_percentage / 100)

    product = {
        "name": name,
        "category": category,
        "cost": cost,
        "profit_percentage": profit_percentage,
        "sale_price": sale_price
    }

    products.append(product)
    print("Product added successfully.\n")


def show_products():
    if len(products) == 0:
        print("No products available.\n")
    else:
        print("\nProduct list:")
        for product in products:
            print(f"Name: {product['name']}")
            print(f"Category: {product['category']}")
            print(f"Cost: {product['cost']}")
            print(f"Profit %: {product['profit_percentage']}")
            print(f"Sale price: {product['sale_price']}")
            print("-" * 30)
        print()


def search_by_category():
    category_search = input("Enter category to search: ")
    found = False

    for product in products:
        if product["category"].lower() == category_search.lower():
            print(f"Name: {product['name']}")
            print(f"Cost: {product['cost']}")
            print(f"Sale price: {product['sale_price']}")
            print("-" * 30)
            found = True

    if not found:
        print("No products found in that category.\n")


def menu():
    while True:
        print("=== Hardware Store System ===")
        print("1. Add product")
        print("2. Show products")
        print("3. Search by category")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_product()
        elif option == "2":
            show_products()
        elif option == "3":
            search_by_category()
        elif option == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid option. Try again.\n")


menu()
