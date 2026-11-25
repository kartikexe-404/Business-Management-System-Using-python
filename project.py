
# BUSINESS MANAGEMENT SYSTEM

products = []
sales = []
expenses = []


# Function to save history in a file
def save_history(message):
    file = open("history.txt", "a")
    file.write(message + "\n")
    file.close()


# Function to add product
def add_product():

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter stock quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)

    print("Product added successfully!")


# Function to view products
def view_products():

    print("\n--- PRODUCT INVENTORY ---")

    if len(products) == 0:
        print("No products available.")

    else:
        for i in range(len(products)):

            print("\nProduct ID:", i + 1)
            print("Name:", products[i]["name"])
            print("Price: Rs.", products[i]["price"])
            print("Quantity:", products[i]["quantity"])


# Function to record sale
def record_sale():

    view_products()

    if len(products) == 0:
        return

    pid = int(input("\nEnter product ID: "))
    qty = int(input("Enter quantity sold: "))

    if pid < 1 or pid > len(products):
        print("Invalid product ID.")

    elif qty <= 0:
        print("Quantity must be greater than zero.")

    else:

        product = products[pid - 1]

        if qty <= product["quantity"]:

            total = qty * product["price"]

            product["quantity"] -= qty
            sales.append(total)

            print("\nSale successful!")
            print("Product:", product["name"])
            print("Quantity:", qty)
            print("Total amount: Rs.", total)

            # Save sale history
            save_history(
                "SALE | Product: " + product["name"] +
                " | Quantity: " + str(qty) +
                " | Total: Rs. " + str(total)
            )

        else:
            print("Insufficient stock!")


# Function to add expense
def add_expense():

    name = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))

    if amount > 0:

        expenses.append(amount)

        print("Expense added successfully!")

        # Save expense history
        save_history(
            "EXPENSE | Description: " + name +
            " | Amount: Rs. " + str(amount)
        )

    else:
        print("Invalid expense amount.")


# Function to view history
def view_history():

    print("\n--- BUSINESS HISTORY ---")

    try:
        file = open("history.txt", "r")
        history = file.read()
        file.close()

        if history == "":
            print("No history available.")

        else:
            print(history)

    except FileNotFoundError:
        print("History file not found.")


# Function to generate business report
def business_report():

    total_sales = sum(sales)
    total_expenses = sum(expenses)

    print("\n--- BUSINESS REPORT ---")

    print("Total Sales: Rs.", total_sales)
    print("Total Expenses: Rs.", total_expenses)

    print("Balance: Rs.", total_sales - total_expenses)


# Main menu
while True:

    print("\n================================")
    print("    BUSINESS MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Product")
    print("2. View Products")
    print("3. Record Sale")
    print("4. Add Expense")
    print("5. Business Report")
    print("6. View History")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        record_sale()

    elif choice == "4":
        add_expense()

    elif choice == "5":
        business_report()

    elif choice == "6":
        view_history()

    elif choice == "7":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")
