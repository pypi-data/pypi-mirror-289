'''
Visualization functions using `matplotlib`.

The function `patches` visualizes `shapely` geometries as a
`matplotlib.collections.PatchCollection`:

>>> from esy.osm.topology.test import example
>>> shapes = [
...     shapely.LineString([[0, 0], [2, 1]]),
...     shapely.MultiLineString([[[3, 1], [5, 0]]]),
...     shapely.LinearRing([[6, 0], [7, 1], [7, 0]]),
...     shapely.Polygon(
...         [[0, 2], [0, 5], [3, 5], [3, 2]],
...         [[[2, 3], [2, 4], [1, 4], [1, 3]]],
...     ),
...     shapely.MultiPolygon([[
...         [[4, 2], [4, 5], [7, 5], [7, 2]],
...         [[[6, 3], [6, 4], [5, 4], [5, 3]]],
...     ]]),
... ]
>>> with example('doc/figure/mpl/shapes.svg') as ax:
...    _ = ax.add_collection(patches(shapes))
...    ax.autoscale_view()

![](../../../../doc/figure/mpl/shapes.svg)

Annotated graphs can be visualized with `annotate_graph`:

>>> import scipy.sparse
>>> coords = np.array([[0, 0], [2, 0], [1, 1]])
>>> edges = scipy.sparse.coo_array(([10, 20, 30], ([0, 1, 2], [1, 2, 0])))
>>> with example('doc/figure/mpl/graph.svg') as ax:
...     annotate_graph(ax, coords, edges)

![](../../../../doc/figure/mpl/graph.svg)
'''

import itertools

import numpy as np, shapely.geometry
import matplotlib.patches, matplotlib.patheffects
from matplotlib.path import Path

import esy.osm.topology.graph


def render(shapes, path_patch_options=None, **defaults):
    '''
    Converts shapes in to path patches.

    Note, that points are not supported:

    >>> render([shapely.Point(0, 0)])
    Traceback (most recent call last):
      ...
    ValueError: Unsupported shape type POINT (0 0)
    '''

    path_patch_options = path_patch_options or {}
    pathpatches = []

    for shape, path_patch_option in itertools.zip_longest(
        shapes, path_patch_options or (), fillvalue={}
    ):
        path_patch_option = {**defaults, **path_patch_option}
        offset = None
        if type(shape) is shapely.geometry.LineString:
            pathpatches.append(matplotlib.patches.PathPatch(
                matplotlib.path.Path(list(shape.coords), closed=False),
                **{'fill': False, 'edgecolor': 'black', **path_patch_option},
            ))
        elif type(shape) is shapely.geometry.MultiLineString:
            vertices, codes = [], []
            for geom in shape.geoms:
                vertices += geom.coords
                codes += [Path.MOVETO] + [Path.LINETO] * (len(geom.coords) - 1)

            pathpatches.append(matplotlib.patches.PathPatch(
                matplotlib.path.Path(vertices, codes, closed=False),
                **{'fill': False, 'edgecolor': 'black', **path_patch_option},
            ))
        elif type(shape) is shapely.geometry.LinearRing:
            pathpatches.append(matplotlib.patches.PathPatch(
                matplotlib.path.Path(list(shape.coords), closed=True),
                **{'fill': False, 'edgecolor': 'black', **path_patch_option},
            ))
        elif type(shape) is shapely.geometry.Polygon:
            vertices = list(shape.exterior.coords)
            codes = (
                [Path.MOVETO] +
                [Path.LINETO] * (len(vertices) - 2) +
                [Path.CLOSEPOLY]
            )

            for ring in shape.interiors:
                ring_vertices = list(ring.coords)
                ring_codes = (
                    [Path.MOVETO] +
                    [Path.LINETO] * (len(ring_vertices) - 2) +
                    [Path.CLOSEPOLY]
                )
                vertices += ring_vertices
                codes += ring_codes
            pathpatches.append(matplotlib.patches.PathPatch(
                matplotlib.path.Path(vertices, codes, closed=True),
                **{'fill': True, **path_patch_option},
            ))
        elif type(shape) is shapely.geometry.MultiPolygon:
            for shape in shape.geoms:
                vertices = list(shape.exterior.coords)
                codes = (
                    [Path.MOVETO] +
                    [Path.LINETO] * (len(vertices) - 2) +
                    [Path.CLOSEPOLY]
                )

                for ring in shape.interiors:
                    ring_vertices = list(ring.coords)
                    ring_codes = (
                        [Path.MOVETO] +
                        [Path.LINETO] * (len(ring_vertices) - 2) +
                        [Path.CLOSEPOLY]
                    )
                    vertices += ring_vertices
                    codes += ring_codes
                pathpatches.append(matplotlib.patches.PathPatch(
                    matplotlib.path.Path(vertices, codes, closed=True),
                    **{'fill': True, **path_patch_option},
                ))
        else:
            raise ValueError('Unsupported shape type {}'.format(shape))

    return pathpatches


