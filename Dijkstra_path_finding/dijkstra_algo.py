import numpy as np


class Error(Exception):
    pass


class BlockedNodeError(Error):
    pass


def dijkstra_dict(nodes_dict, start_node, end_node):
    try:
        if start_node not in nodes_dict or end_node not in nodes_dict:
            raise BlockedNodeError
    except BlockedNodeError:
        print('start node or end node is blocked')
        return
    known_nodes = {start_node: [0, [start_node]]}  # nodes we already know the path to
    unknown_nodes = {k: [np.inf, []] for k in nodes_dict.keys() if k != start_node}  # nodes we don't know the path to
    for k in nodes_dict[start_node].keys():
        unknown_nodes[k] = [nodes_dict[start_node][k], [start_node]]

    while any(np.isfinite([unknown_nodes[k][0] for k in unknown_nodes.keys()])):
        u = min(unknown_nodes, key=unknown_nodes.get)
        u_successors = nodes_dict[u].keys()
        u_predecessors = unknown_nodes[u][1]
        if u == end_node:
            return u_predecessors + [u]
        for successor in u_successors:

            if successor in unknown_nodes.keys() and unknown_nodes[successor][0] > unknown_nodes[u][0] + nodes_dict[u][
                successor]:
                unknown_nodes[successor][0] = unknown_nodes[u][0] + nodes_dict[u][successor]
                unknown_nodes[successor][1] = u_predecessors + [u]
        known_nodes[u] = unknown_nodes[u]
        del unknown_nodes[u]
    print(f'No path between {start_node} and {end_node}')
