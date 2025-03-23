import random

# Store shoe items with their corresponding IDs
items_in_store = {
    1: 'sneakers',
    2: 'running shoes',
    3: 'formal shoes',
    4: 'boots',
    5: 'loafers',
    6: 'sandals',
    7: 'slippers',
    8: 'high heels',
    9: 'flip-flops',
    10: 'wedges'
}

# Function to create random transactions
def create_random_transactions(transaction_count):
    all_transactions = {}
    for txn in range(1, transaction_count + 1):
        transaction_id = f"Txn{txn}"
        item_count = random.randint(3, 5)  # Select 3 to 5 items
        selected_items = random.sample(list(items_in_store.keys()), item_count)
        all_transactions[transaction_id] = [(code, items_in_store[code]) for code in selected_items]
    return all_transactions

# Function to get user-selected items
def get_user_selected_items(items_in_store):
    print("\nAvailable Shoe Items:")
    for code, name in items_in_store.items():
        print(f"{code}: {name}")

    try:
        user_input = input("\nEnter the item numbers to include in your subset (comma-separated): ")
        selected_codes = list(set(map(int, user_input.split(','))))  # Remove duplicates
        selected_items = [(code, items_in_store[code]) for code in selected_codes if code in items_in_store]

        if not selected_items:
            print("No valid items selected. Please try again.")
        return selected_items

    except ValueError:
        print("Invalid input. Please enter valid numeric item codes.")
        return []

# Function to save transactions to a file
def save_transactions_to_file(transactions, file_name):
    with open(file_name, 'w') as file:
        for txn_id, items in transactions.items():
            file.write(f"{txn_id}: {', '.join([f'{code}-{name}' for code, name in items])}\n")
    print(f"\nTransactions have been saved to the file: {file_name}")

# Function to display transactions from a file
def display_transactions_from_file(file_name):
    print("\nTransactions stored in the file:")
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' could not be found.")

# Function to perform reverse lookup on transactions
def perform_reverse_lookup(file_name, items_in_store):
    print("\nReverse Lookup: Transactions Containing Each Item")
    try:
        with open(file_name, 'r') as file:
            txn_lines = file.readlines()
            lookup_table = {code: [] for code in items_in_store.keys()}

            for line in txn_lines:
                txn_id, items_str = line.split(":")
                item_list = items_str.strip().split(", ")

                for item in item_list:
                    item_code = int(item.split("-")[0])
                    if item_code in lookup_table:
                        lookup_table[item_code].append(txn_id.strip())

            for code, txn_ids in lookup_table.items():
                print(f"{code}-{items_in_store[code]}: {', '.join(txn_ids) if txn_ids else 'No transactions'}")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' could not be found.")

# Main program execution
if __name__ == "__main__":
    try:
        num_txns = int(input("Enter the number of transactions to generate: "))
        if num_txns <= 0:
            print("Error: The number of transactions must be greater than zero.")
        else:
            generated_transactions = create_random_transactions(num_txns)

            print("\nGenerated Transactions:")
            for txn_id, items in generated_transactions.items():
                print(f"{txn_id}: {', '.join([f'{code}-{name}' for code, name in items])}")

            selected_items = get_user_selected_items(items_in_store)
            if selected_items:
                print("\nItems Selected by User:")
                print(", ".join([f"{code}-{name}" for code, name in selected_items]))

            file_name = "transactions_data.txt"
            save_transactions_to_file(generated_transactions, file_name)
            display_transactions_from_file(file_name)
            perform_reverse_lookup(file_name, items_in_store)

    except ValueError:
        print("Error: Please enter a valid integer for the number of transactions.")
