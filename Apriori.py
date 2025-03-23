import itertools

# Sample transactions
dataset = [
    ['apple', 'banana'],
    ['milk', 'bread', 'butter'],
    ['tea', 'sugar'],
    ['apple', 'butter'],
    ['milk', 'cheese', 'apple'],
    ['cheese', 'sugar', 'milk'],
    ['tea', 'bread', 'apple', 'sugar', 'butter']
]

# Minimum support threshold
min_support = 0.3
min_count = min_support * len(dataset)

# Get unique items
items = sorted(set(item for transaction in dataset for item in transaction))

def support_count(itemset, transactions):
    return sum(1 for transaction in transactions if set(itemset).issubset(transaction))

def generate_candidates(prev_sets, size):
    return [list(set(a) | set(b)) for i, a in enumerate(prev_sets) for b in prev_sets[i + 1:] if len(set(a) | set(b)) == size]

# Apriori Algorithm
frequent_itemsets = {}
k = 1
current_sets = [[item] for item in items if support_count([item], dataset) >= min_count]
frequent_itemsets[k] = current_sets

while current_sets:
    k += 1
    candidates = generate_candidates(current_sets, k)
    valid_sets = [c for c in candidates if support_count(c, dataset) >= min_count]
    if not valid_sets:
        break
    frequent_itemsets[k] = valid_sets
    current_sets = valid_sets

# Print results
for k, itemsets in frequent_itemsets.items():
    print(f"\nFrequent {k}-Itemsets (Support ≥ {min_support * 100}%):")
    for itemset in itemsets:
        print(f"{set(itemset)} - Support: {support_count(itemset, dataset)}/{len(dataset)} ({(support_count(itemset, dataset) / len(dataset)) * 100:.2f}%)")
