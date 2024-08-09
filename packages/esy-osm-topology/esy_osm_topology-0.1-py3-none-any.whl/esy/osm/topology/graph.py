'''
# Graph utilities
'''

import numpy as np, scipy.sparse, shapely


def merge(graph, map, distances):
    '''
    >>> g = scipy.sparse.coo_array(((1., 1.), ([0, 1], [1, 2])), shape=(4, 4))
    >>> m = merge(g, [0, 0, 2, -9999], [0, 1, 0, np.inf])
    >>> tuple(zip(m.data.tolist(), m.row.tolist(), m.col.tolist()))
    ((2.0, 0, 2),)

    '''
    map, distances = np.asarray(map), np.asarray(distances)
    row, col = map[graph.row], map[graph.col]

    # Add distances to joined edges.
    data = graph.data.copy()

    # Identify edges whose outgoing nodes (row) are to be joined. Add distance
    # to nearest target node to these edges.
    join = row != graph.row
    data[join] += distances[graph.row[join]]

    # Repeat this for edges with joined incoming nodes (col).
    join = col != graph.col
    data[join] += distances[graph.col[join]]

    # Trim graph to unique edges.
    # Note: scipy.sparse.coo_array will sum up duplicate edges automatically.
    valid = row != col
    return scipy.sparse.coo_array(
        (data[valid], (row[valid], col[valid])), shape=graph.shape
    )


def unique(coords, graph):
    '''
    Merges nodes of `graph` with identical `coords`.

    Note: May result in duplicate edges, from which the first is selected.

    >>> coords = np.array([[0, 0], [1, 1], [0, 0], [1, 1], [0, 0], [2, 2]])
    >>> graph = scipy.sparse.coo_array(
    ...     ((1, 1, 1), ([0, 2, 4], [1, 3, 5])), shape=(6, 6)
    ... )
    >>> graph, node_index, edge_index = unique(coords, graph)
    >>> node_index, edge_index
    (array([0, 1, 5]), array([0, 2]))
    >>> tuple(zip(graph.data.tolist(), graph.row.tolist(), graph.col.tolist()))
    ((1, 0, 1), (1, 0, 5))

    '''
    _, node_index, node_inverse = np.unique(
        coords, axis=0, return_index=True, return_inverse=True
    )

    if node_inverse.ndim == 2:
        # Since numpy 2, inverse of unique maintains input dimensions.
        node_inverse = node_inverse.squeeze()

    (row, col), edge_index = np.unique(
        [node_inverse[graph.row], node_inverse[graph.col]], axis=1,
        return_index=True
    )
    graph = scipy.sparse.coo_array(
        (graph.data[edge_index], (node_index[row], node_index[col])),
        shape=graph.shape
    )

    return graph, node_index, edge_index


def from_string_coordinates(coords):
    data = np.concatenate([
        np.sum(np.diff(np.asarray(c), axis=0) ** 2, axis=1) ** 0.5
        for c in coords
    ])
    a, row, col, edge_index = 0, [], [], []
    for i, c in enumerate(coords):
        b = a + len(c)
        row.extend(range(a, b - 1))
        col.extend(range(a + 1, b))
        edge_index.extend([i] * (len(c) - 1))
        a = b

    return (
        np.concatenate(coords),
        scipy.sparse.coo_array((data, (row, col)), shape=(a,) * 2),
        np.array(edge_index),
    )


def degrees(sparse):
    '''
    >>> a = scipy.sparse.coo_array(
    ...     ([1, 1, 1], ([0, 1, 2], [1, 2, 2])), shape=(3, 3)
    ... )
    >>> a.toarray()
    array([[0, 1, 0],
           [0, 0, 1],
           [0, 0, 1]])
    >>> degrees(a)
    array([1, 2, 3])
    '''
    degrees = np.zeros(sparse.shape[0], dtype=int)
    for index in np.unique([sparse.row, sparse.col], axis=1):
        unique, count = np.unique(index, return_counts=True)
        degrees[unique] += count
    return degrees


def filter_edges(graph, selection):
    return scipy.sparse.coo_array(
        (graph.data[selection], (graph.row[selection], graph.col[selection])),
        shape=graph.shape
    )


def predecessor_path(predecessors, a):
    '''
    Reconstructs the path from `a` back to its origin using `predecessors`.

    >>> predecessor_path([-9999, 3, 0, 2], 1)
    [1, 3, 2, 0]

    '''
    p = [a]
    while True:
        b = predecessors[a]
        if b < 0:
            return p
        p.append(b)
        a = b


def shortest_path(graph, predecessors, sources, edge):
    '''
    Construct the shortest path which passes through `edge` by following the
    `predecessors` back to the `sources`.
    '''
    a, b = graph.row[edge], graph.col[edge]
    if sources[a] == sources[b]:
        raise ValueError(f'Edge is not on a shortest path')
    return (
        predecessor_path(predecessors, a)[::-1] +
        predecessor_path(predecessors, b)
    )