def patches(shapes, path_patch_options=None, **path_patch_defaults):
    '''
    Visualize `shapes` as a `matplotlib.collections.PatchCollection`. 

    Path patch options can be specified individually as a `list` of `dict`s in
    `path_patch_options` or generally using keyword arguments in
    `path_patch_defaults`.
    '''
    return matplotlib.collections.PatchCollection(
        render(shapes, path_patch_options, **path_patch_defaults),
        match_original=True
    )


def graph(coords, edges, **path_patch_options):
    '''
    Visualizes a graph from `edges` at `coords` as a
    `matplotlib.patches.PathPatch`.
    '''
    coords = np.asarray(coords)
    vertices = coords[np.stack([edges.row, edges.col], axis=-1).reshape(-1)]
    codes = np.tile([Path.MOVETO, Path.LINETO], len(edges.row))
    return matplotlib.patches.PathPatch(
        matplotlib.path.Path(vertices, codes, closed=False),
        **path_patch_options,
    )


def annotate_edges(ax, coords, edges):
    '''
    Add annotations to all `edges` between `coords` with the edges data to the
    axes `ax`.
    '''
    for row, col, data in zip(edges.row, edges.col, edges.data):
        a, b = coords[[row, col]]
        center = np.sum([a, b], axis=0) * 0.5
        angle = np.arcsin((b[1] - a[1]) / np.sum((a - b) ** 2) ** 0.5)
        ax.annotate(
            str(data), center, ha='center', va='center',
            rotation=((np.degrees(angle) + 90) % 180) - 90,
            bbox=dict(
                boxstyle='square,pad=0.1', facecolor='white', edgecolor='none'
            ),
            fontsize='x-small',
        )


def annotate_coords(
    ax, coords, names=None, size=160, round=0.125, facecolor='red',
    labelcolor='white',
):
    '''
    Add circles at `coords` to axes `ax` and annotate with `names`.

    `coords` are rounded to `round` to identify overlapping coordinates, which
    will be represented with a separate label.
    '''
    names = names if names is not None else np.arange(len(coords))

    # Add circles at each coordinate.
    ax.add_collection(
        matplotlib.collections.CircleCollection(
            sizes=(size,) * len(coords), offsets=coords, facecolor=facecolor,
            transOffset=ax.transData,
        ),
        autolim=True,
    )

    # Round coordinates and use annotations for overlapping coordinates.
    group_coords, index, inverse, counts = np.unique(
        np.round(coords / round) * round, axis=0,
        return_index=True, return_inverse=True, return_counts=True,
    )

    if inverse.ndim == 2:
        # Since numpy 2, inverse of unique maintains input dimensions.
        inverse = inverse.squeeze()

    inplace = counts == 1
    for name, coord in zip(names[index[inplace]], coords[index[inplace]]):
        ax.annotate(
            str(name), coord, ha='center', va='center', fontsize='small',
            color=labelcolor
        )

    for idx_group in np.where(~inplace)[0]:
        group_name = ','.join(f'{n}' for n in names[inverse == idx_group])
        ax.annotate(
            group_name, group_coords[idx_group],
            xytext=group_coords[idx_group] + [round * 2, round * 2],
            ha='left', va='bottom', fontsize='small',
            bbox=dict(boxstyle='round', fc='white'),
            arrowprops=dict(arrowstyle='-'),
        )


def annotate_graph(ax, coords, edges, **path_patch_options):
    '''
    Adds an annotated `coords` and `edges` of a graph to the axes `ax`.

    See `annotate_coords` and `annotate_edges` for details.
    '''
    coords = np.asarray(coords)

    index = np.unique([edges.row, edges.col])

    ax.add_patch(graph(coords, edges))
    annotate_edges(ax, coords, edges)
    annotate_coords(ax, coords[index], index, **path_patch_options)

    ax.autoscale_view()
