import itertools

# Sports equipment dataset (transactions)
sports_transactions = [
    ['Football', 'Jersey'],
    ['Basketball', 'Shoes', 'Jersey'],
    ['Jersey', 'Football', 'Shoes'],
    ['Football', 'Gloves'],
    ['Shoes', 'Basketball', 'Gloves'],
    ['Basketball', 'Football', 'Jersey'],
    ['Football', 'Jersey', 'Shoes', 'Gloves']
]

min_support = 0.3  # 30% minimum support
num_transactions = len(sports_transactions)  # Total transactions
min_count = min_support * num_transactions  # Minimum count threshold

# Extract unique items
unique_items = sorted(set(item for t in sports_transactions for item in t))  # Sorted list of all items


# Function to calculate support count for an itemset
def count_support(itemset, transactions):
    return sum(1 for t in transactions if set(itemset).issubset(set(t)))


# Generate and display candidate & frequent itemsets
print("\n--- CANDIDATE & FREQUENT ITEMSETS ---\n")
frequent_itemsets = {}
for size in range(1, len(unique_items) + 1):
    print(f"\nCandidate {size}-itemsets:")
    candidate_itemsets = {}

    for itemset in itertools.combinations(unique_items, size):
        support_count = count_support(itemset, sports_transactions)
        candidate_itemsets[itemset] = support_count
        print(f"{itemset}: {support_count}")

    # Filter to get only frequent itemsets
    frequent = {k: v for k, v in candidate_itemsets.items() if v >= min_count}
    if not frequent:
        break  # Stop if no frequent itemsets are found at this level

    frequent_itemsets[size] = frequent

    print(f"\nFrequent {size}-itemsets:")
    for itemset, count in frequent.items():
        print(f"{itemset}: {count}")

print("\n--- FINAL FREQUENT ITEMSETS ---")
for size, itemsets in frequent_itemsets.items():
    print(f"\nFrequent {size}-itemsets:")
    for itemset, count in itemsets.items():
        print(f"{itemset}: {count}")
