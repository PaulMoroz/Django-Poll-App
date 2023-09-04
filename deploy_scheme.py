import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define nodes
nodes = [
    "GitHub Repository",
    "AWS EC2",
    "Postgres Database",
    "Jenkins Master",
    "Jenkins Slave",
]

# Add nodes to the graph
G.add_nodes_from(nodes)

# Define edges (steps in the pipeline)
edges = [
    ("GitHub Repository", "Jenkins Slave"),
    ("Jenkins Slave","AWS EC2"),
    ("Postgres Database", "AWS EC2"),
    ("Jenkins Master", "Jenkins Slave"),
]

# Add edges to the graph
G.add_edges_from(edges)

# Set node positions for better visualization
pos = {
    "GitHub Repository": (1, 4),
    "AWS EC2": (3, 4),
    "Postgres Database": (3, 2),
    "Jenkins Master": (5, 5),
    "Jenkins Slave": (5, 3),
}

# Draw the graph
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1000,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
)
edge_labels = {(n1, n2): f"{n1} -> {n2}" for n1, n2 in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=None, font_size=8)
plt.title("GitHub App Deployment Pipeline with Jenkins Slave")
plt.axis("off")
plt.show()
