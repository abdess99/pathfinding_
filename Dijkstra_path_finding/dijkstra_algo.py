import numpy as np
from create_map import put_zeros_before_int, create_map_visualizer
import pygame
import time


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


def dijkstra_dict_visualizer(nodes_dict, start_node, end_node, blockSize, screen):
    Orange = (255, 215, 0)
    BLUE = (0, 0, 255)
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
        for node in known_nodes.keys():
            if node != start_node and node != end_node:
                rect = pygame.Rect(int(node[2:]) * blockSize + 200, int(node[:2]) * blockSize, blockSize,
                                   blockSize)
                pygame.draw.rect(screen, Orange, rect, 0)
        pygame.display.flip()
        time.sleep(0.01)
        u = min(unknown_nodes, key=unknown_nodes.get)
        u_successors = nodes_dict[u].keys()
        u_predecessors = unknown_nodes[u][1]
        if u == end_node:
            for node in u_predecessors + [u]:
                if node != start_node and node != end_node:
                    rect = pygame.Rect(int(node[2:]) * blockSize + 200, int(node[:2]) * blockSize, blockSize,
                                       blockSize)
                    pygame.draw.rect(screen, BLUE, rect, 0)
            pygame.display.flip()
            return u_predecessors + [u]
        for successor in u_successors:

            if successor in unknown_nodes.keys() and unknown_nodes[successor][0] > unknown_nodes[u][0] + nodes_dict[u][
                successor]:
                unknown_nodes[successor][0] = unknown_nodes[u][0] + nodes_dict[u][successor]
                unknown_nodes[successor][1] = u_predecessors + [u]
        known_nodes[u] = unknown_nodes[u]
        del unknown_nodes[u]
    print(f'No path between {start_node} and {end_node}')