def normalize_undirected_graph(graph):
    '''
    Normalizes the undirected `graph` and moves edge information to the upper
    triangle of the connectivity matrix.

    >>> normalize_undirected_graph(scipy.sparse.coo_array([
    ...     [1, 1, 0],
    ...     [0, 0, 0],
    ...     [2, 3, 0],
    ... ])).todense()
    array([[1, 1, 2],
           [0, 0, 3],
           [0, 0, 0]])
    
    '''
    row, col = np.array(graph.row), np.array(graph.col)
    lower = row > col
    row[lower], col[lower] = col[lower], row[lower]
    return scipy.sparse.coo_array((graph.data, (row, col)), graph.shape)


def make_edge_index(graph):
    '''
    Constructs the tuple `(size, index, order)` containing the size of the
    graph, the linear index for the edges of `graph` including the sorting
    order.

    >>> make_edge_index(scipy.sparse.coo_array([
    ...     [1, 1, 0],
    ...     [0, 0, 0],
    ...     [2, 3, 0],
    ... ]))
    (3, array([0, 1, 2, 5], dtype=int32), array([0, 1, 2, 3]))

    '''
    graph = normalize_undirected_graph(graph)
    size = graph.shape[0]
    index = graph.row * size + graph.col
    order = np.argsort(index)
    return size, index, order


def path_edge_index(edge_index, path):
    '''
    Maps a `path` of nodes to edge indice using an `edge_index` tuple.

    >>> graph = scipy.sparse.coo_array(
    ...     ((1, 1, 1), ([0, 2, 2], [1, 0, 1])), shape=(3, 3)
    ... )
    >>> path_edge_index(make_edge_index(graph), [0, 2, 1])
    array([1, 2])

    '''
    size, index, order = edge_index

    row, col = np.array(path[:-1]), np.array(path[1:])
    lower = row > col
    row[lower], col[lower] = col[lower], row[lower]

    index_path = row * size + col
    index_edge = np.searchsorted(index, index_path, sorter=order)
    return order[index_edge]


def query_terminals(coords, graph, terminals, predicate='contains'):
    '''
    Query `coords` which overlap with `terminals`.
    '''
    strtree = shapely.STRtree(shapely.points(coords))
    terminal_idx, coord_idx = strtree.query(terminals, predicate=predicate)
    terminal_map = np.full(len(coords), -1)
    terminal_map[coord_idx] = terminal_idx
    terminal_edges = terminal_map[[graph.row, graph.col]]

    # Select edges which are not connected to terminals or connected different
    # terminals.
    valid_edge = (
        np.all(terminal_edges < 0, axis=0) |
        (terminal_edges[0] != terminal_edges[1])
    )
    terminal_nodes = np.unique(np.concatenate([
        graph.row[terminal_edges[0] >= 0], graph.col[terminal_edges[1] >= 0]
    ]))
    return terminal_nodes, terminal_map, np.where(valid_edge)[0]


def extract_links(graph, sources, linkmap):
    link_sources = np.array(sources)
    valid = sources >= 0
    link_sources[valid] = linkmap[sources[valid]]
    return np.where(link_sources[graph.row] != link_sources[graph.col])[0]


def shortest_terminal_paths(graph, predecessors, sources, terminal_index):
    '''
    Constructs shortest `(node_paths, edge_paths)`.
    '''
    node_paths = [
        shortest_path(graph, predecessors, sources, link)
        for link in extract_links(graph, sources, terminal_index)
    ]

    # Lookup edge indice from node paths.
    edge_index = make_edge_index(graph)
    edge_paths = [path_edge_index(edge_index, path) for path in node_paths]
    return node_paths, edge_paths


def int32_coo_array(array):
    '''
    Returns a copy of `array` with row and col indice converted to `int32`.
    '''
    # scipy.sparse.csgraph.dijkstra doesn't support int64 indice as of scipy
    # version 1.11.
    return scipy.sparse.coo_array(
        (array.data, (array.row.astype(np.int32), array.col.astype(np.int32))),
        shape=array.shape
    )


def terminal_topology(coords, graph, terminals, terminal_index):
    '''
    Computes the topology of the `terminals` nodes of `graph`.
    '''
    distances, predecessors, sources = scipy.sparse.csgraph.dijkstra(
        int32_coo_array(graph), directed=False, indices=terminals,
        return_predecessors=True, min_only=True
    )

    node_paths, edge_paths = shortest_terminal_paths(
        graph, predecessors, sources, terminal_index
    )

    # TODO This doesn't prune self-connections.
    topology = merge(graph, sources, distances)
    topology = filter_edges(
        topology, terminal_index[topology.row] != terminal_index[topology.col]
    )

    shapes = [shapely.linestrings(coords[path]) for path in node_paths]

    return topology, shapes, edge_paths

