import networkx as nx
from pyvis.network import Network

G = nx.petersen_graph()

print("Adjacency List:")
for node in G.nodes():
    print(f"{node}: {list(G.neighbors(node))}")

print("Degrees:")
for node in G.nodes():
    print(f"Vertex {node}: Degree = {G.degree[node]}")

adj_matrix = nx.to_numpy_array(G, dtype=int)

print("\nAdjacency Matrix:")
print(adj_matrix)

# ד. שמירת מטריצת השכנויות כקובץ HTML
html = """
<html>
<head>
    <title>Adjacency Matrix</title>
    <style>
        table {
            border-collapse: collapse;
            margin: 20px;
        }
        td, th {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
    </style>
</head>
<body>
<h2>Petersen Graph - Adjacency Matrix</h2>
<table>
"""

# כותרת עמודות
html += "<tr><th></th>"
for i in range(len(adj_matrix)):
    html += f"<th>{i}</th>"
html += "</tr>"

# תוכן המטריצה
for i in range(len(adj_matrix)):
    html += f"<tr><th>{i}</th>"
    for j in range(len(adj_matrix)):
        html += f"<td>{adj_matrix[i][j]}</td>"
    html += "</tr>"

html += """
</table>
</body>
</html>
"""

with open("adjacency_matrix.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\nThe adjacency matrix was saved to adjacency_matrix.html")
