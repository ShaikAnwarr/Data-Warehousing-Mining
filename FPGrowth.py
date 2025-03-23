import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import fpgrowth

# Step 1: Sample Transactions
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

# Step 2: Convert transactions to DataFrame
unique_items = sorted(set(item for transaction in dataset for item in transaction))
df = pd.DataFrame([{item: (item in transaction) for item in unique_items} for transaction in dataset])

# Step 3: Apply FP-Growth Algorithm
min_support = 0.3  # Minimum support threshold
frequent_itemsets = fpgrowth(df, min_support=min_support, use_colnames=True)

# Display Frequent Itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)

# -------------------- FP-Tree Construction --------------------
class TreeNode:
    """Node structure for FP-Tree"""
    def __init__(self, item, count, parent):
        self.item = item
        self.count = count
        self.parent = parent
        self.children = {}

    def increment(self, count):
        """Increment the count of a node"""
        self.count += count

# Step 4: Build FP-Tree
def build_fptree(transactions, min_support):
    """Construct FP-Tree from transactions"""
    # Count item frequency
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1

    # Remove items below minimum support
    items = {item for item, count in item_counts.items() if count >= min_support * len(transactions)}
    if not items:
        return None

    # Reorder transactions by frequency
    ordered_transactions = []
    for transaction in transactions:
        ordered_transactions.append(sorted([item for item in transaction if item in items], key=lambda i: -item_counts[i]))

    # Build tree
    root = TreeNode(None, 1, None)
    for transaction in ordered_transactions:
        current_node = root
        for item in transaction:
            if item in current_node.children:
                current_node.children[item].increment(1)
            else:
                new_node = TreeNode(item, 1, current_node)
                current_node.children[item] = new_node
            current_node = current_node.children[item]
    return root

# Build the FP-Tree
fp_tree = build_fptree(dataset, min_support=0.3)

# -------------------- FP-Tree Visualization --------------------
def draw_fptree(node, graph=None, parent=None):
    """Recursive function to draw FP-Tree using NetworkX"""
    if graph is None:
        graph = nx.DiGraph()

    if node.item is not None:
        graph.add_node(node.item, label=f"{node.item} ({node.count})")
        if parent is not None:
            graph.add_edge(parent, node.item)

    for child in node.children.values():
        draw_fptree(child, graph, node.item)

    return graph

# Visualize the FP-Tree
graph = draw_fptree(fp_tree)
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(graph, seed=42)
labels = nx.get_node_attributes(graph, "label")
nx.draw(graph, pos, with_labels=True, labels=labels, node_size=2000, node_color="lightblue", edge_color="gray", font_size=10)
plt.title("FP-Tree Visualization (Sports Accessories)")
plt.show()
