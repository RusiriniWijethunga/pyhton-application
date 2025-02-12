import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes for each step in the process
nodes = [
    "Start", "Frontend UI Design", "Frontend User Input", "Frontend API Call",
    "Backend Handle Request", "Backend Code Analysis (Optional)", "AI Model Integration",
    "Data Preprocessing", "Generate SRS Document", "Return Document to Frontend",
    "User Interaction", "User Authentication (Optional)", "Backend Document Storage (Optional)", "End"
]
G.add_nodes_from(nodes)

# Add directed edges to represent the flow between steps
edges = [
    ("Start", "Frontend UI Design"),
    ("Frontend UI Design", "Frontend User Input"),
    ("Frontend User Input", "Frontend API Call"),
    ("Frontend API Call", "Backend Handle Request"),
    ("Backend Handle Request", "Backend Code Analysis (Optional)"),
    ("Backend Handle Request", "AI Model Integration"),
    ("AI Model Integration", "Data Preprocessing"),
    ("Data Preprocessing", "Generate SRS Document"),
    ("Generate SRS Document", "Return Document to Frontend"),
    ("Return Document to Frontend", "User Interaction"),
    ("User Interaction", "User Authentication (Optional)"),
    ("User Authentication (Optional)", "Backend Document Storage (Optional)"),
    ("Backend Document Storage (Optional)", "End"),
    ("User Interaction", "End")
]
G.add_edges_from(edges)

# Set up plot
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # Positioning of nodes
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)

# Show the graph
plt.title("AI-powered SRS Document Generation Flow")
plt.show()
