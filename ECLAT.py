import pandas as pd
import itertools
import networkx as nx
import matplotlib.pyplot as plt

# Sample Transactions (Customers buying sports accessories)
dataset = [
    ['Football', 'Shoes', 'Jersey'],
    ['Cricket Bat', 'Shoes', 'Jersey', 'Gloves'],
    ['Football', 'Jersey', 'Basketball'],
    ['Tennis Racket', 'Shoes'],
    ['Football', 'Shoes', 'Jersey', 'Basketball'],
    ['Cricket Bat', 'Gloves'],
    ['Tennis Racket', 'Shoes', 'Jersey'],
    ['Basketball', 'Football', 'Jersey'],
]

# Convert transactions into vertical format (Item -> Transaction IDs)
transaction_dict = {}
for tid, transaction in enumerate(dataset):
    for item in transaction:
        if item not in transaction_dict:
            transaction_dict[item] = set()
        transaction_dict[item].add(tid)

# ECLAT Algorithm
def eclat(prefix, items, min_support, frequent_itemsets):
    """Recursive ECLAT algorithm to find frequent itemsets."""
    while items:
        item, tids = items.pop()
        support = len(tids) / len(dataset)
        if support >= min_support:
            new_prefix = prefix + [item]
            frequent_itemsets.append((new_prefix, support))

            # Compute intersections with remaining items
            new_items = [(other, tids & transaction_dict[other]) for other, _ in items]
            new_items = [(item, tids) for item, tids in new_items if len(tids) / len(dataset) >= min_support]

            eclat(new_prefix, new_items, min_support, frequent_itemsets)

# Run ECLAT
min_support = 0.3
frequent_itemsets = []
eclat([], list(transaction_dict.items()), min_support, frequent_itemsets)

# Convert frequent itemsets to DataFrame
frequent_itemsets_df = pd.DataFrame(frequent_itemsets, columns=["Itemset", "Support"])
frequent_itemsets_df["Itemset"] = frequent_itemsets_df["Itemset"].apply(lambda x: ', '.join(x))

# Display Frequent Itemsets
print("Frequent Itemsets:")
print(frequent_itemsets_df)

# -------------------- ECLAT Graph Visualization --------------------
def draw_eclat_graph(frequent_itemsets):
    """Visualize item relationships from frequent itemsets using NetworkX."""
    G = nx.Graph()

    for itemset, support in frequent_itemsets:
        items = itemset.split(", ")
        if len(items) > 1:
            for pair in itertools.combinations(items, 2):
                G.add_edge(pair[0], pair[1], weight=support)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    labels = {edge: f"{G.edges[edge]['weight']:.2f}" for edge in G.edges}
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightgreen", edge_color="gray", font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
    plt.title("ECLAT Item Relationship Graph (Sports Accessories)")
    plt.show()

# Draw the ECLAT Graph
draw_eclat_graph(frequent_itemsets_df.values)
