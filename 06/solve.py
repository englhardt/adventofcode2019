import networkx as nx
g = nx.Graph([x.split(")") for x in open("input.txt").read().splitlines()])
print(sum([nx.shortest_path_length(g, "COM", x) for x in g.nodes]))
print(nx.shortest_path_length(g, "YOU", "SAN") - 2)
