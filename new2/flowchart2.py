import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes for each step in the process
nodes = [
    "Start", "Design Frontend UI", "User Input on Frontend", "API Call to Backend",
    "Backend Receives Request", "Optional Backend Code Analysis", "AI Model Integration",
    "Preprocessing Data", "Generate SRS Document", "Return Document to Frontend",
    "User Interacts with Document", "Optional User Authentication", "Optional Document Storage", "End"
]
G.add_nodes_from(nodes)

# Add directed edges to represent the flow between steps
edges = [
    ("Start", "Design Frontend UI"),
    ("Design Frontend UI", "User Input on Frontend"),
    ("User Input on Frontend", "API Call to Backend"),
    ("API Call to Backend", "Backend Receives Request"),
    ("Backend Receives Request", "Optional Backend Code Analysis"),
    ("Backend Receives Request", "AI Model Integration"),
    ("AI Model Integration", "Preprocessing Data"),
    ("Preprocessing Data", "Generate SRS Document"),
    ("Generate SRS Document", "Return Document to Frontend"),
    ("Return Document to Frontend", "User Interacts with Document"),
    ("User Interacts with Document", "Optional User Authentication"),
    ("Optional User Authentication", "Optional Document Storage"),
    ("Optional Document Storage", "End"),
    ("User Interacts with Document", "End")
]
G.add_edges_from(edges)

# Set up plot
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # Positioning of nodes
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)

# Show the graph
plt.title("AI-powered SRS Document Generation Flow")
plt.show()
