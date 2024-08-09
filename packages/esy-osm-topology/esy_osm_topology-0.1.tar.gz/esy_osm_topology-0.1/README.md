
[`esy.osm.topology`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology.html) is a library to implement topology construction heuristics
from visual data like [OpenStreetMap](https://www.openstreetmap.org). It can be
used to construct workflows to extract infrastructure topologies like
electricity grids from OpenStreetMap data, for example.

As it is very unlikely that visual data is complete and coherent, the topology
construction is usually ambiguous. Missing data or inaccuracies must be fixed
case-by-case in individual workflows.

[`esy.osm.topology`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology.html) is designed for frictionless embedding into workflows and
tries to limit its dependencies to [numpy](https://numpy.org) for number
crunching, [scipy](https://scipy.org) for graph algorithms and
[shapely](https://shapely.readthedocs.io) for geometry processing.
[esy.osm.shape](https://dlr-ve-esy.gitlab.io/esy-osm-pbf/) (which pulls in
[Protocol Buffers](https://protobuf.dev) as transitive dependency) is required
to extract geometries from OpenStreetMap. Additionally,
[pyproj](https://pyproj4.github.io/pyproj/) is recommended for OpenStreetMap
data to convert coordinates to cartesian.

# Features

What it provides:

- Functions to construct graphs from [shapely](https://shapely.readthedocs.io)
  geometry and vice-versa.
- Functions to reduce visual representations to topologies.
- Matplotlib graph visualization functions.
- GeoJSON output functions.

What it *doesn't* provide:

- Ready to use extraction of topology datasets from OpenStreetMap. For example
  users need to:
  - Assign topology attributes (like link capacities, ...)
  - Merge multiple topologies (like electricity grid voltage levels, ...)

# Installation

Use `pip` to install [`esy.osm.topology`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology.html):

```
$ pip install esy-osm-topology
```

# Example workflow

[`esy.osm.topology`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology.html) provides functions to construct topologies from geometry
objects.

```python
>>> import numpy as np, scipy.sparse, matplotlib.pyplot as plt, shapely
>>> from esy.osm.topology.test import example
>>> import esy.osm.topology.graph, esy.osm.topology.mpl
>>> 
>>> lines = [shapely.LineString(coords) for coords in [
...     [[0, 1], [0, 0], [1, 0], [2, 0], [4, 0]],
...     [[1, 0], [1, 1]],
...     [[2, 0], [2, 1]],
...     [[7, 0], [8, 0], [8, 2]],
...     [[0, 0], [0, -1], [4, -1]],
...     [[4, 0], [7, 0]],
... ]]
>>> terminals = [shapely.Polygon(coords) for coords in [
...     [[-0.25, 0.75], [0.25, 0.75], [0, 1.25]],
...     [[0.75, 0.75], [1.25, 0.75], [1, 1.25]],
...     [[1.75, 0.75], [2.25, 0.75], [2, 1.25]],
...     [[7.75, 1.75], [8.25, 1.75], [8, 2.25]],
...     [[3.75, 0.25], [4.25, 0.25], [4.25, -1.25], [3.75, -1.25]],
...     [[6.75, 0.25], [7.25, 0.25], [7.25, -0.25], [6.75, -0.25]],
... ]]
>>> with example('doc/figure/example/a.svg') as ax:
...     _ = ax.add_collection(esy.osm.topology.mpl.patches(lines))
...     _ = ax.add_collection(esy.osm.topology.mpl.patches(
...         terminals, edgecolor='none', facecolor='lightgray')
...     )
...     ax.autoscale_view()
  
```

![](https://gitlab.com/dlr-ve/esy/esy.osm.topology/-/raw/main/doc/figure/example/a.svg)

## Construct graph from strings

Linestrings can be transformed to a spatial graph, that is an array of
coordinates and a sparse matrix of edges connecting those. The
[`esy.osm.topology.graph.from_string_coordinates()`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology/graph.html#from_string_coordinates) function constructs a spatial
graph from a list of shapely linestrings:

```python
>>> coords, graph, line_index = esy.osm.topology.graph.from_string_coordinates(
...     [line.coords for line in lines]
... )
>>> coords.shape, graph.shape, line_index
((17, 2), (17, 17), array([0, 0, 0, 0, 1, 2, 3, 3, 4, 4, 5]))
>>> with example('doc/figure/example/b.svg') as ax:
...     _ = ax.add_collection(esy.osm.topology.mpl.patches(
...         terminals, edgecolor='none', facecolor='lightgray')
...     )
...     esy.osm.topology.mpl.annotate_graph(ax, coords, graph)

```

![](https://gitlab.com/dlr-ve/esy/esy.osm.topology/-/raw/main/doc/figure/example/b.svg)

[`esy.osm.topology.graph.from_string_coordinates()`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology/graph.html#from_string_coordinates) computes the coordinate array
and edges between those coordinates as well as an index to the originating
coordinate list.

As can be seen from the example, visual data may contain duplicate coordinates.
[`esy.osm.topology.graph.unique()`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology/graph.html#unique) can be used to detect duplicate coordinates
and remap edges.

```python
>>> graph, node_index, edge_index = esy.osm.topology.graph.unique(coords, graph)
>>> list(zip(graph.row.tolist(), graph.col.tolist()))
[(13, 14), (1, 13), (1, 2), (0, 1), (2, 6), (2, 3), (3, 8), (3, 4), (4, 9), (9, 10), (10, 11)]
>>> with example('doc/figure/example/c.svg') as ax:
...     _ = ax.add_collection(esy.osm.topology.mpl.patches(
...         terminals, edgecolor='none', facecolor='lightgray')
...     )
...     esy.osm.topology.mpl.annotate_graph(ax, coords, graph)

```

![](https://gitlab.com/dlr-ve/esy/esy.osm.topology/-/raw/main/doc/figure/example/c.svg)

## Identify terminal nodes

Terminal nodes of the infrastructure topologies might be visualized as geometry
shapes. The [`esy.osm.topology.graph.query_terminals()`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology/graph.html#query_terminals) function will identify
all edges that connect terminal nodes:

```python
>>> terminal_idx, terminal_map, edge_index = (
...     esy.osm.topology.graph.query_terminals(coords, graph, terminals)
... )
>>> terminal_idx.tolist()
[0, 4, 6, 8, 9, 11, 14]
>>> graph = esy.osm.topology.graph.filter_edges(graph, edge_index)
>>> with example('doc/figure/example/d.svg') as ax:
...     _ = ax.add_collection(esy.osm.topology.mpl.patches(
...         terminals, edgecolor='none', facecolor='lightgray')
...     )
...     esy.osm.topology.mpl.annotate_graph(ax, coords, graph)
...     esy.osm.topology.mpl.annotate_coords(
...         ax, coords[terminal_idx], terminal_idx, facecolor='blue'
...     )

```

![](https://gitlab.com/dlr-ve/esy/esy.osm.topology/-/raw/main/doc/figure/example/d.svg)

## Shortest path topology

Electricity grids tend to be mostly sequential line connections between terminal
nodes. A power line may be represented by a single linestring in the original
data, although it consists of multiple cables. The heuristic used to resolve
this ambiguity is the shortest path.

The [`esy.osm.topology.graph.terminal_topology()`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology/graph.html#terminal_topology) function computes the shortest
paths between all terminal nodes and collapses these into a topology graph.

```python
>>> topology, shapes, edge_paths = esy.osm.topology.graph.terminal_topology(
...     coords, graph, terminal_idx, terminal_map
... )
>>> list(zip(topology.row.tolist(), topology.col.tolist(), topology.data.tolist()))
[(0, 14, 6.0), (0, 6, 3.0), (6, 8, 3.0), (8, 4, 3.0), (4, 9, 3.0), (9, 11, 3.0)]
>>> with example('doc/figure/example/e.svg') as ax:
...     _ = ax.add_collection(esy.osm.topology.mpl.patches(
...         terminals, edgecolor='none', facecolor='lightgray')
...     )
...     esy.osm.topology.mpl.annotate_graph(ax, coords, topology, facecolor='blue')

```

![](https://gitlab.com/dlr-ve/esy/esy.osm.topology/-/raw/main/doc/figure/example/e.svg)

# Powergrid example

See the [`esy.osm.topology.power`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology/power.html) module for an example based on real world data.

# Design & Development

Design and development notes are available in [`esy.osm.topology.test`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology/test.html).

# Contributions

We would be happy to accept contributions via merge request, but due to
corporate policy we can only accept contributions if you signed our
[contribution license agreement](CLA.md).

# License

[`esy.osm.topology`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology.html) is published under the
[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html) license.

# The Team

[`esy.osm.topology`](https://dlr-ve.gitlab.io/esy/esy.osm.topology/esy/osm/topology.html) is developed at the
[DLR](https://www.dlr.de/EN/Home/home_node.html) Institute of
[Networked Energy Systems](
https://www.dlr.de/ve/en/desktopdefault.aspx/tabid-12472/21440_read-49440/)
in the departement for [Energy Systems Analysis](
https://www.dlr.de/ve/en/desktopdefault.aspx/tabid-12471/21741_read-49802/).

# Acknowledgements

The authors would like to thank the Federal Government and the Heads of
Government of the Länder, as well as the Joint Science Conference (GWK), for
their funding and support within the framework of the NFDI4Ing consortium.
Funded by the German Research Foundation (DFG) - project number 442146713.
